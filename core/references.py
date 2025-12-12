"""
Referenzverwaltungs- und Zitierlogik für CSNova.

Dieses Modul enthält alle Funktionen zur Verwaltung und Verarbeitung von
Fachliteratur-Referenzen, einschließlich Validierung, Zitierung und
Duplikatsprüfung.
"""

# Definiere Pflichtfelder pro Referenztyp
REQUIRED_FIELDS = {
    "book": ["title", "authors", "year", "publisher"],
    "book_chapter": ["title", "authors", "year", "chapter_title", "publisher"],
    "journal_article": ["title", "authors", "year", "journal"],
    "conference": ["title", "authors", "year", "conference_name"],
    "dissertation": ["title", "authors", "year", "institution", "degree_type"],
    "website": ["title", "authors", "year", "url"],
    "newspaper": ["title", "authors", "year", "newspaper"]
}


def validate_reference(reference):
    """
    Validiert eine Referenz auf Pflichtfelder basierend auf ihrem Typ.
    Gibt eine Liste von Validierungsfehlern zurück (leer wenn valid).
    
    Args:
        reference (dict): Referenz-Objekt
    
    Returns:
        list: Liste von Fehlermeldungen (leer wenn valid)
    """
    errors = []
    ref_type = reference.get("type", "")
    
    if not ref_type or ref_type not in REQUIRED_FIELDS:
        errors.append(f"Unbekannter oder fehlender Referenztyp: '{ref_type}'")
        return errors
    
    required = REQUIRED_FIELDS[ref_type]
    
    for field in required:
        if field not in reference or not reference[field]:
            errors.append(f"Pflichtfeld '{field}' fehlt oder ist leer")
        elif field == "authors" and isinstance(reference[field], list):
            if len(reference[field]) == 0:
                errors.append(f"Mindestens ein Autor ist erforderlich")
            else:
                for i, author in enumerate(reference[field]):
                    if not author.get("name") or not author.get("firstname"):
                        errors.append(f"Autor {i+1}: Vor- und Nachname erforderlich")
    
    return errors


def generate_initial(firstname, name):
    """
    Generiert Initialen aus Vor- und Nachname.
    
    Args:
        firstname (str): Vorname des Autors
        name (str): Nachname des Autors
    
    Returns:
        str: Initialen im Format "F. L." oder "" bei ungültigen Eingaben
    
    Beispiel:
        generate_initial("John", "Miller") -> "J. M."
        generate_initial("Marie-Claire", "Dupont") -> "M. D."
    """
    if not firstname or not name:
        return ""
    
    # Nimm ersten Buchstaben von firstname und name
    first_initial = firstname.strip()[0].upper()
    last_initial = name.strip()[0].upper()
    
    return f"{first_initial}. {last_initial}."


def normalize_authors(authors_list):
    """
    Normalisiert eine Autorenliste durch Generierung fehlender Initialen.
    Modifiziert die Liste in-place.
    
    Args:
        authors_list (list): Liste von Autor-Objekten
    
    Returns:
        list: Normalisierte Autorenliste
    """
    for author in authors_list:
        if not author.get("initial") and author.get("firstname") and author.get("name"):
            author["initial"] = generate_initial(author["firstname"], author["name"])
    
    return authors_list


def check_duplicate_references(references_list):
    """
    Prüft auf doppelte Referenzen basierend auf Autor, Titel und Jahr.
    
    Args:
        references_list (list): Liste von Referenz-Objekten
    
    Returns:
        list: Liste von Duplikat-Objekten mit Details
    
    Beispiel:
        Zwei Referenzen mit gleichem Author/Title/Year werden erkannt
    """
    duplicates = []
    
    for i, ref1 in enumerate(references_list):
        for j, ref2 in enumerate(references_list):
            if i >= j:  # Nur vorwärts prüfen (keine Doppelprüfung)
                continue
            
            # Erstelle Duplikat-Signatur (Author + Title + Year)
            sig1 = _get_duplicate_signature(ref1)
            sig2 = _get_duplicate_signature(ref2)
            
            if sig1 and sig2 and sig1 == sig2:
                duplicates.append({
                    "index1": i,
                    "index2": j,
                    "ref1_id": ref1.get("id", "?"),
                    "ref2_id": ref2.get("id", "?"),
                    "signature": sig1
                })
    
    return duplicates


def _get_duplicate_signature(reference):
    """
    Erstellt eine eindeutige Signatur für eine Referenz (Duplikat-Prüfung).
    
    Args:
        reference (dict): Referenz-Objekt
    
    Returns:
        str: Signatur im Format "Author|Title|Year" oder "" wenn unvollständig
    """
    authors = reference.get("authors", [])
    title = reference.get("title", "").lower().strip()
    year = reference.get("year", "").strip()
    
    if not authors or not title or not year:
        return ""
    
    # Nimm Namen des ersten Autors
    first_author = authors[0].get("name", "").lower().strip()
    
    if not first_author:
        return ""
    
    # Erstelle Signatur
    return f"{first_author}|{title}|{year}"


