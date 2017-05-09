# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_files\project_dialog.ui'
#
# Created: Tue May 09 09:41:16 2017
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(517, 545)
        self.verticalLayout = QtGui.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.dialog_label = QtGui.QLabel(Dialog)
        self.dialog_label.setStyleSheet(_fromUtf8("color: rgb(71, 143, 202);\n"
"font: 18pt;"))
        self.dialog_label.setObjectName(_fromUtf8("dialog_label"))
        self.verticalLayout.addWidget(self.dialog_label)
        self.line = QtGui.QFrame(Dialog)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout.addWidget(self.line)
        self.project_info_formLayout = QtGui.QFormLayout()
        self.project_info_formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.project_info_formLayout.setObjectName(_fromUtf8("project_info_formLayout"))
        self.name_label = QtGui.QLabel(Dialog)
        self.name_label.setObjectName(_fromUtf8("name_label"))
        self.project_info_formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.name_label)
        self.name_fields_verticalLayout = QtGui.QVBoxLayout()
        self.name_fields_verticalLayout.setObjectName(_fromUtf8("name_fields_verticalLayout"))
        self.name_validator_label = QtGui.QLabel(Dialog)
        self.name_validator_label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.name_validator_label.setObjectName(_fromUtf8("name_validator_label"))
        self.name_fields_verticalLayout.addWidget(self.name_validator_label)
        self.project_info_formLayout.setLayout(0, QtGui.QFormLayout.FieldRole, self.name_fields_verticalLayout)
        self.code_label = QtGui.QLabel(Dialog)
        self.code_label.setObjectName(_fromUtf8("code_label"))
        self.project_info_formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.code_label)
        self.code_fields_verticalLayout = QtGui.QVBoxLayout()
        self.code_fields_verticalLayout.setObjectName(_fromUtf8("code_fields_verticalLayout"))
        self.code_validator_label = QtGui.QLabel(Dialog)
        self.code_validator_label.setStyleSheet(_fromUtf8("color: rgb(255, 0, 0);"))
        self.code_validator_label.setObjectName(_fromUtf8("code_validator_label"))
        self.code_fields_verticalLayout.addWidget(self.code_validator_label)
        self.project_info_formLayout.setLayout(1, QtGui.QFormLayout.FieldRole, self.code_fields_verticalLayout)
        self.type_label = QtGui.QLabel(Dialog)
        self.type_label.setObjectName(_fromUtf8("type_label"))
        self.project_info_formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.type_label)
        self.type_comboBox = QtGui.QComboBox(Dialog)
        self.type_comboBox.setEditable(True)
        self.type_comboBox.setObjectName(_fromUtf8("type_comboBox"))
        self.project_info_formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.type_comboBox)
        self.date_label = QtGui.QLabel(Dialog)
        self.date_label.setObjectName(_fromUtf8("date_label"))
        self.project_info_formLayout.setWidget(3, QtGui.QFormLayout.LabelRole, self.date_label)
        self.date_dateEdit = QtGui.QDateEdit(Dialog)
        self.date_dateEdit.setObjectName(_fromUtf8("date_dateEdit"))
        self.project_info_formLayout.setWidget(3, QtGui.QFormLayout.FieldRole, self.date_dateEdit)
        self.image_format_label = QtGui.QLabel(Dialog)
        self.image_format_label.setObjectName(_fromUtf8("image_format_label"))
        self.project_info_formLayout.setWidget(4, QtGui.QFormLayout.LabelRole, self.image_format_label)
        self.image_format_horizontalLayout = QtGui.QHBoxLayout()
        self.image_format_horizontalLayout.setObjectName(_fromUtf8("image_format_horizontalLayout"))
        self.image_format_comboBox = QtGui.QComboBox(Dialog)
        self.image_format_comboBox.setObjectName(_fromUtf8("image_format_comboBox"))
        self.image_format_horizontalLayout.addWidget(self.image_format_comboBox)
        self.update_image_format_pushButton = QtGui.QPushButton(Dialog)
        self.update_image_format_pushButton.setObjectName(_fromUtf8("update_image_format_pushButton"))
        self.image_format_horizontalLayout.addWidget(self.update_image_format_pushButton)
        self.create_image_format_pushButton = QtGui.QPushButton(Dialog)
        self.create_image_format_pushButton.setObjectName(_fromUtf8("create_image_format_pushButton"))
        self.image_format_horizontalLayout.addWidget(self.create_image_format_pushButton)
        self.image_format_horizontalLayout.setStretch(0, 1)
        self.project_info_formLayout.setLayout(4, QtGui.QFormLayout.FieldRole, self.image_format_horizontalLayout)
        self.fps_label = QtGui.QLabel(Dialog)
        self.fps_label.setObjectName(_fromUtf8("fps_label"))
        self.project_info_formLayout.setWidget(5, QtGui.QFormLayout.LabelRole, self.fps_label)
        self.fps_spinBox = QtGui.QSpinBox(Dialog)
        self.fps_spinBox.setMinimum(1)
        self.fps_spinBox.setProperty("value", 25)
        self.fps_spinBox.setObjectName(_fromUtf8("fps_spinBox"))
        self.project_info_formLayout.setWidget(5, QtGui.QFormLayout.FieldRole, self.fps_spinBox)
        self.label_3 = QtGui.QLabel(Dialog)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.project_info_formLayout.setWidget(6, QtGui.QFormLayout.LabelRole, self.label_3)
        self.repository_horizontalLayout = QtGui.QHBoxLayout()
        self.repository_horizontalLayout.setObjectName(_fromUtf8("repository_horizontalLayout"))
        self.repository_comboBox = QtGui.QComboBox(Dialog)
        self.repository_comboBox.setObjectName(_fromUtf8("repository_comboBox"))
        self.repository_horizontalLayout.addWidget(self.repository_comboBox)
        self.update_repository_pushButton = QtGui.QPushButton(Dialog)
        self.update_repository_pushButton.setObjectName(_fromUtf8("update_repository_pushButton"))
        self.repository_horizontalLayout.addWidget(self.update_repository_pushButton)
        self.create_repository_pushButton = QtGui.QPushButton(Dialog)
        self.create_repository_pushButton.setObjectName(_fromUtf8("create_repository_pushButton"))
        self.repository_horizontalLayout.addWidget(self.create_repository_pushButton)
        self.repository_horizontalLayout.setStretch(0, 1)
        self.project_info_formLayout.setLayout(6, QtGui.QFormLayout.FieldRole, self.repository_horizontalLayout)
        self.label_4 = QtGui.QLabel(Dialog)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.project_info_formLayout.setWidget(7, QtGui.QFormLayout.LabelRole, self.label_4)
        self.structure_horizontalLayout = QtGui.QHBoxLayout()
        self.structure_horizontalLayout.setObjectName(_fromUtf8("structure_horizontalLayout"))
        self.structure_comboBox = QtGui.QComboBox(Dialog)
        self.structure_comboBox.setObjectName(_fromUtf8("structure_comboBox"))
        self.structure_horizontalLayout.addWidget(self.structure_comboBox)
        self.update_structure_pushButton = QtGui.QPushButton(Dialog)
        self.update_structure_pushButton.setObjectName(_fromUtf8("update_structure_pushButton"))
        self.structure_horizontalLayout.addWidget(self.update_structure_pushButton)
        self.create_structure_pushButton = QtGui.QPushButton(Dialog)
        self.create_structure_pushButton.setObjectName(_fromUtf8("create_structure_pushButton"))
        self.structure_horizontalLayout.addWidget(self.create_structure_pushButton)
        self.structure_horizontalLayout.setStretch(0, 1)
        self.project_info_formLayout.setLayout(7, QtGui.QFormLayout.FieldRole, self.structure_horizontalLayout)
        self.label_5 = QtGui.QLabel(Dialog)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.project_info_formLayout.setWidget(8, QtGui.QFormLayout.LabelRole, self.label_5)
        self.status_comboBox = QtGui.QComboBox(Dialog)
        self.status_comboBox.setObjectName(_fromUtf8("status_comboBox"))
        self.project_info_formLayout.setWidget(8, QtGui.QFormLayout.FieldRole, self.status_comboBox)
        self.verticalLayout.addLayout(self.project_info_formLayout)
        self.label_2 = QtGui.QLabel(Dialog)
        self.label_2.setStyleSheet(_fromUtf8("color: rgb(71, 143, 202);\n"
"font: 18pt;"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.verticalLayout.addWidget(self.label_2)
        self.line_2 = QtGui.QFrame(Dialog)
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.verticalLayout.addWidget(self.line_2)
        self.client_info_formLayout = QtGui.QFormLayout()
        self.client_info_formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.client_info_formLayout.setObjectName(_fromUtf8("client_info_formLayout"))
        self.client_label = QtGui.QLabel(Dialog)
        self.client_label.setObjectName(_fromUtf8("client_label"))
        self.client_info_formLayout.setWidget(0, QtGui.QFormLayout.LabelRole, self.client_label)
        self.client_comboBox = QtGui.QComboBox(Dialog)
        self.client_comboBox.setEditable(True)
        self.client_comboBox.setObjectName(_fromUtf8("client_comboBox"))
        self.client_info_formLayout.setWidget(0, QtGui.QFormLayout.FieldRole, self.client_comboBox)
        self.agency_label = QtGui.QLabel(Dialog)
        self.agency_label.setObjectName(_fromUtf8("agency_label"))
        self.client_info_formLayout.setWidget(1, QtGui.QFormLayout.LabelRole, self.agency_label)
        self.agency_comboBox = QtGui.QComboBox(Dialog)
        self.agency_comboBox.setEditable(True)
        self.agency_comboBox.setObjectName(_fromUtf8("agency_comboBox"))
        self.client_info_formLayout.setWidget(1, QtGui.QFormLayout.FieldRole, self.agency_comboBox)
        self.production_company_label = QtGui.QLabel(Dialog)
        self.production_company_label.setObjectName(_fromUtf8("production_company_label"))
        self.client_info_formLayout.setWidget(2, QtGui.QFormLayout.LabelRole, self.production_company_label)
        self.production_company_comboBox = QtGui.QComboBox(Dialog)
        self.production_company_comboBox.setEditable(True)
        self.production_company_comboBox.setObjectName(_fromUtf8("production_company_comboBox"))
        self.client_info_formLayout.setWidget(2, QtGui.QFormLayout.FieldRole, self.production_company_comboBox)
        self.verticalLayout.addLayout(self.client_info_formLayout)
        self.buttonBox = QtGui.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName(_fromUtf8("buttonBox"))
        self.verticalLayout.addWidget(self.buttonBox)
        self.verticalLayout.setStretch(2, 2)
        self.verticalLayout.setStretch(5, 1)

        self.retranslateUi(Dialog)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("accepted()")), Dialog.accept)
        QtCore.QObject.connect(self.buttonBox, QtCore.SIGNAL(_fromUtf8("rejected()")), Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Project Dialog", None, QtGui.QApplication.UnicodeUTF8))
        self.dialog_label.setText(QtGui.QApplication.translate("Dialog", "Create Project", None, QtGui.QApplication.UnicodeUTF8))
        self.name_label.setText(QtGui.QApplication.translate("Dialog", "Name", None, QtGui.QApplication.UnicodeUTF8))
        self.name_validator_label.setText(QtGui.QApplication.translate("Dialog", "Validator Message", None, QtGui.QApplication.UnicodeUTF8))
        self.code_label.setText(QtGui.QApplication.translate("Dialog", "Code", None, QtGui.QApplication.UnicodeUTF8))
        self.code_validator_label.setText(QtGui.QApplication.translate("Dialog", "Validator Message", None, QtGui.QApplication.UnicodeUTF8))
        self.type_label.setText(QtGui.QApplication.translate("Dialog", "Type", None, QtGui.QApplication.UnicodeUTF8))
        self.date_label.setText(QtGui.QApplication.translate("Dialog", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.image_format_label.setText(QtGui.QApplication.translate("Dialog", "Image Format", None, QtGui.QApplication.UnicodeUTF8))
        self.update_image_format_pushButton.setText(QtGui.QApplication.translate("Dialog", "Update...", None, QtGui.QApplication.UnicodeUTF8))
        self.create_image_format_pushButton.setText(QtGui.QApplication.translate("Dialog", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.fps_label.setText(QtGui.QApplication.translate("Dialog", "FPS", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Dialog", "Repository", None, QtGui.QApplication.UnicodeUTF8))
        self.update_repository_pushButton.setText(QtGui.QApplication.translate("Dialog", "Update...", None, QtGui.QApplication.UnicodeUTF8))
        self.create_repository_pushButton.setText(QtGui.QApplication.translate("Dialog", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Dialog", "Structure", None, QtGui.QApplication.UnicodeUTF8))
        self.update_structure_pushButton.setText(QtGui.QApplication.translate("Dialog", "Update...", None, QtGui.QApplication.UnicodeUTF8))
        self.create_structure_pushButton.setText(QtGui.QApplication.translate("Dialog", "New...", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Dialog", "Status", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Dialog", "Client Info", None, QtGui.QApplication.UnicodeUTF8))
        self.client_label.setText(QtGui.QApplication.translate("Dialog", "Client", None, QtGui.QApplication.UnicodeUTF8))
        self.agency_label.setText(QtGui.QApplication.translate("Dialog", "Agency", None, QtGui.QApplication.UnicodeUTF8))
        self.production_company_label.setText(QtGui.QApplication.translate("Dialog", "<html><head/><body><p align=\"right\">Production<br/>Company</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))

