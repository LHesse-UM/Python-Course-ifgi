# import modules
import csv

# Get a reference to the map canvas in QGIS
mc = iface.mapCanvas()

# Get the currently selected layer from the map canvas
ml = mc.currentLayer() 

# Get the currently selected features from ml
featuresML = ml.selectedFeatures()


# adjust path to your desired csv destination here!
path = 'C:/Users/lucah/OneDrive/Desktop/'

# create csv
with open(path + 'SchoolReport.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')

    # headers
    writer.writerow(['Name','X','Y'])

    # iterate through all features in featuresML
    for feature in featuresML:

        # write name and coordinates into csv
        schoolNameAtt = feature.attributes()[1]
        geometry = feature.geometry()
        x, y = geometry.asPoint()
        writer.writerow([schoolNameAtt,x,y])

    
    print('Done!')
