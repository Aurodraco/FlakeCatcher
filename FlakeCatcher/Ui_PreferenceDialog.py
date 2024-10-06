# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'untitled.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (
    QCoreApplication,
    QMetaObject,
    Qt,
)
from PySide6.QtWidgets import (
    QCheckBox,
    QGridLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QRadioButton,
    QSlider,
)


class Ui_PreferenceDialog(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.label = QLabel(Form)
        self.label.setObjectName("label")

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.lineEdit = QLineEdit(Form)
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.lineEdit, 0, 1, 1, 2)

        self.label_2 = QLabel(Form)
        self.label_2.setObjectName("label_2")

        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)

        self.fontEdit = QLineEdit(Form)
        self.fontEdit.setObjectName("fontEdit")
        self.fontEdit.setReadOnly(True)

        self.gridLayout.addWidget(self.fontEdit, 1, 1, 1, 1)

        self.selectFontButton = QPushButton(Form)
        self.selectFontButton.setObjectName("selectFontButton")

        self.gridLayout.addWidget(self.selectFontButton, 1, 2, 1, 1)

        self.label_3 = QLabel(Form)
        self.label_3.setObjectName("label_3")

        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)

        self.horizontalSlider = QSlider(Form)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider.setMinimum(1)
        self.horizontalSlider.setMaximum(10)
        self.horizontalSlider.setPageStep(1)
        self.horizontalSlider.setOrientation(Qt.Orientation.Horizontal)

        self.gridLayout.addWidget(self.horizontalSlider, 2, 1, 1, 1)

        self.sliderLable = QLabel(Form)
        self.sliderLable.setObjectName("sliderLable")
        self.sliderLable.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.sliderLable, 2, 2, 1, 1)

        self.label_5 = QLabel(Form)
        self.label_5.setObjectName("label_5")

        self.gridLayout.addWidget(self.label_5, 3, 0, 1, 1)

        self.checkDarkStyle = QRadioButton(Form)
        self.checkDarkStyle.setObjectName("checkDarkStyle")

        self.gridLayout.addWidget(self.checkDarkStyle, 3, 1, 1, 1)

        self.checkLightStyle = QRadioButton(Form)
        self.checkLightStyle.setObjectName("checkLightStyle")

        self.gridLayout.addWidget(self.checkLightStyle, 3, 2, 1, 1)

        self.label_6 = QLabel(Form)
        self.label_6.setObjectName("label_6")

        self.gridLayout.addWidget(self.label_6, 4, 0, 1, 1)

        self.checkBox = QCheckBox(Form)
        self.checkBox.setObjectName("checkBox")

        self.gridLayout.addWidget(self.checkBox, 4, 1, 1, 2)

        self.confirmButton = QPushButton(Form)
        self.confirmButton.setObjectName("confirmButton")

        self.gridLayout.addWidget(self.confirmButton, 5, 1, 1, 1)

        self.horizontalLayout.addLayout(self.gridLayout)

        self.retranslateUi(Form)
        self.horizontalSlider.valueChanged.connect(self.sliderLable.setNum)

        QMetaObject.connectSlotsByName(Form)

    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", "\u8bbe\u7f6e", None))
        self.label.setText(
            QCoreApplication.translate(
                "Form", "\u5f53\u524d\u6570\u636e\u5e93\u76ee\u5f55", None
            )
        )
        self.label_2.setText(
            QCoreApplication.translate(
                "Form", "\u5f53\u524d\u5b57\u4f53\u5b57\u53f7", None
            )
        )
        self.selectFontButton.setText(
            QCoreApplication.translate("Form", "\u9009\u62e9", None)
        )
        self.label_3.setText(
            QCoreApplication.translate(
                "Form", "\u53f3\u4fa7\u6846\u663e\u793a\u6761\u6570", None
            )
        )
        self.sliderLable.setText(QCoreApplication.translate("Form", "no_data", None))
        self.label_5.setText(
            QCoreApplication.translate("Form", "\u754c\u9762\u98ce\u683c", None)
        )
        self.checkDarkStyle.setText(
            QCoreApplication.translate("Form", "\u6697\u8272", None)
        )
        self.checkLightStyle.setText(
            QCoreApplication.translate("Form", "\u660e\u4eae", None)
        )
        self.label_6.setText(
            QCoreApplication.translate(
                "Form", "\u6362\u884c\u65f6\u4fdd\u5b58\u5f53\u524d\u884c", None
            )
        )
        self.checkBox.setText(QCoreApplication.translate("Form", "是", None))
        self.confirmButton.setText(
            QCoreApplication.translate("Form", "\u786e\u8ba4", None)
        )

    # retranslateUi
