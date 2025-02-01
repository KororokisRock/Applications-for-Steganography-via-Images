import sys
from function import *

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('data\\01.ui', self)
        self.textEdit.append('Enter text here')
        self.pushButton_choose_image.clicked.connect(self.set_base_image)
        self.pushButton_crypto.clicked.connect(self.crypto_text)
        self.pushButton_choose_image_decrypto.clicked.connect(self.set_decrypto_image)
        self.pushButton_decrypto.clicked.connect(self.decrypto_text)
        self.pushButton_choose_keys.clicked.connect(self.set_keys_file)
        self.pushButton_export.clicked.connect(self.export_decrypto_text)
        self.path_base_image = ''
        self.path_decrypto_image = ''
        self.path_keys_file = ''

    def set_base_image(self):
        try:
            path = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
            if len(path) > 0:
                self.path_base_image = path
            self.label_path_base_image.setText('Selected picture: ' + self.path_base_image)
        except:
            self.label_path_base_image.setText('Selected picture: ' + self.path_base_image)

    def crypto_text(self):
        try:
            self.label_error_crypto.setText('')
            path = QFileDialog.getExistingDirectory(self, "Open Directory",
                                       "",
                                       QFileDialog.ShowDirsOnly
                                       | QFileDialog.DontResolveSymlinks)
            if self.path_base_image == '':
                self.label_error_crypto.setText('You did not select an image for encryption')
            else:
                self.label_error_crypto.setText('Progress...')
                stenography(path_keys=path, path_image_new=path, path_image_base=self.path_base_image, text=self.textEdit.toPlainText())
                self.label_error_crypto.setText('Ready')
        except:
            print('Error')

    def set_decrypto_image(self):
        try:
            path = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
            if len(path) > 0:
                self.path_decrypto_image = path
            self.label_path_decrypto_image.setText('Selected picture for decryption: ' + self.path_decrypto_image)
        except:
            self.label_path_decrypto_image.setText('Selected picture for decryption: ' + self.path_decrypto_image)

    def set_keys_file(self):
        try:
            path = QFileDialog.getOpenFileName(self, 'Open file', '')[0]
            if len(path) > 0:
                self.path_keys_file = path
            self.label_path_keys.setText('Selected key file: ' + self.path_keys_file)
        except:
            self.label_path_keys.setText('Selected key file: ' + self.path_keys_file)

    def decrypto_text(self):
        try:
            self.label_error_decrypto.setText("")
            if self.path_keys_file == '':
                self.label_error_decrypto.setText("You did not select a file with decryption keys")
            elif self.path_decrypto_image == '':
                self.label_error_decrypto.setText("You have not selected an image for decryption")
            else:
                self.label_error_decrypto.setText("Progress...")
                self.textEdit.setText(destenography(path_keys=self.path_keys_file, path_image=self.path_decrypto_image))
                self.label_error_decrypto.setText("Ready")
        except:
            self.label_error_decrypto.setText("Error")

    def export_decrypto_text(self):
        try:
            self.label_error_decrypto.setText("")
            path = QFileDialog.getSaveFileName(self, "Save F:xile",
                                       "",
                                       "All Files (*)")[0]
            if self.path_keys_file == '':
                self.label_error_decrypto.setText("You did not select a file with decryption keys")
            elif self.path_decrypto_image == '':
                self.label_error_decrypto.setText("You have not selected an image for decryption")
            else:
                self.label_error_decrypto.setText("Progress...")
                with open(path, 'w') as file:
                    file.write(destenography(path_keys=self.path_keys_file, path_image=self.path_decrypto_image))
                self.label_error_decrypto.setText("Ready")
        except:
            print('Error')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())

