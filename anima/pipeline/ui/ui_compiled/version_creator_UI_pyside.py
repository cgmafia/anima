# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui_files/version_creator.ui'
#
# Created: Sun Nov 24 15:52:50 2013
#      by: pyside-uic 0.2.14 running on PySide 1.1.2
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setWindowModality(QtCore.Qt.ApplicationModal)
        Dialog.resize(1704, 769)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setSizeGripEnabled(True)
        Dialog.setModal(True)
        self.horizontalLayout = QtGui.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalWidget = QtGui.QWidget(Dialog)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.verticalWidget.sizePolicy().hasHeightForWidth())
        self.verticalWidget.setSizePolicy(sizePolicy)
        self.verticalWidget.setObjectName("verticalWidget")
        self.verticalLayout = QtGui.QVBoxLayout(self.verticalWidget)
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetMaximumSize)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_11 = QtGui.QHBoxLayout()
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem)
        self.logged_in_as_label = QtGui.QLabel(self.verticalWidget)
        self.logged_in_as_label.setTextFormat(QtCore.Qt.AutoText)
        self.logged_in_as_label.setObjectName("logged_in_as_label")
        self.horizontalLayout_11.addWidget(self.logged_in_as_label)
        self.logged_in_user_label = QtGui.QLabel(self.verticalWidget)
        self.logged_in_user_label.setObjectName("logged_in_user_label")
        self.horizontalLayout_11.addWidget(self.logged_in_user_label)
        self.logout_pushButton = QtGui.QPushButton(self.verticalWidget)
        self.logout_pushButton.setObjectName("logout_pushButton")
        self.horizontalLayout_11.addWidget(self.logout_pushButton)
        self.verticalLayout.addLayout(self.horizontalLayout_11)
        self.line_3 = QtGui.QFrame(self.verticalWidget)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.verticalLayout.addWidget(self.line_3)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.tasks_groupBox = QtGui.QGroupBox(self.verticalWidget)
        self.tasks_groupBox.setObjectName("tasks_groupBox")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.tasks_groupBox)
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.my_tasks_only_checkBox = QtGui.QCheckBox(self.tasks_groupBox)
        self.my_tasks_only_checkBox.setChecked(False)
        self.my_tasks_only_checkBox.setObjectName("my_tasks_only_checkBox")
        self.verticalLayout_2.addWidget(self.my_tasks_only_checkBox)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.search_task_lineEdit = QtGui.QLineEdit(self.tasks_groupBox)
        self.search_task_lineEdit.setObjectName("search_task_lineEdit")
        self.horizontalLayout_4.addWidget(self.search_task_lineEdit)
        self.verticalLayout_2.addLayout(self.horizontalLayout_4)
        self.tasks_treeView = QtGui.QTreeView(self.tasks_groupBox)
        self.tasks_treeView.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tasks_treeView.setAlternatingRowColors(True)
        self.tasks_treeView.setUniformRowHeights(True)
        self.tasks_treeView.setObjectName("tasks_treeView")
        self.tasks_treeView.header().setCascadingSectionResizes(True)
        self.verticalLayout_2.addWidget(self.tasks_treeView)
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.find_from_path_lineEdit = QtGui.QLineEdit(self.tasks_groupBox)
        self.find_from_path_lineEdit.setObjectName("find_from_path_lineEdit")
        self.horizontalLayout_3.addWidget(self.find_from_path_lineEdit)
        self.find_from_path_pushButton = QtGui.QPushButton(self.tasks_groupBox)
        self.find_from_path_pushButton.setObjectName("find_from_path_pushButton")
        self.horizontalLayout_3.addWidget(self.find_from_path_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.thumbnail_graphicsView = QtGui.QGraphicsView(self.tasks_groupBox)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.thumbnail_graphicsView.sizePolicy().hasHeightForWidth())
        self.thumbnail_graphicsView.setSizePolicy(sizePolicy)
        self.thumbnail_graphicsView.setMinimumSize(QtCore.QSize(320, 180))
        self.thumbnail_graphicsView.setMaximumSize(QtCore.QSize(320, 180))
        self.thumbnail_graphicsView.setAutoFillBackground(False)
        self.thumbnail_graphicsView.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.thumbnail_graphicsView.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.thumbnail_graphicsView.setBackgroundBrush(brush)
        self.thumbnail_graphicsView.setInteractive(False)
        self.thumbnail_graphicsView.setRenderHints(QtGui.QPainter.Antialiasing|QtGui.QPainter.HighQualityAntialiasing|QtGui.QPainter.SmoothPixmapTransform|QtGui.QPainter.TextAntialiasing)
        self.thumbnail_graphicsView.setObjectName("thumbnail_graphicsView")
        self.verticalLayout_2.addWidget(self.thumbnail_graphicsView)
        self.horizontalLayout_16 = QtGui.QHBoxLayout()
        self.horizontalLayout_16.setContentsMargins(-1, -1, -1, 10)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_16.addItem(spacerItem1)
        self.upload_thumbnail_pushButton = QtGui.QPushButton(self.tasks_groupBox)
        self.upload_thumbnail_pushButton.setObjectName("upload_thumbnail_pushButton")
        self.horizontalLayout_16.addWidget(self.upload_thumbnail_pushButton)
        self.verticalLayout_2.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_14.addWidget(self.tasks_groupBox)
        self.new_version_groupBox = QtGui.QGroupBox(self.verticalWidget)
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.new_version_groupBox.setFont(font)
        self.new_version_groupBox.setObjectName("new_version_groupBox")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.new_version_groupBox)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.takes_label = QtGui.QLabel(self.new_version_groupBox)
        self.takes_label.setMinimumSize(QtCore.QSize(35, 0))
        font = QtGui.QFont()
        font.setWeight(50)
        font.setBold(False)
        self.takes_label.setFont(font)
        self.takes_label.setObjectName("takes_label")
        self.gridLayout_3.addWidget(self.takes_label, 0, 0, 1, 1)
        self.description_label = QtGui.QLabel(self.new_version_groupBox)
        self.description_label.setMinimumSize(QtCore.QSize(35, 0))
        self.description_label.setObjectName("description_label")
        self.gridLayout_3.addWidget(self.description_label, 1, 0, 1, 1)
        self.horizontalLayout_6 = QtGui.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.takes_listWidget = QtGui.QListWidget(self.new_version_groupBox)
        self.takes_listWidget.setObjectName("takes_listWidget")
        self.horizontalLayout_6.addWidget(self.takes_listWidget)
        self.add_take_toolButton = QtGui.QToolButton(self.new_version_groupBox)
        self.add_take_toolButton.setObjectName("add_take_toolButton")
        self.horizontalLayout_6.addWidget(self.add_take_toolButton)
        self.gridLayout_3.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)
        self.description_textEdit = QtGui.QTextEdit(self.new_version_groupBox)
        self.description_textEdit.setEnabled(True)
        self.description_textEdit.setTabChangesFocus(True)
        self.description_textEdit.setObjectName("description_textEdit")
        self.gridLayout_3.addWidget(self.description_textEdit, 1, 1, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_3)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem2)
        self.update_paths_checkBox = QtGui.QCheckBox(self.new_version_groupBox)
        self.update_paths_checkBox.setChecked(True)
        self.update_paths_checkBox.setObjectName("update_paths_checkBox")
        self.horizontalLayout_7.addWidget(self.update_paths_checkBox)
        self.publish_checkBox = QtGui.QCheckBox(self.new_version_groupBox)
        self.publish_checkBox.setObjectName("publish_checkBox")
        self.horizontalLayout_7.addWidget(self.publish_checkBox)
        self.verticalLayout_6.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.export_as_pushButton = QtGui.QPushButton(self.new_version_groupBox)
        self.export_as_pushButton.setObjectName("export_as_pushButton")
        self.horizontalLayout_2.addWidget(self.export_as_pushButton)
        self.save_as_pushButton = QtGui.QPushButton(self.new_version_groupBox)
        self.save_as_pushButton.setDefault(True)
        self.save_as_pushButton.setObjectName("save_as_pushButton")
        self.horizontalLayout_2.addWidget(self.save_as_pushButton)
        self.verticalLayout_6.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_14.addWidget(self.new_version_groupBox)
        self.previous_versions_groupBox = QtGui.QGroupBox(self.verticalWidget)
        self.previous_versions_groupBox.setObjectName("previous_versions_groupBox")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.previous_versions_groupBox)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.show_published_only_checkBox = QtGui.QCheckBox(self.previous_versions_groupBox)
        self.show_published_only_checkBox.setObjectName("show_published_only_checkBox")
        self.horizontalLayout_10.addWidget(self.show_published_only_checkBox)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem4)
        self.show_only_label = QtGui.QLabel(self.previous_versions_groupBox)
        self.show_only_label.setObjectName("show_only_label")
        self.horizontalLayout_10.addWidget(self.show_only_label)
        self.version_count_spinBox = QtGui.QSpinBox(self.previous_versions_groupBox)
        self.version_count_spinBox.setMaximum(999999)
        self.version_count_spinBox.setProperty("value", 25)
        self.version_count_spinBox.setObjectName("version_count_spinBox")
        self.horizontalLayout_10.addWidget(self.version_count_spinBox)
        self.verticalLayout_7.addLayout(self.horizontalLayout_10)
        self.previous_versions_tableWidget = QtGui.QTableWidget(self.previous_versions_groupBox)
        self.previous_versions_tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.previous_versions_tableWidget.setAlternatingRowColors(True)
        self.previous_versions_tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.previous_versions_tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.previous_versions_tableWidget.setShowGrid(False)
        self.previous_versions_tableWidget.setColumnCount(5)
        self.previous_versions_tableWidget.setObjectName("previous_versions_tableWidget")
        self.previous_versions_tableWidget.setColumnCount(5)
        self.previous_versions_tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.previous_versions_tableWidget.setHorizontalHeaderItem(4, item)
        self.previous_versions_tableWidget.horizontalHeader().setStretchLastSection(True)
        self.previous_versions_tableWidget.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_7.addWidget(self.previous_versions_tableWidget)
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.useNameSpace_checkBox = QtGui.QCheckBox(self.previous_versions_groupBox)
        self.useNameSpace_checkBox.setChecked(True)
        self.useNameSpace_checkBox.setObjectName("useNameSpace_checkBox")
        self.horizontalLayout_5.addWidget(self.useNameSpace_checkBox)
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem5)
        self.chose_pushButton = QtGui.QPushButton(self.previous_versions_groupBox)
        self.chose_pushButton.setObjectName("chose_pushButton")
        self.horizontalLayout_5.addWidget(self.chose_pushButton)
        self.open_pushButton = QtGui.QPushButton(self.previous_versions_groupBox)
        self.open_pushButton.setObjectName("open_pushButton")
        self.horizontalLayout_5.addWidget(self.open_pushButton)
        self.reference_pushButton = QtGui.QPushButton(self.previous_versions_groupBox)
        self.reference_pushButton.setObjectName("reference_pushButton")
        self.horizontalLayout_5.addWidget(self.reference_pushButton)
        self.import_pushButton = QtGui.QPushButton(self.previous_versions_groupBox)
        self.import_pushButton.setObjectName("import_pushButton")
        self.horizontalLayout_5.addWidget(self.import_pushButton)
        self.close_pushButton = QtGui.QPushButton(self.previous_versions_groupBox)
        self.close_pushButton.setStyleSheet("")
        self.close_pushButton.setDefault(False)
        self.close_pushButton.setFlat(False)
        self.close_pushButton.setObjectName("close_pushButton")
        self.horizontalLayout_5.addWidget(self.close_pushButton)
        self.verticalLayout_7.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_14.addWidget(self.previous_versions_groupBox)
        self.horizontalLayout_14.setStretch(2, 1)
        self.verticalLayout.addLayout(self.horizontalLayout_14)
        self.horizontalLayout.addWidget(self.verticalWidget)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        Dialog.setTabOrder(self.add_take_toolButton, self.description_textEdit)
        Dialog.setTabOrder(self.description_textEdit, self.export_as_pushButton)
        Dialog.setTabOrder(self.export_as_pushButton, self.save_as_pushButton)
        Dialog.setTabOrder(self.save_as_pushButton, self.previous_versions_tableWidget)
        Dialog.setTabOrder(self.previous_versions_tableWidget, self.open_pushButton)
        Dialog.setTabOrder(self.open_pushButton, self.reference_pushButton)
        Dialog.setTabOrder(self.reference_pushButton, self.import_pushButton)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QtGui.QApplication.translate("Dialog", "Version Creator - Stalker", None, QtGui.QApplication.UnicodeUTF8))
        self.logged_in_as_label.setText(QtGui.QApplication.translate("Dialog", "<b>Logged In As:</b>", None, QtGui.QApplication.UnicodeUTF8))
        self.logged_in_user_label.setText(QtGui.QApplication.translate("Dialog", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.logout_pushButton.setText(QtGui.QApplication.translate("Dialog", "Logout", None, QtGui.QApplication.UnicodeUTF8))
        self.tasks_groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Tasks", None, QtGui.QApplication.UnicodeUTF8))
        self.my_tasks_only_checkBox.setText(QtGui.QApplication.translate("Dialog", "Show my tasks only", None, QtGui.QApplication.UnicodeUTF8))
        self.tasks_treeView.setToolTip(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Right Click:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To go to the <span style=\" font-weight:600;\">Dependent Tasks</span></li><li style=\" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">To go to the <span style=\" font-weight:600;\">Dependee Tasks</span></li></ul><p><br/></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.find_from_path_lineEdit.setPlaceholderText(QtGui.QApplication.translate("Dialog", "Find From Path", None, QtGui.QApplication.UnicodeUTF8))
        self.find_from_path_pushButton.setText(QtGui.QApplication.translate("Dialog", "Find", None, QtGui.QApplication.UnicodeUTF8))
        self.upload_thumbnail_pushButton.setText(QtGui.QApplication.translate("Dialog", "Upload Thumbnail...", None, QtGui.QApplication.UnicodeUTF8))
        self.new_version_groupBox.setTitle(QtGui.QApplication.translate("Dialog", "New Version", None, QtGui.QApplication.UnicodeUTF8))
        self.takes_label.setText(QtGui.QApplication.translate("Dialog", "Take", None, QtGui.QApplication.UnicodeUTF8))
        self.description_label.setText(QtGui.QApplication.translate("Dialog", "Desc.", None, QtGui.QApplication.UnicodeUTF8))
        self.add_take_toolButton.setText(QtGui.QApplication.translate("Dialog", "+", None, QtGui.QApplication.UnicodeUTF8))
        self.description_textEdit.setHtml(QtGui.QApplication.translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Cantarell\'; font-size:11pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Sans Serif\'; font-size:9pt;\"><br /></p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.update_paths_checkBox.setText(QtGui.QApplication.translate("Dialog", "Update Paths", None, QtGui.QApplication.UnicodeUTF8))
        self.publish_checkBox.setText(QtGui.QApplication.translate("Dialog", "Publish", None, QtGui.QApplication.UnicodeUTF8))
        self.export_as_pushButton.setText(QtGui.QApplication.translate("Dialog", "Export Selection As", None, QtGui.QApplication.UnicodeUTF8))
        self.save_as_pushButton.setText(QtGui.QApplication.translate("Dialog", "Save As", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_groupBox.setTitle(QtGui.QApplication.translate("Dialog", "Previous Versions", None, QtGui.QApplication.UnicodeUTF8))
        self.show_published_only_checkBox.setText(QtGui.QApplication.translate("Dialog", "Show Published Only", None, QtGui.QApplication.UnicodeUTF8))
        self.show_only_label.setText(QtGui.QApplication.translate("Dialog", "Show Only", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.setToolTip(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Right click to:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li><span style=\" font-weight:600;\">Copy Path</span></li><li><span style=\" font-weight:600;\">Browse Path</span></li><li><span style=\" font-weight:600;\">Change Description</span></li></ul><p>Double click to:</p><ul style=\"margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;\"><li style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-weight:600;\">Open</span></li></ul></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("Dialog", "Version", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("Dialog", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(2).setText(QtGui.QApplication.translate("Dialog", "File Size", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(3).setText(QtGui.QApplication.translate("Dialog", "Date", None, QtGui.QApplication.UnicodeUTF8))
        self.previous_versions_tableWidget.horizontalHeaderItem(4).setText(QtGui.QApplication.translate("Dialog", "Description", None, QtGui.QApplication.UnicodeUTF8))
        self.useNameSpace_checkBox.setToolTip(QtGui.QApplication.translate("Dialog", "<html><head/><body><p>Uncheck it if you are going to use <span style=\" font-weight:600;\">Alembic Cache</span>.</p></body></html>", None, QtGui.QApplication.UnicodeUTF8))
        self.useNameSpace_checkBox.setText(QtGui.QApplication.translate("Dialog", "Use Namespace", None, QtGui.QApplication.UnicodeUTF8))
        self.chose_pushButton.setText(QtGui.QApplication.translate("Dialog", "Choose", None, QtGui.QApplication.UnicodeUTF8))
        self.open_pushButton.setText(QtGui.QApplication.translate("Dialog", "Open", None, QtGui.QApplication.UnicodeUTF8))
        self.reference_pushButton.setText(QtGui.QApplication.translate("Dialog", "Reference", None, QtGui.QApplication.UnicodeUTF8))
        self.import_pushButton.setText(QtGui.QApplication.translate("Dialog", "Import", None, QtGui.QApplication.UnicodeUTF8))
        self.close_pushButton.setText(QtGui.QApplication.translate("Dialog", "Close", None, QtGui.QApplication.UnicodeUTF8))

