from PIL import Image
from meshDimensionLoader import MeshdimnsionLoader

class ImageLoader:

    # empty constructor
    def __init__(self, filename):
        self.filename = filename 

    def getImage(self):
        image = Image.open(self.filename , mode="r")
        try: 
            image = Image.open(self.filename , mode="r")
        except IOError:
            pass
        return image
    
    def getOptimalColumnMesh(self, columnRowRatio, typeOfMesh):
        meshDimensionLoader = MeshdimnsionLoader()
        if typeOfMesh == '3':
            columnDict = meshDimensionLoader.getColumn15Dict()
            optimalMesh = meshDimensionLoader.getOptimalMesh(columnDict, columnRowRatio)
        elif typeOfMesh == '4':
            columnDict =  meshDimensionLoader.getColumn20Dict()
            optimalMesh = meshDimensionLoader.getOptimalMesh(columnDict, columnRowRatio)
        elif typeOfMesh == '5':
            columnDict =  meshDimensionLoader.getColumn25Dict()
            optimalMesh = meshDimensionLoader.getOptimalMesh(columnDict, columnRowRatio)
        elif typeOfMesh == '6':
            rowDict =  meshDimensionLoader.getRow15Dict()
            optimalMesh = meshDimensionLoader.getOptimalMesh(rowDict, columnRowRatio)
        elif typeOfMesh == '7':
            rowDict =  meshDimensionLoader.getRow20Dict()
            optimalMesh = meshDimensionLoader.getOptimalMesh(rowDict, columnRowRatio)
        elif typeOfMesh == '8':
            rowDict =  meshDimensionLoader.getRow25Dict()
            optimalMesh = meshDimensionLoader.getOptimalMesh(rowDict, columnRowRatio)
  
        return optimalMesh

    def getMeshDimension(self, columnRowRatio):
        if columnRowRatio > 0.9 and columnRowRatio < 1.111:
            print("Select the grid dimesions")
            print("5 x 5 -> 1")
            print("10 x 10 -> 2")
            print("*****************************")
        elif columnRowRatio > 1.111 and columnRowRatio < 1.75:
            print("*****************************")
            print("Select number of column cells ")
            print("  15 columns select -> 3 ")
            print("  20 columns select -> 4 ")
            print("  25 columns select -> 5 ")
            print("*****************************")
            typeOfMesh = input()
            return self.getOptimalColumnMesh(columnRowRatio, typeOfMesh)
        elif columnRowRatio > 0.6 and columnRowRatio < 0.9:
            print("*****************************")
            print("Select number of row cells ")
            print("  15 rows select -> 6 ")
            print("  20 rows select -> 7 ")
            print("  25 rows select -> 8 ")
            print("*****************************")
            typeOfMesh = input()
            return self.getOptimalColumnMesh(columnRowRatio, typeOfMesh)
