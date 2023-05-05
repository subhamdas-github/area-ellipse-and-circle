# area-ellipse-and-circle
Piece of code demonstrate only the intersection of circle and ellipse.

## Required Packages:
1. matplotlib
2. descartes
3. shapely

## Download of packages:
Open cmd and type ```pip --version``` (to check pip is installed)
1. '''pip install matplotlib'''
2. pip install descartes
3. pip install shapely

## Modify patch.py of descartes
Navigate to this path '''C:\Users\OFFICE\AppData\Local\Programs\Python\Python310\Lib\site-packages\descartes'''
and open the 'patch.py' file using vscode and modify line 62 '''t.exterior''' to '''t.exterior.coords'''

Save the file and close the window.

## run script
run the area_of_ellipse_and_circle.py file
