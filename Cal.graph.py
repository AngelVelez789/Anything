from tkinter import *
import parser
window = Tk()
window.title("Cal Angel")


display= Entry(window, font=("Calibri 20"))
display.grid(row = 0, column = 0,columnspan = 25, padx =4, pady = 4 )

i=0

def get_numbers(n):
    global i
    display.insert(i,n)
    i+=1

def get_operation(operator):
    global i
    operator_length = len(operator)
    display.insert(i,operator)
    i+=operator_length


def clear_display():
    display.delete(0, END)

def undo():
    display_state = display.get()
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0,display_new_state)
    else:
        clear_display()
        display.insert(0, "Error")


def calculate():
    display_state = display.get()
    try:
        math_expression= parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except expression as identifier:
        clear_display()
        display.insert(0, "Error")

#Num
Button(window, text="1",command=lambda:get_numbers(1)).grid(row=2,column=0)
Button(window, text="2",command=lambda:get_numbers(2)).grid(row=2,column=1)
Button(window, text="3",command=lambda:get_numbers(3)).grid(row=2,column=2)

Button(window, text="4",command=lambda:get_numbers(4)).grid(row=3,column=0)
Button(window, text="5",command=lambda:get_numbers(5)).grid(row=3,column=1)
Button(window, text="6",command=lambda:get_numbers(6)).grid(row=3,column=2)

Button(window, text="7",command=lambda:get_numbers(7)).grid(row=4,column=0)
Button(window, text="8",command=lambda:get_numbers(8)).grid(row=4,column=1)
Button(window, text="9",command=lambda:get_numbers(9)).grid(row=4,column=2)


#Buttons Part 2


Button(window, text="AC",command=lambda:clear_display()).grid(row=5,column=0)
Button(window, text="0",command=lambda:get_numbers(0)).grid(row=5,column=1)
Button(window, text="%",command=lambda: get_operation("%")).grid(row=5,column=2)

Button(window, text="+",command=lambda: get_operation("+")).grid(row=2,column=3)
Button(window, text="-",command=lambda: get_operation("-")).grid(row=3,column=3)
Button(window, text="*",command=lambda: get_operation("*")).grid(row=4,column=3)
Button(window, text="/",command=lambda: get_operation("/")).grid(row=5,column=3)


Button(window, text="←",command=lambda: undo()).grid(row=2,column=4,sticky=W+E,columnspan=2)
Button(window, text="exp",command=lambda: get_operation("**")).grid(row=3,column=4,sticky=W+E)
Button(window, text="^2",command=lambda: get_operation("**2")).grid(row=3,column=5,sticky=W+E )
Button(window, text="(", command=lambda: get_operation("(")).grid(row=4,column=4,sticky=W+E)
Button(window, text=")", command=lambda: get_operation(")")).grid(row=4,column=5,sticky=W+E)
Button(window, text="=",command=lambda :calculate()).grid(row=5, column=4,sticky=W+E,columnspan=2)

window.mainloop() 
