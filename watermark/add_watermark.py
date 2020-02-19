# Code adapted from
#
# https://www.life2coding.com/how-to-add-logo-or-image-watermark-on-images-with-opencv-python/
	
import os
import pathlib
import sys
 
import cv2 as cv

LOGO_FILEPATH = os.path.join(os.path.dirname(__file__), "made@makespace_logo.png")
OPACITY = 0.3

def transparent_overlay(img, overlay, pos, scale = 1):
    src = img.copy()
    overlay = cv.resize(overlay, (0, 0), fx=scale, fy=scale)
    h, w, _ = overlay.shape  # Size of foreground
    rows, cols, _ = src.shape  # Size of background Image
    y, x = pos[0], pos[1]  # Position of foreground/overlay image
 
    # loop over all pixels and apply the blending equation
    for i in range(h):
        for j in range(w):
            if x + i >= rows or y + j >= cols:
                continue
            alpha = float(overlay[i][j][3] / 255.0)  # read the alpha channel
            src[x + i][y + j] = alpha * overlay[i][j][:3] + (1 - alpha) * src[x + i][y + j]
            
    return src
 
def add_watermark(img_filepath, logo_filepath, opacity):

    if not os.path.exists(img_filepath):
        raise ValueError("Image filepath missing: '%s'" % img_filepath)

    if not os.path.exists(logo_filepath):
        raise ValueError("Logo filepath missing: '%s'" % logo_filepath)
    
    img = cv.imread(img_filepath, -1)
    img_h, img_w, _ = img.shape
    
    logo = cv.imread(logo_filepath, -1)
    logo_h, logo_w, _ = logo.shape

    # resize the logo to take half the width or height, whichever is smaller
    new_logo_w = round(min(img_w / 2, img_h / 2 * logo_w / logo_h))
    new_logo_h = round(new_logo_w * logo_h / logo_w)
    new_logo = cv.resize(logo, (new_logo_w, new_logo_h), interpolation = cv.INTER_AREA)
    
    # Calculate position in center
    pos_x = round((img_w - new_logo_w) / 2)
    pos_y = round((img_h - new_logo_h) / 2)
 
    overlay = transparent_overlay(img, new_logo, pos = (pos_x, pos_y))

    # apply the overlay
    output = img.copy()
    cv.addWeighted(overlay, opacity, output, 1 - opacity, 0, output)
 
    path = pathlib.Path(img_filepath)
    new_filepath = os.path.join(path.parents[0], path.stem + "_makespace" + path.suffix)

    cv.imwrite(new_filepath, output)
    return new_filepath

def main():
    new_filepath = add_watermark(img_filepath = sys.argv[1], logo_filepath = LOGO_FILEPATH, opacity = OPACITY)
    print("Added watermark at '%s'" % new_filepath)
 
if '__main__' == __name__:
    main()
