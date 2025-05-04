import numpy as np
import pywt
import cv2
import matplotlib.pyplot as plt


#stackover flow and modifed also by GPT

def w2d(img, mode='haar', level=1):
    # Convert to grayscale
    img_gray = cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
    
    # Convert to float and normalize
    img_gray = np.float32(img_gray)
    img_gray /= 255.0

    # Compute wavelet coefficients (ensure the correct wavelet argument)
    coeffs = pywt.wavedec2(img_gray, wavelet=mode, level=level)

    # Zero out the approximation coefficients (keep only detail coefficients)
    coeffs_H = list(coeffs)
    coeffs_H[0] *= 0

    # Reconstruct the image using only detail coefficients
    img_reconstructed = pywt.waverec2(coeffs_H, wavelet=mode)
    img_reconstructed *= 255
    img_reconstructed = np.uint8(np.clip(img_reconstructed, 0, 255))

    return img_reconstructed



