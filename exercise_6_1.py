# exercise 6.1
import csv

layer = QgsVectorLayer("MultiPolygon", "temp_standard_land_value_muenster", "memory")
layer.setCrs(QgsCoordinateReferenceSystem("EPSG:25832"))
provider = layer.dataProvider()

standard_land_value = QgsField("standard_land_value", QVariant.Double)
type_field = QgsField("type_field", QVariant.String)
district = QgsField("district", QVariant.String)
provider.addAttributes([standard_land_value, type_field, district])
layer.updateFields()
flds = layer.fields()



with open(r"C:\Users\lucah\Downloads\Data_for_Session 6\Data for Session 6\standard_land_value_muenster.csv") as csv_data:
    csv_reader = csv.reader(csv_data, delimiter=';')
    heading = True
    counter = 0
    for line in csv_reader:
        if heading:
            heading = False
        else:
            feature = QgsFeature(layer.fields())
            attributes = [None] * len(flds) 

            # Setze die Werte in die entsprechenden Positionen der Liste
            attributes[flds.indexOf("standard_land_value")] = line[0]
            attributes[flds.indexOf("type_field")] = line[1]
            attributes[flds.indexOf("district")] = line[2]

            feature.setAttributes(attributes)  # Übergebe die Liste an setAttributes

            geom = QgsGeometry.fromWkt(line[3])
            feature.setGeometry(geom)
            provider.addFeatures([feature])
            counter = counter + 1
            if counter == 10:
                break
    layer.updateFields()
    QgsProject.instance().addMapLayer(layer)
