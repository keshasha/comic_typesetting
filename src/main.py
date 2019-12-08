import sys
import os
import cv2
import numpy as np

from PyQt5 import QtGui, QtWidgets
from PyQt5.QtCore import pyqtSlot, Qt
from PyQt5.QtGui import QPixmap, QImage
from PyQt5.QtWidgets import QGraphicsScene, QDialog

from src.ui.ui_main import Ui_Dialog

from src.image_process import get_bubble
from src.custom_item_widget import item
from src.utils import check_image_file, open_dir

DEBUG = 0

# TODO: font size
# TODO: custom selection
# TODO: black background
# TODO: load zip file
# TODO: recent opened
# TODO: each page and items keep together
# TODO: Change to MVC model
# TODO: using database


class Form(QDialog):

    class CustomScene(QGraphicsScene):
        def __init__(self, mainForm):
            QGraphicsScene.__init__(self)
            self.mainForm = mainForm

        def mousePressEvent(self, e) -> None:
            x = e.scenePos().x()
            y = e.scenePos().y()
            image = self.mainForm.images[self.mainForm.page]

            if self.mainForm.select_mode:
                image_roi, image_cleaned, roi = get_bubble(image, (x, y))
                widget = item(image_roi, image_cleaned, roi, self.mainForm)
                itemN = QtWidgets.QListWidgetItem()
                itemN.setSizeHint(widget.sizeHint())
                self.mainForm.ui.listWidget.addItem(itemN)
                self.mainForm.ui.listWidget.setItemWidget(itemN, widget)
                self.mainForm.ui.listWidget.scrollToBottom()

            self.mainForm.load_image_on_scene()

    def __init__(self, parent=None):
        QDialog.__init__(self, parent)

        self.loaded = False
        self.dir_name = None
        self.images = []
        self.file_name = []
        self.num_images = 0
        self.page = 0

        self.zoom = 1

        self.select_mode = True

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()

        # Graphics view
        # self.scene = QGraphicsScene(parent=self)  # parent 없이 종료시 crash
        self.scene = self.CustomScene(mainForm=self)
        self.ui.graphicsView.setScene(self.scene)

        # signal 연결
        self.ui.pushButton.clicked.connect(self.open_images)
        self.ui.pushButton_save.clicked.connect(self.save)
        self.ui.pushButton_next.clicked.connect(self.next_image)
        self.ui.pushButton_prev.clicked.connect(self.prev_image)
        self.ui.pushButton_originalsize.clicked.connect(self.originalsize_image)
        self.ui.pushButton_fit.clicked.connect(self.fit_image)
        self.ui.pushButton_select.clicked.connect(self.select_toggle)

        self.ui.pushButton_selectall.clicked.connect(self.selectall)
        self.ui.pushButton_deselectall.clicked.connect(self.deselect)

        # mouse 사용
        self.setMouseTracking(True)

        if DEBUG:
            self.select_mode = True

            # open test folder
            dir_name = '/Users/jongha/Documents/your name 1'
            files_list = os.listdir(dir_name)
            files_list = sorted(files_list)
            for file in files_list:
                if check_image_file(file):
                    self.file_name.append(file)
                    # image = QPixmap(dir_name + "/" + file)
                    image = cv2.imread(dir_name + "/" + file)
                    self.images.append(image)
                    print("{} is loaded.".format(file))
            self.num_images = len(self.images)
            self.loaded = True
            self.load_image_on_scene()


    @pyqtSlot()
    def save(self):
        if self.dir_name:
            dir_save_name = self.dir_name + '_edited'
            try:
                os.mkdir(dir_save_name)
            except OSError:
                print("Creation of the directory %s failed" % dir_save_name)
            else:
                print("Successfully created the directory %s " % dir_save_name)

            for i, image in enumerate(self.images):
                cv2.imwrite(dir_save_name + '/' + self.file_name[i], image)

    @pyqtSlot()
    def open_images(self):
        # open_file()
        dir_name = open_dir()
        self.dir_name = dir_name
        if dir_name:
            self.images.clear()
            self.file_name.clear()
            files_list = os.listdir(dir_name)
            files_list = sorted(files_list)
            for file in files_list:
                if check_image_file(file):
                    self.file_name.append(file)
                    # image = QPixmap(dir_name + "/" + file)
                    image = cv2.imread(dir_name + "/" + file)
                    self.images.append(image)
                    print("{} is loaded.".format(file))
            self.num_images = len(self.images)
            self.loaded = True
            self.load_image_on_scene()

    @pyqtSlot()
    def next_image(self):
        if self.loaded and (self.page < self.num_images - 1):
            self.page += 1
            self.scene.clear()
            self.ui.listWidget.clear()
            self.load_image_on_scene()

    @pyqtSlot()
    def prev_image(self):
        if self.loaded and self.page > 0:
            self.page -= 1
            self.scene.clear()
            self.ui.listWidget.clear()
            self.load_image_on_scene()

    @pyqtSlot()
    def originalsize_image(self):
        self.ui.graphicsView.resetTransform()

    @pyqtSlot()
    def fit_image(self):
        if self.images:
            self.ui.graphicsView.fitInView(self.scene.sceneRect(), Qt.KeepAspectRatio)

    @pyqtSlot()
    def selectall(self):
        self.ui.listWidget.selectAll()

    @pyqtSlot()
    def deselect(self):
        self.ui.listWidget.clearSelection()

    @pyqtSlot()
    def select_toggle(self):
        self.select_mode = not self.select_mode

    def load_image_on_scene(self, image=None):
        if image == None:
            image = self.images[self.page]
            image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            height, width, channel = image.shape
            bytesPerLine = 3 * width
            qImg = QImage(image.data, width, height, bytesPerLine, QImage.Format_RGB888)
            image = QPixmap.fromImage(qImg)
            self.scene.addPixmap(image)
            self.scene.update()
            self.fit_image()

            self.ui.label_filename.setText("{}  {}/{}".format(self.file_name[self.page], self.page+1, self.num_images))

    def wheelEvent(self, event):
        modifiers = QtWidgets.QApplication.keyboardModifiers()
        if modifiers == Qt.ControlModifier:
            if event.angleDelta().y() > 0:
                zoom = 1.1
            else:
                zoom = 0.9
            self.ui.graphicsView.scale(zoom, zoom)

    def keyPressEvent(self, e):
        key = e.key()
        if key == Qt.Key_F:
            self.fit_image()
        elif key == Qt.Key_Right:
            self.next_image()
        elif key == Qt.Key_Left:
            self.prev_image()
        elif key == Qt.Key_Delete:
            items = self.ui.listWidget.selectedItems()
            if items:
                for item in items:
                    self.ui.listWidget.takeItem(self.ui.listWidget.row(item))

    def mousePressEvent(self, e: QtGui.QMouseEvent) -> None:

        pass

    def resizeEvent(self, event):
        self.fit_image()


def main():
    app = QtWidgets.QApplication(sys.argv)
    w = Form()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
