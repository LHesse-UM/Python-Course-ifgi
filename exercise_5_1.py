# Create a map canvas object
mc = iface.mapCanvas()

# create parent window for the sub-windows later on
parent = iface.mainWindow()


# get Muenster_City_Districts.shp layer in the TOC
districtLayers = QgsProject.instance().mapLayersByName("Muenster_City_Districts")
districtLayer = districtLayers[0]

# Create QgsFeatureRequest() instance
request = QgsFeatureRequest()

# Definde clause
nameClause = QgsFeatureRequest.OrderByClause("Name", ascending = True)

# Set clause
orderby = QgsFeatureRequest.OrderBy([nameClause])

# assign orderby to the request
request.setOrderBy(orderby)

# create list for the distric names
district_names = []


# save features ordered by attribute "Name"
for feature in districtLayer.getFeatures(request):
    district_names.append(feature["Name"])

# save dialog input as well as boolean value whether 'ok' was clicked or not 
sDistrict, bOk = QInputDialog.getItem(parent, "District Names", "Select District", district_names)


# do nothing if the user cancled the input dialog
if bOk == False:
    QMessageBox.warning(parent, "Schools", "User cancelled")

else:

    # get Schools.shp layer in the TOC
    schoolLayers = QgsProject.instance().mapLayersByName("Schools")
    schoolLayer = schoolLayers[0]
    
    # get the different features from the school layer
    schoolFeatures = schoolLayer.getFeatures()
    

    # select the district, which was chosen in the dialog
    districtLayer.selectByExpression(f"\"Name\" = '{sDistrict}'", QgsVectorLayer.SetSelection)
    
    # retreive the feature of the district
    feature = districtLayer.selectedFeatures()[0]

    # save geometry of the district feature
    districtGeometry = feature.geometry()
    
    
    # create a Distance Area and assign the ETRS89 reference system to it for later distance calculations
    da = QgsDistanceArea()
    da.setEllipsoid("ETRS89")


    # create centroid of the district geometry and save it's x and y value
    centroid = districtGeometry.centroid()
    centroidX = centroid.get().x()
    centroidY = centroid.get().y()

    # create variable for result message
    message = ""

    # iterate through all schools
    for school in schoolFeatures:

        # save school geometry and it's x and y value
        schoolGeometry = school.geometry()
        schoolGeometryX = schoolGeometry.get().x()
        schoolGeometryY = schoolGeometry.get().y()
        
        # check whether school geometry is inside the district's
        if districtGeometry.contains(schoolGeometry):
            
            # calculate distance between centroid and the school
            distance = da.measureLine([QgsPointXY(centroidX,centroidY),QgsPointXY(schoolGeometryX,schoolGeometryY)])/1000

            # attach school metadata as well as the distance to the result message
            message = message + school.attributes()[1] + ", " + school.attributes()[2] + "\nDistance to district centrum " + str(round(distance, 2)) + " km\n\n"
    
    
    # present the result message in a information window
    QMessageBox.information(parent, f"Schools in {sDistrict}", message)
