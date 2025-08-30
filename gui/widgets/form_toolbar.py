from PySide6.QtWidgets import QToolBar, QStyle, QGraphicsDropShadowEffect
from PySide6.QtGui import QAction, QColor
from PySide6.QtCore import QSize

# Import zentrale Logging-Funktionen
from core.lloger import log_section, log_subsection, log_info, log_error

class FormToolbar(QToolBar):
    def __init__(self, parent=None):
        log_section("form_toolbar.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.setIconSize(QSize(56, 56))

            self.setStyleSheet("""
                QToolBar {
                    background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                        stop:0 #f4f4f4, stop:1 #666666);
                    border: 2px solid #4F4F4F;
                    border-radius: 8px;
                    padding: 6px;
                    margin-bottom: 6px;
                }
            """)

            # Schatteneffekt direkt nach dem StyleSheet
            shadow = QGraphicsDropShadowEffect(self)
            shadow.setBlurRadius(18)
            shadow.setOffset(0, 6)
            shadow.setColor(QColor(80, 60, 30, int(0.3 * 255)))
            self.setGraphicsEffect(shadow)

            self.new_action = QAction(parent.style().standardIcon(QStyle.SP_FileIcon), "Neuer Datensatz", self)
            self.delete_action = QAction(parent.style().standardIcon(QStyle.SP_TrashIcon), "Datensatz löschen", self)
            self.prev_action = QAction(parent.style().standardIcon(QStyle.SP_ArrowBack), "Zurück", self)
            self.next_action = QAction(parent.style().standardIcon(QStyle.SP_ArrowForward), "Vor", self)
            self.save_action = QAction(parent.style().standardIcon(QStyle.SP_DialogSaveButton), "Datensatz speichern", self)

            self.addAction(self.new_action)
            self.addAction(self.delete_action)
            self.addSeparator()
            self.addAction(self.prev_action)
            self.addAction(self.next_action)
            self.addSeparator()
            self.addAction(self.save_action)

            log_info("FormToolbar initialized successfully.")
        except Exception as e:
            log_error(f"Error initializing FormToolbar: {str(e)}")