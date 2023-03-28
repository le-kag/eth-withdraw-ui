import tkinter as tk
import webbrowser
import constants.links as link_constants
import constants.tkinter_values as tkinter_constants
from gui.SimplePage import SimplePage


class ConfirmCredentialsPage(SimplePage):
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
        
        self.refresh_mainFrame(mainFrame, controller)

        warning_label = tk.Label(
            titleFrame,
            text="*** this is a ONE TIME process *** \n press confirm after checking your values",
            font=("Verdana", 12),
        )
        warning_label.grid()

        cancel_btn = tk.Button(
            botLeftFrame,
            text="Cancel",
            height=1,
            width=5,
            command=lambda: [
                controller.show_frame(
                    tkinter_constants.PageNumber.InputCredentialsPage.value
                ),
                self.refresh_mainFrame(mainFrame, controller)
            ],
        )
        cancel_btn.grid()

        confirm_btn = tk.Button(
            botRightFrame,
            text="Confirm",
            height=1,
            width=5,
            command=lambda: [
                controller.show_frame(
                    tkinter_constants.PageNumber.UpdateCredentialsPage.value
                )
            ],
        )
        confirm_btn.grid()

    def refresh_mainFrame(self, mainFrame, controller):
        mainFrame.unbind(
            "<Configure>"
        )
        
        for widget in mainFrame.winfo_children():
            widget.destroy()
        
        reveal_btn = tk.Button(
            mainFrame,
            text="Reveal secrets",
            height=1,
            width=10,
            command=lambda: [
                self.reveal_secrets(mainFrame, controller),
                reveal_btn.grid_forget(),
            ],
        )
        reveal_btn.grid()

    def reveal_secrets(self, mainFrame, controller):
        mnemonic, withdrawal_addr = controller.get_secrets()

        etherscan_link = link_constants.ETHERSCAN_LINK + withdrawal_addr

        mnemonic_msg = tk.Label(mainFrame, text="This is your mnemonic:")
        mnemonic_msg.grid(column=0, row=1, pady=(20, 0), sticky=tk.W)
        mnemonic_check = tk.Label(
            mainFrame,
            text=f"{mnemonic}",
            wraplength=mainFrame.winfo_width(),
            font=("Verdana", 10, "italic"),
        )
        mnemonic_check.grid(column=0, row=2,columnspan=2, pady=(0, 10), sticky=tk.W)
        mainFrame.bind(
            "<Configure>",
            lambda e: mnemonic_check.config(wraplength=mainFrame.winfo_width()),
        )

        withdrawal_check = tk.Label(mainFrame, text=f"check your withdrawal address:")
        withdrawal_check.grid(column=0, row=3, sticky=tk.W)
        withdrawal_etherscan_link = tk.Label(
            mainFrame,
            text=f"{etherscan_link}",
            fg="blue",
            cursor="hand2",
            font=("Helveticabold"),
        )
        withdrawal_etherscan_link.grid(column=0, row=4, sticky=tk.W)
        withdrawal_etherscan_link.bind(
            "<Button-1>", lambda e: webbrowser.open_new_tab(etherscan_link)
        )
        