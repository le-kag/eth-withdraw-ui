import tkinter as tk


class SimplePage(tk.Frame):
    def __init__(self):
        pass

    def grid_configure(self):
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=20)
        self.grid_columnconfigure(2, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.grid_rowconfigure(1, weight=8)
        self.grid_rowconfigure(2, weight=1)

        titleFrame = tk.Frame(self)
        mainFrame = tk.Frame(self)
        leftFrame = tk.Frame(self)
        rightFrame = tk.Frame(self)
        botLeftFrame = tk.Frame(self)
        botRightFrame = tk.Frame(self)

        titleFrame.grid(column=0, row=0, columnspan=3)
        mainFrame.grid(column=1, row=1)
        leftFrame.grid(column=0, row=1, sticky="WENS")
        rightFrame.grid(column=2, row=1, sticky="WENS")
        botLeftFrame.grid(column=0, row=2)
        botRightFrame.grid(column=2, row=2)

        return titleFrame, mainFrame, leftFrame, rightFrame, botLeftFrame, botRightFrame
