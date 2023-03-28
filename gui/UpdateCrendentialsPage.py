import tkinter as tk
import subprocess
import constants.ethdo_values as ethdo_constants
import constants.tkinter_values as tkinter_constants
from gui.SimplePage import SimplePage


class UpdateCrendentialsPage(SimplePage):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.ethdo_bin_path = controller.get_bin_path()
        (
            titleFrame,
            mainFrame,
            leftFrame,
            rightFrame,
            botLeftFrame,
            botRightFrame,
        ) = self.grid_configure()

        intro_msg = tk.Label(
            titleFrame,
            text="Press broadcast button to complete the process",
            font=tkinter_constants.LARGE_FONT,
        )
        intro_msg.grid(column=0, row=0)

        self.success_msg = tk.Label(mainFrame, text="Broadcast completed!")
        self.success_msg.grid(column=0, row=2)
        self.error_msg = tk.Label(mainFrame, text="Error!", fg="red")
        self.success_msg.grid(column=0, row=2)
        self.hide_result_msg()

        self.broadcast_btn = tk.Button(
            mainFrame,
            text="Broadcast",
            command=lambda: [
                self.broadcast_changes(controller.get_secrets()),
                self.disable_broadcast(),
            ],
        )
        self.broadcast_btn.grid(column=0, row=1)

        cancel_btn = tk.Button(
            botLeftFrame,
            text="Cancel",
            command=lambda: [
                controller.show_frame(
                    tkinter_constants.PageNumber.ConfirmCredentialsPage.value
                ),
                self.reset_page(),
            ],
        )
        cancel_btn.grid(column=0, row=0)

        self.end_btn = tk.Button(
            botRightFrame, text="End", command=controller.destroy, state=tk.DISABLED
        )
        self.end_btn.grid(column=0, row=0)

    def hide_result_msg(self):
        self.success_msg.grid_forget()
        self.error_msg.grid_forget()

    def broadcast_changes(self, secrets):
        mnemonic, withdrawal_addr = secrets
        # online process
        result = subprocess.run(
            [
                f'{self.ethdo_bin_path} validator credentials set --mnemonic="{mnemonic}" --withdrawal-address={withdrawal_addr} --connection={ethdo_constants.BEACON_NODE} --verbose'
            ],
            shell=True,
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(
                "Failed to broadcast using online process, please check the logs: {}".format(
                    result.stderr
                )
            )
            self.error_msg.grid()
        else:
            print("Success!")
            self.success_msg.grid()
        self.end_btn["state"] = tk.NORMAL

    def disable_broadcast(self):
        self.broadcast_btn["state"] = tk.DISABLED

    def reset_page(self):
        self.end_btn["state"] = tk.DISABLED
        self.broadcast_btn["state"] = tk.NORMAL
        self.hide_result_msg()
