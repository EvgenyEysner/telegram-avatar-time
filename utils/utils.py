from datetime import datetime

import cv2  # https://pypi.org/project/opencv-python/
import numpy as np


# convert the time to a string
def convert_time_to_string(dt):
    return f"{dt.hour}:{dt.minute:02}"


# if the time changes
def time_has_changed(prev_time):
    return convert_time_to_string(datetime.now()) != convert_time_to_string(prev_time)


# I create an array with zeros 500 x 500
def get_black_background():
    return np.zeros((500, 500))


def generate_time_image_bytes(dt):
    """
    every minute I create a new photo
    text quotas horizontally multiplied by the shift (int(image.shape[0]*0.35)
    and the same for the vertical int(image.shape[1]*0.5)
    1.5 is the font size
    3 - line width
    """
    text = convert_time_to_string(dt)
    image = get_black_background()
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(image, text, (int(image.shape[0] * 0.35), int(image.shape[1] * 0.5)), font, 1.5, (255, 255, 0), 3,
                cv2.LINE_AA)
    _, bts = cv2.imencode('.jpg', image)
    return bts.tobytes()
