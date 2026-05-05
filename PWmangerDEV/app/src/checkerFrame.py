import customtkinter as ctk
import string, clipboard, hashlib, requests, json, os

from zxcvbn import zxcvbn
from PIL import Image

unkownIcon =  'app/icons/png/unkownIcon.png'
checkIcon = 'app/icons/png/checkIcon.png'
noCheckIcon = 'app/icons/png/noCheckIcon.png'

HISTORY_FILE = "checker_history.json"

class checkerFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
            fg_color="#030D17", #030D17
            width=1058, 
            height=800,
            corner_radius=0,
            border_width=1,
            border_color="#212830"
        )

        self.title = ctk.CTkLabel(master=self,
            text="Passwort-Checker",
            font=("Segoe UI", 20, "bold"),
            text_color="#EDECE5"
        )
        self.title.place(anchor="center", relx=0.1, rely=0.05)

        self.text = ctk.CTkLabel(master=self,
            text="Prüfe die Sicherheit deiner Passwörter und erhalte Empfehlungen zur Verbesserung.",
            font=("Segoe UI", 14),
            text_color="#677073"
        )
        self.text.place(anchor="center", relx=0.2625, rely=0.08)

        # password frame
        self.enterPasswordFrame = ctk.CTkFrame(master=self,
            fg_color="#08131F",
            width=400,
            height=350,
            corner_radius=8,
            border_width=1,
            border_color="#19232F"
        )
        self.enterPasswordFrame.place(anchor="center", relx=0.208, rely=0.33)

        self.passwordTitle = ctk.CTkLabel(master=self.enterPasswordFrame,
            text="Passwort prüfen",
            font=("Roboto Medium", 17),
            text_color="#EDECE5"
        )
        self.passwordTitle.place(anchor="center", relx=0.22, rely=0.1)

        self.enterPassword = ctk.CTkEntry(master=self.enterPasswordFrame,
            placeholder_text="Passwort eingeben...",
            text_color="#E9EBEF",
            width=360,
            height=45,
            border_width=1,
            border_color="#0D2A55",
            fg_color="#020C17",
            font=("Segoe UI", 14)
        )
        self.enterPassword.place(anchor="center", relx=0.5, rely=0.3)

        # #4A4D50 transparent \ kW is not available
        self.veryWeakBar = ctk.CTkProgressBar(master=self.enterPasswordFrame,
            width=70,
            height=10,
            progress_color="#4A4D50"
        )
        self.veryWeakBar.place(anchor="center", relx=0.14, rely=0.45)

        self.weakBar = ctk.CTkProgressBar(master=self.enterPasswordFrame,
            width=70,
            height=10,
            progress_color="#4A4D50"
        )
        self.weakBar.place(anchor="center", relx=0.32, rely=0.45)

        self.midBar = ctk.CTkProgressBar(master=self.enterPasswordFrame,
            width=70,
            height=10,
            progress_color="#4A4D50"
        )
        self.midBar.place(anchor="center", relx=0.50, rely=0.45)

        self.strongBar = ctk.CTkProgressBar(master=self.enterPasswordFrame,
            width=70,
            height=10,
            progress_color="#4A4D50"
        )
        self.strongBar.place(anchor="center", relx=0.68, rely=0.45)

        self.veryStrongBar = ctk.CTkProgressBar(master=self.enterPasswordFrame,
            width=70,
            height=10,
            progress_color="#4A4D50"
        )
        self.veryStrongBar.place(anchor="center", relx=0.86, rely=0.45)

        # set bar values to 1
        self.veryWeakBar.set(1)
        self.weakBar.set(1)
        self.midBar.set(1)
        self.strongBar.set(1)
        self.veryStrongBar.set(1)

        self.strengthText = ctk.CTkLabel(master=self.enterPasswordFrame,
            text="Stärke:",
            font=("Roboto Medium", 14.5),
            text_color="#EDECE5"
        )
        self.strengthText.place(anchor="center", relx=0.115, rely=0.53)

        self.strengthTextValue = ctk.CTkLabel(master=self.enterPasswordFrame,
            text="Unbekannt",
            font=("Roboto Medium", 14.5),
            text_color="#677073"
        )
        self.strengthTextValue.place(anchor="center", relx=0.28, rely=0.53)

        self.checkStrengthButton = ctk.CTkButton(master=self.enterPasswordFrame,
            text="Passwort prüfen",
            width=360,
            height=45,
            corner_radius=8,
            fg_color="#032A82",
            hover_color="#07329B",
            image=ctk.CTkImage(dark_image=Image.open("app/icons/png/checkPasswordButton.png"), size=(25, 25)),
            command=lambda:self.checkPasswordStrength()
        )
        self.checkStrengthButton.place(anchor="center", relx=0.5, rely=0.75)

        self.information = ctk.CTkButton(master=self.enterPasswordFrame,
            text="Analyse erfolgt lokal auf deinem Gerät.",
            fg_color="transparent",
            hover="disabled",
            text_color="#677073",
            image=ctk.CTkImage(dark_image=Image.open("app/icons/png/informationClosedIcon.png"), size=(20, 20)),
        )
        self.information.place(anchor="center", relx=0.5, rely=0.9)

        # analysis frame
        self.analysisFrame = ctk.CTkFrame(master=self,
            fg_color="#08131F",
            width=620,
            height=350,
            corner_radius=8,
            border_width=1,
            border_color="#19232F"
        )
        self.analysisFrame.place(anchor="center", relx=0.695, rely=0.33)

        self.analysisTitle = ctk.CTkLabel(master=self.analysisFrame,
            text="Analyse",
            font=("Roboto Medium", 17),
            text_color="#EDECE5"
        )
        self.analysisTitle.place(anchor="center", relx=0.07, rely=0.1)

        self.analysisLengthCheck = ctk.CTkButton(master=self.analysisFrame,
            text="Länge                                                                                                                                                 16 Zeichen",
            width=600,
            height=50,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            corner_radius=0,
            text_color="#777477",
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)),
            font=("Roboto Medium", 14)
        )
        self.analysisLengthCheck.place(anchor="center", relx=0.5, rely=0.3)

        self.analysisUppercase = ctk.CTkButton(master=self.analysisFrame,
            text="Großbuchstaben                                                                                                                          Vorhanden",
            width=600,
            height=50,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            corner_radius=0,
            text_color="#777477",
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)),
            font=("Roboto Medium", 14)
        )
        self.analysisUppercase.place(anchor="center", relx=0.5, rely=0.44)

        self.analysisLowercase = ctk.CTkButton(master=self.analysisFrame,
            text="Kleinbuchstaben                                                                                                                          Vorhanden",
            width=600,
            height=50,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            corner_radius=0,
            text_color="#777477",
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)),
            font=("Roboto Medium", 14)
        )
        self.analysisLowercase.place(anchor="center", relx=0.5, rely=0.58)

        self.analysisNumbers = ctk.CTkButton(master=self.analysisFrame,
            text="Zahlen                                                                                                                                               Vorhanden",
            width=600,
            height=50,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            corner_radius=0,
            text_color="#777477",
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)),
            font=("Roboto Medium", 14)
        )
        self.analysisNumbers.place(anchor="center", relx=0.5, rely=0.72)

        self.analysisPuncs = ctk.CTkButton(master=self.analysisFrame,
            text="Sonderzeichen                                                                                                                               Vorhanden",
            width=600,
            height=50,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            corner_radius=0,
            text_color="#777477",
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)),
            font=("Roboto Medium", 14)
        )
        self.analysisPuncs.place(anchor="center", relx=0.5, rely=0.86)

        # security Evaluation frame
        self.securityEvaluationFrame = ctk.CTkFrame(master=self,
            fg_color="#08131F",
            width=300,
            height=250,
            corner_radius=8,
            border_width=1,
            border_color="#19232F"
        )
        self.securityEvaluationFrame.place(anchor="center", relx=0.161, rely=0.72)

        self.securityEvaluationTitle = ctk.CTkLabel(master=self.securityEvaluationFrame,
            text="Sicherheitsbewertung",
            font=("Roboto Medium", 17),
            text_color="#EDECE5"
        )
        self.securityEvaluationTitle.place(anchor="center", relx=0.35, rely=0.1)

        self.frequencyEvaluation = ctk.CTkLabel(master=self.securityEvaluationFrame,
            text="Häufigkeit:",
            font=("Roboto Medium", 14),
            text_color="#EDECE5",
            wraplength=280,
        )
        self.frequencyEvaluation.place(anchor="center", relx=0.2, rely=0.3)

        self.frequencyEvaluationValue = ctk.CTkLabel(master=self.securityEvaluationFrame,
            text="Unbekannt",
            font=("Roboto Medium", 14),
            fg_color="transparent",
            text_color="#677073",
            corner_radius=4
        )
        self.frequencyEvaluationValue.place(anchor="center", relx=0.5, rely=0.3)

        self.timeToCrackEvaluation = ctk.CTkLabel(master=self.securityEvaluationFrame,
            text="Geschätzte Zeit:",
            font=("Roboto Medium", 14),
            text_color="#EDECE5"
        )
        self.timeToCrackEvaluation.place(anchor="center", relx=0.255, rely=0.5)

        self.timeToCrackEvaluationValue = ctk.CTkLabel(master=self.securityEvaluationFrame,
            text="Unbekannt",
            font=("Roboto Medium", 14),
            text_color="#677073"
        )
        self.timeToCrackEvaluationValue.place(anchor="center", relx=0.62, rely=0.5)

        # recommendation frame
        self.recommendationFrame = ctk.CTkFrame(master=self,
            fg_color="#08131F",
            width=350,
            height=250,
            corner_radius=8,
            border_width=1,
            border_color="#19232F"
        )
        self.recommendationFrame.place(anchor="center", relx=0.474, rely=0.72)

        self.recommendationTitle = ctk.CTkLabel(master=self.recommendationFrame,
            text="Empfehlungen",
            font=("Roboto Medium", 17),
            text_color="#EDECE5"
        )
        self.recommendationTitle.place(anchor="center", relx=0.2, rely=0.1)

        self.recommendationUnkown = ctk.CTkLabel(master=self.recommendationFrame,
            text="Keine Empfehlungen verfügbar",
            font=("Roboto Medium", 16),
            text_color="#677073",
            fg_color="transparent"
        )
        self.recommendationUnkown.place(anchor="center", relx=0.5, rely=0.5)

        self.recommendationLength = ctk.CTkButton(master=self.recommendationFrame,
            text="Dein Passwort sollte mindestens 16 Zeichen lang sein",
            font=("Roboto", 12.5),
            text_color="#677073",
            hover="disabled",
            fg_color="transparent",
            image=ctk.CTkImage(dark_image=Image.open("app/icons/png/missing.png"), size=(25, 25))
        )

        self.recommendationUppercase = ctk.CTkButton(master=self.recommendationFrame,
            text="Füge Großbuchstaben hinzu",
            font=("Roboto", 12.5),
            text_color="#677073",
            hover="disabled",
            fg_color="transparent",
            image=ctk.CTkImage(dark_image=Image.open("app/icons/png/missing.png"), size=(25, 25))
        )

        self.recommendationLowercase = ctk.CTkButton(master=self.recommendationFrame,
            text="Füge Kleinbuchstaben hinzu",
            font=("Roboto", 12.5),
            text_color="#677073",
            hover="disabled",
            fg_color="transparent",
            image=ctk.CTkImage(dark_image=Image.open("app/icons/png/missing.png"), size=(25, 25))
        )

        self.recommendationDigits = ctk.CTkButton(master=self.recommendationFrame,
            text="Füge Zahlen hinzu",
            font=("Roboto", 12.5),
            text_color="#677073",
            hover="disabled",
            fg_color="transparent",
            image=ctk.CTkImage(dark_image=Image.open("app/icons/png/missing.png"), size=(25, 25))
        )

        self.recommendationPuncs = ctk.CTkButton(master=self.recommendationFrame,
            text="Füge Sonderzeichen hinzu",
            font=("Roboto", 12.5),
            text_color="#677073",
            hover="disabled",
            fg_color="transparent",
            image=ctk.CTkImage(dark_image=Image.open("app/icons/png/missing.png"), size=(25, 25))
        )

        # history frame
        self.historyFrame = ctk.CTkFrame(master=self,
            fg_color="#08131F",
            width=360,
            height=250,
            corner_radius=8,
            border_width=1,
            border_color="#19232F"
        )
        self.historyFrame.place(anchor="center", relx=0.817, rely=0.72)

        self.historyTitle = ctk.CTkLabel(master=self.historyFrame,
            text="Verlauf",
            font=("Roboto Medium", 17),
            text_color="#EDECE5"
        )
        self.historyTitle.place(anchor="center", relx=0.15, rely=0.1)

        self.historyPassword1 = ctk.CTkButton(master=self.historyFrame,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5",
            width=300,
            height=35,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            anchor="w",
            corner_radius=0,
            command=lambda:clipboard.copy(self.historyPassword1.cget("text"))
        )
        self.historyPassword1.place(anchor="center", relx=0.5, rely=0.245)

        self.historyPassword1Strength = ctk.CTkLabel(master=self.historyPassword1,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5"
        )
        self.historyPassword2 = ctk.CTkButton(master=self.historyFrame,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5",
            width=300,
            height=35,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            anchor="w",
            corner_radius=0,
            command=lambda:clipboard.copy((self.historyPassword2.cget("text")))
        )
        self.historyPassword2.place(anchor="center", relx=0.5, rely=0.375)

        self.historyPassword2Strength = ctk.CTkLabel(master=self.historyPassword2,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5"
        )

        self.historyPassword3 = ctk.CTkButton(master=self.historyFrame,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5",
            width=300,
            height=35,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            anchor="w",
            corner_radius=0,
            command=lambda:clipboard.copy((self.historyPassword3.cget("text")))
        )
        self.historyPassword3.place(anchor="center", relx=0.5, rely=0.5)

        self.historyPassword3Strength = ctk.CTkLabel(master=self.historyPassword3,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5"
        )

        self.historyPassword4 = ctk.CTkButton(master=self.historyFrame,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5",
            width=300,
            height=35,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            anchor="w",
            corner_radius=0,
            command=lambda:clipboard.copy((self.historyPassword4.cget("text")))
        )
        self.historyPassword4.place(anchor="center", relx=0.5, rely=0.625)

        self.historyPassword4Strength = ctk.CTkLabel(master=self.historyPassword4,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5"
        )

        self.historyPassword5 = ctk.CTkButton(master=self.historyFrame,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5",
            width=300,
            height=35,
            fg_color="transparent",
            hover="disabled",
            border_width=1,
            border_color="#19232F",
            anchor="w",
            corner_radius=0,
            command=lambda:clipboard.copy((self.historyPassword5.cget("text")))
        )
        self.historyPassword5.place(anchor="center", relx=0.5, rely=0.75)

        self.historyPassword5Strength = ctk.CTkLabel(master=self.historyPassword5,
            text="",
            font=("Roboto Medium", 12),
            text_color="#EDECE5"
        )

        self.deleteHistoryButton = ctk.CTkButton(master=self.historyFrame,
            text="Verlauf löschen",
            width=300,
            height=30,
            corner_radius=8,
            fg_color="#032A82",
            hover_color="#07329B",
            image=ctk.CTkImage(dark_image=Image.open("app/icons/png/calculatorTrashCan.png"), size=(25, 25)),
            command=lambda:self.deleteHistory()
        )
        self.deleteHistoryButton.place(anchor="center", relx=0.5, rely=0.91)

        # tip frame
        self.tipFrame = ctk.CTkButton(master=self,
            fg_color="#08131F",
            text="Ein sicheres Passwort sollte mindestens 12 Zeichen lang sein und eine Kombination aus Groß- und Kleinbuchstaben, Zahlen und Sonderzeichen enthalten.",
            text_color="#8EA5A5",
            width=1025,
            height=60,
            corner_radius=8,
            border_width=1,
            border_color="#19232F",
            hover="disabled",
            image=ctk.CTkImage(dark_image=Image.open('app/icons/png/proTipIcon.png'), size=(35, 35)),
            font=("Segoe UI", 12),
        )
        self.tipFrame.place(anchor="center", relx=0.5032, rely=0.94)
    
        self.historyList = self.loadHistory()
        if not isinstance(self.historyList, list):
            self.historyList = []

        self.updateHistoryUI()


    def checkPasswordStrength(self):
        # reset bars
        self.veryWeakBar.configure(progress_color="#4A4D50")
        self.weakBar.configure(progress_color="#4A4D50")
        self.midBar.configure(progress_color="#4A4D50")
        self.strongBar.configure(progress_color="#4A4D50")
        self.veryStrongBar.configure(progress_color="#4A4D50")

        lenPassword = len(self.enterPassword.get())
        checkedPassword = self.enterPassword.get()
        
        if lenPassword == 0:
            self.strengthTextValue.configure(text="Unbekannt", text_color="#677073")
            self.strengthTextValue.place(anchor="center", relx=0.28, rely=0.53)

            self.frequencyEvaluationValue.configure(text="Unbekannt", text_color="#677073", fg_color="transparent")
            self.timeToCrackEvaluationValue.configure(text="Unbekannt", text_color="#677073")
            self.timeToCrackEvaluationValue.place(anchor="center", relx=0.62, rely=0.5)
            self.frequencyEvaluationValue.place(anchor="center", relx=0.5, rely=0.3)

            self.recommendationUnkown.configure(text="Keine Empfehlungen verfügbar", text_color="#677073")
            self.recommendationUnkown.place(anchor="center", relx=0.5, rely=0.5)
            self.recommendationLength.place_forget()
            self.recommendationUppercase.place_forget()
            self.recommendationLowercase.place_forget()
            self.recommendationDigits.place_forget()
            self.recommendationPuncs.place_forget()

            self.analysisLengthCheck.configure(image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)))
            self.analysisUppercase.configure(image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)))
            self.analysisLowercase.configure(image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)))
            self.analysisNumbers.configure(image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)))
            self.analysisPuncs.configure(image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25)))
            return
        self.recommendationUnkown.place_forget()
        self.checkFrequency()

        '''
        Rules for Strength:
        Very Weak = Length min 1
        Weak = Length min 5
        Mid = Length min 8 and need small/big/punc and Number in password
        Strong = length min 12
        Extreme Strong = length min 16
        '''
        points = 0

        if lenPassword >= 1:
            points+=1
            self.veryWeakBar.configure(progress_color="#F32334")

        if lenPassword >= 5 and points == 1:
            points+=1
            self.weakBar.configure(progress_color="#F7722E")
        
        if (
            any(c in checkedPassword for c in string.ascii_uppercase) and
            any(c in checkedPassword for c in string.ascii_lowercase) and
            any(c in checkedPassword for c in string.digits) and
            any(c in checkedPassword for c in string.punctuation) and
            lenPassword >= 8 and points == 2
            ):
            points+=1
            self.midBar.configure(progress_color="#FBBC04")
        
        if lenPassword >= 12 and points == 3:
            points+=1
            self.strongBar.configure(progress_color="#22D341")
        
        if lenPassword >= 16 and points == 4:
            points+=1
            self.veryStrongBar.configure(progress_color="#21C53C")
        
        if points == 1:
            self.strengthTextValue.configure(text="Sehr schwach", text_color="#F32334")
            self.strengthTextValue.place(anchor="center", relx=0.305, rely=0.53)
        elif points == 2:
            self.strengthTextValue.configure(text="Schwach", text_color="#F7722E")
            self.strengthTextValue.place(anchor="center", relx=0.275, rely=0.53)
        elif points == 3:
            self.strengthTextValue.configure(text="Mittel", text_color="#FBBC04")
            self.strengthTextValue.place(anchor="center", relx=0.25, rely=0.53)
        elif points == 4:
            self.strengthTextValue.configure(text="Stark", text_color="#22D341")
            self.strengthTextValue.place(anchor="center", relx=0.25, rely=0.53)
        elif points == 5:
            self.strengthTextValue.configure(text="Sehr stark", text_color="#21C53C")
            self.strengthTextValue.place(anchor="center", relx=0.275, rely=0.53)
            self.recommendationUnkown.configure(text="Dein Passwort ist sehr stark!\nWeiter so!", text_color="#21C53C")
            self.recommendationUnkown.place(anchor="center", relx=0.5, rely=0.5)

        if lenPassword >= 16:
            self.analysisLengthCheck.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
            self.recommendationLength.place_forget()
        else:
            self.analysisLengthCheck.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
            self.recommendationLength.place(anchor="center", relx=0.5, rely=0.3)

        if any(c in checkedPassword for c in string.ascii_uppercase):
            self.analysisUppercase.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
            self.recommendationUppercase.place_forget()
        else:
            self.analysisUppercase.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
            self.recommendationUppercase.place(anchor="center", relx=0.305, rely=0.45)
        
        if any(c in checkedPassword for c in string.ascii_lowercase):
            self.analysisLowercase.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
            self.recommendationLowercase.place_forget()
        else:
            self.analysisLowercase.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
            self.recommendationLowercase.place(anchor="center", relx=0.305, rely=0.6)
        
        if any(c in checkedPassword for c in string.digits):
            self.analysisNumbers.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
            self.recommendationDigits.place_forget()
        else:
            self.analysisNumbers.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
            self.recommendationDigits.place(anchor="center", relx=0.23, rely=0.75)
        
        if any(c in checkedPassword for c in string.punctuation):
            self.analysisPuncs.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
            self.recommendationPuncs.place_forget()
        else:
            self.analysisPuncs.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
            self.recommendationPuncs.place(anchor="center", relx=0.288, rely=0.9)

        self.historyList.insert(0, checkedPassword)

        if len(self.historyList) > 5:
            self.historyList.pop()

        self.saveHistory()
        self.updateHistoryUI()

    def checkFrequency(self):
        try:
            self.changeValueCrackTime()
        except Exception:
                self.timeToCrackEvaluationValue.configure(text="Passwort zu lang\num es auszurechnen", text_color="#F32334")
                self.timeToCrackEvaluationValue.place(anchor="center", relx=0.69, rely=0.5)
                return

        password = self.enterPassword.get().encode('utf-8')

        fullHash = hashlib.sha1(password).hexdigest().upper()
        prefix = fullHash[:5]
        suffix = fullHash[5:]
        
        apiURL = f"https://api.pwnedpasswords.com/range/{prefix}"
        response = requests.get(apiURL, timeout=5)

        if response.status_code == 429:
            self.frequencyEvaluationValue.configure(text="Rate limit", text_color="#F32334", fg_color="#2A141A")
            self.timeToCrackEvaluationValue.configure(text="Rate limit", text_color="#F32334")
            return

        if response.status_code == 200:
            hashes = (line.split(':') for line in response.text.splitlines())
            
            for hashSuffix, count in hashes:
                if hashSuffix == suffix:
                    if int(count) > 10000:
                        self.frequencyEvaluationValue.configure(text="Sehr häufig", text_color="#F32334", fg_color="#2A141A")
                        self.frequencyEvaluationValue.place(anchor="center", relx=0.5, rely=0.3)
                    elif int(count) > 1000:
                        self.frequencyEvaluationValue.configure(text="Häufig", text_color="#F7722E", fg_color="#312919")
                        self.frequencyEvaluationValue.place(anchor="center", relx=0.45, rely=0.3)
                    elif int(count) >= 1:
                        self.frequencyEvaluationValue.configure(text="Gelegentlich", text_color="#FBBC04", fg_color="#292620")
                        self.frequencyEvaluationValue.place(anchor="center", relx=0.5, rely=0.3)
                    return
            
            self.frequencyEvaluationValue.configure(text="Nicht gefunden", text_color="#22D341", fg_color="#142A1F")
            self.frequencyEvaluationValue.place(anchor="center", relx=0.52, rely=0.3)

    def changeValueCrackTime(self):
        result = zxcvbn(self.enterPassword.get())

        text = result["crack_times_display"]["offline_fast_hashing_1e10_per_second"]
        if len(text) > 15:
            self.timeToCrackEvaluationValue.place(anchor="center", relx=0.7, rely=0.5)
            self.timeToCrackEvaluationValue.configure(text=text, text_color="#19B8EC")
            return
            
        self.timeToCrackEvaluationValue.configure(text=text, text_color="#19B8EC")
        self.timeToCrackEvaluationValue.place(anchor="center", relx=0.62, rely=0.5)

    def deleteHistory(self):
        self.historyList = []
        self.saveHistory()
        self.updateHistoryUI()

    def loadHistory(self):
        if not os.path.exists(HISTORY_FILE):
            return []

        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except:
            return []

    def saveHistory(self):
        with open(HISTORY_FILE, "w") as f:
            json.dump(self.historyList, f)

    def updateHistoryUI(self):
        buttons = [
            self.historyPassword1,
            self.historyPassword2,
            self.historyPassword3,
            self.historyPassword4,
            self.historyPassword5
        ]

        for i, btn in enumerate(buttons):
            if i < len(self.historyList):
                pw = self.historyList[i]

                if len(pw) >= 33:
                    btn.configure(text=pw[:32] + "...")
                else:
                    btn.configure(text=pw,)
            else:
                btn.configure(text="")