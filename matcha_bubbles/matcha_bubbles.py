import os
from krita import Extension
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QFontDatabase

PLUGIN_DIR = os.path.dirname(os.path.abspath(__file__))
QSS_PATH = os.path.join(PLUGIN_DIR, "style.qss")
FONT_DIR = os.path.join(PLUGIN_DIR, "fonts")
ICON_DIR = os.path.join(PLUGIN_DIR, "icons").replace("\\", "/")


class MatchaBubbles(Extension):
    def __init__(self, parent):
        super().__init__(parent)
        self._applied = False
        self._fonts_loaded = False

    def setup(self):
        pass

    def createActions(self, window):
        reload_action = window.createAction(
            "matcha_bubbles_reload", "Matcha Bubbles: Reload Style", "tools/scripts")
        reload_action.triggered.connect(self.apply)
        off_action = window.createAction(
            "matcha_bubbles_off", "Matcha Bubbles: Turn Off (this session)", "tools/scripts")
        off_action.triggered.connect(self.remove)
        if not self._applied:
            self.apply()

    def _load_fonts(self):
        if self._fonts_loaded:
            return
        if os.path.isdir(FONT_DIR):
            for name in os.listdir(FONT_DIR):
                if name.lower().endswith((".ttf", ".otf")):
                    QFontDatabase.addApplicationFont(os.path.join(FONT_DIR, name))
        self._fonts_loaded = True

    def apply(self):
        try:
            self._load_fonts()
            with open(QSS_PATH, "r", encoding="utf-8") as f:
                qss = f.read().replace("__ICONS__", ICON_DIR)
            QApplication.instance().setStyleSheet(qss)
            self._applied = True
        except Exception as e:
            print("Matcha Bubbles: could not load style:", e)

    def remove(self):
        QApplication.instance().setStyleSheet("")
        self._applied = False
