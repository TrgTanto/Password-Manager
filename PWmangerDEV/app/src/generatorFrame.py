import customtkinter as ctk
import clipboard, string, secrets, random, json, os

from PIL import Image
genPassword = ''
lenText = 12
lenPuncs = 2

HISTORY_FILE = "password_history.json"

unkownIcon =  'app/icons/png/unkownIcon.png'
checkIcon = 'app/icons/png/checkIcon.png'
noCheckIcon = 'app/icons/png/noCheckIcon.png'


class generatorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
            fg_color="#030D17",#030D17
            width=1058, 
            height=800,
            corner_radius=0,
            border_width=1,
            border_color="#212830"
        )

        self.title = ctk.CTkLabel(master=self,
            text="Passwort Generator",
            font=("Roboto Medium", 22),
            text_color="#DDDDE0"
        )
        self.title.place(anchor="center", relx=0.115, rely=0.035)

        self.infoText = ctk.CTkLabel(master=self,
            text="Erstelle sichere Passwörter mit anpassbaren Optionen nach deinen Bedürfnissen.",
            font=("Roboto", 13.5),
            text_color="#717A87"
        )
        self.infoText.place(anchor="center", relx=0.2605, rely=0.065)

        # generate Password
        self.generateFrame = ctk.CTkFrame(master=self,
            width=500,
            height=625,
            fg_color="#09131E",
            border_width=1,
            border_color="#29323D",
            corner_radius=8,
        )
        self.generateFrame.place(anchor="center", relx=0.26, rely=0.5)

        self.generateTitle = ctk.CTkLabel(master=self.generateFrame,
            text="Generiertes Passwort",
            text_color="#9FAAB9",
            font=("Roboto", 15)
        )
        self.generateTitle.place(anchor="center", relx=0.185, rely=0.05)

        self.generatedPassword = ctk.CTkButton(master=self.generateFrame,
            text="Du hast noch kein Passwort generiert.",
            width=460,
            height=55,
            border_width=1,
            border_color="#29323D",
            corner_radius=8,
            fg_color="#040F1A",
            text_color="#DEDBDA",
            anchor="center",
            font=("Roboto Medium", 14),
            hover="disabled",
            command=lambda: clipboard.copy(self.generatedPassword.cget("text").replace("\n", "")),
        )
        self.generatedPassword.place(anchor="center", relx=0.5, rely=0.12)

        self.passwordLengthText = ctk.CTkLabel(master=self.generateFrame,
            text="Passwortlänge:",
            font=("Roboto", 14.5),
            text_color="#DEDBDA"
        )
        self.passwordLengthText.place(anchor="center", relx=0.14, rely=0.25)

        self.passwordLength = ctk.CTkLabel(master=self.generateFrame,
            text=lenText,
            font=("Roboto", 14.5),
            text_color="#DEDBDA"
        )
        if lenText < 10:
            self.passwordLength.place(anchor="center", relx=0.255, rely=0.25)
        else:
            self.passwordLength.place(anchor="center", relx=0.267, rely=0.25)

        self.LengthSlider = ctk.CTkSlider(master=self.generateFrame,
            from_=4,
            to=64,
            width=415,
            height=18,
            fg_color="#1F2832",
            progress_color="#044EF3",
            button_color="#4889FF",
            hover="disabled",
            command=self.changeLenText
        )
        self.LengthSlider.place(anchor="center", relx=0.445, rely=0.3)

        self.vcmd = (self.register(self.checkEntry), "%P")
        self.SliderEntry = ctk.CTkEntry(master=self.generateFrame,
            placeholder_text=0,
            fg_color="#040F1A",
            validate="key",
            validatecommand=self.vcmd,
            border_color="#29323D",
            border_width=1,
            width=50,
            height=40,
            justify="center",
            font=("Roboto", 13.5)
        )
        self.SliderEntry.place(anchor="center", relx=0.915, rely=0.3)

        self.minText = ctk.CTkLabel(master=self.generateFrame,
            text="4",
            font=("Roboto", 14),
            text_color="#717A87"
        )
        self.minText.place(anchor="center", relx=0.048, rely=0.34)

        self.maxText = ctk.CTkLabel(master=self.generateFrame,
            text="64",
            font=("Roboto", 14),
            text_color="#717A87"
        )
        self.maxText.place(anchor="center", relx=0.84, rely=0.34)

        self.checkBoxesText = ctk.CTkLabel(master=self.generateFrame,
            text="Zeichenarten",
            font=("Roboto", 15),
            text_color="#DEDBDA"
        )
        self.checkBoxesText.place(anchor="center", relx=0.13, rely=0.4)

        self.lettersUp = ctk.CTkCheckBox(master=self.generateFrame,
            text="Großbuchstaben (A-Z)",
            text_color="#717A87",
            hover="disabled",
            fg_color="#065AF9",
            checkmark_color="#D3EAFD",
            font=("Roboto", 13),
            corner_radius=6,
            border_width=1,
            border_color="#29323D"
        )
        self.lettersUp.place(anchor="center", relx=0.20, rely=0.45)

        self.lettersDown = ctk.CTkCheckBox(master=self.generateFrame,
            text="Kleinbuchstaben (a-z)",
            text_color="#717A87",
            hover="disabled",
            fg_color="#065AF9",
            checkmark_color="#D3EAFD",
            font=("Roboto", 13),
            corner_radius=6,
            border_width=1,
            border_color="#29323D"
        )
        self.lettersDown.place(anchor="center", relx=0.198, rely=0.5)

        self.digitsBox = ctk.CTkCheckBox(master=self.generateFrame,
            text="Zahlen (0-9)",
            text_color="#717A87",
            hover="disabled",
            fg_color="#065AF9",
            checkmark_color="#D3EAFD",
            font=("Roboto", 13),
            corner_radius=6,
            border_width=1,
            border_color="#29323D"
        )
        self.digitsBox.place(anchor="center", relx=0.144, rely=0.55)

        self.puncsBox = ctk.CTkCheckBox(master=self.generateFrame,
            text="Sonderzeichen (!@#$%^&*)",
            text_color="#717A87",
            hover="disabled",
            fg_color="#065AF9",
            checkmark_color="#D3EAFD",
            font=("Roboto", 13),
            corner_radius=6,
            border_width=1,
            border_color="#29323D"
        )
        self.puncsBox.place(anchor="center", relx=0.228, rely=0.6)

        # all checkBoxes automatically true
        self.lettersUp.select()
        self.lettersDown.select()
        self.digitsBox.select()
        self.puncsBox.select()

        self.passwordLengthTextPuncs = ctk.CTkLabel(master=self.generateFrame,
            text="Anzahl Sonderzeichen (wird addiert):",
            font=("Roboto", 14.5),
            text_color="#DEDBDA"
        )
        self.passwordLengthTextPuncs.place(anchor="center", relx=0.265, rely=0.68)

        self.passwordLengthPuncs = ctk.CTkLabel(master=self.generateFrame,
            text=lenPuncs,
            font=("Roboto", 14.5),
            text_color="#DEDBDA"
        )

        self.passwordLengthPuncs.place(anchor="center", relx=0.52, rely=0.68)

        self.LengthSliderPuncs = ctk.CTkSlider(master=self.generateFrame,
            from_=1,
            to=10,
            width=415,
            height=18,
            fg_color="#1F2832",
            progress_color="#044EF3",
            button_color="#4889FF",
            hover="disabled",
            command=self.changeLenTextPuncs
        )
        self.LengthSliderPuncs.place(anchor="center", relx=0.445, rely=0.73)

        self.vcmdPuncs = (self.register(self.checkEntryPuncs), "%P")
        self.SliderEntryPuncs = ctk.CTkEntry(master=self.generateFrame,
            placeholder_text=0,
            fg_color="#040F1A",
            validate="key",
            validatecommand=self.vcmdPuncs,
            border_color="#29323D",
            border_width=1,
            width=50,
            height=40,
            justify="center",
            font=("Roboto", 13.5)
        )
        self.SliderEntryPuncs.place(anchor="center", relx=0.915, rely=0.73)

        self.minTextPuncs = ctk.CTkLabel(master=self.generateFrame,
            text="1",
            font=("Roboto", 14),
            text_color="#717A87"
        )
        self.minTextPuncs.place(anchor="center", relx=0.048, rely=0.77)

        self.maxTextPuncs = ctk.CTkLabel(master=self.generateFrame,
            text="10",
            font=("Roboto", 14),
            text_color="#717A87"
        )
        self.maxTextPuncs.place(anchor="center", relx=0.84, rely=0.77)

        self.generateButton = ctk.CTkButton(master=self.generateFrame,
            text="Neues Passwort generieren",
            text_color="#B6C6ED",
            fg_color="#0639BF",
            border_width=1,
            border_color="#09276C",
            width=460,
            height=45,
            hover_color="#112758",
            font=("Roboto Medium", 14),
            image=ctk.CTkImage(dark_image=Image.open('app/icons/png/overviewGeneratorGenerate.png'), size=(20, 20)),
            command=lambda:self.generatePassword()
        )
        self.generateButton.place(anchor="center", relx=0.5, rely=0.9)

        # analysis 
        self.analysisFrame = ctk.CTkFrame(master=self,
            width=500,
            height=625,
            fg_color="#09131E",
            border_width=1,
            border_color="#29323D",
            corner_radius=8,
        )
        self.analysisFrame.place(anchor="center", relx=0.74, rely=0.5)

        self.strengthText = ctk.CTkLabel(master=self.analysisFrame,
            text="Stärke",
            text_color="#DEDBDA",
            font=("Roboto", 15)
        )
        self.strengthText.place(anchor="center", relx=0.08, rely=0.07)

        self.strengthTextChange = ctk.CTkLabel(master=self.analysisFrame,
            text="Unbekannt",
            font=("Roboto", 15),
            text_color="#717A87"
        )
        self.strengthTextChange.place(anchor="center", relx=0.872, rely=0.07)

        # #4A4D50 == transparent \ kW transparent not available in ctk
        self.veryWeakBar = ctk.CTkProgressBar(master=self.analysisFrame,
            width=64,
            height=10,
            progress_color="#4A4D50"
        )
        self.veryWeakBar.place(anchor="center", relx=0.1, rely=0.1)

        self.weakBar = ctk.CTkProgressBar(master=self.analysisFrame,
            width=64,
            height=10,
            progress_color="#4A4D50"
        )
        self.weakBar.place(anchor="center", relx=0.23, rely=0.1)

        self.ratherWeak = ctk.CTkProgressBar(master=self.analysisFrame,
            width=64,
            height=10,
            progress_color="#4A4D50"
        )
        self.ratherWeak.place(anchor="center", relx=0.36, rely=0.1)

        self.mid = ctk.CTkProgressBar(master=self.analysisFrame,
            width=64,
            height=10,
            progress_color="#4A4D50"
        )
        self.mid.place(anchor="center", relx=0.49, rely=0.1)

        self.rahterStrong = ctk.CTkProgressBar(master=self.analysisFrame,
            width=64,
            height=10,
            progress_color="#4A4D50"
        )
        self.rahterStrong.place(anchor="center", relx=0.62, rely=0.1)

        self.strong = ctk.CTkProgressBar(master=self.analysisFrame,
            width=64,
            height=10,
            progress_color="#4A4D50"
        )
        self.strong.place(anchor="center", relx=0.75, rely=0.1)

        self.veryStrong = ctk.CTkProgressBar(master=self.analysisFrame,
            width=64,
            height=10,
            progress_color="#4A4D50"
        )
        self.veryStrong.place(anchor="center", relx=0.88, rely=0.1)

        # all bars to max
        self.veryWeakBar.set(1)
        self.weakBar.set(1)
        self.ratherWeak.set(1)
        self.mid.set(1)
        self.rahterStrong.set(1)
        self.strong.set(1)
        self.veryStrong.set(1)

        # Analyse Text
        self.analysisText = ctk.CTkLabel(master=self.analysisFrame,
            text="Analyse",
            text_color="#DEDBDA",
            font=("Roboto", 15)
        )
        self.analysisText.place(anchor="center", relx=0.09, rely=0.23)

        self.analysisLengthText = ctk.CTkButton(master=self.analysisFrame,
            text="Länge                                                                                                    16 Zeichen",
            width=460,
            height=30,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 14),
            hover="disabled",
            text_color="#737983",
            corner_radius=0,
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25))
        )
        self.analysisLengthText.place(anchor="center", relx=0.5, rely=0.28)

        self.analysisUpLetterText = ctk.CTkButton(master=self.analysisFrame,
            text="Großbuchstaben                                                                              Vorhanden",
            width=460,
            height=30,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 14),
            hover="disabled",
            text_color="#737983",
            corner_radius=0,
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25))
        )
        self.analysisUpLetterText.place(anchor="center", relx=0.5, rely=0.33)

        self.analysisLowLetterText = ctk.CTkButton(master=self.analysisFrame,
            text="Kleinbuchstaben                                                                              Vorhanden",
            width=460,
            height=30,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 14),
            hover="disabled",
            text_color="#737983",
            corner_radius=0,
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25))
        )
        self.analysisLowLetterText.place(anchor="center", relx=0.5, rely=0.378)

        self.analysisNumberText = ctk.CTkButton(master=self.analysisFrame,
            text="Zahlen                                                                                                   Vorhanden",
            width=460,
            height=30,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 14),
            hover="disabled",
            text_color="#737983",
            corner_radius=0,
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25))
        )
        self.analysisNumberText.place(anchor="center", relx=0.5, rely=0.426)

        self.analysisPuncsText = ctk.CTkButton(master=self.analysisFrame,
            text="Sonderzeichen                                                                                  Vorhanden",
            width=460,
            height=30,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 14),
            hover="disabled",
            text_color="#737983",
            corner_radius=0,
            image=ctk.CTkImage(dark_image=Image.open(unkownIcon), size=(25, 25))
        )
        self.analysisPuncsText.place(anchor="center", relx=0.5, rely=0.474)

        self.historyText = ctk.CTkLabel(master=self.analysisFrame,
            text="Verlauf",
            text_color="#DEDBDA",
            font=("Roboto", 15)
        )
        self.historyText.place(anchor="center", relx=0.09, rely=0.565)

        self.analysisHistoryPassword1 = ctk.CTkButton(master=self.analysisFrame,
            text="",
            width=460,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 15),
            hover="disabled",
            command=lambda:clipboard.copy(self.historyList[0] if len(self.historyList) > 0 else ""),
            text_color="#DEDBDA",
            corner_radius=0
        )
        self.analysisHistoryPassword1.place(anchor="center", relx=0.5, rely=0.63)

        self.analysisHistoryPassword2 = ctk.CTkButton(master=self.analysisFrame,
            text="",
            width=460,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 15),
            hover="disabled",
            command=lambda:clipboard.copy(self.historyList[1] if len(self.historyList) > 1 else ""),
            text_color="#DEDBDA",
            corner_radius=0
        )
        self.analysisHistoryPassword2.place(anchor="center", relx=0.5, rely=0.69)

        self.analysisHistoryPassword3 = ctk.CTkButton(master=self.analysisFrame,
            text="",
            width=460,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 15),
            hover="disabled",
            command=lambda:clipboard.copy(self.historyList[2] if len(self.historyList) > 2 else ""),
            text_color="#DEDBDA",
            corner_radius=0
        )
        self.analysisHistoryPassword3.place(anchor="center", relx=0.5, rely=0.75)

        self.analysisHistoryPassword4 = ctk.CTkButton(master=self.analysisFrame,
            text="",
            width=460,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 15),
            hover="disabled",
            command=lambda:clipboard.copy(self.historyList[3] if len(self.historyList) > 3 else ""),
            text_color="#DEDBDA",
            corner_radius=0
        )
        self.analysisHistoryPassword4.place(anchor="center", relx=0.5, rely=0.81)

        self.analysisHistoryPassword5 = ctk.CTkButton(master=self.analysisFrame,
            text="",
            width=460,
            height=40,
            fg_color="transparent",
            border_width=1,
            border_color="#29323D",
            font=("Roboto", 15),
            hover="disabled",
            command=lambda:clipboard.copy(self.historyList[4] if len(self.historyList) > 4 else ""),
            text_color="#DEDBDA",
            corner_radius=0
        )
        self.analysisHistoryPassword5.place(anchor="center", relx=0.5, rely=0.87)

        self.analysisDeleteHistory = ctk.CTkButton(master=self.analysisFrame,
            text="Verlauf löschen",
            text_color="#B6C6ED",
            fg_color="#0639BF",
            border_width=1,
            border_color="#09276C",
            width=460,
            height=35,
            hover_color="#112758",
            font=("Roboto Medium", 14),
            image=ctk.CTkImage(dark_image=Image.open('app/icons/png/calculatorTrashCan.png'), size=(20, 20)),
            command=lambda:self.clearHistory()
        )
        self.analysisDeleteHistory.place(anchor="center", relx=0.5, rely=0.95)

        # Pro Tip
        self.proTipText = ctk.CTkButton(master=self,
            text="Verwende Passphrasen für noch mehr Sicherheit! Kombiniere mehrere Wörter, um ein langes und leicht zu merkendes Passwort zu erstellen.",
            width=1010,
            height=60,
            text_color="#8EA5A5",
            fg_color="#08131F",
            border_color="#29323D",
            hover="disabled",
            border_width=1,
            font=("Segoe UI", 12),
            image=ctk.CTkImage(dark_image=Image.open('app/icons/png/proTipIcon.png'), size=(35, 35)),
        )
        self.proTipText.place(anchor="center", relx=0.5, rely=0.95)

        self.historyList = self.loadHistory()
        if not isinstance(self.historyList, list):
            self.historyList = []
        self.updateHistoryUI()

    def changeLenText(self, value):
        global lenText
        newText = int(value)
        lenText = newText
        self.passwordLength.configure(text=lenText)

    def changeLenTextPuncs(self, value):
        global lenPuncs
        newText = int(value)
        lenPuncs = newText
        self.passwordLengthPuncs.configure(text=lenPuncs)

    def checkEntry(self, n):
        global lenText

        # deleting space
        if n == "":
            return True
        
        # only numbers allowed
        if not n.isdigit():
            return False
        
        # only 2 digits allowed
        if len(n) > 2:
            return False

        # max value 64
        if int(n) > 64:
            return False

        if int(n) <= 0:
            self.LengthSlider.set(12)
            self.passwordLength.configure(text="12")
        elif int(n) < 4:
            lenText = int(4)
            self.LengthSlider.set(4)
            self.passwordLength.configure(text="4") 
        else:
            lenText = int(n)
            self.LengthSlider.set(int(n))
            self.passwordLength.configure(text=f"{int(n)}")

        return True

    def checkEntryPuncs(self, n):
        global lenPuncs

        # deleting space
        if n == "":
            return True
        
        # only numbers allowed
        if not n.isdigit():
            return False
        
        # only 2 digits allowed
        if len(n) > 2:
            return False

        # max value 10
        if int(n) > 10:
            return False

        if int(n) == 0:
            self.LengthSliderPuncs.set(1)
            self.passwordLengthPuncs.configure(text="1")
        else:
            lenPuncs = int(n)
            self.LengthSliderPuncs.set(int(n))
            self.passwordLengthPuncs.configure(text=lenPuncs)

        return True
    
    def resetStrengthBars(self):
        self.veryWeakBar.configure(progress_color="#4A4D50")
        self.weakBar.configure(progress_color="#4A4D50")
        self.ratherWeak.configure(progress_color="#4A4D50")
        self.mid.configure(progress_color="#4A4D50")
        self.rahterStrong.configure(progress_color="#4A4D50")
        self.strong.configure(progress_color="#4A4D50")
        self.veryStrong.configure(progress_color="#4A4D50")

    def generatePassword(self):
        global genPassword, lenText, lenPuncs
        self.resetStrengthBars()

        bigLetters = self.lettersUp.get()
        smallLetters = self.lettersDown.get()
        digits = self.digitsBox.get()
        puncs = self.puncsBox.get()
        allChars = ''
        amountPuncs = int(self.LengthSliderPuncs.get())
        optionsEnabled = sum([bigLetters, smallLetters, digits, puncs])
        mustChars = ''

        if bigLetters:
            allChars += string.ascii_uppercase
            mustChars += secrets.choice(string.ascii_uppercase)

        if smallLetters:
            allChars += string.ascii_lowercase
            mustChars += secrets.choice(string.ascii_lowercase)

        if digits:
            allChars += string.digits
            mustChars += secrets.choice(string.digits)

        if puncs:
            allChars += string.punctuation
            mustChars += secrets.choice(string.punctuation)

        if len(allChars) == 0:
            self.generatedPassword.configure(text="Du musst mindestens eine Zeichenart auswählen.")
            self.strengthTextChange.configure(text="Unbekannt", text_color="#717A87")
            self.strengthTextChange.place(anchor="center", relx=0.872, rely=0.07)
            return

        pw = ''
        lenPw = int(self.LengthSlider.get()) - len(mustChars)

        for n in range(lenPw):
            pw += secrets.choice(allChars)
        if puncs:
            for n in range(amountPuncs):
                pw += secrets.choice(string.punctuation)
        
        pw = list(pw + mustChars)
        random.shuffle(pw)
        pw = ''.join(pw)
        genPassword = pw

        self.historyList.insert(0, pw)

        if len(self.historyList) > 5:
            self.historyList.pop()

        self.saveHistory(self.historyList)
        self.updateHistoryUI()
        lenPw = len(genPassword)
        if lenPw >= 33:
            cleanPasswordText = genPassword[:32] + '\n' + genPassword[32:]
        else:
            cleanPasswordText = genPassword
        self.generatedPassword.configure(text=cleanPasswordText, font=("Roboto Medium", 16))

        '''
        Rules for StrengthBar:
        veryWeak = Length min 1
        weak = Length min 5
        ratherWeak = Length min 8
        mid = Length min 8 and need small/big/punc and Number in password
        ratherStrong = length min 10
        strong = length min 12
        veryStrong = length min 16
        '''
        points = 0

        if lenPw >= 1:
            points += 1
            self.veryWeakBar.configure(progress_color="#F22E3B")
        
        if lenPw >= 5 and points == 1:
            points += 1
            self.weakBar.configure(progress_color="#F97D18")

        if lenPw >= 8 and points == 2:
            points += 1
            self.ratherWeak.configure(progress_color="#DE990D")
        
        if optionsEnabled >= 4 and points == 3:
            points += 1
            self.mid.configure(progress_color="#FDCC01")   
        
        if lenPw >= 10 and points == 4:
            points += 1
            self.rahterStrong.configure(progress_color="#6ADD1E")
        
        if lenPw >= 12 and points == 5:
            points += 1
            self.strong.configure(progress_color="#37CB2D")

        if lenPw >= 16 and points == 6:
            points += 1
            self.veryStrong.configure(progress_color="#19DB41")
        
        if points == 1:
            strengthText = "Sehr schwach"
            self.strengthTextChange.configure(text=strengthText, text_color="#FF0000")
            self.strengthTextChange.place(anchor="center", relx=0.848, rely=0.07)
        elif points == 2:
            strengthText = "Schwach"
            self.strengthTextChange.configure(text=strengthText, text_color="#F97D18")
            self.strengthTextChange.place(anchor="center", relx=0.879, rely=0.07)
        elif points == 3:
            strengthText = "eher schwach"
            self.strengthTextChange.configure(text=strengthText, text_color="#DE990D")
            self.strengthTextChange.place(anchor="center", relx=0.85, rely=0.07)
        elif points == 4:
            strengthText = "Mittel"
            self.strengthTextChange.configure(text=strengthText, text_color="#FDCC01")
            self.strengthTextChange.place(anchor="center", relx=0.9, rely=0.07)
        elif points == 5:
            strengthText = "eher stark"
            self.strengthTextChange.configure(text=strengthText, text_color="#6ADD1E")
            self.strengthTextChange.place(anchor="center", relx=0.875, rely=0.07)
        elif points == 6:
            strengthText = "Stark"
            self.strengthTextChange.configure(text=strengthText, text_color="#37CB2D")
            self.strengthTextChange.place(anchor="center", relx=0.905, rely=0.07)
        elif points == 7:
            strengthText = "Sehr Stark"
            self.strengthTextChange.configure(text=strengthText, text_color="#19DB41")
            self.strengthTextChange.place(anchor="center", relx=0.872, rely=0.07)
        
        if lenPw >= 16:
            self.analysisLengthText.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
        else:
            self.analysisLengthText.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
        
        if any(c in pw for c in string.ascii_uppercase):
            self.analysisUpLetterText.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
        else:
            self.analysisUpLetterText.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
        
        if any(c in pw for c in string.ascii_lowercase):
            self.analysisLowLetterText.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
        else:
            self.analysisLowLetterText.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
        
        if any(c in pw for c in string.digits):
            self.analysisNumberText.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
        else:
            self.analysisNumberText.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
        
        if any(c in pw for c in string.punctuation):
            self.analysisPuncsText.configure(image=ctk.CTkImage(dark_image=Image.open(checkIcon), size=(25, 25)))
        else:
            self.analysisPuncsText.configure(image=ctk.CTkImage(dark_image=Image.open(noCheckIcon), size=(25, 25)))
    

    def clearHistory(self):
        self.historyList = []
        self.saveHistory(self.historyList)
        self.updateHistoryUI()

    def loadHistory(self):
        if not os.path.exists(HISTORY_FILE):
            return []

        try:
            with open(HISTORY_FILE, "r") as f:
                return json.load(f)
        except:
            return []

    def saveHistory(self, history):
        with open(HISTORY_FILE, "w") as f:
            json.dump(history, f)

    def updateHistoryUI(self):
        buttons = [
            self.analysisHistoryPassword1,
            self.analysisHistoryPassword2,
            self.analysisHistoryPassword3,
            self.analysisHistoryPassword4,
            self.analysisHistoryPassword5
        ]

        for i, btn in enumerate(buttons):
            if i < len(self.historyList):
                pw = self.historyList[i]
                if len(pw) >= 32:
                    pw = pw[:32] + '\n' + pw[32:]
                btn.configure(text=pw)
            else:
                btn.configure(text="")