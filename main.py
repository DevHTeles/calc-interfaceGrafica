"""
    Create Professional Calculate User
        I'm Beginner
    🚀
"""
# IMPORT TKINTER
from tkinter import *

# COLORS //color picker "google"
color1 = "#D3D4E0"  # LIGHT BLUE
color2 = "#b0c6d9"  #
color3 = "#031017"  #
color4 = "#BED1E6"  #
color5 = "#E66500"  #

window = Tk()
window.title("Calculate")
window.geometry("235x306")
window.config(bg=color1)

# CREATE FRAMES
frame_display = Frame(window, width=235, height=50)
frame_display.grid(row=0, column=0)

frame_body = Frame(window, width=235, height=256)
frame_body.grid(row=1, column=0)

# VARIABLE ALL VALUES
all_values = ''

# CREATE LABEL
value_text = StringVar()


# CREATE FUNCTION
def input_values(event):

  global all_values

  all_values = all_values + str(event)

  # PASSING VALUE ON SCREEN
  value_text.set(all_values)


# CREATE FUNCTION CALCULATE
def calculate():
  global all_values
  result = eval(all_values)

  value_text.set(str(result))
  # all_values = str(result)


# DISPLAY CLEAR
def clear_display():
  global all_values
  all_values = ''
  value_text.set("")


app_label = Label(frame_display,
                  textvariable=value_text,
                  width=16,
                  height=2,
                  padx=7,
                  relief=FLAT,
                  anchor="e",
                  justify=RIGHT,
                  font=('Yvi 18'),
                  bg=color2)
app_label.place(x=0, y=0)

# CREATE BUTTON
b1 = Button(frame_body,
            command=clear_display,
            text="C",
            width=11,
            height=2,
            bg=color4,
            font=('Yvi 13 bold'),
            relief=RAISED,
            overrelief=RIDGE)
b1.place(x=0, y=0)
b2 = Button(frame_body,
            command=lambda: input_values('%'),
            text="%",
            width=5,
            height=2,
            bg=color4,
            font=('Yvi 13 bold'),
            relief=RAISED,
            overrelief=RIDGE)
b2.place(x=117, y=0)
b3 = Button(frame_body,
            command=lambda: input_values('/'),
            text="/",
            width=5,
            height=2,
            bg=color5,
            fg=color2,
            font=('Yvi 13 bold'),
            relief=RAISED,
            overrelief=RIDGE)
b3.place(x=175, y=0)

b4 = Button(frame_body,
            command=lambda: input_values('7'),
            text="7",
            width=5,
            height=2,
            bg=color4,
            font=('Yvi 13 bold'),
            relief=RAISED,
            overrelief=RIDGE)
b4.place(x=0, y=51)
b5 = Button(frame_body,
            command=lambda: input_values('8'),
            text="8",
            width=5,
            height=2,
            bg=color4,
            font=('Yvi 13 bold'),
            relief=RAISED,
            overrelief=RIDGE)
b5.place(x=59, y=51)
b6 = Button(frame_body,
            command=lambda: input_values('9'),
            text="9",
            width=5,
            height=2,
            bg=color4,
            font=('Yvi 13 bold'),
            relief=RAISED,
            overrelief=RIDGE)
b6.place(x=117, y=51)
b7 = Button(frame_body,
            command=lambda: input_values('*'),
            text="*",
            width=5,
            height=2,
            bg=color5,
            fg=color2,
            font=('Yvi 13 bold'),
            relief=RAISED,
            overrelief=RIDGE)
b7.place(x=175, y=51)

b8 = Button(frame_body,
            command=lambda: input_values('4'),
            text="4",
            width=5,
            height=2,
            bg=color4,
            font=('Yvi 13 bold'),
            relief=RAISED,
            overrelief=RIDGE)
b8.place(x=0, y=102)
b9 = Button(frame_body,
            command=lambda: input_values('5'),
            text="5",
            width=5,
            height=2,
            bg=color4,
            font=('Yvi 13 bold'),
            relief=RAISED,
            overrelief=RIDGE)
b9.place(x=59, y=102)
b10 = Button(frame_body,
             command=lambda: input_values('6'),
             text="6",
             width=5,
             height=2,
             bg=color4,
             font=('Yvi 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b10.place(x=117, y=102)
b11 = Button(frame_body,
             command=lambda: input_values('-'),
             text="-",
             width=5,
             height=2,
             bg=color5,
             fg=color2,
             font=('Yvi 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b11.place(x=175, y=102)

b12 = Button(frame_body,
             command=lambda: input_values('1'),
             text="1",
             width=5,
             height=2,
             bg=color4,
             font=('Yvi 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b12.place(x=0, y=153)
b13 = Button(frame_body,
             command=lambda: input_values('2'),
             text="2",
             width=5,
             height=2,
             bg=color4,
             font=('Yvi 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b13.place(x=59, y=153)
b14 = Button(frame_body,
             command=lambda: input_values('3'),
             text="3",
             width=5,
             height=2,
             bg=color4,
             font=('Yvi 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b14.place(x=117, y=153)
b15 = Button(frame_body,
             command=lambda: input_values('+'),
             text="+",
             width=5,
             height=2,
             bg=color5,
             fg=color2,
             font=('Yvi 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b15.place(x=175, y=153)

b16 = Button(frame_body,
             command=lambda: input_values('0'),
             text="0",
             width=11,
             height=2,
             bg=color4,
             font=('Yvi 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b16.place(x=0, y=204)
b17 = Button(frame_body,
             command=lambda: input_values('.'),
             text=".",
             width=5,
             height=2,
             bg=color4,
             font=('Yvi 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b17.place(x=117, y=204)
b18 = Button(frame_body,
             command=calculate,
             text="=",
             width=5,
             height=2,
             bg=color5,
             fg=color2,
             font=('Yvi 13 bold'),
             relief=RAISED,
             overrelief=RIDGE)
b18.place(x=175, y=204)

window.mainloop()
