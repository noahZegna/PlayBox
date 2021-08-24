from tkinter import *
from PIL import Image
from imageLoader import ImageLoader

class BasicUI:

    # empty constructor
    def __init__(self, columnRowRatio):
        self.columnRowRatio = columnRowRatio 

    def myClickRow15():
        return 15
    def myClickRow20():
        return 20
    def myClickRow25():
        return 25

    def myClickColumn15():
        return 15
    def myClickColumn20():
        return 20
    def myClickColumn25():
        return 25
     
    root = Tk()

    # Creating Widgets
    myLabel = Label(root, text = "Select number of Rows")
    myLabel.pack()

    image = Image.open("/home/julian/Desktop/picture_sampling/UnsampledImages/testImage2.png", mode="r")
    canvas = Canvas(root, width = image.size[0], height = image.size[1])
    img = PhotoImage(file="/home/julian/Desktop/picture_sampling/UnsampledImages/testImage2.png")
    canvas.create_image(0,0, anchor=NW, image=img)  

    if image.size[0]/image.size[1] < 1:
        buttonRow15= Button(root, text = " 15 rows ", padx= 40, pady = 20,command = myClickRow15 )
        buttonRow20= Button(root, text = " 20 rows ", padx= 40, pady = 20 ,command = myClickRow20 )
        buttonRow25= Button(root, text = " 25 rows ", padx= 40, pady = 20 ,command = myClickRow25 )
        buttonRow15.pack()
        buttonRow20.pack()
        buttonRow25.pack()
    else:
        buttonColum15= Button(root, text = " 15 columns ", padx= 40, pady = 20,command = myClickColumn15() )
        buttonColum20= Button(root, text = " 20 columns ", padx= 40, pady = 20 ,command = myClickColumn20() )
        buttonColum25= Button(root, text = " 25 columns ", padx= 40, pady = 20 ,command = myClickColumn25() )
        buttonColum15.pack()
        buttonColum20.pack()
        buttonColum25.pack()


    canvas.pack()
 
    # Constant loop
    root.mainloop()

