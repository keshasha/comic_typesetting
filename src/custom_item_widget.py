import cv2

from PyQt5 import QtWidgets
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QGraphicsScene, QGraphicsTextItem

from src.utils import mat2qpixmap, ocr_core

from src.ui.ui_item import Ui_Form


class item(QtWidgets.QWidget):
    def __init__(self, image_origin=None, image_cleaned=None, roi=None):
        super(item, self).__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.image = image_cleaned
        self.roi = roi

        scene_origin = QGraphicsScene()
        qpixmap_origin = mat2qpixmap(image_origin)
        scene_origin.addPixmap(qpixmap_origin)
        scene_origin.update()
        self.ui.graphicsView_origin.setScene(scene_origin)

        self.scene_edit = QGraphicsScene()
        self.qPixmap = mat2qpixmap(image_cleaned)
        self.scene_edit.addPixmap(self.qPixmap)
        self.scene_edit.update()
        self.ui.graphicsView_edit.setScene(self.scene_edit)

        txt = ocr_core(image_origin)
        self.ui.textEdit_ocr.setText(txt)

        self.ui.textEdit_edit.textChanged.connect(self.texting)

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

        qPixmapWidth = self.qPixmap.width()
        qTextWidth = qText.boundingRect().width()
        qPixmapHeight = self.qPixmap.height()
        qTextHeigt = qText.boundingRect().height()

        posX = (qPixmapWidth - qTextWidth) / 2
        posY = (qPixmapHeight - qTextHeigt) / 2

        qText.setPos(posX,posY)

        self.scene_edit.addItem(qText)
        self.scene_edit.update()
