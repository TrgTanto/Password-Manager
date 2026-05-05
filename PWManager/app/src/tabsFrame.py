import customtkinter as ctk
import tkinter as tk

from PIL import Image
from src.resourcePath import resource_path
from src.settingFrame import settingFrame
from src.passwordFrame import passwordFrame
from src.generatorFrame import generatorFrame
from src.checkerFrame import checkerFrame
from src.calculatorFrame import calculatorFrame

class tabsFrame(ctk.CTkFrame):
    def __init__(self, master):
        super().__init__(master,
            fg_color="#010811",
            width=250,
            height=850,
            corner_radius=0,
            border_width=1,
            border_color="#212830"
        )

        # tabsFrame Design
        self.appIcon = ctk.CTkLabel(master=self,
            text="",
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/inApp.png")), size=(45, 45)),
        )
        self.iconText = ctk.CTkButton(master=self,
            text="TantoVault",
            fg_color="transparent",
            hover="disabled",
            font=("Segoe UI", 19, "bold"),
            text_color="#ECEEEF",
            width=20,
            height=20,
        )
        self.passwordManagerText = ctk.CTkLabel(master=self,
            text="Passwort-Manager",
            font=("Segoe UI", 12.5),
            text_color="#90939C"
            )
        # Buttons
        self.passwordFrameButton = ctk.CTkButton(master=self,
            text="Passwörter",
            fg_color="transparent",
            hover_color="#07329B",
            border_width=1,
            border_color="#010910",
            width=225,
            height=40,
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/passwordButton.png")), size=(25, 25)),
            anchor="w",
            font=("Roboto Medium", 15),
            text_color="#8E97A8",
            corner_radius=4,
            command=lambda:self.changeButtonColor("passwordFrameButton")
        )
        self.generatorFrameButton = ctk.CTkButton(master=self,
            text="Generator",
            fg_color="transparent",
            hover_color="#07329B",
            border_width=1,
            border_color="#010910",
            width=225,
            height=40,
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/generatorButton.png")), size=(25, 25)),
            anchor="w",
            font=("Roboto Medium", 15),
            text_color="#8E97A8",
            corner_radius=4,
            command=lambda:self.changeButtonColor("generatorFrameButton")
        )
        self.checkerFrameButton = ctk.CTkButton(master=self,
            text="Passwort-Checker",
            fg_color="transparent",
            hover_color="#07329B",
            border_width=1,
            border_color="#010910",
            width=225,
            height=40,
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/checkerButton.png")), size=(25, 25)),
            anchor="w",
            font=("Roboto Medium", 15),
            text_color="#8E97A8",
            corner_radius=4,
            command=lambda:self.changeButtonColor("checkerFrameButton")
        )
        self.calculatorFrameButton = ctk.CTkButton(master=self,
            text="Hash-Rechner",
            fg_color="transparent",
            hover_color="#07329B",
            border_width=1,
            border_color="#010910",
            width=225,
            height=40,
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/calculatorButton.png")), size=(25, 25)),
            anchor="w",
            font=("Roboto Medium", 15),
            text_color="#8E97A8",
            corner_radius=4,
            command=lambda:self.changeButtonColor("calculatorFrameButton")
        )

        # place all Widgets
        self.appIcon.place(anchor="center", relx=0.175, rely=0.06)
        self.iconText.place(anchor="center", relx=0.488, rely=0.05)
        self.passwordManagerText.place(anchor="center", relx=0.49, rely=0.076)
        self.passwordFrameButton.place(anchor="center", relx=0.52, rely=0.15)
        self.generatorFrameButton.place(anchor="center", relx=0.52, rely=0.20)
        self.checkerFrameButton.place(anchor="center", relx=0.52, rely=0.25)
        self.calculatorFrameButton.place(anchor="center", relx=0.52, rely=0.3)


        # Load all Frames
        self.settingFrame = settingFrame(master)
        self.passwordFrame = passwordFrame(master)
        self.generatorFrame = generatorFrame(master)
        self.checkerFrame = checkerFrame(master)
        self.calculatorFrame = calculatorFrame(master)
    
        # Set settingFrame
        self.settingFrame.place(anchor="center", relx=0.593, rely=0.03)
        self.changeButtonColor("passwordFrameButton") # startFrame

    def resetButtonColors(self):
        self.passwordFrameButton.configure(fg_color="transparent", border_color="#010910")
        self.generatorFrameButton.configure(fg_color="transparent", border_color="#010910")
        self.checkerFrameButton.configure(fg_color="transparent", border_color="#010910")
        self.calculatorFrameButton.configure(fg_color="transparent", border_color="#010910")
    
    def resetFrames(self):
        self.passwordFrame.place_forget()
        self.generatorFrame.place_forget()
        self.checkerFrame.place_forget()
        self.calculatorFrame.place_forget()

    def changeButtonColor(self, button):
        self.resetButtonColors()

        if button == "passwordFrameButton":
            self.passwordFrameButton.configure(fg_color="#07329B", border_color="#328EFB")
            self.raiseFrame("passwordFrame")
        
        elif button == "generatorFrameButton":
            self.generatorFrameButton.configure(fg_color="#07329B", border_color="#328EFB")
            self.raiseFrame("generatorFrame")

        elif button == "checkerFrameButton":
            self.checkerFrameButton.configure(fg_color="#07329B", border_color="#328EFB")
            self.raiseFrame("checkerFrame")

        elif button == "calculatorFrameButton":
            self.calculatorFrameButton.configure(fg_color="#07329B", border_color="#328EFB")
            self.raiseFrame("calculatorFrame")

    def raiseFrame(self, frame: str,):
        self.resetFrames()
        
        if frame == "passwordFrame":
            self.passwordFrame.place(anchor="center", relx=0.593, rely=0.529)
            return

        elif frame == "generatorFrame":
            self.generatorFrame.place(anchor="center", relx=0.593, rely=0.529)
            return

        elif frame == "checkerFrame":
            self.checkerFrame.place(anchor="center", relx=0.593, rely=0.529)
            return

        elif frame == "calculatorFrame":
            self.calculatorFrame.place(anchor="center", relx=0.593, rely=0.529)
            return