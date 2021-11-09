from tkinter import *
import irtaxscript as calculator

window = Tk("Imperium Romanum Tax Calculator")

res = [0.0, 0.0]

def process():
    for i in window.winfo_children():
        if isinstance(i, Entry):
            if not (i.get() == "" or i.get() == ''):
                result = calculator.calculate(float(i.get()))
                res[0] = result[0]
                res[1] = result[1]
    cleanScreen()
    main()

def cleanScreen():
    for i in window.winfo_children():
        i.destroy()     

def main():
    widgets = [
        Label(window, text="Tax Calculator", font=70),
        Entry(window, text="Salary", width=50),
        Button(window, text="Enter", command=process, width=20, height=2),
    ]

    if (res[0] != 0.0) or (res[1] != 0.0):
        widgets.append(Label(window, text="takehome $"+str(res[0])))
        widgets.append(Label(window, text="tax $"+str(res[1])))

    for i in widgets:
        i.pack(fill=None, expand=False)

if __name__ == '__main__':
    main()

window.mainloop()