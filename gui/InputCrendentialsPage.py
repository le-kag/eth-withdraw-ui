import tkinter as tk
import tkinter.ttk as ttk
import module.entryEx as entryEx
import constants.tkinter_values as tkinter_constants
from gui.SimplePage import SimplePage


class InputCrendentialsPage(SimplePage):
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

        intro_line = tk.Label(titleFrame, text="Input your credentials and verify them")
        intro_line.grid()

        tk.Label(mainFrame, text="Insert your mnemonic").grid(sticky="WENS")
        self.mnemonic_entry = entryEx.EntryEx(mainFrame)
        self.mnemonic_entry.grid(column=1, row=0, columnspan=2, sticky="WENS")

        tk.Label(mainFrame, text="Insert your new withdrawal address").grid(
            column=0, row=2, padx=(20, 0), sticky="WENS"
        )
        self.withdrawal_addr_entry = entryEx.EntryEx(mainFrame)
        self.withdrawal_addr_entry.grid(column=1, row=2, columnspan=2, sticky="WENS")

        self.continue_btn = tk.Button(
            botRightFrame,
            text="Continue",
            height=1,
            width=5,
            command=lambda: [self.next_page(controller)],
        )
        self.continue_btn.grid()

        reset_btn = tk.Button(
            botLeftFrame,
            text="Reset",
            height=1,
            width=5,
            command=lambda: self.reset_page(),
        )
        reset_btn.grid()

        cancel_btn = tk.Button(
            botLeftFrame,
            text="Cancel",
            height=1,
            width=5,
            command=lambda: controller.show_frame(
                tkinter_constants.PageNumber.HomePage.value
            ),
        )
        cancel_btn.grid(row=1)

    def reset_page(self):
        for entry in [self.mnemonic_entry, self.withdrawal_addr_entry]:
            entry["state"] = tk.NORMAL
            entry.delete(0, tk.END)

    def next_page(self, controller):
        controller.update_values(self.mnemonic_entry, self.withdrawal_addr_entry)
        controller.show_frame(tkinter_constants.PageNumber.ConfirmCredentialsPage.value)
