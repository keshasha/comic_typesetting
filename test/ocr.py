import pytesseract as ocr
import cv2

file_name = '0.jpg'


def ocr_core(image):
    text = ocr.image_to_string(image, lang='eng+deu')
    return ' '.join(text.split())


def main():
    img = cv2.imread(file_name)

    txt = ocr_core(img)
    print(txt)

    # cv2.imshow('w', img)
    # cv2.waitKey()


if __name__ == '__main__':
    main()

