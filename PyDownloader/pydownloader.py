from PyQt4.QtCore import *
from PyQt4.QtGui import *
import sys

import urllib.request


class Downloader(QDialog):
    def __init__(self):
        QDialog.__init__(self)

        layout = QVBoxLayout()  #detrmine box layout

        self.url = QLineEdit()
        self.save_location = QLineEdit()
        progress = QProgressBar()
        download = QPushButton("Download")
        browse = QPushButton("Browse")

        layout.addWidget(self.url)
        layout.addWidget(self.save_location)
        layout.addWidget(browse)
        layout.addWidget(progress)
        layout.addWidget(download)

        self.url.setPlaceholderText("URL")
        self.save_location.setPlaceholderText("File save location")

        progress.setValue(0)
        progress.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)

        self.setWindowTitle("PyDownloader")
        self.setFocus()

        download.clicked.connect(self.download)
        browse.clicked.connect(self.browse_file)

    def download(self):
        url = self.url.text()
        save_location = self.save_location.text()

        try:
            urllib.request.urlretrieve(url, save_location, self.report)
        except Exception:
            QMessageBox.warning(self, "Warning", "The download failed")
            return

        QMessageBox.information(self, "Information", "The download is complete")
        self.progress.setValue(0)
        self.url.setText("")
        self.save_location.setText("")

    def report(self, blocknum, blocksize, totalsize):
        readsofar = blocknum * blocksize
        if totalsize > 0:
            percent = readsofar * 100 / totalsize
            self.progress.setValue(int(percent))

    def browse_file(self):
        save_file = QFileDialog.getSaveFileName(self,caption= "Save File As", directory=".",
                                                filter="All Files(*.*)")

        self.save_location.setText(QDir.toNativeSeparators(save_file))


app = QApplication(sys.argv)
dialog = Downloader()
dialog.show()
app.exec_()
