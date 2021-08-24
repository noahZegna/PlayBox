from gridImpl import GridImpl
from imageLoader import ImageLoader
# from basicUI import BasicUI

from PIL import Image

imagePath = "/home/julian/Desktop/picture_sampling/UnsampledImages/testImage2.png"
imageLoader = ImageLoader(imagePath)
image = imageLoader.getImage()

columnRowRatio = image.size[0]/image.size[1]
numberOfCells = imageLoader.getMeshDimension(columnRowRatio)

gridObject = GridImpl(image, numberOfCells)
leftOffset, rightOffset, topOffset, bottomOffset = gridObject.getPixelOffset()
imageCropped = gridObject.getCroppedImage(leftOffset, rightOffset, topOffset, bottomOffset)
print ("size of cropped image is")
print (imageCropped.size)

#Image Class is mutable -> imageGrid states are altered in getFinalImage
imageGrid = gridObject.getGridImage()
gridObject.getFinalImage(imageCropped, imageGrid)
finalImage = imageGrid
finalImage.show()

if __name__ == '__main__':
    print("generateMesh script: if not imported by another this is the main")