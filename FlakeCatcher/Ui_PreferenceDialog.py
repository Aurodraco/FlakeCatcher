# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled1.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QMetaObject, Qt)
from PySide6.QtWidgets import (QGridLayout, QHBoxLayout, QLabel, QLineEdit,
                               QPushButton, QRadioButton, QSizePolicy, QSlider)


class Ui_Form(object):

    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_5 = QLabel(Form)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.selectFontButton = QPushButton(Form)
        self.selectFontButton.setObjectName(u"pushButton")

        self.gridLayout.addWidget(self.selectFontButton, 1, 2, 1, 1)

        self.label_4 = QLabel(Form)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.label_4, 2, 2, 1, 1)

        self.label = QLabel(Form)
        self.label.setObjectName(u"label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.checkLightStyle = QRadioButton(Form)
        self.checkLightStyle.setObjectName(u"checkLightStyle")

        self.gridLayout.addWidget(self.checkLightStyle, 3, 2, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName(u"lineEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding,
                                 QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(1)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)

        self.fontEdit = QLineEdit(Form)
        self.fontEdit.setObjectName(u"fontEdit")
        sizePolicy.setHeightForWidth(
            self.fontEdit.sizePolicy().hasHeightForWidth())
        self.fontEdit.setSizePolicy(sizePolicy)
        self.fontEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.fontEdit, 1, 1, 1, 1)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName(u"horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)
        self.horizontalSlider.setPageStep(1)

        self.gridLayout.addWidget(self.horizontalSlider, 2, 1, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName(u"label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.confirmButton = QPushButton(Form)
        self.confirmButton.setObjectName(u"confirmButton")

        self.gridLayout.addWidget(self.confirmButton, 4, 1, 1, 1)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.checkDarkStyle = QRadioButton(Form)
        self.checkDarkStyle.setObjectName(u"checkDarkStyle")
        self.checkDarkStyle.setChecked(True)

        self.gridLayout.addWidget(self.checkDarkStyle, 3, 1, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        self.horizontalSlider.valueChanged.connect(self.label_4.setNum)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(
            QCoreApplication.translate("Form", u"\u8bbe\u7f6e", None))
        self.label_5.setText(
            QCoreApplication.translate("Form",
                                       u"\u754c\u9762\u98ce\u683c\uff1a",
                                       None))
        self.selectFontButton.setText(
            QCoreApplication.translate("Form", u"\u9009\u62e9", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"1", None))
        self.label.setText(
            QCoreApplication.translate(
                "Form", u"\u5f53\u524d\u6570\u636e\u5e93\u76ee\u5f55\uff1a",
                None))
        self.checkLightStyle.setText(
            QCoreApplication.translate("Form", u"\u660e\u4eae", None))
        self.lineEdit.setText(
            QCoreApplication.translate(
                "Form", u"\u6570\u636e\u5e93\u76ee\u5f55\u672a\u83b7\u5f97",
                None))
        self.fontEdit.setText(
            QCoreApplication.translate(
                "Form", u"\u5b57\u4f53\u5b57\u53f7\u672a\u83b7\u5f97", None))
        self.label_3.setText(
            QCoreApplication.translate(
                "Form", u"\u53f3\u4fa7\u6846\u663e\u793a\u6761\u6570\uff1a",
                None))
        self.confirmButton.setText(
            QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.label_2.setText(
            QCoreApplication.translate(
                "Form", u"\u5f53\u524d\u5b57\u4f53\u5b57\u53f7\uff1a", None))
        self.checkDarkStyle.setText(
            QCoreApplication.translate("Form", u"\u6697\u8272", None))

    # retranslateUi
