from tkinter import *
import cmath
import math

#FONT SECTION =======================================================================================================

font_1 = ('Tahoma',20)
font_2 = ('Tahoma',12)

#END FONT SECTION ==========================================================================================================================================================================================================


#GUI SECTION ==========================================================================================================================================================================================================

root = Tk()
root.title('Matrix Solver')
root.geometry('200x300')
root.overrideredirect(False)
root.resizable(height = False, width = False)

#IMAGE SECTION ==========================================================================================================================================================================================================

image_bg_1 = PhotoImage(file='bg_1.png')


#END IMAGE SECTION ==========================================================================================================================================================================================================


Label_bg = Label(root,image = image_bg_1,highlightthickness=0)
Label_bg.pack()

Entry_row = Entry(root,width=10,bg='#414950',fg='#B1B1B1',highlightthickness=0,	relief=FLAT, font= font_2,insertbackground='#B1B1B1')
Entry_row.place(x=80,y=72)

Entry_col = Entry(root,width=10,bg='#414950',fg='#B1B1B1',highlightthickness=0,	relief=FLAT, font= font_2,insertbackground='#B1B1B1')
Entry_col.place(x=80,y=136)

#END GUI SECTION ==========================================================================================================================================================================================================


root.mainloop()