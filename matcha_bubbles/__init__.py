from krita import Krita
from .matcha_bubbles import MatchaBubbles

Krita.instance().addExtension(MatchaBubbles(Krita.instance()))
