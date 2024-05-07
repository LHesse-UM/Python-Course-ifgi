# Create a map canvas object
mc = iface.mapCanvas()

# get Muenster_City_Districts.shp layer in the TOC
layers = QgsProject.instance().mapLayersByName("Muenster_City_Districts")
layer = layers[0]

# Create QgsFeatureRequest() instance
request = QgsFeatureRequest()

# Definde clause
nameClause = QgsFeatureRequest.OrderByClause("Name", ascending = True)

# Set clause
orderby = QgsFeatureRequest.OrderBy([nameClause])
request.setOrderBy(orderby)

district_names = []

# Print features ordered by attribute "Name"
for feature in layer.getFeatures(request):
    district_names.append(feature["Name"])

#print(district_names)



sDistrict, bOk = QInputDialog.getItem(parent, "District Names", "Select District", district_names)

if bOk == False:
    QMessageBox.warning(parent, "Schools", "User cancelled")

else:


    schoolLayer = QgsProject.instance().mapLayersByName("Schools")
    schools = schoolLayer[0]
    
    schoolFeatures = schools.getFeatures()
    
    
    
    #print(f"\"Name\" == '{sDistrict}'")


    layer.selectByExpression(f"\"Name\" = '{sDistrict}'", QgsVectorLayer.SetSelection)
    feature = layer.selectedFeatures()[0]
    districtGeometry = feature.geometry()
    
    message = ""
    
    da = QgsDistanceArea()
    da.setEllipsoid("ETRS89")
    
    for school in schoolFeatures:
        schoolGeometry = school.geometry()
        
        if districtGeometry.contains(schoolGeometry):
            
            
            centroid = districtGeometry.centroid()
            centroidX = centroid.get().x()
            centroidY = centroid.get().y()
            
            schoolGeometryX = schoolGeometry.get().x()
            schoolGeometryY = schoolGeometry.get().y()
            

            print(centroid)
            distance = da.measureLine([QgsPointXY(centroidX,centroidY),QgsPointXY(schoolGeometryX,schoolGeometryY)])/1000
            print(distance)
            message = message + school.attributes()[1] + ", " + school.attributes()[2] + "\nDistance to district centrum " + str(round(distance, 2)) + " km\n\n"
    
    
    QMessageBox.information(parent, f"Schools in {sDistrict}", message)


print(sDistrict)

print(bOk)
