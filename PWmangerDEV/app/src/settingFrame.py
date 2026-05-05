import customtkinter as ctk

class settingFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
            fg_color="#030D17",
            width=1058,
            height=50,
            corner_radius=0,
            border_width=1,
            border_color="#212830"
        )