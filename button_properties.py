from tkinter import *

root = Tk()
root.title("Button Example")
root.geometry("400x300")

# Function to handle button clicks
def button_clicked():
    label.config(text="Button clicked!")

# Label to show the result of the button click
label = Label(root, text="Nothing Pressed", font=("Helvetica", 12))
label.pack(pady=10)

# Create a button with all available options
button = Button(
    root,
    text="Click Me",              # text on the button
    command=button_clicked,        # function to call when button is clicked
    activebackground="lightblue",  # background color when button is clicked or hovered
    activeforeground="red",        # text color when button is clicked or hovered
    bg="blue",                     # background color
    fg="white",                    # text color
    font=("Arial", 14, "bold"),    # font for the text
    padx=20,                       # padding on the x-axis
    pady=10,                       # padding on the y-axis
    height=2,                      # height of the button
    width=15,                      # width of the button
    state=NORMAL,                  # state of the button (NORMAL, DISABLED)
    relief=RAISED,                 # type of border (RAISED, SUNKEN, FLAT, GROOVE, RIDGE)
    cursor="hand2",                # changes cursor to a hand icon when hovering
    anchor=CENTER,                 # alignment of the text (CENTER, N, S, E, W, etc.)
)

button.pack(pady=20)

root.mainloop()
