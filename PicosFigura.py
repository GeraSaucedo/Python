from Tkinter import *
 
root = Tk()
root.title('canvas')

# linea (Picos inicial)
canvas = Canvas(width=300, height=210, bg='white')
canvas.pack(expand=YES, fill=BOTH) 
canvas.create_line(150, 30, 150, 180, width=10, fill='red')


 
# linea (Picos inicial)
#canvas = Canvas(width=300, height=210, bg='white')
#canvas.pack(expand=YES, fill=BOTH) 
#canvas.create_line(30, 180, 270, 180, width=10, fill='blue')
#canvas.create_line(150, 30, 150, 180, width=10, fill='blue')


 
root.mainloop()