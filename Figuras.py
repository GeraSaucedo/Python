from Tkinter import *
 
root = Tk()
root.title('canvas')
 
# circulo
canvas = Canvas(width=300, height=210, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_oval(10, 10, 200, 200, width=5, fill='blue')
 
# rectangulo
canvas = Canvas(width=300, height=210, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_rectangle(10, 10, 200, 200, width=5, fill='red')
 
# linea
canvas = Canvas(width=300, height=210, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_line(0, 200, 200, 0, width=10, fill='green')
canvas.create_line(0, 0, 200, 200, width=10, fill='red')
 
# quesito
canvas = Canvas(width=300, height=200, bg='white')
canvas.pack(expand=YES, fill=BOTH)
canvas.create_arc(10, 10, 190, 190, start=270, extent=90, fill='gray90')
 
# arco
canvas = Canvas(root, width =300, height=200, bg='white')
canvas.pack(expand=YES, fill=BOTH)
xy = 10, 10, 190, 190
canvas.create_arc(xy, start=0, extent=270, fill='gray60')
 
root.mainloop()