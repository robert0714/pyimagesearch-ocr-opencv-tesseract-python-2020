# import the necessary packages
from difflib import SequenceMatcher as SQ
import pytesseract
import argparse
import cv2

# construct the argument parser and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-m", "--model", required=True,
	help="path to trained digit classifier")
ap.add_argument("-i", "--image", required=True,
	help="path to input sudoku puzzle image")
ap.add_argument("-d", "--debug", type=int, default=-1,
	help="whether or not we are visualizing each step of the pipeline")
args = vars(ap.parse_args())

# load the input image and convert it from BGR to RGB channel
# ordering
image = cv2.imread(args["image"])
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# use Tesseract to OCR the image
print("[INFO] OCR'ing the image...")
predictedText = pytesseract.image_to_string(image, lang=args["name"])
print(predictedText)

# read text from the ground-truth file
with open(args["ground_truth"], "r") as f:
    target = f.read()

# calculate the accuracy of the model with respect to the ratio of
# sequences matched in between the predicted and ground-truth labels
accuracyScore = SQ(None, target, predictedText).ratio() * 100

# round off the accuracy score and print it out
accuracyScore = round(accuracyScore, 2)
print("[INFO] accuracy of {} model: {}%...".format(args["name"],
    accuracyScore))

