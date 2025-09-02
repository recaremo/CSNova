from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QLabel, QLineEdit, QComboBox, QDateEdit, QSpinBox,
    QPushButton, QFileDialog, QHBoxLayout
)
from PySide6.QtGui import QPixmap
from PySide6.QtCore import Qt
from gui.widgets.form_toolbar import FormToolbar
from core.logger import log_section, log_subsection, log_info, log_exception

class ProjectForm(QWidget):
    def __init__(self, translator, parent=None):
        log_section("form_projects.py")
        log_subsection("__init__")
        try:
            super().__init__(parent)
            self.translator = translator

            # Hauptlayout horizontal: links Formular, rechts Bild
            main_layout = QHBoxLayout(self)

            # Linkes Layout für Formular
            form_layout = QVBoxLayout()
            self.toolbar = FormToolbar(self.translator, "project", self)
            form_layout.addWidget(self.toolbar)

            self.heading_label = QLabel(self.translator.tr("project_window_title"), self)
            form_layout.addWidget(self.heading_label)

            self.title_label = QLabel(self.translator.tr("project_title"), self)
            form_layout.addWidget(self.title_label)
            self.title_edit = QLineEdit(self)
            form_layout.addWidget(self.title_edit)

            self.subtitle_label = QLabel(self.translator.tr("project_detail_subtitle"), self)
            form_layout.addWidget(self.subtitle_label)
            self.subtitle_edit = QLineEdit(self)
            form_layout.addWidget(self.subtitle_edit)

            self.author_label = QLabel(self.translator.tr("project_detail_author"), self)
            form_layout.addWidget(self.author_label)
            self.author_edit = QLineEdit(self)
            form_layout.addWidget(self.author_edit)

            self.genre_label = QLabel(self.translator.tr("project_detail_genre"), self)
            form_layout.addWidget(self.genre_label)
            self.genre_edit = QLineEdit(self)
            form_layout.addWidget(self.genre_edit)

            self.cover_label = QLabel(self.translator.tr("project_detail_cover_image"), self)
            form_layout.addWidget(self.cover_label)
            cover_path_layout = QHBoxLayout()
            self.cover_edit = QLineEdit(self)
            cover_path_layout.addWidget(self.cover_edit)
            self.cover_btn = QPushButton(self.translator.tr("project_detail_cover_image") + " ...", self)
            self.cover_btn.clicked.connect(self._load_cover_image)
            cover_path_layout.addWidget(self.cover_btn)
            form_layout.addLayout(cover_path_layout)

            self.start_date_label = QLabel(self.translator.tr("project_start_date"), self)
            form_layout.addWidget(self.start_date_label)
            self.start_date_edit = QDateEdit(self)
            form_layout.addWidget(self.start_date_edit)

            self.deadline_label = QLabel(self.translator.tr("project_deadline"), self)
            form_layout.addWidget(self.deadline_label)
            self.deadline_edit = QDateEdit(self)
            form_layout.addWidget(self.deadline_edit)

            self.words_goal_label = QLabel(self.translator.tr("project_words_count_goal"), self)
            form_layout.addWidget(self.words_goal_label)
            self.words_goal_spin = QSpinBox(self)
            self.words_goal_spin.setMaximum(1000000)
            form_layout.addWidget(self.words_goal_spin)

            self.narrative_label = QLabel(self.translator.tr("project_detail_narrative_perspective"), self)
            form_layout.addWidget(self.narrative_label)
            self.narrative_edit = QLineEdit(self)
            form_layout.addWidget(self.narrative_edit)

            self.premise_label = QLabel(self.translator.tr("project_detail_premise"), self)
            form_layout.addWidget(self.premise_label)
            self.premise_edit = QLineEdit(self)
            form_layout.addWidget(self.premise_edit)

            self.target_group_label = QLabel(self.translator.tr("project_detail_target_group"), self)
            form_layout.addWidget(self.target_group_label)
            self.target_group_edit = QLineEdit(self)
            form_layout.addWidget(self.target_group_edit)

            # Rechtes Layout für Bild
            image_layout = QVBoxLayout()
            image_layout.addStretch()
            self.cover_pixmap_label = QLabel(self)
            self.cover_pixmap_label.setFixedSize(300, 300)
            self.cover_pixmap_label.setScaledContents(True)
            image_layout.addWidget(self.cover_pixmap_label)
            image_layout.addStretch()

            # Layouts ins Hauptlayout einfügen
            main_layout.addLayout(form_layout, stretch=3)
            main_layout.addLayout(image_layout, stretch=1)

            self.setLayout(main_layout)
            log_info("ProjectForm initialized successfully.")
        except Exception as e:
            log_exception("Error initializing ProjectForm", e)

    def _load_cover_image(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, self.translator.tr("project_detail_cover_image"),
            "", "Image Files (*.png *.jpg *.jpeg *.bmp *.gif)"
        )
        if file_path:
            self.cover_edit.setText(file_path)
            pixmap = QPixmap(file_path)
            if not pixmap.isNull():
                self.cover_pixmap_label.setPixmap(pixmap.scaled(
                    self.cover_pixmap_label.size(),
                    Qt.KeepAspectRatio
                ))
            else:
                self.cover_pixmap_label.clear()