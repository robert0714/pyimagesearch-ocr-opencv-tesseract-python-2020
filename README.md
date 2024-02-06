# Chapter 3 Handwriting Recognition with Keras and TensorFlow
## OCR-Handwriting-Recognition

- we used Keras and TensorFlow to train a deep neural network to recognize both digits (0-9) and alphabetic characters (A-Z).

- To train our network to recognize these sets of characters, we utilized the MNIST digits dataset as well as the NIST Special Database 19 (for the A-Z characters).

- Our model obtained 96% accuracy on the testing set for handwriting recognition.

OCR-Handwriting-Recognition/ directory contains the following:

- deeplearning module:

        Includes the sub-modules az_dataset
        for I/O helper functions and models
        for implementing the ResNet deep
        learning model.

- a_z_handwritten_data.csv: 

        A CSV file that contains the Kaggle
        A-Z dataset

- train_ocr_model.py:

        The main Python driver file that 
        we used to train our ResNet
        model and display our results. Our
        model and training plot files include:

    - handwriting.model: 
        
            The custom OCR ResNet model we
            saved after train our resnet model

    - plot.png: 
        
            A plot of the results of our most
            recent OCR training run

- images/ sub-directory: 
        
        Contains PNG or jpeg itest files for
        us to OCR with our Python driver script

- ocr_handwriting.py: 

        The main Python script for that we
        will use to OCR to test new images
        handwriting samples.

- ocr_handwriting.py: 
* https://pyimagesearch.com/ocr-with-opencv-tesseract-and-python/
```bash
python ocr_handwriting.py  --model handwriting.model --image images/hello_world.png
python ocr_handwriting.py  --model handwriting.model --image images/umbc_address.png
```

# Chapter 4  Denoising Dirty Documents
* Kaggle’s Denoising Dirty Documents dataset: https://www.kaggle.com/c/denoising-dirty-documents/data
* The UC Irvine Machine Learning Repository: https://archive.ics.uci.edu/

Image credit: http://pyimg.co/j6ylr

The Denoising Document Algorithm: http://pyimg.co/dp06u

