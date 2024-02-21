# OCR’ing a Document, Form, or Invoic
* https://pyimagesearch.com/2020/09/07/ocr-a-document-form-or-invoice-with-tesseract-opencv-and-python/

## Official 2020 IRS W-4 form
https://www.irs.gov/pub/irs-prior/fw4--2020.pdf
https://www.irs.gov/pub/irs-pdf/fw4.pdf

## Convert the form_w4.png from a PDF file
```bash
choco install -y imagemagick.app

convert form_w4.pdf form_w4.png
```



## Content
Inside the project folder, you’ll find three images:
* ``scans/scan_01.jpg``: An example IRS W-4 document that has been filled with my real name but fake tax data.
* ``scans/scan_02.jpg``: A similar example IRS W-4 document that has been populated with fake tax information.
* ``form_w4.png``: The official 2020 IRS W-4 form template. This empty form does not have any information entered into it. We need it and the field locations so that we can line up the scans and ultimately extract information from the scans. We’ll manually determine the field locations with an external photo editing/previewing application.

And we have just a single Python driver script to review: ``ocr_form.py``. This form parser relies on two helper functions:
* ``align_images``: Contained within the alignment submodule and was first introduced in Chapter06. We won’t be reviewing this method again this week, so be sure to refer to my previous tutorial if you missed it!
* ``cleanup_text``: This function is presented at the top of our driver script and simply eliminates non-ASCII characters detected by OCR (I’ll share more about this function in the next section).

## OCR results using OpenCV and Tesseract
```bash
$ python ocr_form.py --image scans/scan_01.jpg --template form_w4.png
[INFO] loading images...
[INFO] aligning images...
[INFO] OCR'ing document...
step1_first_name
================
Adrian


step1_last_name
===============
Rosebrock


step1_address
=============
PO Box 17598 #17900


step1_city_state_zip
====================
Baltimore, MD 21297-1598


step5_employee_signature
========================
Adrian Rosebrock


step5_date
==========
2020/06/10


employee_name_address
=====================
PylmageSearch
PO BOX 1234
Philadelphia, PA 19019


employee_ein
============
12-3456789
```
## Reference
* https://github.com/shejz/OCR
* https://github.com/Kasra1377/document-invoice
* https://github.com/alexngun/OCR
* https://github.com/garrlicbread/OCR-Invoice-Detection/
* https://github.com/dloperab/PyImageSearch-CV-DL-CrashCourse
