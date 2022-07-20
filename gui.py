from asyncio.windows_events import NULL
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from styles import styles
from googletrans import Translator
from PyQt5.QtCore import Qt
import sys
import os
import yake
import requests
import cv2


translator = Translator()
kw_extractor = yake.KeywordExtractor()
language = "en"
max_ngram_size = 1
deduplication_threshold = 0.9
numOfKeywords = 1
image = NULL
reso_image = NULL
custom_kw_extractor = yake.KeywordExtractor(
    lan=language,
    n=max_ngram_size,
    dedupLim=deduplication_threshold,
    top=numOfKeywords,
    features=None,
)


class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)
        self.init()

    def init(self):
        self.layout = QHBoxLayout()
        self.layout1 = QVBoxLayout()

        self.image = QLabel(self)
        self.image.setStyleSheet(styles.text_style)
        self.image.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.label = QLabel("Preparing...", self)
        self.label.setAlignment(
            Qt.AlignmentFlag.AlignCenter | Qt.AlignmentFlag.AlignTop
        )
        self.label.setStyleSheet(styles.text_style)
        self.label.setVisible(False)

        self.environment = os.environ["HOMEPATH"]
        self.dir = os.getcwd()

        self.textInput = QTextEdit()
        self.textInput.setStyleSheet(styles.text_edit_style)
        self.textInput.setPlaceholderText("Enter text here (280 character limit)")

        self.resolution_list = ["Resolution", "256", "512", "736"]
        self.numIterations_list = ["NumIterations", "400", "600", "800"]

        self.resolution_combobox = QComboBox()
        self.resolution_combobox.setStyleSheet(styles.combobox_style)
        self.resolution_combobox.addItems(self.resolution_list)
        self.resolution_combobox.setPlaceholderText("Resolution")

        self.numIterations_combobox = QComboBox()
        self.numIterations_combobox.setStyleSheet(styles.combobox_style)
        self.numIterations_combobox.addItems(self.numIterations_list)

        self.output_path_button = QPushButton("Output Path")
        self.output_path_button.setStyleSheet(styles.button_style)
        self.output_path_button.clicked.connect(self.modify_output_path)

        self.create_button = QPushButton("Save")
        self.create_button.setStyleSheet(styles.button_style)
        self.create_button.clicked.connect(self.timeout)

        self.reset_button = QPushButton("Reset")
        self.reset_button.setStyleSheet(styles.button_style)
        self.reset_button.clicked.connect(self.reset)

        self.placement()
        self.setLayout(self.layout)

    def reset(self):
        self.textInput.setText("")
        self.image.setPixmap(QtGui.QPixmap(""))
        self.resolution_combobox.setCurrentIndex(0)
        self.numIterations_combobox.setCurrentIndex(0)
        self.label.setVisible(False)

    def placement(self):
        h_box = QHBoxLayout()
        h_box.addWidget(self.output_path_button)
        h_box.addWidget(self.create_button)
        h_box.addWidget(self.reset_button)

        self.layout1.addWidget(self.textInput)
        self.layout1.addWidget(self.resolution_combobox)
        self.layout1.addWidget(self.numIterations_combobox)
        self.layout1.addLayout(h_box)
        self.layout1.addWidget(self.label)
        self.layout1.addWidget(self.image)
        self.layout1.addStretch()

        self.layout.addStretch()
        self.layout.addLayout(self.layout1)
        self.layout.addStretch()

    def timeout(self):
        global keywords
        keywords = custom_kw_extractor.extract_keywords(self.textInput.toPlainText())
        # print(keywords)
        if keywords == []:
            self.message_box(
                QMessageBox.Warning,
                QMessageBox.Ok,
                "Warning",
                "No keywords found. Please enter some text.",
            )
            return
        if self.textInput.toPlainText() == "":
            self.message_box(
                QMessageBox.Icon.Warning,
                QMessageBox.Ok,
                "Warning",
                "Please enter a valid text input.",
            )
        elif len(self.textInput.toPlainText()) > 280:
            self.message_box(
                QMessageBox.Icon.Warning,
                QMessageBox.Ok,
                "Warning",
                "There is a 280 character limit on the text input.",
            )
        elif self.resolution_combobox.currentText() == "Resolution":
            self.message_box(
                QMessageBox.Icon.Warning,
                QMessageBox.Ok,
                "Warning",
                "Please select a valid resolution.",
            )
        elif self.numIterations_combobox.currentText() == "NumIterations":
            self.message_box(
                QMessageBox.Icon.Warning,
                QMessageBox.Ok,
                "Warning",
                "Please select a valid number of iterations.",
            )
        else:
            self.timeout_subfunc()

    def timeout_subfunc(self):
        self.label.setVisible(True)
        self.message_box(
            QMessageBox.Icon.Information,
            QMessageBox.Ok,
            "Information",
            "Creating image process has been started.",
        )
        self.create_image()

        image = cv2.imread(os.path.join(self.dir, "artymind_output.png"))
  
        if self.resolution_combobox.currentText() == "256":
            reso_image = cv2.resize(image, (256, 256))
        if self.resolution_combobox.currentText() == "512":
            reso_image = cv2.resize(image, (512, 512))
        if self.resolution_combobox.currentText() == "736":
            reso_image = cv2.resize(image, (736, 736))
            
        cv2.imwrite(os.path.join(self.dir, "artymind_output.png"), reso_image)

    def create_image(self):
        word = keywords[0][0]
        # print(word)
        translated_word = translator.translate(word)
        print(translated_word.text)
        r = requests.post(
            "https://api.deepai.org/api/text2img",
            data={
                "text": translated_word.text,
            },
            headers={"api-key": "Enter your api-key here."},
        )

        # print(r.json())
        response = requests.get(r.json()["output_url"])
        with open(f"{self.dir}/artymind_output.png", "wb") as file:
            file.write(response.content)
        pixmap = QtGui.QPixmap(f"{self.dir}/artymind_output.png")
        self.image.setPixmap(pixmap)
        self.label.setVisible(False)
        self.message_box(
            QMessageBox.Information,
            QMessageBox.Ok,
            "Success",
            f"Image created as {self.dir}/artymind_output.png.",
        )

    def message_box(self, icon, buttons, title, text):
        msg = QMessageBox()
        msg.setIcon(icon)
        msg.setText(text)
        msg.setStandardButtons(buttons)
        msg.setWindowTitle(title)
        return msg.exec()

    def modify_output_path(self):
        self.temp_path = self.dir
        self.dir = QFileDialog.getExistingDirectory(
            None, "Select project folder:", self.environment, QFileDialog.ShowDirsOnly
        )
        if self.dir == "":
            self.dir = self.temp_path


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setStyleSheet("background-color: rgba(255, 255, 255, .1);")
        self.setGeometry(400, 200, 1200, 600)
        self.startMainMenu()

    def startMainMenu(self):
        self.window = Window(self)
        self.setWindowTitle("Artymind")
        self.setCentralWidget(self.window)
        self.showMaximized()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec())
