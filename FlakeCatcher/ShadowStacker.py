from PySide6.QtWidgets import QTextEdit, QMenu
from PySide6.QtCore import Signal
from PySide6.QtGui import QAction


class ShadowStacker(QTextEdit):
    # 自定义 QTextEdit 类，添加了自定义的右键菜单项

    exportCurrentContentSignal = Signal()
    exportEntireContentSignal = Signal()
    removeContentSignal = Signal()
    setPreferenceSignal = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)

    def contextMenuEvent(self, event):
        self.setReadOnly(True)
        menu = QMenu(self)

        exportCurrentContent = QAction("导出左侧文本框内容", self)
        exportCurrentContent.triggered.connect(self.emitExportCurrentContent)
        menu.addAction(exportCurrentContent)

        exportEntireContent = QAction("导出数据库内容", self)
        exportEntireContent.triggered.connect(self.emitExportEntireContent)
        menu.addAction(exportEntireContent)

        removeContent = QAction("删除特定内容", self)
        removeContent.triggered.connect(self.emitRemoveContent)
        menu.addAction(removeContent)

        menu.addSeparator()

        setPreference = QAction("设置", self)
        setPreference.triggered.connect(self.emitSetPreference)
        menu.addAction(setPreference)

        # 显示自定义的上下文菜单
        menu.exec(self.mapToGlobal(event.pos()))

    def emitExportCurrentContent(self):
        self.exportCurrentContentSignal.emit()

    def emitExportEntireContent(self):
        self.exportEntireContentSignal.emit()

    def emitSetPreference(self):
        self.setPreferenceSignal.emit()

    def emitRemoveContent(self):
        self.removeContentSignal.emit()
