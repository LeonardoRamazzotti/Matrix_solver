from tkinter import *
import cmath
import math

#FONT SECTION =======================================================================================================

font_1 = ('Tahoma',20)
font_2 = ('Tahoma',12)

#END FONT SECTION ==========================================================================================================================================================================================================
#FUNCTION SECTION ==========================================================================================================================================================================================================


def grid_tuple(n):  # function that create a list of tuple for the grid layout (row,column)

    c = 0 

    lista_tuple = []

    while c < n :
        m=0
        while m < n:
            tupla = (c,m)
            lista_tuple.append(tupla)
            m+=1
        m =0
        c+=1

    return lista_tuple

def list_matrix(num):
    
    list_a =[]
    
    i=0
    while i < num:
        list_a.append(i)
        i+=1
        
        
    return list_a

# COMMENTAAAAA

def main_window(): # COMMENTAAAAA
    main_win = Toplevel(root)
    main_win.title('Matrix Solver')
    main_win.geometry('700x600')

    row = int(Entry_row.get())  
    col = int(Entry_col.get())  
    
    n=row*col
    
    
    list_grid= grid_tuple(row)
    
    list_val = list_matrix(n)
    
    i=0
    
    for element in list_val :
       
        r = list_grid[i][0]
        c = list_grid[i][1]    
             
        m = str(i)
        
        globals()['Entry_'+m]= Entry(main_win,width=10,font=font_2).grid(row= r, column = c,padx=20,pady=20)
        
        i+=1
        


    #creare un ciclo for che aggiunga per ogni elemento in lis_matrix (tuple) un numero partendo da zero con un contatore.
    # creare un ciclo che prenda il valore nella posizione n (contatore) delle due liste e crei un entry box con global e gli assegni
    # un grid layout come definito nella tupla ( Entry.grid(row=list_matrix[n[0]], col = list_matrix[n[1]])    )




#END FUNCTION SECTION ==========================================================================================================================================================================================================
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

Button_main_window = Button(root,text='Commit', width=5,font = font_1, bg='white',fg='#B1B1B1',highlightthickness=0,relief=FLAT,command = main_window)
Button_main_window.place(x=50,y=200)



#END GUI SECTION ==========================================================================================================================================================================================================


root.mainloop()