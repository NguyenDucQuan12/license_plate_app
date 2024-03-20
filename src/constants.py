import sys
import os


if getattr(sys, "frozen", False):
    ROOT = sys._MEIPASS # type: ignore
else:
    ROOT = os.path.dirname(__file__)
