.. title:: Codices Scriptoria Nova

Codices Scriptoria Nova (CSNova)
================================

1. Objectif
-----------

Développement d'une application de bureau multiplateforme (Linux, Windows, macOS) destinée aux auteur·e·s pour planifier, organiser et soutenir de manière créative leurs projets de livre. Le logiciel combine une gestion de projet basée sur une base de données, une interface graphique moderne, des fonctionnalités d’IA intégrées et un lecteur personnalisé capable d’afficher du contenu multimédia, des animations et des modèles 3D.

2. Fonctionnalités principales
------------------------------

* Gestion de projet : création, modification et archivage de projets de livre
* Base de données de personnages : tables principales et secondaires (physionomie, psychologie, formation, origine, etc.)
* Gestion des chapitres et des scènes, y compris intrigues, chronologies, lieux, objets
* Module de relations et cartes mentales (personnages, groupes, connexions)
* Statistiques et vues d’ensemble (fiches, listes de tâches, suivi de progression)
* Conseils d’écriture intégrés, guides de genres, gestion des sources, outils de brainstorming
* Intégration multimédia (images, audio, vidéo, animations)
* Exportation vers divers formats (EPUB, PDF, HTML, format propriétaire du lecteur)
* Lecteur multimédia personnalisé avec mise en page responsive selon la plateforme
* Fonction d’interview IA pour le développement de personnages, idées de scénario, analyse de texte
* Langues : allemand, anglais, …
* Vérification orthographique : allemand, anglais

3. Base technique
-----------------

* Langage de programmation : Python (logique, intégration IA, accès base de données)
* Framework GUI : PySide6 (Qt6)
* Base de données : SQLite (extensible plus tard vers PostgreSQL/MySQL)
* Déploiement : PyInstaller → builds autonomes pour Linux, Windows, macOS
* Intégration IA : connexion API avec gestion d’événements asynchrone
* Modules d’exportation : ebooklib, reportlab, weasyprint
* Multimédia : QtMultimedia, QWebEngineView/QML pour le lecteur

4. Plan de projet & avancement
------------------------------

1. **Installation** ✅  
2. **Mise en place de la structure GUI** 🔄  
3. **Création des tables de données** 🔄  
4. **Test de la connexion à la base de données** 🔄  
5. **Configuration d’un projet exemple** 🔄  
6. **Préparation de la fonction d’exportation** 🔄  
7. **Initialisation du module IA** 🔄  

4.1 Installation
~~~~~~~~~~~~~~~~

* Nom du projet « Codices Scriptoria Nova » vérifié juridiquement
* Logo PNG créé
* Environnement de développement : Linux Mint, Visual Studio Code (anglais)
* Langage : Python
* VSC installé, extension Python intégrée
* Extensions :
  * Black Formatter
  * Github Pull Requests
  * isort
  * Jupyter
  * Pylance
  * Python Debugger
  * Python Environments
* Connexion GitHub active
* Environnement virtuel configuré, outils installés :
  * pyside6
  * ebooklib
  * weasyprint
  * reportlab
  * requests
  * asyncio
  * libxcb-cursor0

::

   frank@recaremo:~/Documents/CSNova$ tree -F ./
   ├── ai/
   │   ├── analysis.py
   │   ├── brainstorming.py
   │   ├── interview.py
   │   ├── models/
   │   └── prompts/
   ├── assets/
   │   ├── icons/
   │   └── media/
   ├── cli.py
   ├── config/
   │   ├── dev.py
   │   ├── prod.py
   │   └── settings.py
   ├── core/
   │   ├── database.py
   │   ├── logic/
   │   │   └── crud.py
   │   ├── models/
   │   │   ├── character.py
   │   │   ├── project.py
   │   │   └── scene.py
   │   └── services/
   ├── docs/
   ├── export/
   │   ├── csnova_export.py
   │   ├── epub_export.py
   │   ├── html_export.py
   │   └── pdf_export.py
   ├── gui/
   │   ├── main_window.py
   │   ├── styles/
   │   ├── tabs/
   │   │   ├── character_tab.py
   │   │   ├── project_tab.py
   │   │   └── scene_tab.py
   │   └── widgets/
   │       ├── dialog.py
   │       └── listview.py
   ├── license.md
   ├── main.py
   ├── readme.md
   ├── setup.py
   └── tests/
       └── conftest.py

4.2 Interface graphique
~~~~~~~~~~~~~~~~~~~~~~~

