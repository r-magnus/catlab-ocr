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
from autocorrect import Speller

# Improve Image Quality
# WIP

# Create Reader
ocr = easyocr.Reader(['en'])
result = ocr.readtext('images/'+'westmont_catalog_5.jpg', detail=0, text_threshold=.6, width_ths=.5)

print(result)

# Spell Checker
# sc = Speller(only_replacements=True)
# checked_result = []
#
# for unchecked in result:
#   checked_result.append(sc(unchecked))
#
# print(checked_result)