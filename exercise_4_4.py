import processing
result = processing.run("native:countpointsinpolygon", { 'CLASSFIELD' : '', 'FIELD' : 'NUMPOINTS', 'OUTPUT' : 'TEMPORARY_OUTPUT', 'POINTS' : 'C:/Users/lucah/Downloads/Muenster/Muenster/Schools.shp', 'POLYGONS' : 'C:/Users/lucah/Downloads/Muenster/Muenster/Muenster_City_Districts.shp', 'WEIGHT' : '' })
vLayer = result['OUTPUT']
features = vLayer.getFeatures()

# variante 1
for feature in features:
    print(f'{feature.attributes()[3]}: {feature.attributes()[7]}')
