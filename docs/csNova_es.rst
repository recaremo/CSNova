.. title:: Codices Scriptoria Nova

Codices Scriptoria Nova (CSNova)
================================

1. Objetivo
-----------

Desarrollo de una aplicación de escritorio multiplataforma (Linux, Windows, macOS) para autores y autoras que facilite la planificación, organización y apoyo creativo de proyectos literarios. El software combina gestión de proyectos basada en bases de datos, una interfaz gráfica moderna, funciones integradas de IA y un lector personalizado capaz de mostrar contenido multimedia, animaciones y modelos 3D.

2. Funcionalidades principales
------------------------------

* Gestión de proyectos: crear, editar y archivar proyectos de libros
* Base de datos de personajes: tablas principales y secundarias (fisonomía, psicología, formación, origen, etc.)
* Gestión de capítulos y escenas, incluyendo tramas, líneas temporales, lugares, objetos
* Módulo de relaciones y mapas mentales (personajes, grupos, conexiones)
* Estadísticas y vistas generales (fichas, listas de tareas, progreso)
* Consejos de escritura integrados, guías de géneros, gestión de fuentes, herramientas de lluvia de ideas
* Integración multimedia (imágenes, audio, vídeo, animaciones)
* Exportación a varios formatos (EPUB, PDF, HTML, formato propio del lector)
* Lector multimedia personalizado con diseño adaptable por plataforma
* Función de entrevista IA para desarrollo de personajes, ideas de trama, análisis de texto
* Idiomas: alemán, inglés, …
* Corrector ortográfico: alemán, inglés

3. Base técnica
---------------

* Lenguaje de programación: Python (lógica, integración IA, acceso a base de datos)
* Framework GUI: PySide6 (Qt6)
* Base de datos: SQLite (ampliable posteriormente a PostgreSQL/MySQL)
* Distribución: PyInstaller → compilaciones independientes para Linux, Windows, macOS
* Integración IA: conexión API con gestión de eventos asíncronos
* Módulos de exportación: ebooklib, reportlab, weasyprint
* Multimedia: QtMultimedia, QWebEngineView/QML para el lector

4. Plan de proyecto y progreso
------------------------------

1. **Instalación** ✅  
2. **Configuración de la estructura básica de la GUI** 🔄  
3. **Creación de tablas de datos** 🔄  
4. **Prueba de conexión a la base de datos** 🔄  
5. **Configuración de proyecto de ejemplo** 🔄  
6. **Preparación de función de exportación** 🔄  
7. **Inicialización del módulo IA** 🔄  

4.1 Instalación
~~~~~~~~~~~~~~~

* Nombre del proyecto “Codices Scriptoria Nova” verificado legalmente
* Logo PNG creado
* Entorno de desarrollo: Linux Mint, Visual Studio Code (inglés)
* Lenguaje: Python
* VSC instalado, complemento Python integrado
* Complementos:
  * Black Formatter
  * Github Pull Requests
  * isort
  * Jupyter
  * Pylance
  * Python Debugger
  * Python Environments
* Conexión a GitHub activa
* Entorno virtual configurado, herramientas instaladas:
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

4.2 Interfaz gráfica
~~~~~~~~~~~~~~~~~~~~

* Framework GUI: PySide6 (Qt6)
* Ventana principal: main_window.py
* Pestañas: character_tab.py, project_tab.py, scene_tab.py
* Widgets: dialog.py, listview.py
* Hojas de estilo: styles/
* Diseño: adaptable, dependiente de la plataforma
* Objetivo: uso intuitivo, extensibilidad modular

4.3 Tablas
~~~~~~~~~~

Todas las tablas SQL están listadas en la sección “Tablas” de tu página – ya formateadas como bloques de código Python.

5. Logo del programa
====================

5.1 Logo grande
~~~~~~~~~~~~~~~

