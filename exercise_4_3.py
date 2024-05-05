# Import modules
from qgis.core import QgsVectorLayer, QgsProject
from qgis.core import *

import os

# set your path to the folder of the layer(s) here!
layer_path = 'C:/Users/lucah/Downloads/Muenster/Muenster'

# set your path to the QGIS project here!
project_path = "C:/Users/lucah/OneDrive/Desktop/Test/myFirstProject.qgz"


# create QGIS instance and load the project
project = QgsProject.instance()
project.read(project_path)

# list of all files in layer folder
directory = os.listdir(layer_path)


# iterate though all files
for file in directory:

    # filter for shapefiles
    if file.endswith('.shp'):

        # create vector layer
        layer = QgsVectorLayer(layer_path + '/' + file, file[:-4], "ogr")

        # error handling
        if not layer.isValid():
            print("Error loading the layer!")
            
        else:

            # add layer to map
            project.addMapLayer(layer)

            # save project
            project.write()

            print("Layer added to project\nProject saved successfully!")

