from tkinter import *

color = "SlateGray4"
width, height = 300, 150
desiredX, desiredY = width * 0.5, height * 0.75
root = Tk()
root.title("Snozberries")

root.geometry(f"{width}x{height}")
root.bind("<Escape>", lambda e: root.destroy())
root.configure(bg=color)


def one():  ##  takes many parameters during construction
    print("Found a button!")


def two(event):     
    print( f'x: {event .x}, y: {event.y}' )
    if (
        event.x >= desiredX - 25
        and event.x <= desiredX + 25
        and event.y >= desiredY - 25
        and event.y <= desiredY + 25
    ):
        print("Found another button!")


Label(root, bg=color, text="We are the musicmakers,").pack()
Label(root, bg=color, text="and we are the dreamers of the dreams.").pack()

Button(
    root,
    bg=color,
    fg=color,
    activebackground=color,
    activeforeground=color,
    highlightbackground=color,
    borderwidth=0,
    command=one,
).pack()

Label(root, bg=color, text="Button, button").pack()
Label(root, bg=color, text="who's got the button?").pack()

root.bind("<Button-1>", two)
root.mainloop()
