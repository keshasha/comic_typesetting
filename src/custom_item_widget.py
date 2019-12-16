import cv2

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot, QRectF, QRect, QSize
from PyQt5.QtGui import QColor, QImage, QPainter, QPixmap, QFont
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem, QGraphicsPixmapItem

from utils import mat2qpixmap, ocr_core, qimage2mat

from ui.ui_item import Ui_Form


class item(QtWidgets.QWidget):
    def __init__(self, image_origin=None, image_cleaned=None, roi=None, mainForm=None):
        super(item, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        if image_cleaned is not None:
            self.image = image_cleaned
        else:
            self.image = image_origin
        self.roi = roi
        self.mainForm = mainForm

        self.posX_default = 0
        self.posY_default = 0

        self.font = QFont()

        scene_origin = QGraphicsScene()
        qpixmap_origin = mat2qpixmap(image_origin)
        scene_origin.addPixmap(qpixmap_origin)
        scene_origin.update()
        self.ui.graphicsView_origin.setScene(scene_origin)

        self.scene_edit = QGraphicsScene()
        self.qPixmap = mat2qpixmap(self.image)
        self.scene_edit.addPixmap(self.qPixmap)
        self.scene_edit.update()
        self.ui.graphicsView_edit.setScene(self.scene_edit)

        txt = ocr_core(image_origin)
        self.ui.textEdit_ocr.setText(txt)

        # signal
        self.ui.textEdit_edit.textChanged.connect(self.texting)
        self.ui.pushButton_apply.clicked.connect(self.render_image)
        self.ui.pushButton_left.clicked.connect(lambda: self.move_text('left'))
        self.ui.pushButton_right.clicked.connect(
            lambda: self.move_text('right'))
        self.ui.pushButton_fontlarger.clicked.connect(
            lambda: self.text_size(1))
        self.ui.pushButton_fontsmaller.clicked.connect(
            lambda: self.text_size(-1))

    @pyqtSlot()
    def texting(self):
        # image = self.image.copy()
        # cv2.putText(image,
        #             self.ui.textEdit_edit.toPlainText(),
        #             (10, 10),
        #             cv2.FONT_HERSHEY_SIMPLEX,
        #             0.6, (0, 0, 0), lineType=cv2.LINE_AA)
        # qpixmap = mat2qpixmap(image)
        # self.scene_edit.clear()
        # self.scene_edit.addPixmap(qpixmap)
        # self.scene_edit.update()

        text = self.ui.textEdit_edit.toPlainText()

        self.scene_edit.clear()
        self.scene_edit.addPixmap(self.qPixmap)
        qText = QGraphicsTextItem()
        qText.setDefaultTextColor(QColor(0, 0, 0))
        qText.setPlainText(text)
        qText.setFont(self.font)

        qPixmapWidth = self.qPixmap.width()
        qTextWidth = qText.boundingRect().width()
        qPixmapHeight = self.qPixmap.height()
        qTextHeigt = qText.boundingRect().height()

        posX = (qPixmapWidth - qTextWidth) / 2 + self.posX_default
        posY = (qPixmapHeight - qTextHeigt) / 2 + self.posY_default

        qText.setPos(posX, posY)

        self.scene_edit.addItem(qText)
        self.scene_edit.update()

    @pyqtSlot()
    def move_text(self, direction, distance=5):
        if direction == 'left':
            self.posX_default -= distance
        elif direction == 'right':
            self.posX_default += distance
        elif direction == 'up':
            self.posY_default -= distance
        elif direction == 'down':
            self.posY_default += distance

        self.texting()

    @pyqtSlot()
    def render_image(self):
        # qimage = QImage(self.qPixmap.size(), QImage.Format_ARGB32_Premultiplied)
        qimage = QImage(self.qPixmap.size(), QImage.Format_RGB32)
        painter = QPainter(qimage)
        self.scene_edit.render(painter, QRectF(
            qimage.rect()), QRectF(self.qPixmap.rect()))
        painter.end()

        qpixmap = QPixmap.fromImage(qimage)
        qpixmapItem = QGraphicsPixmapItem(qpixmap)
        qpixmapItem.setPos(self.roi[2], self.roi[0])
        self.mainForm.scene.addItem(qpixmapItem)

        mainImage = self.mainForm.images[self.mainForm.page]
        qimage = QImage(
            QSize(mainImage.shape[1], mainImage.shape[0]), QImage.Format_RGB32)
        painter = QPainter(qimage)

        self.mainForm.scene.render(painter,
                                   QRectF(qimage.rect()),
                                   QRectF(QRect(0, 0, mainImage.shape[1], mainImage.shape[0])))
        painter.end()
        image = qimage2mat(qimage)
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.mainForm.images[self.mainForm.page] = image

    @pyqtSlot()
    def text_size(self, scaler):
        self.font.setPointSize(self.font.pointSize()+scaler)
        self.texting()
