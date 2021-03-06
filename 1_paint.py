from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox

import PIL
from PIL import Image, ImageDraw, ImageGrab, ImageTk

import os

root = Tk()
root.title('My paint')
root.geometry("800x800")

brush_color = "black"

def paint(e):

	brush_width = '%0.0f' % float(my_slider.get())
	brush_type2 = brush_type.get()

	global lastx,lasty
	x, y = e.x,e.y
	my_canvas.create_line((lastx, lasty, x, y), fill=brush_color, width=brush_width, capstyle=brush_type2, smooth=True)
	lastx, lasty = x, y

def activate_paint(e):
    global lastx, lasty
    my_canvas.bind('<B1-Motion>', paint)
    lastx, lasty = e.x, e.y

# Change The Size Of The Brush 
def change_brush_size(thing):
	slider_label.config(text='%0.0f' % float(my_slider.get()))

# Change Brush Color
def change_brush_color():
	global brush_color
	brush_color = "black"
	brush_color = colorchooser.askcolor(color = brush_color)[1]


# Change Canvas Color
def change_canvas_color():
	global bg_color
	bg_color = "black"
	bg_color = colorchooser.askcolor(color = bg_color)[1]
	my_canvas.config(bg=bg_color)

# Clear Screen
def clear_screen():
	my_canvas.delete(ALL)

# Save Image
def save_as_png():
	if not os.path.exists('images'):
		os.makedirs('images')

	result = filedialog.asksaveasfilename(initialdir="images/", filetypes=( ("png files", "*.png"), ("all files","*.*") ) )

	if result.endswith('.png'):
		pass
	else:
		result += '.png'

	if result:
		x = root.winfo_rootx() + my_canvas.winfo_x()
		y = root.winfo_rooty() + my_canvas.winfo_y()
		
		x1 = x + my_canvas.winfo_width()
		y1 = y + my_canvas.winfo_height()
		ImageGrab.grab().crop( (x,y,x1,y1) ).save(result)
		# print(x)
		# print(root.winfo_rootx(),my_canvas.winfo_x())

		# Pop Up Success Message
		messagebox.showinfo("Image Saved", "Your Image Has Been Saved!")

# Create Our Canvas
my_canvas = Canvas(root, width=600, height=400, bg="white")
my_canvas.pack(pady=20)

my_canvas.bind('<1>', activate_paint)

# Create Brush Option Frame
brush_options_frame = Frame(root)
brush_options_frame.pack(pady=20) 

# Brush Size
brush_size_frame = LabelFrame(brush_options_frame, text="Brush Size")
brush_size_frame.grid(row=0, column=0, padx=50)

# Brush Slider
my_slider = ttk.Scale(brush_size_frame, from_=1, to_=100, command=change_brush_size, orient=VERTICAL, value=10)
my_slider.pack(pady=10, padx=10)

# Brush Slider Label
slider_label = Label(brush_size_frame, text=my_slider.get())
slider_label.pack(pady=5)

# Brush Type
brush_type_frame = LabelFrame(brush_options_frame, text="Brush Type", height=400)
brush_type_frame.grid(row=0, column=1, padx=50)

brush_type = StringVar()
brush_type.set("round")

# Create Radio Button For Brush Type
brush_type_radio1 = Radiobutton(brush_type_frame, text="Round", variable=brush_type, value="round")
brush_type_radio2 = Radiobutton(brush_type_frame, text="Slash", variable=brush_type, value="butt")
brush_type_radio3 = Radiobutton(brush_type_frame, text="Diamond", variable=brush_type, value="projecting")

brush_type_radio1.pack(anchor=W)
brush_type_radio2.pack(anchor=W)
brush_type_radio3.pack(anchor=W)

# Change Colors
change_colors_frame = LabelFrame(brush_options_frame, text="Change Color")
change_colors_frame.grid(row=0, column=2, padx=50)

# Change Brush Color Button
brush_color_button = Button(change_colors_frame, text="Brush Color", command=change_brush_color)
brush_color_button.pack(pady=10,padx=10)

# Change Canvas Background Color
canvas_color_button = Button(change_colors_frame, text="Canvas Color", command=change_canvas_color)
canvas_color_button.pack(pady=10,padx=10)

# Program Options Frame
options_frame = LabelFrame(brush_options_frame, text="Program Options")
options_frame.grid(row=0, column=3, padx=50)

# Clear Screen Button 
clear_button = Button(options_frame, text="Clear Screen", command=clear_screen)
clear_button.pack(padx=10, pady=10) 

# Save Image
save_image_button = Button(options_frame, text="Save to PNG", command=save_as_png)
save_image_button.pack(pady=10,padx=10)
root.mainloop()
