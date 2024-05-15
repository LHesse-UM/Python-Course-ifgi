# exercise 6.1
# import modules
import csv

# creating new vector layer of type MultiPolygon, stored in memory
layer = QgsVectorLayer("MultiPolygon", "temp_standard_land_value_muenster", "memory")
# Set CRS to EPSG:23832
layer.setCrs(QgsCoordinateReferenceSystem("EPSG:25832"))
# get data provider for adding of fields and features
provider = layer.dataProvider()

# Define fields, add them to layer, and update layer
standard_land_value = QgsField("standard_land_value", QVariant.Double)
type_field = QgsField("type_field", QVariant.String)
district = QgsField("district", QVariant.String)
provider.addAttributes([standard_land_value, type_field, district])
layer.updateFields()

# get list of fields
flds = layer.fields()

# open CSV file
## change to your working path here
with open(r"C:\Users\lucah\Downloads\Data_for_Session 6\Data for Session 6\standard_land_value_muenster.csv") as csv_data:
    # create CSV reader with delimiter ';'
    csv_reader = csv.reader(csv_data, delimiter=';')
    
    # create counter for testing and running properly
    counter = 0
    # iterate through each row
    # line = [standard_land_value, type_field, district, geometry]
    for line in csv_reader:
        # skipping header row
        if counter == 0:
            # only incrementing the counter
            counter = counter + 1
        # break loop because 312 is field limit 
        # otherwise we get an error message: _csv.Error: field larger than field limit (131072)
        elif counter == 312:
            break
        else:
            # creating a new feature
            feature = QgsFeature(layer.fields())
            # initializing a list to add the attributes and setting the attribute values from the CSV row
            attributes = [None] * len(flds)
            attributes[flds.indexOf("standard_land_value")] = line[0]
            attributes[flds.indexOf("type_field")] = line[1]
            attributes[flds.indexOf("district")] = line[2]

            # set attributes for feature
            feature.setAttributes(attributes) 

            # creating a geometry from the WKT in the CSV row and set it for the feature
            geom = QgsGeometry.fromWkt(line[3])
            feature.setGeometry(geom)

            # add the feature to the provider
            provider.addFeatures([feature])

            # increment the counter
            counter = counter + 1

    # update the layer to include the new features
    layer.updateFields()

    # add the layer to the map and project
    QgsProject.instance().addMapLayer(layer)
