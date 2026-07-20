try:
    from .presets import *
except (ImportError, ModuleNotFoundError):
    from presets import *