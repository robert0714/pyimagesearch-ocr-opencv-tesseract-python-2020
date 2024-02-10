# Text Detection and OCR with Microsoft Cognitive Services
* https://pyimagesearch.com/2022/03/28/text-detection-and-ocr-with-microsoft-cognitive-services/
* https://arxiv.org/pdf/2305.10825.pdf

## Obtaining Your Microsoft Cognitive Services Keys
* https://customers.pyimagesearch.com/azure-keys/

## Configuring Your Development Environment
To follow this guide, you need to have the OpenCV and Azure Computer Vision libraries installed on your system.
```bash
$ pip install opencv-contrib-python
$ pip install azure-cognitiveservices-vision-computervision
```
## Project Structure
```bash
|-- config
|   |-- __init__.py
│   |-- microsoft_cognitive_services.py
|-- images
|   |-- aircraft.png
|   |-- challenging.png
|   |-- park.png
|   |-- street_signs.png
|-- microsoft_ocr.py
``` 
## Microsoft Cognitive Services OCR Results
Let’s now put the MCS OCR API to work for us. Open a terminal and execute the following command:
```bash
$ python microsoft_ocr.py --image images/aircraft.png
[INFO] making request to Microsoft Cognitive Services API...
WARNING!
LOW FLYING AND DEPARTING AIRCRAFT
BLAST CAN CAUSE PHYSICAL INJURY
```
Let’s try a different image, this one containing several challenging pieces of text:
```
$ python microsoft_ocr.py --image images/challenging.png
[INFO] making request to Microsoft Cognitive Services API...
LITTER
EMERGENCY
First
Eastern National
Bus Times
STOP
```