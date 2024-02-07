# Automatically OCR’ing Receipts and Scans
* https://pyimagesearch.com/2021/10/27/automatically-ocring-receipts-and-scans/
* https://asprise.com/receipt-ocr/blog-github-python-receipt-ocr-api-library-free-example-code-open-source
* https://stackoverflow.com/questions/68891423/finding-the-coordinates-of-the-edges-on-a-rectangluar-object

To follow this guide, you need to have the OpenCV library installed on your system.

Luckily, OpenCV is pip-installable:
```bash
$ pip install opencv-contrib-python scipy  pytesseract tesseract-ocr 
```

## Receipt Scanner and OCR Results

```bash
$ python scan_receipt.py --image whole_foods.jpg
[INFO] raw output:
==================
WHOLE
FOODS
WHOLE FOODS MARKET - WESTPORT, CT 06880
399 POST RD WEST - (203) 227-6858
365 BACON LS NP 4.99
365 BACON LS NP 4.99
365 BACON LS NP 4.99
365 BACON LS NP 4.99
BROTH CHIC NP 4.18
FLOUR ALMOND NP 11.99
CHKN BRST BNLSS SK NP 18.80
HEAVY CREAM NP 3 7
BALSMC REDUCT NP 6.49
BEEF GRND 85/15 NP 5.04
JUICE COF CASHEW C NP 8.99
DOCS PINT ORGANIC NP 14.49
HNY ALMOND BUTTER NP 9.99
eee TAX .00 BAL 101.33
```

The raw output of the Tesseract OCR engine can be seen in our terminal. By specifying ``--psm 4``, Tesseract has been able to OCR the receipt line-by-line, capturing both items:

* name/description
* price

## Tesseract
https://kaichenlab.medium.com/%E5%AF%A6%E7%94%A8%E5%BF%83%E5%BE%97-tesseract-ocr-eef4fcd425f0
```bash
tesseract -l chi_tra 1234.png  1234 --psm 6
```
 