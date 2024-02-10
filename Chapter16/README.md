# Text Detection and OCR with Amazon Rekognition API
* https://pyimagesearch.com/2022/03/21/text-detection-and-ocr-with-amazon-rekognition-api/

To follow this guide, you need to have the OpenCV library installed on your system.

Luckily, OpenCV is pip-installable:
```bash
$ pip install boto3 opencv-contrib-python scipy  imutils scikit-image 
```

## Amazon Rekognition API for OCR
We’ll then show you how to install ``boto3``, the Amazon Web Services (AWS) software development kit (SDK) for Python. Finally, we’ll use the ``boto3`` package to interface with Amazon Rekognition OCR API.


## Obtaining Your AWS Rekognition Keys
* https://customers.pyimagesearch.com/aws-keys/

## Project Structure
```bash
|-- config
|   |-- __init__.py
|   |-- aws_config.py
|-- images
|   |-- aircraft.png
|   |-- challenging.png
|   |-- park.png
|   |-- street_signs.png
|-- amazon_ocr.py
```

## Amazon Rekognition OCR Results
Let’s see our results in action, first by OCR’ing the entire image, line-by-line:
```bash
$ python amazon_ocr.py --image images/aircraft.png
[INFO] making request to AWS Rekognition API...
WARNING!
LOW FLYING AND DEPARTING AIRCRAFT
BLAST CAN CAUSE PHYSICAL INJURY
```
But what if we wanted to obtain our OCR results at the word level instead of the line level?

That’s as simple as supplying the ``--type`` command line argument:
```bash
$ python amazon_ocr.py --image images/aircraft.png --type word
[INFO] making request to AWS Rekognition API...
WARNING!
LOW
FLYING
AND
DEPARTING
AIRCRAFT
BLAST
CAN
CAUSE
PHYSICAL
INJURY
```