import pytesseract as ocr
import cv2
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtWidgets import QFileDialog


def ocr_core(image):
    text = ocr.image_to_string(image, lang='eng+deu')
    return ' '.join(text.split())


def open_dir() -> str:
    dir_name = QFileDialog.getExistingDirectory()
    return dir_name


def open_file():
    file_name, _ = QFileDialog.getOpenFileName()
    if file_name:
        return file_name
    else:
        return None


def check_image_file(filename: str) -> bool:
    image_ext = ['jpg', 'jpeg', 'bmp', 'png', 'gif']
    return filename.split('.')[-1] in image_ext


def mat2qpixmap(img):
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    height, width, channel = img.shape
    bytesPerLine = 3 * width
    qImg = QImage(img.data, width, height, bytesPerLine, QImage.Format_RGB888)
    qpixmap = QPixmap.fromImage(qImg)
    return qpixmap