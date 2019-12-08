# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'src/ui/ui_item.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(601, 363)
        self.gridLayout_2 = QtWidgets.QGridLayout(Form)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(20, 5, 20, 5)
        self.gridLayout.setObjectName("gridLayout")
        self.graphicsView_origin = QtWidgets.QGraphicsView(Form)
        self.graphicsView_origin.setObjectName("graphicsView_origin")
        self.gridLayout.addWidget(self.graphicsView_origin, 0, 0, 1, 1)
        self.graphicsView_edit = QtWidgets.QGraphicsView(Form)
        self.graphicsView_edit.setObjectName("graphicsView_edit")
        self.gridLayout.addWidget(self.graphicsView_edit, 0, 1, 1, 1)
        self.textEdit_edit = QtWidgets.QTextEdit(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_edit.sizePolicy().hasHeightForWidth())
        self.textEdit_edit.setSizePolicy(sizePolicy)
        self.textEdit_edit.setObjectName("textEdit_edit")
        self.gridLayout.addWidget(self.textEdit_edit, 1, 1, 1, 1)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_ocr = QtWidgets.QTextEdit(Form)
        self.textEdit_ocr.setReadOnly(True)
        self.textEdit_ocr.setObjectName("textEdit_ocr")
        self.verticalLayout.addWidget(self.textEdit_ocr)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton_apply = QtWidgets.QPushButton(Form)
        self.pushButton_apply.setObjectName("pushButton_apply")
        self.horizontalLayout.addWidget(self.pushButton_apply)
        self.pushButton_left = QtWidgets.QPushButton(Form)
        self.pushButton_left.setObjectName("pushButton_left")
        self.horizontalLayout.addWidget(self.pushButton_left)
        self.pushButton_right = QtWidgets.QPushButton(Form)
        self.pushButton_right.setObjectName("pushButton_right")
        self.horizontalLayout.addWidget(self.pushButton_right)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(Form)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.pushButton_fontlarger = QtWidgets.QPushButton(Form)
        self.pushButton_fontlarger.setObjectName("pushButton_fontlarger")
        self.horizontalLayout_2.addWidget(self.pushButton_fontlarger)
        self.pushButton_fontsmaller = QtWidgets.QPushButton(Form)
        self.pushButton_fontsmaller.setObjectName("pushButton_fontsmaller")
        self.horizontalLayout_2.addWidget(self.pushButton_fontsmaller)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)
        self.gridLayout.setColumnStretch(0, 1)
        self.gridLayout.setColumnStretch(1, 1)
        self.gridLayout.setRowStretch(0, 3)
        self.gridLayout.setRowStretch(1, 2)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.textEdit_edit.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit_ocr.setHtml(_translate("Form", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.AppleSystemUIFont\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButton_apply.setText(_translate("Form", "Apply"))
        self.pushButton_left.setText(_translate("Form", "<"))
        self.pushButton_right.setText(_translate("Form", ">"))
        self.label.setText(_translate("Form", "Text Size"))
        self.pushButton_fontlarger.setText(_translate("Form", "↑"))
        self.pushButton_fontsmaller.setText(_translate("Form", "↓"))

