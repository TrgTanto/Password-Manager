import customtkinter as ctk

from src.tabsFrame import tabsFrame

class mainAttributes(ctk.CTk):
    def __init__(self):
        super().__init__()
        ctk.set_appearance_mode('dark')
        self.title('Passwort-Manager')
        self.iconbitmap('app/icons/ico/app_icon.ico')
        self.setWindow(1300, 850)
        self.resizable(False, False)

        # Show Tabs
        self.tabs = tabsFrame(self)
        self.tabs.place(anchor="center", relx=0.09, rely=0.5)

        # Overview (Übersicht)
        # Passwords (Passwörter)
        # Generator
        # Passwort-Checker
        # Hash Calculator (Hash-Rechner)
        # Settings (Einstellung)

    def setWindow(self, width: int, height: int):
        x = int((self.winfo_screenwidth() / 2) - (width / 2))
        y = int((self.winfo_screenheight() / 2) - (height / 2))
        self.geometry(f"{width}x{height}+{x}+{y}")