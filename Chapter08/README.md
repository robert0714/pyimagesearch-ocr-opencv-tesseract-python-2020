# OpenCV Sudoku Solver and OCR
https://pyimagesearch.com/2020/08/10/opencv-sudoku-solver-and-ocr/

Once your environment is up and running, you’ll need another package for this tutorial. You need to install [py-sudoku](https://pypi.org/project/py-sudoku/), the library we’ll be using to help us solve Sudoku puzzles:
```bash
pip install py-sudoku   scikit-image   scikit-learn
```

## Training our Sudoku digit recognizer with Keras and TensorFlow
```bash
$ python train_digit_classifier.py --model output/digit_classifier.h5
[INFO] accessing MNIST...
[INFO] compiling model...
[INFO] training network...
[INFO] training network...
Epoch 1/10
469/469 [==============================] - 22s 47ms/step - loss: 0.7311 - accuracy: 0.7530 - val_loss: 0.0989 - val_accuracy: 0.9706
Epoch 2/10
469/469 [==============================] - 22s 47ms/step - loss: 0.2742 - accuracy: 0.9168 - val_loss: 0.0595 - val_accuracy: 0.9815
Epoch 3/10
469/469 [==============================] - 21s 44ms/step - loss: 0.2083 - accuracy: 0.9372 - val_loss: 0.0452 - val_accuracy: 0.9854
...
Epoch 8/10
469/469 [==============================] - 22s 48ms/step - loss: 0.1178 - accuracy: 0.9668 - val_loss: 0.0312 - val_accuracy: 0.9893
Epoch 9/10
469/469 [==============================] - 22s 47ms/step - loss: 0.1100 - accuracy: 0.9675 - val_loss: 0.0347 - val_accuracy: 0.9889
Epoch 10/10
469/469 [==============================] - 22s 47ms/step - loss: 0.1005 - accuracy: 0.9700 - val_loss: 0.0392 - val_accuracy: 0.9889
[INFO] evaluating network...
              precision    recall  f1-score   support
           0       0.98      1.00      0.99       980
           1       0.99      1.00      0.99      1135
           2       0.99      0.98      0.99      1032
           3       0.99      0.99      0.99      1010
           4       0.99      0.99      0.99       982
           5       0.98      0.99      0.98       892
           6       0.99      0.98      0.99       958
           7       0.98      1.00      0.99      1028
           8       1.00      0.98      0.99       974
           9       0.99      0.98      0.99      1009
    accuracy                           0.99     10000
   macro avg       0.99      0.99      0.99     10000
weighted avg       0.99      0.99      0.99     10000
[INFO] serializing digit model...

```
## OpenCV Sudoku puzzle solver OCR results

```bash
$ python solve_sudoku_puzzle.py --model output/digit_classifier.h5 \
	--image Sudoku_puzzle.jpg
[INFO] loading digit classifier...
[INFO] processing image...
[INFO] OCR'd Sudoku board:
+-------+-------+-------+
| 8     |   1   |     9 |
|   5   | 8   7 |   1   |
|     4 |   9   | 7     |
+-------+-------+-------+
|   6   | 7   1 |   2   |
| 5   8 |   6   | 1   7 |
|   1   | 5   2 |   9   |
+-------+-------+-------+
|     7 |   4   | 6     |
|   8   | 3   9 |   4   |
| 3     |   5   |     8 |
+-------+-------+-------+
[INFO] solving Sudoku puzzle...
---------------------------
9x9 (3x3) SUDOKU PUZZLE
Difficulty: SOLVED
---------------------------
+-------+-------+-------+
| 8 7 2 | 4 1 3 | 5 6 9 |
| 9 5 6 | 8 2 7 | 3 1 4 |
| 1 3 4 | 6 9 5 | 7 8 2 |
+-------+-------+-------+
| 4 6 9 | 7 3 1 | 8 2 5 |
| 5 2 8 | 9 6 4 | 1 3 7 |
| 7 1 3 | 5 8 2 | 4 9 6 |
+-------+-------+-------+
| 2 9 7 | 1 4 8 | 6 5 3 |
| 6 8 5 | 3 7 9 | 2 4 1 |
| 3 4 1 | 2 5 6 | 9 7 8 |
+-------+-------+-------+
```
