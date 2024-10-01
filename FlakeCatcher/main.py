from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
    QFileDialog,
    QDialog,
    QFontDialog,
    QInputDialog,
)
from PySide6.QtCore import Qt, QEvent, Slot
from PySide6.QtGui import QTextCursor, QFontDatabase, QFont, QTextBlockFormat, QIcon
from FlakeCatcher.Ui_MainWindow import Ui_MainWindow
from FlakeCatcher.Ui_PreferenceDialog import Ui_Form
import uuid
import math
from pathlib import Path
from datetime import datetime
from txtai import Application
from configparser import ConfigParser
from qt_material import apply_stylesheet


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # 连接信号，加载设置
        self.textEdit.cursorPositionChanged.connect(self.cursorChanged)
        self.textEdit.textChanged.connect(self.textChanged)
        self.textEdit.setContextMenuPolicy(Qt.ContextMenuPolicy.NoContextMenu)
        self.shadowStacker.exportCurrentContentSignal.connect(
            self.exportCurrentContent)
        self.shadowStacker.exportEntireContentSignal.connect(
            self.exportEntireContent)
        self.shadowStacker.removeLineSignal.connect(self.removeLine)
        self.shadowStacker.setPreferenceSignal.connect(self.setPreference)
        self.shadowStacker.setReadOnly(True)

        # 读取配置项
        self.config = ConfigParser()
        self.preferenceDialog = PreferenceDialog()
        self.loadPreference()

        # 连接模型和数据库
        embeddingApp = Application("embeddings.yml")
        self.embeddings = embeddingApp.embeddings
        self.embeddings.load("data")
        self.database = self.embeddings.database

        # 记录当前时间为第一行时间，用于查找此前的文本
        self.firstLineTime = datetime.now()

        # 在文本框添加事件过滤器，检测特定的按键是否被按下并触发相关方法
        self.textEdit.installEventFilter(self)

    def eventFilter(self, obj, event):
        # 检测和处理文本框的按键事件
        if obj is self.textEdit and event.type() == QEvent.Type.KeyPress:
            # 如果按下回车，则增加一行数据
            if event.key() == Qt.Key.Key_Return or event.key(
            ) == Qt.Key.Key_Enter:
                self.insertLine()
                return False
            # 如果按下Ctrl + up，并且光标在文本框开头，则再读取一行数据
            if (event.key() == Qt.Key.Key_Up) and (
                    event.modifiers() & Qt.KeyboardModifier.ControlModifier):
                if self.textEdit.textCursor().atStart():
                    self.readLineFromSqlite()
                return False
            # 如果按下ctrl + S，则保存需要保存的文本
            if (event.key() == Qt.Key.Key_S) and (
                    event.modifiers() & Qt.KeyboardModifier.ControlModifier):
                self.insertDocument()
                return False

        if obj is self.textEdit and event.type() == QEvent.Type.KeyRelease:
            # 如果按下ctrl + V，则在文本更新后保存需要保存的文本
            if (event.key() == Qt.Key.Key_V) and (
                    event.modifiers() & Qt.KeyboardModifier.ControlModifier):
                self.insertDocument()
                return False

        return super().eventFilter(obj, event)

    @Slot()
    def cursorChanged(self):
        # 每次光标移动，则根据当前光标所在行（block），在数据库中查找相似文本
        query = self.textEdit.textCursor().block().text().strip()
        if query == "":
            return

        self.shadowStacker.clear()
        results = self.embeddings.search(query, self.displayCount)
        if results and any(result is not None for result in results):
            for result in results:
                if result is not None:
                    self.shadowStacker.append(result["text"] + "\n")
        else:
            pass

    @Slot()
    def textChanged(self):
        # 实时设置行高为字体高度 1.2 倍，block之间10个像素
        self.textEdit.textChanged.disconnect(self.textChanged)
        cursor = self.textEdit.textCursor()
        cursor.movePosition(QTextCursor.MoveOperation.Start)
        block = cursor.block()
        while block.isValid():
            blockFormat = block.blockFormat()
            if not math.isclose(blockFormat.bottomMargin(), 10.0):
                blockFormat.setLineHeight(
                    120,
                    QTextBlockFormat.LineHeightTypes.ProportionalHeight.value)
                blockFormat.setBottomMargin(10.0)
                cursor.mergeBlockFormat(blockFormat)
            else:
                pass

            cursor.movePosition(QTextCursor.MoveOperation.NextBlock)
            block = block.next()
        self.textEdit.update()
        self.textEdit.textChanged.connect(self.textChanged)

    def insertLine(self):
        # 向数据库中插入当前行（block）
        currentBlockNumber = self.textEdit.textCursor().blockNumber()
        # 此时光标还没有换行
        text = (self.textEdit.document().findBlockByNumber(
            currentBlockNumber).text().strip())

        if text != "":
            cursor = self.getDatabaseCursor()
            cursor.execute("select 1 from sections where text = ? limit 1",
                           (text, ))
            if cursor.fetchone() is None:
                id = str(uuid.uuid4())
                doc = [(id, text, None)]
                self.embeddings.upsert(doc)
                self.embeddings.save("data")
        else:
            pass

    def getDatabaseCursor(self):

        try:
            cursor = self.database.getcursor()
        except Exception as e:
            self.database.load("data/documents")
            cursor = self.database.getcursor()

        return cursor

    def insertDocument(self):
        # 将当前文本框的全部未存储内容存入
        document = self.textEdit.toPlainText()
        lines = document.split("\n")
        cursor = self.getDatabaseCursor()

        for line in lines:
            text = line.strip()
            if text != "":
                cursor.execute("select 1 from sections where text = ? limit 1",
                               (text, ))
                if cursor.fetchone() is None:
                    id = str(uuid.uuid4())
                    doc = [(id, text, None)]
                    self.embeddings.upsert(doc)

        self.embeddings.save("data")

    def readLineFromSqlite(self):
        # 读取前一行，前一行是此次打开编辑器之前存储的
        cursor = self.getDatabaseCursor()
        # 将时间顺序作为查找前一行的依据，显然查询的是打开文本框之前的数据
        cursor.execute(
            "select * from sections where entry < ? order by entry DESC limit 1",
            (self.firstLineTime, ),
        )
        result = cursor.fetchone()
        if result is not None:
            self.firstLineTime = result[4]
            newText = result[2] + "\n"
            textCursor = self.textEdit.textCursor()
            textCursor.movePosition(QTextCursor.MoveOperation.Start)
            textCursor.insertText(newText)
            textCursor.movePosition(QTextCursor.MoveOperation.Start)
            self.textEdit.setTextCursor(textCursor)
        else:
            pass

    @Slot()
    def exportCurrentContent(self):
        # 导出当前文本框内容
        filename, _ = QFileDialog.getSaveFileName(
            self, "保存文件", "untitled.txt",
            "Text Files (*.txt *.md);;All Files (*)")

        if filename:
            content = self.textEdit.toPlainText()
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)

    @Slot()
    def exportEntireContent(self):
        # 导出全部内容
        filename, _ = QFileDialog.getSaveFileName(
            self, "保存文件", "雪花捕手.txt", "Text Files (*.txt *.md);;All Files (*)")

        if filename:
            cursor = self.getDatabaseCursor()
            cursor.execute("select * from sections")
            result = cursor.fetchall()
            content = ""
            for row in result:
                content += row[2] + "\n"
            with open(filename, "w", encoding="utf-8") as file:
                file.write(content)

    @Slot()
    def removeLine(self):

        text, ok = QInputDialog.getText(self, "删除特定行内容", "请输入要删除的单行文本:")

        cursor = self.getDatabaseCursor()
        cursor.execute("select id from sections where text = ? limit 1",
                       (text, ))
        id = cursor.fetchone()
        if id is not None:
            self.embeddings.delete([id[0]])
            self.embeddings.save("data")
        else:
            pass

    @Slot()
    def setPreference(self):
        # 配置设置项

        currentDir = Path.cwd()
        absolutePath = (currentDir / "data").resolve()
        self.preferenceDialog.lineEdit.setText(str(absolutePath))

        # 修改字体字号无需再次确认即有效
        self.preferenceDialog.selectFontButton.clicked.connect(self.selectFont)

        # 修改显示条数和风格需要确认
        self.preferenceDialog.confirmButton.clicked.connect(
            self.confirmPreference)

        self.preferenceDialog.exec()

    @Slot()
    def confirmPreference(self):
        # 确认设置
        self.displayCount = self.preferenceDialog.horizontalSlider.value()
        self.config.set("Preference", "display_count", str(self.displayCount))

        if self.preferenceDialog.checkLightStyle.isChecked():
            self.config.set("Preference", "theme", "light")
            if self.preferenceTheme != "light":
                apply_stylesheet(app, theme="light_blue.xml")
                self.loadFont("black")
        else:
            self.config.set("Preference", "theme", "dark")
            if self.preferenceTheme != "dark":
                apply_stylesheet(app, theme="dark_teal.xml")
                self.loadFont("white")

        with open("config.ini", "w", encoding="utf-8") as configFile:
            self.config.write(configFile)

        self.preferenceDialog.close()

    @Slot()
    def selectFont(self):
        # 选择字体
        qFontDialog = QFontDialog()
        ok, font = qFontDialog.getFont()

        if ok:
            self.config.set("Preference", "font", font.toString())
            self.config.set("Preference", "font_size", str(font.pointSize()))

            with open("config.ini", "w", encoding="utf-8") as configFile:
                self.config.write(configFile)

            pointSize = f"{font.pointSize()}pt"
            self.textEdit.setStyleSheet(
                f"font-family: {font.family()}; font-size: {pointSize}; font-style: {font.styleName()}; color: {self.fontColor};"
            )
            self.shadowStacker.setStyleSheet(
                f"font-family: {font.family()}; font-size: {pointSize}; font-style: {font.styleName()}; color: {self.fontColor};"
            )
            self.preferenceDialog.fontEdit.setText(",".join(
                font.toString().split(",")[:2]))

    def loadPreference(self):
        # 读取已有设置
        self.config.read("config.ini", encoding="utf-8")

        self.preferenceTheme = self.config.get("Preference",
                                               "theme",
                                               fallback="dark")
        self.displayCount = self.config.getint("Preference",
                                               "display_count",
                                               fallback=5)

        self.preferenceDialog.horizontalSlider.setValue(self.displayCount)

    def loadFont(self, color):
        # 加载字体，直接设置到样式表
        font = self.config.get("Preference",
                               "font",
                               fallback="WenQuanYi Micro Hei Mono")
        fontSize = self.config.getint("Preference", "font_size", fallback=16)
        if font.partition(",")[0] == "WenQuanYi Micro Hei Mono":
            fontPath = "resource/WenQuanYi Micro Hei Mono.ttf"
            if (fontId := QFontDatabase.addApplicationFont(fontPath)) >= 0:
                fontFamilies = QFontDatabase.applicationFontFamilies(fontId)
                if fontFamilies:
                    font = QFont(fontFamilies[0], fontSize)
        else:
            font = QFont(font, fontSize)

        self.preferenceDialog.fontEdit.setText(
            font.toString().partition(",")[0] + "," + str(fontSize))

        pointSize = f"{font.pointSize()}pt"
        self.textEdit.setStyleSheet(
            f"font-family: {font.family()}; font-size: {pointSize}; font-style: {font.styleName()}; color: {color};"
        )
        self.shadowStacker.setStyleSheet(
            f"font-family: {font.family()}; font-size: {pointSize}; font-style: {font.styleName()}; color: {color};"
        )
        self.fontColor = color

    def closeEvent(self, event):
        # 在退出时再执行一次保存
        self.insertDocument()


class PreferenceDialog(QDialog, Ui_Form):

    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app = QApplication()
    app.setWindowIcon(QIcon("resource/FlakeCatcher.ico"))
    window = MainWindow()
    if window.preferenceTheme == "light":
        apply_stylesheet(app, theme="light_blue.xml")
        window.loadFont("black")
    else:
        window.preferenceTheme = "dark"
        apply_stylesheet(app, theme="dark_teal.xml")
        window.loadFont("white")
    window.show()
    app.exec()
