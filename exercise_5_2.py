districts_layer = QgsProject.instance().mapLayersByName('Muenster_City_Districts')[0]
parent = iface.mainWindow()
source_crs = QgsCoordinateReferenceSystem("EPSG:4326")
mod_crs = districts_layer.crs() # EPSG:25832

transformation = QgsCoordinateTransform(source_crs, mod_crs, QgsProject.instance())
print(mod_crs)
sCoords, bOK = QInputDialog.getText(parent, "Coordinates", "Enter coordinates as latitude, longitude", text = "51.96066,7.62476")

if not bOK:
    QMessageBox.warning(parent, "FAILED", "huh")

# get the splitted values
lat, lon = map(float, sCoords.split(',')) # float verlangt

inputPoint = QgsPointXY(lon, lat)
inputPointT = transformation.transform(inputPoint)
print(inputPointT)

districtLayers = QgsProject.instance().mapLayersByName("Muenster_City_Districts")
districtLayer = districtLayers[0]

check = False
for district in districtLayer.getFeatures():
    districtGeometry = district.geometry()
    
    if districtGeometry.contains(inputPointT):
        QMessageBox.information(parent, "Checking Point", f"Input Point is in {district['Name']}")
        check = True
        break
    
if check == False:
    QMessageBox.information(parent, "Checking Point", "Input Point was not in any district of Münster")

