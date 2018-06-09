from Tkinter import *
 
root = Tk()
root.title('canvas')

p1x1 = 150
p1y1 = 70
p1x2 = 150
p1y2 = 180

p2x1 = 40
p2y1 = 180
p2x2 = 150
p2y2 = 180

p3x1 = 150
p3y1 = 180
p3x2 = 270
p3y2 = 180

# linea (Picos inicial)
canvas = Canvas(width=300, height=210, bg='white')
canvas.pack(expand=YES, fill=BOTH) 
#Pico inicial 1
#canvas.create_line(p1x1, p1y1, p1x2, p1y2, width=5, fill='red')
canvas.create_line(p1x1, p1y1, p1x2, p1y2, width=5, fill='red')
canvas.create_line(p1x1   , p1y1   , p1x2+40, p1y1, width=5, fill='blue')
canvas.create_line(p1x1-40, p1y1   , p1x1   , p1y1, width=5, fill='green')
canvas.create_line(p1x1   , p1y1-40, p1x1   , p1y1, width=5, fill='black')
#Pico inicial 2
canvas.create_line(p2x1   , p2y1   , p2x2   , p2y2, width=5, fill='red')
canvas.create_line(p2x1-40, p2y2   , p2x1   , p2y2, width=5, fill='black')
canvas.create_line(p2x1   , p2y1-40, p2x1   , p2y2, width=5, fill='blue')
canvas.create_line(p2x1   , p2y1+40, p2x1   , p2y2, width=5, fill='green')


#Pico inicial 3
#canvas.create_line(p3x1, p3y1, p3x2, p3y2, width=5, fill='red')




#canvas.create_line(x1, y1, x2, y2, width=5, fill='red')


 
# linea (Picos inicial)
#canvas = Canvas(width=300, height=210, bg='white')
#canvas.pack(expand=YES, fill=BOTH) 
#canvas.create_line(30, 180, 270, 180, width=10, fill='blue')
#canvas.create_line(150, 30, 150, 180, width=10, fill='blue')


 
root.mainloop()