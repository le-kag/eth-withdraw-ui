import customtkinter
from PIL import Image
import os
import tkinter
import webbrowser

customtkinter.set_appearance_mode("dark")


class App(customtkinter.CTk):
    width = 900
    height = 600

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("eth-do")
        self.geometry(f"{self.width}x{self.height}")
        self.resizable(False, False)

        # load and create background image
        current_path = os.path.dirname(os.path.realpath(__file__))
        self.bg_image = customtkinter.CTkImage(Image.open(current_path + "/assets/gradient2.jpg"),
                                               size=(self.width, self.height))
        self.bg_image_label = customtkinter.CTkLabel(self, image=self.bg_image)
        self.bg_image_label.grid(row=0, column=0)

        # create start & explanation frame
        self.start_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.start_frame.grid(row=0, column=0, padx=100)
        self.start_label = customtkinter.CTkLabel(self.start_frame, text="eth-do", font=customtkinter.CTkFont(size=40, weight="bold"))
        self.start_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.explanation_label = customtkinter.CTkLabel(self.start_frame, text="This is a tool to help you\nwithdraw your ETH from the\nEthereum 2.0 deposit contract",
                                                    font=customtkinter.CTkFont(size=17, weight="bold"))
        self.explanation_label.grid(row=1, column=0, padx=30, pady=(15, 15), sticky="nsew")
        self.start_button = customtkinter.CTkButton(self.start_frame, text="Start", command=self.start_event, width=200)
        self.start_button.grid(row=2, column=0, padx=30, pady=(15, 15))


        # create credentials frame
        self.credentials_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.credentials_frame.grid(row=0, column=0, sticky="ns")
        self.credentials_label = customtkinter.CTkLabel(self.credentials_frame, text="Withdraw file seed phrase",
                                                  font=customtkinter.CTkFont(size=17, weight="bold"))
        self.credentials_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.mnemonic_entry = customtkinter.CTkEntry(self.credentials_frame, width=200, placeholder_text="Withdrawal mnemonic 'word1 word2 ...'")
        self.mnemonic_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.credentials_button = customtkinter.CTkButton(self.credentials_frame, text="Continue", command=self.credentials_event, width=200)
        self.credentials_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.reset_button = customtkinter.CTkButton(self.credentials_frame, text="Reset", width=150)
        self.reset_button.grid(row=4, column=0, padx=30, pady=(0, 30))

        # create credentials success frame
        self.credentials_success_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.credentials_success_frame.grid_columnconfigure(0, weight=1)
        self.credentials_success_label = customtkinter.CTkLabel(self.credentials_success_frame, text="Your seed is confirmed",
                                                    font=customtkinter.CTkFont(size=17, weight="bold"))
        self.credentials_success_label.grid(row=0, column=0, padx=30, pady=(150, 5))
        self.mnemonic_value_label = customtkinter.CTkLabel(self.credentials_success_frame, text="",
                                                    font=customtkinter.CTkFont(size=15))
        self.mnemonic_value_label.grid(row=1, column=0, padx=30, pady=(5, 15))
        self.credentials_success_button = customtkinter.CTkButton(self.credentials_success_frame, text="Continue", command=self.credentials_success_event, width=200)
        self.credentials_success_button.grid(row=2, column=0, padx=30, pady=(15, 15))


        # create credentials error frame
        self.credentials_error_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.credentials_error_frame.grid(row=0, column=0, sticky="ns")
        self.credentials_error_label = customtkinter.CTkLabel(self.credentials_error_frame, text="Your seed is incorrect",
                                                  font=customtkinter.CTkFont(size=17, weight="bold"))
        self.credentials_error_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.credentials_error_button = customtkinter.CTkButton(self.credentials_error_frame, text="Continue", width=200)

        # create wallet frame
        self.wallet_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.wallet_frame.grid_columnconfigure(0, weight=1)
        self.wallet_label = customtkinter.CTkLabel(self.wallet_frame, text="New withdrawal address",
                                                  font=customtkinter.CTkFont(size=17, weight="bold"))
        self.wallet_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.wallet_entry = customtkinter.CTkEntry(self.wallet_frame, width=200, placeholder_text="New withdrawal address")
        self.wallet_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.wallet_button = customtkinter.CTkButton(self.wallet_frame, text="Continue", command=self.wallet_event, width=200)
        self.wallet_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.wallet_reset_button = customtkinter.CTkButton(self.wallet_frame, text="Reset", width=150)
        self.wallet_reset_button.grid(row=4, column=0, padx=30, pady=(0, 30))

        # create confirmation frame
        self.confirmation_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.confirmation_frame.grid_columnconfigure(0, weight=1)
        self.confirmation_label = customtkinter.CTkLabel(self.confirmation_frame, text="Confirm your withdrawal",
                                                    font=customtkinter.CTkFont(size=17, weight="bold"))
        self.confirmation_label.grid(row=0, column=0, padx=30, pady=(150, 5))
        self.wallet_value_label = customtkinter.CTkLabel(self.confirmation_frame, text="",
                                                    font=customtkinter.CTkFont(size=15))
        self.wallet_value_label.grid(row=1, column=0, padx=30, pady=(5, 15))
        self.confirmation_button = customtkinter.CTkButton(self.confirmation_frame, text="Confirm", command=self.confirmation_event, width=200)
        self.confirmation_button.grid(row=2, column=0, padx=30, pady=(15, 15))
        self.confirmation_reset_button = customtkinter.CTkButton(self.confirmation_frame, text="Reset", width=150)
        self.confirmation_reset_button.grid(row=3, column=0, padx=30, pady=(0, 30))

        # create transaction success frame
        self.transaction_success_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.transaction_success_frame.grid_columnconfigure(0, weight=1)
        self.transaction_success_label = customtkinter.CTkLabel(self.transaction_success_frame, text="Your withdrawal is confirmed",
                                                    font=customtkinter.CTkFont(size=17, weight="bold"))
        self.transaction_success_label.grid(row=0, column=0, padx=30, pady=(100, 5))
        self.etherscan_link_label = customtkinter.CTkLabel(self.transaction_success_frame, text="",
                                                            font=customtkinter.CTkFont(size=20))
        self.etherscan_link_label.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.transaction_success_button = customtkinter.CTkButton(self.transaction_success_frame, text="Broadcast", command=self.transaction_success_event, width=200)
        self.transaction_success_button.grid(row=4, column=0, padx=30, pady=(15, 15))


        # create transaction error frame
        self.transaction_error_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.transaction_error_frame.grid(row=0, column=0, sticky="ns")
        self.transaction_error_label = customtkinter.CTkLabel(self.transaction_error_frame, text="Your withdrawal is incorrect",
                                                  font=customtkinter.CTkFont(size=17, weight="bold"))
        self.transaction_error_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.transaction_error_button = customtkinter.CTkButton(self.transaction_error_frame, text="Back", width=200)
        self.transaction_success_button.grid(row=1, column=0, padx=30, pady=(15, 15))

        # create seed frame
        self.seed_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.seed_frame.grid_columnconfigure(0, weight=1)
        self.seed_label = customtkinter.CTkLabel(self.seed_frame, text="⚠️ This is a ONE TIME process ⚠️\nPress confirm after verifying your values",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.seed_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.reveal_button = customtkinter.CTkButton(self.seed_frame, text="Reveal", width=200)
        self.reveal_button.grid(row=1, column=0, padx=30, pady=(80, 30))
        self.confirm_button = customtkinter.CTkButton(self.seed_frame, text="Confirm", command=self.broadcast_event, width=150)
        self.confirm_button.grid(row=2, column=0, padx=30, pady=(15, 30))
        self.back_button = customtkinter.CTkButton(self.seed_frame, text="Back", command=self.back_event, width=150)
        self.back_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        # create broadcast frame
        self.broadcast_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.broadcast_frame.grid_columnconfigure(0, weight=1)
        self.broadcast_label = customtkinter.CTkLabel(self.broadcast_frame, text="Press broadcast to complete the process",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.broadcast_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.broadcast_button = customtkinter.CTkButton(self.broadcast_frame, text="Broadcast", width=150)
        self.broadcast_button.grid(row=1, column=0, padx=30, pady=(60, 30))
        self.back_button2 = customtkinter.CTkButton(self.broadcast_frame, text="Back", command=self.second_back_event, width=150)
        self.back_button2.grid(row=2, column=0, padx=30, pady=(15, 15))

        # create stop node frame
        self.stop_node_frame = customtkinter.CTkFrame(self, corner_radius=20)
        self.stop_node_frame.grid_columnconfigure(0, weight=1)
        self.stop_node_label = customtkinter.CTkLabel(self.stop_node_frame, text="Stopping your node",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.stop_node_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.stop_node_button = customtkinter.CTkButton(self.stop_node_frame, text="ok", width=150)
        self.stop_node_button.grid(row=1, column=0, padx=30, pady=(60, 30))
        self.back_button3 = customtkinter.CTkButton(self.stop_node_frame, text="Back", command=self.third_back_event, width=150)
        self.back_button3.grid(row=2, column=0, padx=30, pady=(15, 15))

        # Hide the credentials frame initially
        self.credentials_frame.grid_remove()

        # Hide the seed frame initially
        self.seed_frame.grid_remove()

        # Hide the broadcast frame initially
        self.broadcast_frame.grid_remove()

        # Hide the stop node frame initially
        self.stop_node_frame.grid_remove()

        # Hide the transaction success frame initially
        self.transaction_success_frame.grid_remove()

        # Hide the transaction error frame initially
        self.transaction_error_frame.grid_remove()

        # Hide the confirmation frame initially
        self.confirmation_frame.grid_remove()

        # Hide the wallet frame initially
        self.wallet_frame.grid_remove()

        # Hide the credentials success frame initially
        self.credentials_success_frame.grid_remove()

        # Hide the credentials error frame initially
        self.credentials_error_frame.grid_remove()

    def credentials_event(self):
        print("credentials pressed - mnemonic:", self.mnemonic_entry.get())
        self.mnemonic_value_label.configure(text=self.mnemonic_entry.get())
        self.credentials_frame.grid_forget()  # remove credentials frame
        # show credentials success frame
        self.credentials_success_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    def credentials_success_event(self):
        self.credentials_success_frame.grid_forget()
        # show wallet frame
        self.wallet_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    def credentials_error_event(self):
        self.credentials_error_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    def wallet_event(self):
        print("wallet pressed")
        self.wallet_value_label.configure(text=self.wallet_entry.get())
        self.wallet_frame.grid_forget()
        # show confirmation frame
        self.confirmation_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    def confirmation_event(self):
        print("confirmation pressed")
        link = "https://etherscan.io/address/" + self.wallet_entry.get()
        self.etherscan_link_label.configure(text=link)
        self.confirmation_frame.grid_forget()
        # show transaction success frame
        self.transaction_success_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    def transaction_success_event(self):
        self.transaction_success_frame.grid_forget()
        self.stop_node_frame.grid(row=0, column=0, sticky="nsew", padx=100)


    def start_event(self):
        print("Start pressed")
        self.start_frame.grid_forget()
        self.credentials_frame.grid(row=0, column=0, sticky="ns")
        self.credentials_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    def back_event(self):
        self.seed_frame.grid_forget()  # remove seed frame
        self.credentials_frame.grid(row=0, column=0, sticky="ns")
        self.credentials_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)  # show credentials frame

    def reveal_event(self):
        print("Reveal pressed")

    def second_back_event(self):
        self.broadcast_frame.grid_forget()
        self.seed_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    def third_back_event(self):
        self.stop_node_frame.grid_forget()
        self.start_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    def broadcast_event(self):
        print("Broadcast pressed")
        self.seed_frame.grid_forget()  # remove seed frame
        self.broadcast_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show broadcast frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
