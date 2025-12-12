#!/usr/bin/env python3
"""
Integrations-Test für CSNova Referenz-Verwaltung.
Testet die neue modulare Architektur ohne GUI.
"""

import sys
import json
from pathlib import Path

# Ensure we're in the right directory
sys.path.insert(0, str(Path(__file__).parent))

from core.data_manager import ReferenceManager, CitationManager
from core.references import (
    REQUIRED_FIELDS, validate_reference, generate_initial,
    normalize_authors, check_duplicate_references, generate_citation
)
from core.logger import log_info, log_error, log_header

def test_required_fields():
    """Test 1: REQUIRED_FIELDS sind für alle Typen definiert"""
    print("\n" + "="*60)
    print("TEST 1: REQUIRED_FIELDS Definition")
    print("="*60)
    
    expected_types = ["book", "book_chapter", "journal_article", "conference", 
                     "dissertation", "website", "newspaper"]
    
    for ref_type in expected_types:
        if ref_type in REQUIRED_FIELDS:
            fields = REQUIRED_FIELDS[ref_type]
            print(f"✓ {ref_type:20} -> {len(fields)} Pflichtfelder: {', '.join(fields[:3])}...")
        else:
            print(f"✗ {ref_type:20} -> NICHT DEFINIERT")
            return False
    
    return True

def test_reference_manager():
    """Test 2: ReferenceManager kann Daten laden und speichern"""
    print("\n" + "="*60)
    print("TEST 2: ReferenceManager Funktionalität")
    print("="*60)
    
    try:
        rm = ReferenceManager("data/references/data_references.json")
        print("✓ ReferenceManager erstellt")
        
        if not rm.ensure_structure():
            print("✗ Konnte Struktur nicht erstellen")
            return False
        print("✓ Struktur sichergestellt")
        
        if not rm.load():
            print("✗ Konnte Referenzen nicht laden")
            return False
        print("✓ Referenzen geladen")
        
        refs = rm.get_all_references()
        print(f"✓ {len(refs)} Referenzen verfügbar")
        
        return True
    except Exception as e:
        print(f"✗ Fehler: {e}")
        return False

def test_validation():
    """Test 3: Validierung funktioniert"""
    print("\n" + "="*60)
    print("TEST 3: Referenzen-Validierung")
    print("="*60)
    
    try:
        rm = ReferenceManager("data/references/data_references.json")
        rm.load()
        
        errors = rm.validate_all()
        print(f"✓ Validierung durchgeführt: {len(errors)} Fehler gefunden")
        
        if errors:
            for ref_id, error_list in list(errors.items())[:2]:
                print(f"  - {ref_id}: {error_list[0]}")
        
        return True
    except Exception as e:
        print(f"✗ Fehler: {e}")
        return False

def test_duplicate_check():
    """Test 4: Duplikat-Prüfung funktioniert"""
    print("\n" + "="*60)
    print("TEST 4: Duplikat-Prüfung")
    print("="*60)
    
    try:
        rm = ReferenceManager("data/references/data_references.json")
        rm.load()
        
        duplicates = rm.check_duplicates()
        print(f"✓ Duplikat-Prüfung durchgeführt: {len(duplicates)} Duplikate")
        
        if duplicates:
            for dup in duplicates[:2]:
                print(f"  - {dup['ref1_id']} ↔ {dup['ref2_id']}")
        
        return True
    except Exception as e:
        print(f"✗ Fehler: {e}")
        return False

def test_citation_manager():
    """Test 5: CitationManager kann Zitate generieren"""
    print("\n" + "="*60)
    print("TEST 5: CitationManager Funktionalität")
    print("="*60)
    
    try:
        cm = CitationManager("data/references/references.json")
        if not cm.load():
            print("✗ Konnte Zitierformate nicht laden")
            return False
        print("✓ Zitierformate geladen")
        
        formats = cm.list_supported_formats()
        print(f"✓ {len(formats)} Formate verfügbar: {', '.join(formats)}")
        
        return True
    except Exception as e:
        print(f"✗ Fehler: {e}")
        return False

def test_citation_generation():
    """Test 6: Zitierung mit echten Daten"""
    print("\n" + "="*60)
    print("TEST 6: Zitat-Generierung")
    print("="*60)
    
    try:
        rm = ReferenceManager("data/references/data_references.json")
        rm.load()
        
        cm = CitationManager("data/references/references.json")
        cm.load()
        
        refs = rm.get_all_references()
        if not refs:
            print("⚠ Keine Referenzen zum Testen vorhanden")
            return True
        
        ref_id = list(refs.keys())[0]
        ref = refs[ref_id]
        
        print(f"Test mit Referenz: {ref_id}")
        
        for format_name in ["APA", "Harvard", "MLA"]:
            citation = cm.get_citation(ref, format_name)
            print(f"  {format_name:10} -> {citation[:50]}...")
        
        return True
    except Exception as e:
        print(f"✗ Fehler: {e}")
        return False

def test_author_functions():
    """Test 7: Author-Hilfsfunktionen"""
    print("\n" + "="*60)
    print("TEST 7: Author-Funktionen")
    print("="*60)
    
    try:
        # generate_initial
        initial = generate_initial("John", "Miller")
        assert initial == "J. M.", f"Initial falsch: {initial}"
        print(f"✓ generate_initial('John', 'Miller') = '{initial}'")
        
        # normalize_authors
        authors = [
            {"firstname": "Jane", "name": "Doe", "initial": ""},
            {"firstname": "Robert", "name": "Smith", "initial": "R. S."}
        ]
        result = normalize_authors(authors)
        assert result[0]["initial"] == "J. D.", f"Initial falsch: {result[0]['initial']}"
        assert result[1]["initial"] == "R. S.", f"Initial sollte gleich bleiben"
        print(f"✓ normalize_authors() generierte Initialen korrekt")
        
        return True
    except AssertionError as e:
        print(f"✗ Assertion fehlgeschlagen: {e}")
        return False
    except Exception as e:
        print(f"✗ Fehler: {e}")
        return False

def main():
    """Führe alle Tests durch"""
    print("\n" + "="*60)
    print("CSNOVA REFERENZ-SYSTEM INTEGRATIONS-TEST")
    print("="*60)
    
    tests = [
        ("REQUIRED_FIELDS", test_required_fields),
        ("ReferenceManager", test_reference_manager),
        ("Validierung", test_validation),
        ("Duplikat-Prüfung", test_duplicate_check),
        ("CitationManager", test_citation_manager),
        ("Zitat-Generierung", test_citation_generation),
        ("Author-Funktionen", test_author_functions),
    ]
    
    results = {}
    for test_name, test_func in tests:
        try:
            results[test_name] = test_func()
        except Exception as e:
            print(f"\n✗ KRITISCHER FEHLER in {test_name}: {e}")
            import traceback
            traceback.print_exc()
            results[test_name] = False
    
    # Summary
    print("\n" + "="*60)
    print("ZUSAMMENFASSUNG")
    print("="*60)
    
    passed = sum(1 for r in results.values() if r)
    total = len(results)
    
    for test_name, result in results.items():
        status = "✓ PASSED" if result else "✗ FAILED"
        print(f"{test_name:25} {status}")
    
    print(f"\nGESAMT: {passed}/{total} Tests bestanden")
    
    if passed == total:
        print("\n✓✓✓ ALLE TESTS ERFOLGREICH ✓✓✓")
        return 0
    else:
        print(f"\n⚠ {total - passed} Test(s) fehlgeschlagen")
        return 1

if __name__ == "__main__":
    sys.exit(main())
