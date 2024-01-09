from tkinter import *


window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=400, height=200)
window.config(padx=100, pady=75)


# This is where the user puts in the number for miles 
miles_entry = Entry(width=10)
miles_entry.insert(END, string="0")
miles_entry.grid(column=2,row=1)

#####################################################

# These are my labels

# This is the "is equal to label" #########################################
is_equal_to_label = Label(text="Is equal to", font = ("Aria",12))
is_equal_to_label.grid(column=1,row=2)
###########################################################################

# This is the "Miles label" #########################################
miles = Label(text=" Miles", font = ("Aria",12))
miles.grid(column=3,row=1)
###########################################################################

# This is the "Km label" #########################################
km_label = Label(text="Km", font = ("Aria",12))
km_label.grid(column=3,row=2)
###########################################################################

# This is the label where it changes the miles to Km #########################################
km_output = Label(text="0", font = ("Aria",12))
km_output.grid(column=2,row=2)
###########################################################################


# This is the button that calculates the conversion from miles to Kilometers

def button_clicked():
    miles = float(miles_entry.get())
    km = miles * 1.609344
    km_str = f"{km:.2f}"
    km_output.config(text = km_str)
    
button = Button(text="Calculate", command=button_clicked)
button.grid(column=2, row=3)

########################################################################################

window.mainloop()