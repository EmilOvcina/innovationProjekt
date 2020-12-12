import sallingUtils as salling
import tkinter as tk


class Main:
    def __init__(self):
        self.window = tk.Tk(className=".Allergen App")
        self.window.geometry("600x400")

        tk.Label(self.window, text="Find Produkt").grid(row=0)
        self.e1 = tk.Entry(self.window)
        self.e1.grid(row=0, column=1)

        self.displayText = tk.Text(self.window, height=40, width=40, foreground="black", font=("Helvetica", 16), wrap=tk.WORD)
        self.displayText.grid(row=3, column=2)
        self.displayText.insert(1.0, "test")
        self.displayText.configure(state='disabled')
        tk.Button(self.window, highlightbackground="black", text="Search", command=self.changeText).grid(row=1, column=0)

        self.window.mainloop()

    def changeText(self):
        if len(self.e1.get()) > 0:
            self.displayText.configure(state='normal')
            self.displayText.delete(1.0, "end")
            self.displayText.insert(1.0, str(salling.find_ingredients(self.e1.get())))
            self.displayText.configure(state='disabled')


app = Main()
