import csv

mc = iface.mapCanvas()

ml = mc.currentLayer()

featuresML = ml.selectedFeatures()


# Pfad anpassen!
path = 'C:/Users/lucah/OneDrive/Desktop/'
with open(path + 'SchoolReport.csv', 'w') as file:
    writer = csv.writer(file, delimiter=';')
    
    writer.writerow(['Name','X','Y'])
    
    for feature in featuresML:

        schoolNameAtt = feature.attributes()[1]
        geometry = feature.geometry()
        x, y = geometry.asPoint()
        writer.writerow([schoolNameAtt,x,y])

    
    print('Fertig')
