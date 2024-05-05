# import modules
import processing

# run method "countpointsinpolygon" with the school data as points and the city districts as polygons and save the result
result = processing.run("native:countpointsinpolygon", { 'CLASSFIELD' : '', 'FIELD' : 'NUMPOINTS', 'OUTPUT' : 'TEMPORARY_OUTPUT', 'POINTS' : 'C:/Users/lucah/Downloads/Muenster/Muenster/Schools.shp', 'POLYGONS' : 'C:/Users/lucah/Downloads/Muenster/Muenster/Muenster_City_Districts.shp', 'WEIGHT' : '' })

# get the result vectorlayer of countpointsinpolygon function
vLayer = result['OUTPUT']

# get features of the result vector layer
features = vLayer.getFeatures()

# iterate through all features and printing their name as well as the number of schools per district
for feature in features:
    print(f'{feature.attributes()[3]}: {feature.attributes()[7]}')
