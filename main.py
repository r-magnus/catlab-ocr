# main.py
# Main location for data recovery based on OCR for salvaging info from images.
# @author Ryan Magnuson rmagnuson@westmont.edu

# DOCUMENTATION: https://www.jaided.ai/easyocr/documentation/

# TODO: EasyOCR is big. Use the following to remove:
# pip uninstall easyocr
#
# Large Packages: (specific)
# torch-2.3.0-cp312-cp312-manylinux1_x86_64.whl (779.1 MB)
# nvidia_cublas_cu12-12.1.3.1-py3-none-manylinux1_x86_64.whl (410.6 MB)
# nvidia_cudnn_cu12-8.9.2.26-py3-none-manylinux1_x86_64.whl (731.7 MB)

# Setup
import easyocr
import os
# from autocorrect import Speller
from spellchecker import SpellChecker

# Image Sharpening
# WIP

# Main Reader
ocr = easyocr.Reader(['en'])
path = "images/"
for box in os.listdir(path):
  path = path + box + "/"
  for img in os.listdir(path):
    result = ocr.readtext(path + img, detail=0, text_threshold=.6, width_ths=.1, paragraph=True)
    # NOTE: If 'paragraph=True' doesn't always work, do manual sort with bounding boxes (detail=1)
    print(result)

    # Spell Check (CURRENTLY VERY INACCURATE)
    # sc = SpellChecker() # only_replacements=True
    # checked = []
    # for section in result:
    #   checked.append(sc.correction(section))
    # print(checked)

    input() # manual delay
