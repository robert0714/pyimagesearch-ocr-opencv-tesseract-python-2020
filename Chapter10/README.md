# OCR’ing Business Cards
* https://pyimagesearch.com/2021/11/03/ocring-business-cards/
* https://asprise.com/receipt-ocr/blog-github-python-receipt-ocr-api-library-free-example-code-open-source
* https://stackoverflow.com/questions/68891423/finding-the-coordinates-of-the-edges-on-a-rectangluar-object
* https://github.com/thucdx/business_card_detection
* https://github.com/situmorang-com/OCR-business-card-python

To follow this guide, you need to have the OpenCV library installed on your system.

Luckily, OpenCV is pip-installable:
```bash
$ pip install opencv-contrib-python scipy  pytesseract tesseract-ocr 
```

## Business Card OCR Results
We are now ready to apply OCR to business cards. Open a terminal and execute the following command:

```bash
$ python ocr_business_card.py --image tony_stark.png --debug 1
PHONE NUMBERS
=============
562-555-0100
562-555-0150
EMAILS
======
NAME/JOB TITLE
==============
Tony Stark
Chief Executive Officer
Stark Industries
```
Figure 3 (top) shows the results of our business card localization. Notice how we have correctly detected the business card in the input image.

Once we have the top-down view of the image (typically required to obtain higher OCR accuracy), we can apply Tesseract to OCR it, the results of which can be seen in our terminal output above.

Note that our script has successfully extracted both phone numbers on Tony Stark’s business card.

No email addresses are reported as there is no email address on the business card.

We then have the name and job title displayed as well. It’s interesting that we can OCR all the text successfully because the text of the name is more distorted than the phone number text. Our perspective transform dealt with all the text effectively even though the amount of distortion changes as you go further away from the camera. That’s the point of perspective transform and why it’s important to the accuracy of our OCR.

Let’s try another example image, this one of an old Larry Page (co-founder of Google) business card:
```bash
$ python ocr_business_card.py --image larry_page.png --debug 1
PHONE NUMBERS
=============
650 330-0100
650 618-1499
EMAILS
======
larry@google.com
NAME/JOB TITLE
==============
Larry Page
CEO
Google
```
