import tkinter as tk
from tkinter import Entry



 # Creating a Label Widget
 
class Example(tk.Frame):
    
    app = tk.Tk()
    
    app.title( "Tres Amigas ")

    app.geometry("750x980") 

    e = Entry(app, width=50, borderwidth=2)

    e.grid(row=0, column=0)

    e2 = Entry(app, width=50, borderwidth=2)

    e2.grid(row=1, column=0)

    C = tk.Canvas(app, width= 750, height= 480)

    myLabel4 = tk.Label(app, text="10:09", padx= 5, pady= 5).grid(row=0, column=2)

    myLabel4 = tk.Label(app, text="9:08", padx= 5, pady= 5).grid(row=1, column=2)

    number1 = tk.Label(app, text="this is a dialog box.sup").grid(row=4, column=0)



    #buttonExample = tk.Button(app, text="Create new window",command=createNewWindow)


    def button_click(self):

        current = e.get()
        
        e.delete(0,END)
        
        e.insert(0, number1)
       
       
    #myLabel2 = Label(root, text="this is a dialog box.sup").grid(row=1, column=0)
    
    def createNewWindow(app1, Second_Window):

            window = tk.Toplevel(app)
            
            app1.title( 'Tres Amigas' )
            
            app.geometry("750x980")

            e1 = Entry(app, width=50, borderwidth=2)
            
            e1.grid(row=0, column=0)

            e22 = Entry(app, width=50, borderwidth=2)
            
            e22.grid(row=1, column=0)
            
            myButton11 = tk.Button(app, text="Add", padx=20, pady=10, command=createNewWindow)
            
            myButton11.grid(row=5, column=0)
            
            myButton22 = tk.Button(app, text="History", padx=32, pady=10)
            
            myButton22.grid(row=6,column=0)
            
            myButton33 = tk.Button(app, text="Back", padx=36, pady=10)
            
            myButton33.grid(row=7,column=0)

     # Shoving to screen!
    myButton1 = tk.Button(app, text="Current Order", padx=20, pady=10, command = createNewWindow)

    myButton2 = tk.Button(app, text="Inventory", padx=32, pady=10)

    myButton3 = tk.Button(app, text="Settings", padx=36, pady=10)

    myButton1.grid(row=5, column=0)

    myButton2.grid(row=6,column=0)

    myButton3.grid(row=7,column=0)


    #for item in [myLabel1, myButton]:

      #  item.pack()
      
    #myLabel1.grid(row=0, column=0)

    #myLabel2.grid(row=1, column=0)

    
    Example(app).pack(side="top", fill="both", expand=True)
    app.mainloop()


# This opens the file and reads each line into the list, then closes it

#file=open('listfile.txt','r')

#list = file.readlines()

#file.close()

#plist = raw_input("What do you want to append: ")

#list.append(plist)

# This opens the file, writes each item in the list to a line and then closes it  
  
#file=open('listfile.txt','w')

#for item in list:

#    file.write(str(item))

#file.close()

#print (list)