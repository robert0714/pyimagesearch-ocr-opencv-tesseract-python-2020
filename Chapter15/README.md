# Improving Text Detection Speed with OpenCV and GPUs
* https://pyimagesearch.com/2022/03/14/improving-text-detection-speed-with-opencv-and-gpus/
* https://www.kaggle.com/datasets/yelmurat/frozen-east-text-detection
* https://www.learnopencv.com/deep-learning-based-text-detection-using-opencv-c-python/

## OpenCV Text Detection (EAST text detector)
* https://pyimagesearch.com/2018/08/20/opencv-text-detection-east-text-detector/
* https://github.com/gifflet/opencv-text-detection
* https://github.com/saurabh1294/python-opencv-text-detection

This tutorial will show you how to take the efficient and accurate scene text detector (EAST) model and run it on OpenCV’s ``dnn`` (deep neural network) module using an NVIDIA GPU. As we’ll see, our text detection throughput rate nearly triples, improving from ``~23`` frames per second (FPS) to an astounding ``~97`` FPS!

In this tutorial, you will:

* Learn how to use OpenCV’s ``dnn`` module to run deep neural networks on an NVIDIA CUDA-based GPU
* Implement a Python script to benchmark text detection speed on both a CPU and GPU
* Implement a second Python script, this one that performs text detection in real-time video streams
* Compare the results of running text detection on a CPU versus a GPU


To follow this guide, you need to have the OpenCV library installed on your system.

Luckily, OpenCV is pip-installable:
```bash
$ pip install opencv-contrib-python scipy  imutils scikit-image 
```

## File Structures
```bash
|-- pyimagesearch
|   |-- __init__.py
|   |-- east
|   |   |-- __init__.py
|   |   |-- east.py
|-- ../models
|   |-- east
|   |   |-- frozen_east_text_detection.pb
-- images
|   |-- car_wash.png
|-- text_detection_speed.py
|-- text_detection_video.py
|-- text_detection_video_v2.py
```
We’ll be reviewing two Python scripts in this tutorial:
* ``text_detection_speed.py``: Benchmarks text detection speed on a CPU versus a GPU using the ``car_wash.png`` image in our ``images`` directory.
* ``text_detection_video_v2.py``: Demonstrates how to perform real-time text detection on your GPU.
* ``frozen_east_text_detection.pb``: https://raw.githubusercontent.com/oyyd/frozen_east_text_detection.pb/master/frozen_east_text_detection.pb

## Speed Test: OCR With and Without GPU
Let’s now measure our EAST text detection FPS throughput rate without a GPU (i.e., running on a CPU):
```bash
$ python text_detection_speed.py --image images/car_wash.png --east ../models/east/frozen_east_text_detection.pb
[INFO] loading EAST text detector...
[INFO] using CPU for inference...
[INFO] running timing trials...
[INFO] avg. text detection took 0.108568 seconds
```
Our average text detection speed is ``~0.1`` seconds, equating to ``~9-10`` FPS. A deep learning model running on a CPU is fast and sufficient for many applications.

Let’s now break out the GPUs:
```bash
$ python text_detection_speed.py --image images/car_wash.png --east ../models/east/frozen_east_text_detection.pb --use-gpu 1
[INFO] loading EAST text detector...
[INFO] setting preferable backend and target to CUDA...
[INFO] running timing trials...
[INFO] avg. text detection took 0.004763 seconds
```
Using an NVIDIA V100 GPU, our average frame processing rate decreases to ``~0.004`` seconds, meaning that we can now process ``~250`` FPS! **As you can see, using your GPU makes a substantial difference!**

## OCR on GPU for Real-Time Video Streams
This section needs to be executed locally on a machine with a GPU. After running the ``text_detection_video_v2.py`` script on an NVIDIA RTX 2070 SUPER GPU (coupled with an i9 9900K processor), I obtained ``~97`` FPS:
```bash
$ python text_detection_video_v2.py --east ../models/east/frozen_east_text_detection.pb --use-gpu 1
[INFO] loading EAST text detector...
[INFO] setting preferable backend and target to CUDA...
[INFO] starting video stream...
[INFO] elapsed time: 74.71
[INFO] approx. FPS: 96.80
```
When I ran the same script without using any GPU, I reached an FPS of ``~23``, which is ``~77%`` slower than the above results.
```bash
$ python text_detection_video_v2.py --east ../models/east/frozen_east_text_detection.pb
[INFO] loading EAST text detector...
[INFO] using CPU for inference...
[INFO] starting video stream...
[INFO] elapsed time: 68.59
[INFO] approx. FPS: 22.70
```
As you can see, using your GPU can dramatically improve the throughput speed of your text detection pipeline!