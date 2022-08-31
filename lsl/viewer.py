import stream_viewer.applications.main as viewer
import sys
from qtpy import QtWidgets, QtCore

window = viewer.LSLViewer()

QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_ShareOpenGLContexts)
app = QtWidgets.QApplication(sys.argv)
app.setOrganizationName("LabStreamingLayer")
app.setOrganizationDomain("labstreaminglayer.org")
app.setApplicationName("LSLViewer")
window.show()
