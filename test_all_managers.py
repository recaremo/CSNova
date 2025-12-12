#!/usr/bin/env python3
"""
Test-Skript für alle Daten-Manager in CSNova.
"""

import sys
import json
from pathlib import Path
from csNova_start import initialize_all_managers

def test_managers():
    """Testet alle Manager."""
    print("=" * 60)
    print("CSNova Manager Test Suite")
    print("=" * 60)
    
    # Initialisiere alle Manager
    managers = initialize_all_managers()
    
    if not managers:
        print("\n❌ Manager-Initialisierung fehlgeschlagen!")
        return False
    
    print("\n✅ Alle Manager initialisiert!")
    
    # Teste jeden Manager
    tests_passed = 0
    tests_total = 0
    
    manager_names = {
        "references": "Referenzen",
        "citations": "Zitierformate",
        "projects": "Projekte",
        "characters": "Charaktere",
        "locations": "Schauplätze",
        "objects": "Objekte",
        "storylines": "Handlungsstränge",
        "ideas": "Ideen",
        "chapters": "Kapitel"
    }
    
    for key, name in manager_names.items():
        print(f"\n--- {name} ---")
        tests_total += 1
        
        try:
            if key in managers:
                manager = managers[key]
                
                if key == "citations":
                    # CitationManager hat andere Methoden
                    formats = manager.list_supported_formats()
                    print(f"✓ {len(formats)} Zitierformate gefunden: {', '.join(formats)}")
                    tests_passed += 1
                else:
                    # Alle anderen Manager erben von DataManager
                    all_items = manager.get_all()
                    print(f"✓ {len(all_items)} Einträge geladen")
                    
                    # Teste auto_complete_keys
                    manager.auto_complete_keys()
                    print(f"✓ auto_complete_keys() ausgeführt")
                    
                    tests_passed += 1
            else:
                print(f"❌ {name} nicht in managers-dict")
        
        except Exception as e:
            print(f"❌ Fehler bei {name}: {e}")
    
    print("\n" + "=" * 60)
    print(f"Test-Ergebnis: {tests_passed}/{tests_total} bestanden")
    print("=" * 60)
    
    return tests_passed == tests_total

if __name__ == "__main__":
    success = test_managers()
    sys.exit(0 if success else 1)
