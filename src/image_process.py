import cv2
import numpy as np


def _find_exterior_contours(img):
    ret = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    if len(ret) == 2:
        return ret[0]
    elif len(ret) == 3:
        return ret[1]
    raise Exception("Check the signature for `cv2.findContours()`.")


def get_bubble(image, point):
    x, y = point
    h, w = image.shape[:2]
    mask = np.zeros((h + 2, w + 2), np.uint8)
    connectivity = 4
    tolerance = (12,) * 3
    flood_fill_flags = (
            connectivity | cv2.FLOODFILL_FIXED_RANGE | cv2.FLOODFILL_MASK_ONLY | 255 << 8
    )  # 255 << 8 tells to fill with the value 255
    cv2.floodFill(image, mask, (int(x), int(y)), (0, 0, 0), tolerance, tolerance, flood_fill_flags)
    mask = mask[1:-1, 1:-1].copy()

    image_cleaned = image.copy()
    contours = _find_exterior_contours(mask)
    cv2.drawContours(image_cleaned, contours, -1, color=(255, 255, 255), thickness=-1)
    x, y, w, h = cv2.boundingRect(mask)
    roi = (y, y + h, x, x + w)
    image_roi = image[y:y + h, x:x + w]
    image_cleaned = image_cleaned[y:y + h, x:x + w]

    return image_roi, image_cleaned, roi