* Motivo: Libro abierto con una mano flotante y una pluma escribiendo en él. El libro está girado 45° en sentido antihorario. El libro es el doble de grande que la mano con la pluma. Todo el motivo está enmarcado por un marco simple.
* Texto: “Codices Scriptoria Nova” en tres líneas
  * “Codices Scriptoria” en fuente medieval, “C” y “S” en azul lapislázuli
  * “Nova” en fuente moderna
  * Motivo a la izquierda – texto a la derecha, fuera del marco
* Fondo: textura de pergamino con signos de desgaste
* Estilo: Albrecht Dürer, grabado medieval
* Composición: regla de los tercios o proporción áurea
* Detalles: ligeras imperfecciones en la textura de impresión

**Prompt (inglés):**

.. code-block:: text

   A hand with quill pen writing in a book. Book is larger than the hand – approximately twice. Motif inside a simple frame. Right of the frame: three lines of black color text. First and second in medieval, third in modern font. First: Codices – C is capital in lapis lazuli blue. Second: Scriptoria – S is capital in lapis lazuli blue. Third: Nova – sans-serif, modern. Style: Albrecht Dürer – medieval woodcut. Background: old, used parchment with hairline fractures, fine cracks. Composition: rule of thirds or golden ratio. Include slight imperfections in the print texture.

5.2 Logo pequeño
~~~~~~~~~~~~~~~~

* Mismo motivo que el logo grande
* Texto: “Codices Scriptoria Nova” en dos líneas
  * “CS” en fuente medieval, “C” y “S” en azul lapislázuli
  * “Nova” en fuente moderna
  * Motivo a la izquierda – texto a la derecha, fuera del marco
* Fondo: textura de pergamino con signos de desgaste
* Estilo: Albrecht Dürer, grabado medieval
* Composición: regla de los tercios o proporción áurea
* Detalles: ligeras imperfecciones en la textura de impresión

**Prompt (inglés):**

.. code-block:: text

   A hand with quill pen writing in a book. Book is larger than the hand – approximately twice. Motif inside a simple frame. Right of the frame: two lines of black color text. First in medieval, second in modern font. First: CS. Second: Nova – sans-serif, modern. Style: Albrecht Dürer – medieval woodcut. Background: old, used parchment with hairline fractures, fine cracks. Composition: rule of thirds or golden ratio. Include slight imperfections in the print texture.

6. Tutoriales, literatura y fuentes
===================================

6.1 PySide6 y desarrollo de interfaces gráficas
-----------------------------------------------

* Create GUI Applications with Python & Qt6 – Martin Fitzpatrick  
* Modern UI with PySide6 – complete app  
* Install & Setup PySide6 and Qt Designer  
* PySide6 + SQLite integration – Qt documentation  

6.2 Bases de datos y migración
------------------------------

* SQL für Einsteiger – Michael Kofler  
* SQLite Tutorial – Jacek Artymiak  
* SQLite Crash Course – freeCodeCamp  
* Datenbankmigration mit Alembic – Heise Developer  
* SQLAlchemy Getting Started  

6.3 Multimedia y animación
--------------------------

* Multimedia Programming with Qt – Marco Piccolino  
* QtMultimedia Tutorial – Audio & Video  
* QML Animation Basics – Qt Academy  
* QtMultimedia & QML – Best Practices  
* PySide6 Animation Tutorial  
* QtMultimedia Docs  

6.4 Formatos de exportación y lector
------------------------------------

* Creating EPUBs with ebooklib – Python Publishing Guide  
* PDF-Export mit ReportLab – Python Tutorials  
* HTML-Export mit WeasyPrint – Web2PDF mit CSS  
* Reader-Entwicklung mit QWebEngineView – Qt Blog  
* ebooklib Dokumentation  
* ReportLab User Guide  
* WeasyPrint Docs  

6.5 Integración de IA
---------------------

* Hands-On AI with Python – Packt Publishing  
* OpenAI API Integration – Python Tutorial  
