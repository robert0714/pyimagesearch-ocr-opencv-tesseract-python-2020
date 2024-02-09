# OCR'ing License Plates with ANPR/ALPR
* https://pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/ 

To follow this guide, you need to have the OpenCV library installed on your system.

Luckily, OpenCV is pip-installable:
```bash
$ pip install opencv-contrib-python scipy  imutils scikit-image pytesseract tesseract-ocr 
```

## File Structures
* **license_plates**: Directory containing two sub-directories of [JPG images](https://github.com/NanoNets/number-plate-detection.git)
* **anpr.py**: Contains the PyImageSearchANPR class responsible for localizing license/number plates and performing OCR
* **ocr_license_plate.py**: Our main driver Python script, which uses our PyImageSearchANPR class to OCR entire groups of images

## Implementing ANPR/ALPR with OpenCV and Python
* Open anpr.py and let’s get to work reviewing the script.
* Our ``PyImageSearchANPR`` class begins on **Line 8**. The constructor accepts three parameters:
  * **minAR**: The minimum aspect ratio used to detect and filter rectangular license plates, which has a default value of ``4``
  * **maxAR**: The maximum aspect ratio of the license plate rectangle, which has a default value of ``5``
  * **debug**: A flag to indicate whether we should display intermediate results in our image processing pipeline
 
## Debugging our computer vision pipeline
With our constructor ready to go, let’s define a helper function to display results at various points in the imaging pipeline when in **debug** mode: 

Our helper function ``debug_imshow`` (**Line 16**) accepts three parameters:

* title: The desired OpenCV window title. Window titles should be unique; otherwise OpenCV will replace the image in the same-titled window rather than creating a new one.
* image: The image to display inside the OpenCV GUI window.
* waitKey: A flag to see if the display should wait for a keypress before completing.

## Locating potential license plate candidates
Our locate_license_plate_candidates expects two parameters:

* **gray**: This function assumes that the driver script will provide a grayscale image containing a potential license plate.
* **keep**: We’ll only return up to this many sorted license plate candidate contours.

## Pruning license plate candidates
Our locate_license_plate function accepts three parameters:
* **gray**: Our input grayscale image
* **candidates**: The license plate contour ``candidates`` returned by the previous method in this class
* **clearBorder**: A boolean indicating whether our pipeline should eliminate any contours that touch the edge of the image

Before we begin looping over the license plate contour ``candidates``, first we initialize variables that will soon hold our license plate contour (lpCnt) and license plate region of interest (``roi``) on **Lines 87 and 88**.

Starting on **Line 91**, our loop begins. This loop aims to isolate the contour that contains the license plate and extract the region of interest of the license plate itself. We proceed by determining the bounding box rectangle of the contour, ``c`` (**Line 94**).

Computing the aspect ratio of the contour’s bounding box (**Line 95**) will help us ensure our contour is the proper rectangular shape of a license plate.

## ANPR results with OpenCV and Python
We are now ready to apply Automatic License/Number Plate Recognition using OpenCV and Python.

```bash
$ python ocr_license_plate.py --input license_plates/group1
[INFO] MH15TC584
[INFO] KL55R2473
[INFO] MH20EE7601
[INFO] KLO7BF5000
[INFO] HR26DA2330
```

Let’s try another set of images, this time where our ANPR solution doesn’t work as well:

```bash
$ python ocr_license_plate.py --input license_plates/group2
[INFO] MHOZDW8351
[INFO] SICAL
[INFO] WMTA
```
Unfortunately, “group 2” vehicle images lead to mixed results. In this case, we are not invoking the option to clear foreground pixels around the border of the license plate, which is detrimental to Tesseract’s ability to decipher the number plate.
While the first result image has the correct ANPR result, the other two are wildly incorrect.

The solution here is to apply our ``clear_border`` function to strip foreground pixels that touch the border of the image that confuse Tesseract OCR:

```bash
$ python ocr_license_plate.py --input license_plates/group2 --clear-border 1
[INFO] MHOZDW8351
[INFO] KA297999
[INFO] KE53E964
```
We’re able to improve the ANPR OCR results for these images by applying the ``clear_border`` function.

However, there is still one mistake in each example. In the top-right case, the letter “Z” is mistaken for the digit “7”. In the bottom case, the letter “L” is mistaken for the letter “E”.

Although these are understandable mistakes, we would hope to do better.
