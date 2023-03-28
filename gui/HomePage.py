import tkinter as tk
import tkinter.ttk as ttk
import constants.tkinter_values as tkinter_constants
from gui.SimplePage import SimplePage


class HomePage(SimplePage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        (
            titleFrame,
            mainFrame,
            leftFrame,
            rightFrame,
            botLeftFrame,
            botRightFrame,
        ) = self.grid_configure()

        intro_line = tk.Label(
            titleFrame,
            text="Welcome to ethdo GUI version",
            font=tkinter_constants.LARGE_FONT,
        )
        intro_line.grid()

        disclaimer_line = tk.Label(
            mainFrame, text="The following functions are implemented: "
        )
        disclaimer_line.grid()

        available_functions_label = ttk.Labelframe(
            mainFrame, text="Available functions"
        )
        available_functions_label.grid(column=0, row=1, pady=(10, 0))

        created_functions = tk.Label(
            available_functions_label, text="change withdrawal credentials"
        )  # TODO this should be a struct or enum
        created_functions.grid(column=0, row=2, pady=(5, 5))

        continue_btn = tk.Button(
            botRightFrame,
            text="Start",
            command=lambda: controller.show_frame(
                tkinter_constants.PageNumber.InputCredentialsPage.value
            ),
        )
        continue_btn.grid()
        quit_btn = tk.Button(
            botLeftFrame, text="Quit", command=lambda: controller.destruct()
        )
        quit_btn.grid()
