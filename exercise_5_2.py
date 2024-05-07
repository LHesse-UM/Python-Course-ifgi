# retreive main window to create sub windows later on
parent = iface.mainWindow()

# save city district layer
districts_layer = QgsProject.instance().mapLayersByName('Muenster_City_Districts')[0]

# create source crs
source_crs = QgsCoordinateReferenceSystem("EPSG:4326")

# create output crs (in this case ETRS89 32N)
mod_crs = districts_layer.crs() 


# create class with created crs's
transformation = QgsCoordinateTransform(source_crs, mod_crs, QgsProject.instance())

# save dialog input as well as boolean value whether 'ok' was clicked or not 
sCoords, bOK = QInputDialog.getText(parent, "Coordinates", "Enter coordinates as latitude, longitude", text = "51.96066,7.62476")

# action canceled
if not bOK:

    # create output and inform the user
    message = "canceled action"
    QMessageBox.warning(parent, "canceled", message)


# get the splitted values and transform them to floats
lat, lon = map(float, sCoords.split(',')) 

# create Point from input coordinates
inputPoint = QgsPointXY(lon, lat)

# transform point to ETRS89 32N (might be different if other layer is used)
inputPointT = transformation.transform(inputPoint)

# create message, which will be used for the output
message = ""

# iterate through all districts
for district in districts_layer.getFeatures():

    # get districts geometry
    districtGeometry = district.geometry()

    # check whether the transformed point is within the district
    if districtGeometry.contains(inputPointT):

        # create output and inform the user
        message = f"Input Point is in {district['Name']}"
        QMessageBox.information(parent, "Checking Point", message)

        # jump out of the loop
        break

# if the string is empty, no matching district was found
if message == "":

    # create output message and inform the user
    message = "Input coordinate did not match with any district in Münster"
    QMessageBox.information(parent, "Checking Point", message)

