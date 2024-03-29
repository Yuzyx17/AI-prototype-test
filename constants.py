"""
THIS FILE IS FOR GLOBAL VARIABLES
"""

NUM_DATA_GEN = 10
IMAGE_PATH = f'dataset/images/'
ANNOT_PATH = f'dataset/annotations/'
MODEL_PATH = f'model'

MODEL = f'{MODEL_PATH}/roi_extraction_model.h5'
TESSERACT = r'D:\Program Files\Tesseract-OCR\tesseract.exe'
FILE_NAME = f'graph-'
IMAGE_EXT = ".png"
ANNOT_EXT = ".xml"

IMG = "{pth}{fn}{idx}{ext}".format(pth=IMAGE_PATH, fn=FILE_NAME, ext=IMAGE_EXT, idx="{}")
ANT = "{pth}{fn}{idx}{ext}".format(pth=ANNOT_PATH, fn=FILE_NAME, ext=ANNOT_EXT, idx="{}")