* Framework GUI : PySide6 (Qt6)
* Fenêtre principale : main_window.py
* Onglets : character_tab.py, project_tab.py, scene_tab.py
* Widgets : dialog.py, listview.py
* Feuilles de style : styles/
* Mise en page : responsive, dépendante de la plateforme
* Objectif : utilisation intuitive, extensibilité modulaire

4.3 Tables
~~~~~~~~~~

Toutes les tables SQL sont listées dans la section « Tables » de ta page – déjà formatées en blocs de code Python.

5. Logo du programme
====================

5.1 Grand logo
~~~~~~~~~~~~~~

* Motif : Livre ouvert avec une main flottante et une plume écrivant dedans. Livre tourné à 45° dans le sens antihoraire. Le livre est deux fois plus grand que la main avec la plume. Motif encadré par un cadre simple.
* Texte : « Codices Scriptoria Nova » en trois lignes
  * « Codices Scriptoria » en police médiévale, « C » et « S » en bleu lapis-lazuli
  * « Nova » en police moderne
  * Motif à gauche – texte à droite, en dehors du cadre
* Fond : texture parchemin avec traces d’usure
* Style : Albrecht Dürer, gravure médiévale
* Composition : règle des tiers ou section dorée
* Détails : légères imperfections dans la texture d’impression

**Prompt (anglais) :**

.. code-block:: text

   A hand with quill pen writing in a book. Book is larger than the hand – approximately twice. Motif inside a simple frame. Right of the frame: three lines of black color text. First and second in medieval, third in modern font. First: Codices – C is capital in lapis lazuli blue. Second: Scriptoria – S is capital in lapis lazuli blue. Third: Nova – sans-serif, modern. Style: Albrecht Dürer – medieval woodcut. Background: old, used parchment with hairline fractures, fine cracks. Composition: rule of thirds or golden ratio. Include slight imperfections in the print texture.

5.2 Petit logo
~~~~~~~~~~~~~~

* Même motif que le grand logo
* Texte : « Codices Scriptoria Nova » en deux lignes
  * « CS » en police médiévale, « C » et « S » en bleu lapis-lazuli
  * « Nova » en police moderne
  * Motif à gauche – texte à droite, en dehors du cadre
* Fond : texture parchemin avec traces d’usure
* Style : Albrecht Dürer, gravure médiévale
* Composition : règle des tiers ou section dorée
* Détails : légères imperfections dans la texture d’impression

**Prompt (anglais) :**

.. code-block:: text

   A hand with quill pen writing in a book. Book is larger than the hand – approximately twice. Motif inside a simple frame. Right of the frame: two lines of black color text. First in medieval, second in modern font. First: CS. Second: Nova – sans-serif, modern. Style: Albrecht Dürer – medieval woodcut. Background: old, used parchment with hairline fractures, fine cracks. Composition: rule of thirds or golden ratio. Include slight imperfections in the print texture.

6. Tutoriels & littérature, sources
-----------------------------------

6.1 PySide6 & développement GUI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Create GUI Applications with Python & Qt6 – Martin Fitzpatrick
* Modern UI with PySide6 – complete app
* Install & Setup PySide6 and Qt Designer
* PySide6 + SQLite integration – Qt documentation

6.2 Database & Migration
~~~~~~~~~~~~~~~~~~~~~~~~~

* SQL for Beginners – Michael Kofler
* SQLite Tutorial – Jacek Artymiak
* SQLite Crash Course – freeCodeCamp
* Database migration with Alembic – Heise Developer
* SQLAlchemy Getting Started

6.3 Multimedia & Animation
~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Multimedia Programming with Qt – Marco Piccolino
* QtMultimedia Tutorial – Audio & Video
* QML Animation Basics – Qt Academy
* QtMultimedia & QML – Best Practices
* PySide6 Animation Tutorial
* QtMultimedia Docs

6.4 Export Formats & Reader
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

* Creating EPUBs with ebooklib – Python Publishing Guide
* PDF Export with ReportLab – Python Tutorials
* HTML Export with WeasyPrint – Web2PDF with CSS
* Reader development with QWebEngineView – Qt Blog
* ebooklib Documentation
* ReportLab User Guide
* WeasyPrint Docs

6.5 AI Integration
~~~~~~~~~~~~~~~~~~

* Hands-On AI with Python – Packt Publishing
* OpenAI API Integration – Python Tutorial
