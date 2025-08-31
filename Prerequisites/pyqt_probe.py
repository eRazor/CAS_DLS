import traceback
import sys
print('Python executable:', sys.executable)
try:
    import pyqtgraph as pg
    print('pyqtgraph import: OK, version=', getattr(pg, '__version__', 'unknown'))
except Exception:
    print('pyqtgraph import: FAILED')
    traceback.print_exc()

for mod in ('PyQt5','PyQt6','PySide2','PySide6'):
    try:
        __import__(mod)
        print(mod, 'installed')
    except Exception as e:
        print(mod, 'not available (', e.__class__.__name__, ')')

# Try importing QtWidgets to trigger platform plugin errors
for mod in ('PyQt5.QtWidgets','PyQt6.QtWidgets','PySide2.QtWidgets','PySide6.QtWidgets'):
    try:
        __import__(mod)
        print(mod, 'QtWidgets import OK')
    except Exception as e:
        print(mod, 'QtWidgets import failed:', str(e))
