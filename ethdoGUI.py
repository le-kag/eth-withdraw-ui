import tkinter as tk
import sys, os
import constants.tkinter_values as tkinter_constants
from gui.HomePage import HomePage
from gui.InputCrendentialsPage import InputCrendentialsPage
from gui.ConfirmCredentialsPage import ConfirmCredentialsPage
from gui.UpdateCrendentialsPage import UpdateCrendentialsPage

if getattr(sys, "frozen", False):
    application_path = sys._MEIPASS
else:
    application_path = os.path.dirname(os.path.abspath(__file__))


if sys.platform.startswith("linux") or sys.platform.startswith("darwin"):
    ETHDO_BIN_PATH = application_path + "/ethdo"
elif sys.platform.startswith("win32"):
    ETHDO_BIN_PATH = application_path + "\ethdo.exe"
else:
    raise RuntimeError("Unsupported operating system: {}".format(sys.platform))


class EthdoGUI(tk.Tk):
    mnemonic = ""
    withdrawal_addr = ""
    ethdo_bin_path = ETHDO_BIN_PATH

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        container = tk.Frame(self)
        container.winfo_toplevel().title("GUI ethdo")
        container.pack(side="top", fill="both", expand=True)

        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for page_number, F in enumerate(
            [
                HomePage,
                InputCrendentialsPage,
                ConfirmCredentialsPage,
                UpdateCrendentialsPage,
            ]
        ):
            frame = F(container, self)
            self.frames[page_number] = frame
            frame.grid(row=0, column=0, sticky="nsew")
        self.show_frame(tkinter_constants.PageNumber.HomePage.value)

    def show_frame(self, new_page):
        frame = self.frames[new_page]
        frame.tkraise()

    def update_values(self, mnemonic, withdrawal_addr):
        self.mnemonic = mnemonic.get()
        self.withdrawal_addr = withdrawal_addr.get()

    def get_secrets(self):
        return (self.mnemonic, self.withdrawal_addr)

    def reset_values(self):
        self.mnemonic = ""
        self.withdrawal_addr = ""

    def get_bin_path(self):
        return self.ethdo_bin_path

    def destruct(self):
        self.destroy()


app = EthdoGUI()
app.mainloop()
