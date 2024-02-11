# OCR’ing Text with Your Custom Tesseract Model
In our previous chapter, you learned how to train a Tesseract model on your custom dataset.

We did so by annotating a sample set of images, providing their ground-truth plaintext
versions, configuring a Tesseract training job, and then fine-tuning Tesseract’s LSTM OCR
model on our custom dataset.

After training is completed, we were left with a serialized OCR model. However, the question
remains:

**“How do we take this trained Tesseract model and use it to OCR input images?”**

The remainder of this chapter will address that exact question.

## Learning Objectives
In this chapter, you will learn how to:
1. Learn how to set your TESSDATA_PREFIX path for inference
2. Load our custom trained Tesseract OCR model
3. Use the model to OCR input images

## OCR with Your Custom Tesseract Model 
In the first part of this chapter, we’ll review our project directory structure. We’ll then
implement a Python script to take our custom trained OCR model and then use it to OCR an 
input image. We’ll wrap up the chapter by comparing our custom model’s accuracy with the
default Tesseract model, noting that our custom model can obtain higher OCR accuracy.
### Project Structure 
```bash
|-- full.png
|-- full.txt
|-- handwriting.traineddata
|-- handwritten_to_text.py
|-- inference_setup.sh
```
Here’s what you need to know about the directory structure:
* The ``inference_setup.sh`` script is used to set our ``TESSDATA_PREFIX`` environment
variable for testing
* The ``handwritten_to_text.py`` file takes an input image (``full.png``), applies OCR
to it, and then compares it to the ground-truth text (``full.txt``)
* The ``handwriting.traineddata`` is our custom trained Tesseract model serialized to
disk (I included it here in the project structure just in case you do not wish to train the
model yourself and instead just want to perform inference)

By the end of this chapter, you’ll be able to take your custom trained Tesseract model and use
it to OCR input images.

### Custom Tesseract OCR Results
We are now ready to use our Python script to OCR handwritten text with our custom trained
Tesseract model.

However, before we can run our ``handwritten_to_text.py`` script, we first need to set our
``TESSDATA_PREFIX`` to point to our custom trained OCR model.
```bash
source inference_setup.sh
```
After executing ``inference_setup.sh``, take a second to validate that your
``TESSDATA_PREFIX`` is properly set:
```bash
$ echo $TESSDATA_PREFIX
/home/pyimagesearch/tesstrain/data
$ ls -l /home/pyimagesearch/tesstrain/data
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov 24 15:44 eng
drwxrwxr-x 3 ubuntu ubuntu 4096 Nov 24 15:46 handwriting
drwxrwxr-x 2 ubuntu ubuntu 4096 Nov 24 15:46 handwriting-ground-truth
-rw-rw-r-- 1 ubuntu ubuntu 11696673 Nov 24 15:50 handwriting.traineddata
-rw-rw-r-- 1 ubuntu ubuntu 330874 Nov 24 15:41 radical-stroke.txt
```
Provided that you can (1) successfully list the contents of the directory and (2) the custom
handwriting model is present, we can then move on to executing the
``handwritten_to_text.py`` script.

Optionally, if you did not train your Tesseract model in the previous chapter and instead want
to utilize the *pre-trained* model included in the downloads associated with this chapter, you
can manually set the ``TESSDATA_PREFIX`` in the following manner:
```bash
$ export TESSDATA_PREFIX=/PATH/TO/PRACTITIONER/BUNDLE/CODE/chapter20-ocr_custom_tesseract_model
```

You will need to update the path above based on where you downloaded the source code for
this text on your own system.

Now that your ``TESSDATA_PREFIX`` is set, you can execute the following command:
```bash
$ python handwritten_to_text.py --name handwriting --image full.png   --ground-truth full.txt

[INFO] OCR'ing the image...
1t wandered relatipn no sureprise
of screened doulptful. Overcame No
mstead ye of ‘rifling husbands.
Might om older hours on found.
Or digsimilar companions fryendship
impossible, at diminumon. Did yoursetp
Carrriage learning rate she man s
replying. gister pidued living her gou
enable mrs off spirit really. Parish
oOppose rerair is me miasery. Quick
may saw zsiyte afier money mis
Now oldest new tostes lblenty mother
calleq misery yer. Longer exatse
or county motr exceprt met its
trung2. Narrow enoughn sex. mornent
desire are. Heid iiho that
come 4hat seen read age
its, Contmimed or estimotes

[INFO] accuracy of handwriting model: 23.28%...
```
full.png displays the sample handwriting text that we are trying to OCR. The terminal
output shows the OCR process results, the accuracy of which is ~23%.

OCR accuracy of 23% may feel extremely **low**, but let’s compare it to the **default** English OCR
model included with Tesseract.

**To start, make sure you open a new terminal so that our TESSDATA_PREFIX environment variable is empty.** Otherwise, Tesseract will attempt to search the
``TESSDATA_PREFIX`` directory for the default English model and be unable to find it.

You can validate that your `TESSDATA_PREFIX` variable is empty/not set by echo’ing its
contents to your terminal:
```bash
$ echo $TESSDATA_PREFIX
```
If the output of your echo command is empty, you can proceed to run the following command:
```bash
$ python handwritten_to_text.py --name eng --image full.png --ground-truth full.txt

[INFO] OCR'ing the image...
IE wandered relation NO surerize
of 2eveened deuotful. Overcane 10
Mstead ye of rifling husbands.
Might om older hours on found.
Or dissimilar companions friendship
MPossinle, a4 diminuinon. Did yourserp
Caxvrriage \egrnwg rate she man "=
fer Ng- User pidues Wing her dou
enave NTs off spirit really. Parish
Opbose Tevrair 1s WwE& mserd. Quick
Yaay saw ae aller mosey:
Nous ©dest new tostes lent nother
Coed Wiser Fer. Longer exase
Lor county Mov exrery met vis
Ang . Navrow Noun sey. noment--
doswre ave. Yd he The
Come A Nar Seen vead age
Sis) Contmned OV Exhmoses

[INFO] accuracy of eng model: 2.77%..
```
OCR’ing the same image (see Figure 20.1) with Tesseract’s default English model obtains
only 2.77% accuracy, **implying that our custom trained handwriting recognition model is nearly 10x more accurate!**

That said, I chose handwriting recognition as the example project for this chapter (as well as
the previous one) to demonstrate that handwriting recognition with the Tesseract OCR engine,
while technically possible, will struggle to obtain higher accuracy.

**It’s instead far better to train/fine-tune Tesseract models on typed text.** Doing so will
yield far higher accuracy with less effort.

> Note: For more information on how you can improve the accuracy of any custom Tesseract
> OCR model, refer to the previous chapter’s discussion on hyperparameter fine-tuning and
> gathering additional training data representative of what the model will see during testing.

If you need a high accuracy OCR engine for handwriting text, be sure to follow Chapter 5, Making OCR “Easy” with EasyOCR, where the developers work with off-the-shelf handwriting
recognition models in several general-purpose scenarios.

## Summary
In this chapter, you learned how to apply a custom trained Tesseract model to an input image.
The actual implementation was simple, requiring less than 40 lines of Python code.

While accuracy wasn’t the best, that’s not a limitation of our inference script — to improve
accuracy; we should spend more time training.

Additionally, we applied Tesseract to the task of handwriting recognition to demonstrate that
while it’s technically possible to train a Tesseract model for handwriting recognition, the results
will be poor compared to typed-text OCR.

Therefore, if you are planning on training your custom Tesseract models, be sure to
apply Tesseract to typed-text datasets versus handwritten text — doing so will yield
higher OCR accuracy.
