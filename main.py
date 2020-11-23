import tkinter as tk

def calculator(display_string):
    ans = eval(display_string)
    return ans


root = tk.Tk()

canvas = tk.Canvas(root, height = 300, width = 200)
canvas.pack()

frame = tk.Frame(root, bg = 'black')
frame.place(relwidth = 1, relheight = 1)




#########
display_string = tk.StringVar()
calculated_value = tk.StringVar()

text1 = tk.Label(frame, textvar = display_string, bg= 'white')
text1.place(relx =0.05, rely = 0, relwidth=0.9, relheight = 0.08)

text2 = tk.Label(frame, textvar = calculated_value, bg= 'grey')
text2.place(relx =0.05, rely = 0.1, relwidth=0.9, relheight = 0.08)

def on_click():
    calculated_value.set(calculator(display_string.get()))

#####Function
def nine(display_string):
    display_string.set(display_string.get()+"9")

def eight(display_string):
    display_string.set(display_string.get()+"8")

def seven(display_string):
    display_string.set(display_string.get()+"7")

def six(display_string):
    display_string.set(display_string.get()+"6")

def five(display_string):
    display_string.set(display_string.get()+"5")

def four(display_string):
    display_string.set(display_string.get()+"4")

def three(display_string):
    display_string.set(display_string.get()+"3")

def two(display_string):
    display_string.set(display_string.get()+"2")

def one(display_string):
    display_string.set(display_string.get()+"1")

def zero(display_string):
    display_string.set(display_string.get()+"0")


def add(display_string):
    display_string.set(display_string.get()+"+")
def minus(display_string):
    display_string.set(display_string.get()+"-")
def multiply(display_string):
    display_string.set(display_string.get() + "*")
def divide(display_string):
    display_string.set(display_string.get() + "/")


def clear(display_string,calculated_value):
    display_string.set("")
    calculated_value.set("")










#######Button

button7 = tk.Button(frame, text = " 7 ", bg = "pink", command = lambda:seven(display_string))
button7.place(relx=0.1,rely = 0.2, relwidth=0.14, relheight = 0.15)

button8 = tk.Button(frame, text = " 8 ", bg = "pink", command = lambda:eight(display_string))
button8.place(relx=0.3,rely = 0.2, relwidth=0.14, relheight = 0.15)

button9 = tk.Button(frame, text = " 9 ", bg = "pink", command = lambda:nine(display_string))
button9.place(relx=0.5,rely = 0.2, relwidth=0.14, relheight = 0.15)

button4 = tk.Button(frame, text = " 4 ", bg = "pink", command = lambda:four(display_string))
button4.place(relx=0.1,rely = 0.4, relwidth=0.14, relheight = 0.15)

button5 = tk.Button(frame, text = " 5 ", bg = "pink", command = lambda:five(display_string))
button5.place(relx=0.3,rely = 0.4, relwidth=0.14, relheight = 0.15)

button6 = tk.Button(frame, text = " 6 ", bg = "pink", command = lambda:six(display_string))
button6.place(relx=0.5,rely = 0.4, relwidth=0.14, relheight = 0.15)

button1 = tk.Button(frame, text = " 1 ", bg = "pink", command = lambda:one(display_string))
button1.place(relx=0.1,rely = 0.6, relwidth=0.14, relheight = 0.15)

button2 = tk.Button(frame, text = " 2 ", bg = "pink", command = lambda:two(display_string))
button2.place(relx=0.3,rely = 0.6, relwidth=0.14, relheight = 0.15)

button3 = tk.Button(frame, text = " 3 ", bg = "pink", command = lambda:three(display_string))
button3.place(relx=0.5,rely = 0.6, relwidth=0.14, relheight = 0.15)

buttonC = tk.Button(frame, text = " C ", bg = "red", command = lambda:clear(display_string, calculated_value))
buttonC.place(relx=0.1,rely = 0.8, relwidth=0.14, relheight = 0.15)

button0 = tk.Button(frame, text = " 0 ", bg = "pink", command = lambda:zero(display_string))
button0.place(relx=0.3,rely = 0.8, relwidth=0.14, relheight = 0.15)

buttonEq = tk.Button(frame, text = " = ", bg = "red", command = on_click)
buttonEq.place(relx=0.5,rely = 0.8, relwidth=0.14, relheight = 0.15)

######

buttonD = tk.Button(frame, text = " / ", bg = "orange", command = lambda:divide(display_string))
buttonD.place(relx=0.7,rely = 0.2, relwidth=0.16, relheight = 0.15)

buttonM = tk.Button(frame, text = " * ", bg = "orange", command = lambda:multiply(display_string))
buttonM.place(relx=0.7,rely = 0.4, relwidth=0.16, relheight = 0.15)

buttonS = tk.Button(frame, text = " - ", bg = "orange", command = lambda:minus(display_string))
buttonS.place(relx=0.7,rely = 0.6, relwidth=0.16, relheight = 0.15)

buttonA = tk.Button(frame, text = " + ", bg = "orange", command = lambda:add(display_string))
buttonA.place(relx=0.7,rely = 0.8, relwidth=0.16, relheight = 0.15)




root.mainloop()