def generate_citation(reference, format_style="APA", references_formats=None):
    """
    Generiert ein formatiertes Zitat basierend auf Referenzdaten und Zitierformat.
    
    Args:
        reference (dict): Referenz-Objekt aus data_references.json
        format_style (str): Zitierformat (APA, Harvard, Oxford, MLA, Chicago, Vancouver, IEEE)
        references_formats (dict): Die references.json Daten (Format-Definitionen)
    
    Returns:
        str: Formatiertes Zitat oder Fehlermeldung
    
    Beispiel:
        ref = {"title": "The Art of Writing", "authors": [...], "year": "2020", ...}
        citation = generate_citation(ref, "APA", ref_formats)
        -> "Miller, J. A. (2020). The Art of Writing. ..."
    """
    if references_formats is None or format_style not in references_formats:
        return f"[Fehler: Format '{format_style}' nicht definiert]"
    
    format_def = references_formats[format_style]
    citation_parts = []
    
    # Normalisiere Autoren (generiere Initialen falls fehlend)
    authors = normalize_authors(reference.get("authors", []))
    
    for field in format_def.get("order", []):
        part = _format_citation_field(field, reference, format_def, authors)
        if part:
            citation_parts.append(part)
    
    citation = " ".join(citation_parts)
    
    # Bereinige überflüssige Leerzeichen und Interpunktion
    citation = citation.replace("  ", " ").strip()
    
    return citation if citation else "[Keine ausreichenden Daten für Zitierung]"


def _format_citation_field(field, reference, format_def, authors):
    """
    Formatiert ein einzelnes Feld für die Zitierung.
    
    Args:
        field (str): Feldname (z.B. "author", "year", "title")
        reference (dict): Referenz-Objekt
        format_def (dict): Format-Definition aus references.json
        authors (list): Normalisierte Autorenliste
    
    Returns:
        str: Formatiertes Feldstück oder ""
    """
    if field == "author":
        author_format = format_def.get("author_format", "")
        if not authors:
            return ""
        
        # Formatiere Autoren nach Vorgabe
        if "Initialen" in author_format:
            return f"{authors[0].get('name', '')}, {authors[0].get('initial', '')}"
        elif "Vorname" in author_format:
            return f"{authors[0].get('firstname', '')} {authors[0].get('name', '')}"
        else:
            return f"{authors[0].get('name', '')}, {authors[0].get('firstname', '')}"
    
    elif field == "year":
        year = reference.get("year", "")
        year_format = format_def.get("year_format", "")
        if year:
            return year_format.replace("Jahr", year) if year_format else f"({year})"
        return ""
    
    elif field == "title":
        title = reference.get("title", "")
        if title:
            return f"{title}."
        return ""
    
    elif field == "edition":
        edition = reference.get("edition", "")
        edition_format = format_def.get("edition_format", "")
        if edition:
            return edition_format.replace("Auflage", edition) if edition_format else f"{edition}."
        return ""
    
    elif field == "publisher":
        publisher = reference.get("publisher", "")
        publisher_format = format_def.get("publisher_format", "")
        if publisher:
            return publisher_format.replace("Verlag", publisher) if publisher_format else f"{publisher}."
        return ""
    
    elif field == "place":
        place = reference.get("place", "")
        place_format = format_def.get("place_format", "")
        if place:
            return place_format.replace("Ort", place) if place_format else f"{place}:"
        return ""
    
    elif field == "journal":
        journal = reference.get("journal", "")
        journal_format = format_def.get("journal_format", "")
        if journal:
            return journal_format.replace("Zeitschrift", journal) if journal_format else f"{journal}."
        return ""
    
    elif field == "volume":
        volume = reference.get("volume", "")
        volume_format = format_def.get("volume_format", "")
        if volume:
            return volume_format.replace("Band", volume) if volume_format else f"vol. {volume}"
        return ""
    
    elif field == "issue":
        issue = reference.get("issue", "")
        issue_format = format_def.get("issue_format", "")
        if issue:
            return issue_format.replace("Heft", issue) if issue_format else f"no. {issue}"
        return ""
    
    elif field == "pages":
        pages = reference.get("pages", "")
        pages_format = format_def.get("pages_format", "")
        if pages:
            return pages_format.replace("Seitenzahl(en)", pages) if pages_format else f"pp. {pages}"
        return ""
    
    elif field == "doi":
        doi = reference.get("doi", "")
        doi_format = format_def.get("doi_format", "")
        if doi:
            return doi_format.replace("xxxxx", doi) if doi_format else f"https://doi.org/{doi}"
        return ""
    
    return ""
