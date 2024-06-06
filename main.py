from tkinter import *
FONT = ("Calibri", 12, "normal")

# Create GUI window
window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)


# Function for conversion on button click
def convert():
    miles = input.get()
    km = int(miles) * 1.6
    label_kmv.config(text=km)


# Label - Miles
label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)


# Label - "is equal to"
label_eq = Label(text="is equal to", font=FONT)
label_eq.grid(column=0, row=1)

# Label - Km value
label_kmv = Label(text="0", font=FONT)
label_kmv.grid(column=1, row=1)

# Label - Km
label_km = Label(text="Km", font=FONT)
label_km.grid(column=2, row=1)

# Entry for miles
input = Entry(width=7)
input.grid(column=1, row=0)
# input.config()

# Button - Calculate
button = Button(text="Calculate", command=convert)
button.grid(column=1, row=2)


window.mainloop()
