# Import modules
from qgis.core import QgsVectorLayer, QgsProject
from qgis.core import *

import os

# Layer Path setzen
layer_path = 'C:/Users/lucah/Downloads/Muenster/Muenster'

# Project Path setzen
project_path = "C:/Users/lucah/OneDrive/Desktop/Test/myFirstProject.qgz"


project = QgsProject.instance()
project.read(project_path)

directory = os.listdir(layer_path)

for file in directory:
    if file.endswith('.shp'):
        layer = QgsVectorLayer(layer_path + '/' + file, file[:-4], "ogr")

        if not layer.isValid():
            print("Error loading the layer!")
        else:
            
            project.addMapLayer(layer)

            project.write()

            print("Layer added to project\nProject saved successfully!")

