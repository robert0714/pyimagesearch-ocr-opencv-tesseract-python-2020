# Text Detection and OCR with Google Cloud Vision API
* https://pyimagesearch.com/2022/03/31/text-detection-and-ocr-with-google-cloud-vision-api/

## Obtaining Your Google Cloud Vision API Keys
### Prerequisite
A Google Cloud account with billing enabled is all you’ll need to use the Google Cloud Vision
API. You can find the Google Cloud guide on how to modify your billing settings here:
* https://cloud.google.com/billing/docs/how-to/modify-project

### Steps to Enable Google Cloud Vision API and Download Credentials
* You can find our guide to getting your keys at the following site: https://customers.pyimagesearch.com/gcp-keys/ .These
keys are required if you want to follow this chapter or use the Google Cloud Vision API in your
projects.

### Configuring Your Development Environment for the Google Cloud Vision API
If you have not already installed the ``google-cloud-vision`` Python package in your Python
development environment, take a second to do so now:
```bash
$ pip install opencv-contrib-python
$ pip install --upgrade google-cloud-vision
```
## Project Structure
Let’s inspect the project directory structure for our Google Cloud Vision API OCR project:
```bash
|-- images
|   |-- aircraft.png
|   |-- challenging.png
|   |-- street_signs.png
|-- client_id.json
|-- google_ocr.py
```
We will apply our ``google_ocr.py`` script to several examples in the ``images`` directory.

## Google Cloud Vision API OCR Results
Let's now put the Google Cloud Vision API to work! Open a terminal and execute the following command:

```bash
$ python google_ocr.py --image images/aircraft.png --client client_id.json
[INFO] making request to Google Cloud Vision API...
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

Let’s try a more challenging image
```bash
$ python google_ocr.py --image images/challenging.png --client client_id.json
[INFO] making request to Google Cloud Vision API...
LITTER
First
Eastern
National
Bus
Fimes
EMERGENCY
STOP
```
Interestingly, the Google Cloud Vision API does make a mistake, thinking that the “T” in “Times” is an “F.”

Let’s look at one final image, this one of a street sign:
```bash
$ python google_ocr.py --image images/street_signs.png --client client_id.json
[INFO] making request to Google Cloud Vision API...
Old
Town
Rd
STOP
ALL
WAY
```
## SDK
* https://cloud.google.com/vision/docs/ocr

## AutoML Vision deprecations
Migrate to [Vertex AI](https://cloud.google.com/vertex-ai/docs/start/migrating-to-vertex-ai), which includes all functionality of legacy AutoML Vision as well as new features.
