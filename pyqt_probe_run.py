import sys, traceback, os
print('python', sys.version)

try:
    import pyqtgraph as pg
    print('pyqtgraph', getattr(pg, '__version__', 'unknown'))
except Exception:
    print('pyqtgraph import FAILED')
    traceback.print_exc()

try:
    import qtpy
    print('qtpy.api', qtpy.API)
except Exception:
    print('qtpy import FAILED')
    traceback.print_exc()

for mod in ('PyQt5','PyQt6','PySide2','PySide6'):
    try:
        __import__(mod)
        print(mod, 'present')
    except Exception:
        print(mod, 'not present')

# Try to instantiate a PlotWidget (offscreen) to detect runtime GUI issues
try:
    from pyqtgraph import PlotWidget
    print('PlotWidget class found')
    os.environ.setdefault('QT_QPA_PLATFORM', 'offscreen')
    try:
        # prefer PyQt5 if present
        if 'PyQt5' in sys.modules or 'PyQt5' in (m for m in sys.modules):
            from PyQt5 import QtWidgets
            app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
            pw = PlotWidget()
            print('Created PlotWidget OK (PyQt5)')
            app.quit()
        else:
            # try generic Qt
            try:
                from qtpy import QtWidgets
                app = QtWidgets.QApplication.instance() or QtWidgets.QApplication([])
                pw = PlotWidget()
                print('Created PlotWidget OK (qtpy)')
                app.quit()
            except Exception:
                raise
    except Exception:
        print('Failed to create PlotWidget (runtime GUI issue)')
        traceback.print_exc()
except Exception:
    print('PlotWidget class not available or pyqtgraph failed')
    traceback.print_exc()
