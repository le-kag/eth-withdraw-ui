import customtkinter
from PIL import Image
import os
import tkinter

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

        # create credentials frame
        self.credentials_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.credentials_frame.grid(row=0, column=0, sticky="ns")
        self.credentials_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
        self.credentials_label = customtkinter.CTkLabel(self.credentials_frame, text="Input your credentials\n& press continue",
                                                  font=customtkinter.CTkFont(size=17, weight="bold"))
        self.credentials_label.grid(row=0, column=0, padx=30, pady=(150, 15))
        self.mnemonic_entry = customtkinter.CTkEntry(self.credentials_frame, width=200, placeholder_text="Mnemonic")
        self.mnemonic_entry.grid(row=1, column=0, padx=30, pady=(15, 15))
        self.withdraw_entry = customtkinter.CTkEntry(self.credentials_frame, width=200, placeholder_text="Withdrawal address '0x...'")
        self.withdraw_entry.grid(row=2, column=0, padx=30, pady=(0, 15))
        self.credentials_button = customtkinter.CTkButton(self.credentials_frame, text="Continue", command=self.credentials_event, width=200)
        self.credentials_button.grid(row=3, column=0, padx=30, pady=(15, 15))
        self.reset_button = customtkinter.CTkButton(self.credentials_frame, text="Reset", width=150)
        self.reset_button.grid(row=4, column=0, padx=30, pady=(0, 30))

        # create main frame
        self.main_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.main_frame.grid_columnconfigure(0, weight=1)
        self.main_label = customtkinter.CTkLabel(self.main_frame, text="⚠️ This is a ONE TIME process ⚠️\nPress confirm after verifying your values",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.main_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.reveal_button = customtkinter.CTkButton(self.main_frame, text="Reveal", width=200)
        self.reveal_button.grid(row=1, column=0, padx=30, pady=(80, 30))
        self.confirm_button = customtkinter.CTkButton(self.main_frame, text="Confirm", command=self.broadcast_event, width=150)
        self.confirm_button.grid(row=2, column=0, padx=30, pady=(15, 30))
        self.back_button = customtkinter.CTkButton(self.main_frame, text="Back", command=self.back_event, width=150)
        self.back_button.grid(row=3, column=0, padx=30, pady=(15, 15))

        # create broadcast frame
        self.broadcast_frame = customtkinter.CTkFrame(self, corner_radius=0)
        self.broadcast_frame.grid_columnconfigure(0, weight=1)
        self.broadcast_label = customtkinter.CTkLabel(self.broadcast_frame, text="Press broadcast to complete the process",
                                                 font=customtkinter.CTkFont(size=20, weight="bold"))
        self.broadcast_label.grid(row=0, column=0, padx=30, pady=(30, 15))
        self.broadcast_button = customtkinter.CTkButton(self.broadcast_frame, text="Broadcast", width=150)
        self.broadcast_button.grid(row=1, column=0, padx=30, pady=(60, 30))
        self.back_button2 = customtkinter.CTkButton(self.broadcast_frame, text="Back", command=self.second_back_event, width=150)
        self.back_button2.grid(row=2, column=0, padx=30, pady=(15, 15))


    def credentials_event(self):
        print("credentials pressed - mnemonic:", self.mnemonic_entry.get(), "withdraw:", self.withdraw_entry.get())

        self.credentials_frame.grid_forget()  # remove credentials frame
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show main frame

    def back_event(self):
        self.main_frame.grid_forget()  # remove main frame
        self.credentials_frame.grid(row=0, column=0, sticky="ns")
        self.credentials_frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)  # show credentials frame

    def reveal_event(self):
        print("Reveal pressed")

    def second_back_event(self):
        self.broadcast_frame.grid_forget()
        self.main_frame.grid(row=0, column=0, sticky="nsew", padx=100)

    def broadcast_event(self):
        print("Broadcast pressed")
        self.main_frame.grid_forget()  # remove main frame
        self.broadcast_frame.grid(row=0, column=0, sticky="nsew", padx=100)  # show broadcast frame


if __name__ == "__main__":
    app = App()
    app.mainloop()
