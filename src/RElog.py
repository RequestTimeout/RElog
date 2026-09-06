from PyQt5 import QtCore, QtGui, QtWidgets
import re, os


class RElogUI(object):
    def __init__(self, RElog):
        self.regexOUT = ""
        RElog.setObjectName("RElog")
        RElog.resize(900, 680)
        RElog.setMinimumSize(QtCore.QSize(640, 480))
        RElog.setStyleSheet("QWidget#RElog {\n"
                            "    background-color: #1e1e2e;\n"
                            "}\n"
                            "\n"
                            "QLabel {\n"
                            "    color: #cdd6f4;\n"
                            "    font-size: 13px;\n"
                            "    padding-top: 2px;\n"
                            "}\n"
                            "\n"
                            "QLineEdit, QPlainTextEdit {\n"
                            "    background-color: #282a3d;\n"
                            "    color: #e6e6f0;\n"
                            "    border: 1px solid #3b3d54;\n"
                            "    border-radius: 6px;\n"
                            "    padding: 8px;\n"
                            "    selection-background-color: #94e2d5;\n"
                            "    selection-color: #1e1e2e;\n"
                            "}\n"
                            "\n"
                            "QLineEdit:focus, QPlainTextEdit:focus {\n"
                            "    border: 1px solid #94e2d5;\n"
                            "}\n"
                            "\n"
                            "QLineEdit#logPathInput {\n"
                            "    border-left: 3px solid #94e2d5;\n"
                            "}\n"
                            "\n"
                            "QLineEdit#regexInput {\n"
                            "    border-left: 3px solid #fab387;\n"
                            "}\n"
                            "\n"
                            "QPlainTextEdit#logViewOutput {\n"
                            "    border-left: 3px solid #89b4fa;\n"
                            "}\n"
                            "\n"
                            "QPlainTextEdit#filteredOutput {\n"
                            "    background-color: #232437;\n"
                            "    border-left: 3px solid #a6e3a1;\n"
                            "    color: #d6f5d6;\n"
                            "}\n"
                            "\n"
                            "QPushButton {\n"
                            "    background-color: #45475a;\n"
                            "    color: #cdd6f4;\n"
                            "    border: none;\n"
                            "    border-radius: 6px;\n"
                            "    padding: 8px 16px;\n"
                            "    font-size: 13px;\n"
                            "}\n"
                            "\n"
                            "QPushButton:hover {\n"
                            "    background-color: #585b70;\n"
                            "}\n"
                            "\n"
                            "QPushButton:pressed {\n"
                            "    background-color: #3b3d54;\n"
                            "}\n"
                            "\n"
                            "QPushButton#saveButton {\n"
                            "    background-color: #a6e3a1;\n"
                            "    color: #1e1e2e;\n"
                            "    font-weight: bold;\n"
                            "}\n"
                            "\n"
                            "QPushButton#saveButton:hover {\n"
                            "    background-color: #b9f0b5;\n"
                            "}\n"
                            "\n"
                            "QPushButton#saveButton:pressed {\n"
                            "    background-color: #8fd189;\n"
                            "}\n"
                            "\n"
                            "QScrollBar:vertical {\n"
                            "    background: #1e1e2e;\n"
                            "    width: 10px;\n"
                            "    margin: 0px;\n"
                            "}\n"
                            "\n"
                            "QScrollBar::handle:vertical {\n"
                            "    background: #45475a;\n"
                            "    border-radius: 5px;\n"
                            "    min-height: 20px;\n"
                            "}\n"
                            "\n"
                            "QScrollBar::handle:vertical:hover {\n"
                            "    background: #585b70;\n"
                            "}\n"
                            "\n"
                            "QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {\n"
                            "    height: 0px;\n"
                            "}\n"
                            "\n"
                            "QScrollBar:horizontal {\n"
                            "    background: #1e1e2e;\n"
                            "    height: 10px;\n"
                            "    margin: 0px;\n"
                            "}\n"
                            "\n"
                            "QScrollBar::handle:horizontal {\n"
                            "    background: #45475a;\n"
                            "    border-radius: 5px;\n"
                            "    min-width: 20px;\n"
                            "}\n"
                            "\n"
                            "QScrollBar::handle:horizontal:hover {\n"
                            "    background: #585b70;\n"
                            "}\n"
                            "\n"
                            "QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {\n"
                            "    width: 0px;\n"
                            "}")
        self.mainLayout = QtWidgets.QVBoxLayout(RElog)
        self.mainLayout.setContentsMargins(16, 16, 16, 16)
        self.mainLayout.setSpacing(10)
        self.mainLayout.setObjectName("mainLayout")
        self.logPathLabel = QtWidgets.QLabel(RElog)
        font = QtGui.QFont()
        font.setBold(True)
        self.logPathLabel.setFont(font)
        self.logPathLabel.setObjectName("logPathLabel")
        self.mainLayout.addWidget(self.logPathLabel)
        self.logPathRow = QtWidgets.QHBoxLayout()
        self.logPathRow.setSpacing(8)
        self.logPathRow.setObjectName("logPathRow")
        self.logPathInput = QtWidgets.QLineEdit(RElog)
        self.logPathInput.setMinimumSize(QtCore.QSize(0, 32))
        self.logPathInput.setObjectName("logPathInput")
        self.logPathRow.addWidget(self.logPathInput)
        self.mainLayout.addLayout(self.logPathRow)
        self.regexLabel = QtWidgets.QLabel(RElog)
        font = QtGui.QFont()
        font.setBold(True)
        self.regexLabel.setFont(font)
        self.regexLabel.setObjectName("regexLabel")
        self.mainLayout.addWidget(self.regexLabel)
        self.regexInput = QtWidgets.QLineEdit(RElog)
        self.regexInput.setMinimumSize(QtCore.QSize(0, 32))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.regexInput.setFont(font)
        self.regexInput.setObjectName("regexInput")
        self.mainLayout.addWidget(self.regexInput)
        self.outputsRow = QtWidgets.QHBoxLayout()
        self.outputsRow.setSpacing(12)
        self.outputsRow.setObjectName("outputsRow")
        self.leftColumn = QtWidgets.QVBoxLayout()
        self.leftColumn.setSpacing(6)
        self.leftColumn.setObjectName("leftColumn")
        self.logViewLabel = QtWidgets.QLabel(RElog)
        font = QtGui.QFont()
        font.setBold(True)
        self.logViewLabel.setFont(font)
        self.logViewLabel.setObjectName("logViewLabel")
        self.leftColumn.addWidget(self.logViewLabel)
        self.logViewOutput = QtWidgets.QPlainTextEdit(RElog)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.logViewOutput.setFont(font)
        self.logViewOutput.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.logViewOutput.setReadOnly(True)
        self.logViewOutput.setObjectName("logViewOutput")
        self.leftColumn.addWidget(self.logViewOutput)
        self.outputsRow.addLayout(self.leftColumn)
        self.rightColumn = QtWidgets.QVBoxLayout()
        self.rightColumn.setSpacing(6)
        self.rightColumn.setObjectName("rightColumn")
        self.filteredLabel = QtWidgets.QLabel(RElog)
        font = QtGui.QFont()
        font.setBold(True)
        self.filteredLabel.setFont(font)
        self.filteredLabel.setObjectName("filteredLabel")
        self.rightColumn.addWidget(self.filteredLabel)
        self.filteredOutput = QtWidgets.QPlainTextEdit(RElog)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.filteredOutput.setFont(font)
        self.filteredOutput.setLineWrapMode(QtWidgets.QPlainTextEdit.NoWrap)
        self.filteredOutput.setReadOnly(True)
        self.filteredOutput.setObjectName("filteredOutput")
        self.rightColumn.addWidget(self.filteredOutput)
        self.outputsRow.addLayout(self.rightColumn)
        self.mainLayout.addLayout(self.outputsRow)
        self.bottomRow = QtWidgets.QHBoxLayout()
        self.bottomRow.setObjectName("bottomRow")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.bottomRow.addItem(spacerItem)
        self.saveButton = QtWidgets.QPushButton(RElog)
        self.saveButton.setMinimumSize(QtCore.QSize(200, 34))
        self.saveButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.saveButton.setObjectName("saveButton")
        self.bottomRow.addWidget(self.saveButton)
        self.mainLayout.addLayout(self.bottomRow)

        self.retranslateUi(RElog)
        QtCore.QMetaObject.connectSlotsByName(RElog)

        self.logPathInput.textChanged.connect(self.changed)
        self.regexInput.textChanged.connect(self.changed)
        self.saveButton.clicked.connect(self.saveToFile)

    def retranslateUi(self, RElog):
        _translate = QtCore.QCoreApplication.translate
        RElog.setWindowTitle(_translate("RElog", "RElog — Log Regex Viewer"))
        self.logPathLabel.setText(_translate("RElog", "Log File Path"))
        self.logPathInput.setPlaceholderText(
            _translate("RElog", "Path to log file, e.g. /var/log/syslog/latest.log.txt"))
        self.regexLabel.setText(_translate("RElog", "Regex Pattern"))
        self.regexInput.setPlaceholderText(_translate("RElog", "Enter regex to search the log, e.g. ERROR|WARN"))
        self.logViewLabel.setText(_translate("RElog", "Original Log"))
        self.logViewOutput.setPlaceholderText(_translate("RElog", "Log file contents will appear here..."))
        self.filteredLabel.setText(_translate("RElog", "Filtered Output (Regex Matches)"))
        self.filteredOutput.setPlaceholderText(_translate("RElog", "Lines matching the regex will appear here..."))
        self.saveButton.setText(_translate("RElog", "Save Filtered Output…"))

    def changed(self):
        log_path = self.logPathInput.text()
        pattern = self.regexInput.text()
        if not log_path or not pattern:
            return
        if not os.path.isfile(log_path):
            self.logViewOutput.clear()
            self.filteredOutput.clear()
            return
        try:
            with open(log_path, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except OSError as e:
            print(f"Could not read file: {e}")
            return
        original = "".join(f"[{line_no}] {line}" for line_no, line in enumerate(lines, 1))
        self.logViewOutput.setPlainText(original)
        try:
            regex = re.compile(pattern)
        except re.error as e:
            print(f"Invalid regex: {e}")
            self.filteredOutput.clear()
            return
        matches = []
        for line_no, line in enumerate(lines, 1):
            match = regex.search(line)
            if match:
                matches.append(f"[{line_no}] {match.group()}")
        self.regexOUT = "\n".join(matches)
        self.filteredOutput.setPlainText("\n".join(matches))

    def saveToFile(self):
        try:
            with open(self.logPathInput.text().rstrip(".txt").rstrip(".log") + "_REGEX.log", "w+",
                      encoding="utf-8") as file:
                file.write(self.regexOUT)
        except Exception as e:
            print(f"Encounter unknown error: {e}\nCould not write content to file")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QWidget()
    ui = RElogUI(window)
    window.show()
    sys.exit(app.exec_())
