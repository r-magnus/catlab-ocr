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
# TODO: Implement image sharpening to improve OCR accuracy.
# NOTE: Making a manual list of images that need sharpening will probably be best

# File Writing
def write_page(page):
  """
  Given a list of lines, opens a new .txt and writes each line.
  :param page: List of lines to write. Also serves as .txt file name.
  """
  file = open("pages/%s.txt" % (page[0].replace(".jpg", "").replace("000", "")), 'w')
  for line in page:
    file.write(line + "\n")
  file.close()

# Main Reader
ocr = easyocr.Reader(['en'])
path = "images/"
for box in sorted(os.listdir(path)):
  print("Box: %s" % (box)) # debug sout

  path = "images/"
  path = path + box + "/"
  for img in sorted(os.listdir(path)):
    print("File: %s" % (img)) # debug sout

    result = ocr.readtext(path + img, detail=0, text_threshold=.6, width_ths=.1, paragraph=True,
                          contrast_ths=.1, decoder="greedy",
                          ) # NOTE: ~4.73sec per page
    result.insert(0, str(img).replace("000", ""))
    # NOTE: If 'paragraph=True' doesn't always work, do manual sort with bounding boxes (detail=1)
    print("Content: %s" % (result)) # debug sout

    # pages.append(result)
    write_page(result)

    # Spell Check (CURRENTLY VERY INACCURATE)
    # sc = SpellChecker() # only_replacements=True
    # checked = []
    # for section in result:
    #   checked.append(sc.correction(section))
    # print(checked)

    if input('> ') == 'q': break # manual delay
