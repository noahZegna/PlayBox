from PIL import Image
from numpy import *

class GridImpl:

    def __init__(self, image, numberOfCells): 
        self.image = image
        self.initialColumnLength = image.size[0]
        self.initialRowLength = image.size[1]
        if (numberOfCells[0] == numberOfCells[1]): 
            self.numberOfColumnCells = numberOfCells[0]
            self.numberOfRowCells = self.numberOfColumnCells
        else:
            self.numberOfColumnCells = numberOfCells[0]
            self.numberOfRowCells = numberOfCells[1]      
        self.columnCellLength = int((image.size[0] - image.size[0] % self.numberOfColumnCells)/self.numberOfColumnCells)
        self.rowCellLength = int((image.size[1] - image.size[1] % self.numberOfRowCells)/self.numberOfRowCells)
        self.girdWidth = 2
        self.simpleBlank = Image.new('RGB',(self.columnCellLength*self.numberOfColumnCells + (self.numberOfColumnCells-1)*self.girdWidth, self.rowCellLength*self.numberOfRowCells + (self.numberOfRowCells-1)*self.girdWidth), (250,250,250))

    def getPixelOffset(self):
        if (self.initialColumnLength % self.numberOfColumnCells)%2 == 0:
            leftOffset = (self.initialColumnLength % self.numberOfColumnCells)/2
            rightOffset = leftOffset
        else:
            leftOffset = int((self.initialColumnLength % self.numberOfColumnCells)/2)
            rightOffset = self.initialColumnLength % self.numberOfColumnCells - leftOffset
        if (self.initialRowLength % self.numberOfRowCells)%2 == 0:    
            topOffset = int((self.initialRowLength % self.numberOfRowCells)/2)
            bottomOffset = topOffset
        else:
            topOffset = int((self.initialRowLength % self.numberOfRowCells)/2)
            bottomOffset = self.initialRowLength % self.numberOfRowCells - topOffset
        return leftOffset, rightOffset, topOffset, bottomOffset
                
    def getCroppedImage(self, leftOffset, rightOffset, topOffset, bottomOffset):
        left = leftOffset
        top = topOffset
        right = self.initialColumnLength - rightOffset
        bottom =  self.initialRowLength - bottomOffset
        return self.image.crop((left, top, right, bottom))

    # ToDo: This method needs performance increase -> replace putpixel
    def getGridImage(self):
        for row in range(self.simpleBlank.size[1]):
            for column in range(self.simpleBlank.size[0]):
                for num in range(1, self.numberOfColumnCells):
                    if column == num*self.columnCellLength + (num - 1)*self.girdWidth:
                        for count in range(0, self.girdWidth):
                            self.simpleBlank.putpixel((column + count, row), (0, 0, 0))
                for num in range(1, self.numberOfRowCells):    
                    if row == num*self.rowCellLength + (num-1)*self.girdWidth:
                        for count in range(0, self.girdWidth):
                            self.simpleBlank.putpixel((column, row + count), (0, 0, 0))
        return self.simpleBlank
            
    def getFinalImage(self, imageCropped, imageGrid):
        for rowIdx in range(self.numberOfRowCells):
            for columnIdx in range(self.numberOfColumnCells):
                left = columnIdx*self.columnCellLength 
                right = self.columnCellLength*(columnIdx + 1) 
                top = rowIdx*self.rowCellLength 
                bottom = self.rowCellLength*(rowIdx + 1)
                imageSingleCell = imageCropped.crop((left, top, right, bottom))
                #careful -> PIL Image class is mutable !
                imageGrid.paste(imageSingleCell,(columnIdx*(self.columnCellLength+self.girdWidth),rowIdx*(self.rowCellLength+self.girdWidth)))
        
        