from PyQt5 import QtCore, QtGui, QtWidgets

"""
    This function sets up the user interface for the form creation tool.

    Parameters: CreateForm (QWidget): The main window of the form creation tool.
"""
 
class Ui_CreateForm(object):
 # Set the window properties
    def setupUi(self, CreateForm):
        CreateForm.setObjectName("CreateForm")
        CreateForm.resize(816, 600)
        font = QtGui.QFont()
        font.setFamily("Verdana")
        CreateForm.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/images/logo.ico"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CreateForm.setWindowIcon(icon)
        CreateForm.setToolTipDuration(0)
        CreateForm.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.footer = QtWidgets.QFrame(CreateForm)
        self.footer.setGeometry(QtCore.QRect(0, 540, 811, 61))
        self.footer.setStyleSheet("#footer{\n"
        "   border-top: 1px solid rgb(138, 138, 138);\n"
        "}")

        # footer frame
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
          
        # save button
        self.save_button = QtWidgets.QPushButton(self.footer)
        self.save_button.setGeometry(QtCore.QRect(420, 10, 120, 35))
        self.save_button.setMinimumSize(QtCore.QSize(120, 35))
        self.save_button.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.save_button.setFont(font)
        self.save_button.setStyleSheet("QPushButton{\n"
        "  color: rgb(255, 255, 255);\n"
        "   background-color: rgb(0, 74, 0);\n"
        "   border-radius: 4px;\n"
        "   border: 2px solid rgb(5, 136, 71); \n"
        "}")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/images/save.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.save_button.setIcon(icon1)
        self.save_button.setIconSize(QtCore.QSize(21, 21))
        self.save_button.setCheckable(True)
        self.save_button.setDefault(False)
        self.save_button.setFlat(False)
        self.save_button.setObjectName("save_button")

        # add column button
        self.add_column = QtWidgets.QPushButton(self.footer)
        self.add_column.setGeometry(QtCore.QRect(270, 10, 120, 35))
        self.add_column.setMinimumSize(QtCore.QSize(120, 35))
        self.add_column.setMaximumSize(QtCore.QSize(100, 30))
        font = QtGui.QFont()
        font.setFamily("Verdana")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.add_column.setFont(font)
        self.add_column.setStyleSheet("QPushButton{\n"
        "   color: rgb(138, 138, 138);\n"
        "   background-color: transparent;\n"
        "   border-radius: 4px;\n"
        "   border: 2px solid rgb(5, 136, 71); \n"
        "}\n"
        "")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/images/plus-circle.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.add_column.setIcon(icon2)
        self.add_column.setIconSize(QtCore.QSize(21, 21))
        self.add_column.setCheckable(True)
        self.add_column.setAutoDefault(False)
        self.add_column.setDefault(False)
        self.add_column.setFlat(False)
        self.add_column.setObjectName("add_column")

        # main frame
        self.frame = QtWidgets.QFrame(CreateForm)
        self.frame.setGeometry(QtCore.QRect(0, 0, 811, 541))
        self.frame.setStyleSheet("#Editor{\n"
        "   border-radius: 4px;\n"
        "   border: 1px solid rgb(5, 136, 71); \n"
        "}\n"

        "QTableWidget{\n"
        "   border-radius: 4px;\n"
        "   border: 1px solid rgb(5, 136, 71); \n"
        "}\n"
        
        "#FormPreview{\n"
        "   border-radius: 4px;\n"
        "   border: 1px solid rgb(5, 136, 71); \n"
        "}")
        self.frame.setObjectName("frame")

        # horizontal layout for the main frame
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(1, 6, 1, -1)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")

        # editor widget
        self.Editor = QtWidgets.QWidget(self.frame)
        self.Editor.setObjectName("Editor")

        # table widget in the editor
        self.tableWidget = QtWidgets.QTableWidget(self.Editor)
        self.tableWidget.setGeometry(QtCore.QRect(10, 0, 391, 521))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.horizontalLayout.addWidget(self.Editor) # Add the editor widget to the horizontal layout
        
        # form preview widget
        self.FormPreview = QtWidgets.QWidget(self.frame)
        self.FormPreview.setObjectName("FormPreview")

        # Add the form preview widget to the horizontal layout
        self.horizontalLayout.addWidget(self.FormPreview)
        self.frame.raise_()
        self.footer.raise_()

        # Connect the slots to the signals
        self.retranslateUi(CreateForm)
        QtCore.QMetaObject.connectSlotsByName(CreateForm)

    def retranslateUi(self, CreateForm):
        _translate = QtCore.QCoreApplication.translate
        CreateForm.setWindowTitle(_translate("CreateForm", "New Form"))
        self.save_button.setText(_translate("CreateForm", "Save"))
        self.add_column.setText(_translate("CreateForm", "Add column"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CreateForm = QtWidgets.QWidget()
    ui = Ui_CreateForm()
    ui.setupUi(CreateForm)
    CreateForm.show()
    sys.exit(app.exec_())
