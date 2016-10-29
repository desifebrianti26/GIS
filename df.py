import shapefile
fbi = shapefile.Reader("E:/Countries/Countries.shp")
shapes = fbi.shapes()
print len (shapes)