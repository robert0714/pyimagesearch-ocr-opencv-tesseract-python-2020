# Image alignment and registration with OpenCV
* https://pyimagesearch.com/2020/08/31/image-alignment-and-registration-with-opencv/

```bash
python align_document.py --template form_w4.png --image scans/scan_01.jpg

python align_document.py --template form_w4.png --image scans/scan_02.jpg
```
## References
* youtube: https://www.youtube.com/watch?v=_o6fSMCmNnQ
* [Feature Based Image Alignment using OpenCV (C++/Python)](https://learnopencv.com/image-alignment-feature-based-using-opencv-c-python/)

## Official 2020 IRS W-4 form
https://www.irs.gov/pub/irs-prior/fw4--2020.pdf
https://www.irs.gov/pub/irs-pdf/fw4.pdf

### We have a simple project structure for this tutorial consisting of the following images:
* ``scans/``: Contains two JPG testing photos of a tax form
* ``form_w4.png``: Our template image of the official 2020 IRS W-4 form

Additionally, we’ll be reviewing two Python files:
* ``align_images.py``: Holds our helper function which aligns a scan to a template by means of an OpenCV pipeline
* ``align_document.py``: Our driver file in the main directory which brings all the pieces together to perform image alignment and registration with OpenCV