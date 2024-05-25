from tkinter import *

root = Tk()
canvas_width = 800
canvas_height = 400

root.geometry(f"{canvas_width}x{canvas_height}")

root.title("Canvas in tkinter")

# Creating the canvas widget

draw_canvas = Canvas(root,width=canvas_width,height=canvas_height)
draw_canvas.pack()

draw_canvas.create_line(0,0,800,400)
draw_canvas.create_line(0,400,800,0)



draw_canvas.create_rectangle(30,50,700,300,fill="salmon")

draw_canvas.create_oval(30,50,700,300)
draw_canvas.create_text(200,200,text="Arnab Mitra",font="helvetica 19 bold",angle=45)

draw_canvas.create_arc(90,160,450,300,fill="teal")


root.mainloop()