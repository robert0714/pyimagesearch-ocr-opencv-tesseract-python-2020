# OCR'ing Video Streams
* https://pyimagesearch.com/2022/03/07/ocring-video-streams/
* https://www.youtube.com/watch?v=oooDn5SBUAg
* https://www.youtube.com/watch?v=YlF8hI5BGi8

To follow this guide, you need to have the OpenCV library installed on your system.

Luckily, OpenCV is pip-installable:
```bash
$ pip install opencv-contrib-python scipy  imutils scikit-image 
```

## File Structures
```bash
|-- pyimagesearch
|   |-- __init__.py
|   |-- helpers.py
|   |-- blur_detection
|   |   |-- __init__.py
|   |   |-- blur_detector.py
|   |-- video_ocr
|   |   |-- __init__.py
|   |   |-- visualization.py
|-- output
|   |-- ocr_video_output.avi
|-- video
|   |-- business_card.mp4
|-- ocr_video.py
```

## Real-Time Video OCR Results
We are now ready to put our video OCR script to the test! Open a terminal and execute the following command:
```bash
$ python ocr_video.py --input video/business_card.mp4 --output output/ocr_video_output.avi
[INFO] opening video file...
```