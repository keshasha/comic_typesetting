import cv2
import numpy as np
file_name = '/Users/jongha/Documents/your name 1/0000.jpg'


def _find_exterior_contours(img):
    ret = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(ret) == 2:
        return ret[0]
    elif len(ret) == 3:
        return ret[1]
    raise Exception("Check the signature for `cv.findContours()`.")


def mouse_event(event, x, y, flags, params):
    global img
    if event == cv2.EVENT_LBUTTONDOWN:
        print("{}, {}".format(x, y))
        h, w = img.shape[:2]
        mask = np.zeros((h + 2, w + 2), np.uint8)
        connectivity = 4
        tolerance = (25,)*3
        flood_fill_flags = (
                connectivity | cv2.FLOODFILL_FIXED_RANGE | cv2.FLOODFILL_MASK_ONLY |  255 << 8
        )  # 255 << 8 tells to fill with the value 255
        cv2.floodFill(img, mask, (int(x), int(y)), (0,0,0), tolerance, tolerance, flood_fill_flags)
        mask = mask[1:-1, 1:-1].copy()
        viz = img.copy()
        contours = _find_exterior_contours(mask)
        viz = cv2.drawContours(viz, contours, -1, color=(255, 0, 0), thickness=-1)
        # viz = cv2.addWeighted(img, 0.75, viz, 0.25, 0)
        # viz = cv2.drawContours(viz, contours, -1, color=(255,) * 3, thickness=1)
        # cv2.imshow('w', viz)

        x, y, w, h = cv2.boundingRect(mask)
        cv2.rectangle(viz, (x,y),(x+w,y+h), (0,0,255), 2)
        cv2.imshow('w', viz)


def main():
    global img
    img = cv2.imread(file_name)
    # img = cv2.GaussianBlur(img, (5,5), 1)

    cv2.namedWindow("w")
    cv2.setMouseCallback("w", mouse_event)
    cv2.imshow('w', img)
    cv2.waitKey()
    cv2.destroyAllWindows()


if __name__ == '__main__':
    main()
