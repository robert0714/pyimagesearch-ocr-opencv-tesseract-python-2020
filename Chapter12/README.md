# Multi-Column Table OCR
* https://pyimagesearch.com/2020/09/21/opencv-automatic-license-number-plate-recognition-anpr-with-python/ 
* https://github.com/krzischp/Multi_Column_Table_OCR.git
* https://github.com/aws-samples/amazon-textract-textractor

To follow this guide, you need to have the OpenCV library installed on your system.

Luckily, OpenCV is pip-installable:
```bash
$  pip install opencv-contrib-python tabulate pandas
```

## File Structures
```bash
Multi-Column Table OCR
|-- michael_jordan_stats.png
|-- multi_column_ocr.py
|-- results.csv
```
Our ``multi_column_ocr.py`` script will accept an input image, ``michael_jordan_stats.png``, detect the data table, extract it, and then OCR it associating rows/columns along the way.

## Multi-Column OCR Results
We are now ready to see our multi-column OCR script in action!

Open a terminal and execute the following command:
```bash
$ python multi_column_ocr.py --image michael_jordan_stats.png --output results.csv
+----+---------+---------+-----+---------+-------+-------+-------+-------+-------+--------+
|    | Year    | CLUB    |   G |     FG% |   REB |   AST | STL   | BLK   |   PTS |   AVG. |
|----+---------+---------+-----+---------+-------+-------+-------+-------+-------+--------|
|  0 | 1984-85 | CHICAGO |  82 | 515     |   534 |   481 | 196   | 69    |  2313 |  282   |
|  1 | 1985-86 | CHICAGO |  18 |   0.457 |    64 |    53 | ar    | A     |   408 |  227   |
|  2 | 1986-87 | CHICAGO |  82 | 482     |   430 |   377 | 236   | 125   |  3041 |   37.1 |
|  3 | 1987-88 | CHICAGO |  82 | 535     |   449 |   485 | 259   | 131   |  2868 |   35   |
|  4 | 1988-89 | CHICAGO |  81 | 538     |   652 |   650 | 234   | 65    |  2633 |  325   |
|  5 | 1989-90 | CHICAGO |  82 | 526     |   565 |   519 | 227   | 54    |  2763 |   33.6 |
|  6 | TOTALS  |         | 427 | 516     |  2694 |  2565 | 1189  | 465   | 14016 |  328   |
+----+---------+---------+-----+---------+-------+-------+-------+-------+-------+--------+
[INFO] saving CSV file to disk...
```