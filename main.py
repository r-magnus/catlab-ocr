# main.py
# Main location for data recovery based on OCR for salvaging info from images.
# @author Ryan Magnuson rmagnuson@westmont.edu

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

# Create Reader
ocr = easyocr.Reader(['en']) # TODO: Only run this line once! (allegedly)
result = ocr.readtext('images/'+'test.jpg')

print(result)
# Spell Checker
sc = Speller(only_replacements=True)