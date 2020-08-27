from tkinter import *


def hello():
    print("NANDU")

def name():
    print("how are you")

def age():
    print("HAVE A GREAT DAY")


root =Tk()


root.geometry("655x333")
root.title("My GUI")

#Attributes of Labels:
#Textbg
#bg -- background
#fg -- foreground
#font --setting the font
#padx --x padding
#pady --y padding
#relief --Borderstyling,SUNKEN,RAISED,GROOVE,RIDGE

#title_label = Label (text =  "hello world " , bg = "red" , fg = "white" ,padx = 45 ,pady =94 ,font = "comicsansms 19 bold" , borderwidth  = 14 , relief = SUNKEN)

#title_label.pack(side = LEFT, fill = Y, padx = 34 ,pady = 34 )

#side = top ,bottom,left,right 

#frames

#f1 = Frame(root ,bg = "grey", borderwidth = 6 , relief = SUNKEN )
#f1.pack(side = LEFT, fill = Y)

#f2 = Frame(root ,bg = "grey", borderwidth = 8 , relief = SUNKEN )
#f2.pack(side = TOP, fill = Y)

#l = Label(f1, text = "project tkinter")
#l.pack( pady = 142)

#l = Label(f2 , text = "welcome" , font = "helvetica 16 bold", fg ="red")
#l.pack()

#Buttons

Frame = Frame(root , borderwidth = 6 ,bg ="grey" , relief = SUNKEN)
Frame.pack(side =LEFT , anchor = "nw")

b1 = Button(Frame, fg = "red" , text = "printNow" ,command = hello)
b1.pack(side = LEFT , padx = 23)

b2 = Button(Frame, fg = "red" , text = "tellMe" ,command = name)
b2.pack(side = LEFT , padx = 23)

b2 = Button(Frame, fg = "red" , text = "hitHere" ,command = age)
b2.pack(side = LEFT , padx = 23)



root.mainloop()
