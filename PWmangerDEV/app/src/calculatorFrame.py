import customtkinter as ctk
import hashlib, clipboard

from PIL import Image

hashValue = ''
currentAlgorithm = ''

class calculatorFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
            fg_color="#030D17",
            width=1058, 
            height=800,
            corner_radius=0,
            border_width=1,
            border_color="#212830"
        )

        # title + hashtext
        self.title = ctk.CTkLabel(master=self,
            text="Hash-Rechner",
            font=("Segoe UI", 22, "bold"),
            text_color="#EDECE5"
        )
        self.title.place(anchor="center", relx=0.085, rely=0.04)

        self.hashText = ctk.CTkLabel(master=self,
            text="Berechne Hash-Werte für beliebige Eingaben mit verschiedenen Algorithmen.",
            font=("Segoe UI", 14),
            text_color="#677073"
        )
        self.hashText.place(anchor="center", relx=0.24, rely=0.07)

        # entryFrame
        self.entryFrame = ctk.CTkFrame(master=self,
            width=1020,
            height=200,
            border_width=2,
            border_color="#131B23",
            fg_color="#0C161E",
            corner_radius=8
        )
        self.entryFrame.place(anchor="center", relx=0.5, rely=0.22)

        self.entryTitle = ctk.CTkLabel(master=self.entryFrame,
            text="Eingabe",
            text_color="#EDECE5",
            font=("Roboto Medium", 15)
        )
        self.entryTitle.place(anchor="center", relx=0.05, rely=0.12)

        self.entryField = ctk.CTkTextbox(master=self.entryFrame,
            width=970,
            height=130,
            fg_color="#09131E",
            border_width=1,
            border_color="#29323D",
            corner_radius=8,
            scrollbar_button_color="#29323D",
            scrollbar_button_hover_color="#29323D",
            font=("Roboto", 14),
            text_color="#8EA5A5"
        )
        self.entryField.place(anchor="center", relx=0.5, rely=0.6)
        self.entryField.insert("1.0", "Text oder Passwort eingeben...")

        self.entryFieldClear = ctk.CTkButton(master=self.entryFrame,
            text="Eingabe löschen",
            image=ctk.CTkImage(dark_image=Image.open('app/icons/png/calculatorTrashCan.png'), size=(20, 20)),
            corner_radius=8,
            fg_color="#0639BF",
            text_color="#B6C6ED",
            border_width=1,
            border_color="#09276C",
            hover_color="#112758",
            font=("Roboto Medium", 14),
            width=100,
            height=35,
            command=lambda:self.clearEntry()
        )
        self.entryFieldClear.place(anchor="center", relx=0.9, rely=0.12)

        # algorithmFrame
        self.algorithmFrame = ctk.CTkFrame(master=self,
            width=1020,
            height=180,
            border_width=2,
            border_color="#131B23",
            fg_color="#0C161E",
            corner_radius=8
        )
        self.algorithmFrame.place(anchor="center", relx=0.5, rely=0.465)

        self.algorithmTitle = ctk.CTkLabel(master=self.algorithmFrame,
            text="Algorithmus",
            text_color="#EDECE5",
            font=("Roboto Medium", 15)
        )
        self.algorithmTitle.place(anchor="center", relx=0.06, rely=0.12)

        self.MD5button = ctk.CTkButton(master=self.algorithmFrame,
            text="MD5",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("MD5")
        )
        self.MD5button.place(anchor="center", relx=0.11, rely=0.4)

        self.SHA1button = ctk.CTkButton(master=self.algorithmFrame,
            text="SHA-1",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("SHA-1")
        )
        self.SHA1button.place(anchor="center", relx=0.305, rely=0.4)

        self.SHA224button = ctk.CTkButton(master=self.algorithmFrame,
            text="SHA-224",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("SHA-224")
        )
        self.SHA224button.place(anchor="center", relx=0.5, rely=0.4)

        self.SHA256button = ctk.CTkButton(master=self.algorithmFrame,
            text="SHA-256",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("SHA-256")
        )
        self.SHA256button.place(anchor="center", relx=0.695, rely=0.4)

        self.SHA384button = ctk.CTkButton(master=self.algorithmFrame,
            text="SHA-384",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("SHA-384")
        )
        self.SHA384button.place(anchor="center", relx=0.89, rely=0.4)

        self.SHA512button = ctk.CTkButton(master=self.algorithmFrame,
            text="SHA-512",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("SHA-512")
        )
        self.SHA512button.place(anchor="center", relx=0.11, rely=0.7)

        self.SHA3_224button = ctk.CTkButton(master=self.algorithmFrame,
            text="SHA3-224",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("SHA3-224")
        )
        self.SHA3_224button.place(anchor="center", relx=0.305, rely=0.7)

        self.SHA3_256button = ctk.CTkButton(master=self.algorithmFrame,
            text="SHA3-256",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("SHA3-256")
        )
        self.SHA3_256button.place(anchor="center", relx=0.5, rely=0.7)

        self.SHA3_384button = ctk.CTkButton(master=self.algorithmFrame,
            text="SHA3-384",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("SHA3-384")
        )
        self.SHA3_384button.place(anchor="center", relx=0.695, rely=0.7)

        self.SHA3_512button = ctk.CTkButton(master=self.algorithmFrame,
            text="SHA3-512",
            width=195,
            height=40,
            fg_color="#08121C",
            border_width=1,
            border_color="#16202B",
            hover_color="#07329B",
            font=("Roboto Medium", 17.5),
            command=lambda:self.changeButtonColor("SHA3-512")
        )
        self.SHA3_512button.place(anchor="center", relx=0.89, rely=0.7)

        # resultFrame
        self.resultFrame= ctk.CTkFrame(master=self,
            width=1020,
            height=160,
            border_width=2,
            border_color="#131B23",
            fg_color="#0C161E",
            corner_radius=8
        )
        self.resultFrame.place(anchor="center", relx=0.5, rely=0.685)

        self.resultTitle = ctk.CTkLabel(master=self.resultFrame,
            text="Ergebnis",
            text_color="#EDECE5",
            font=("Roboto Medium", 15)
        )
        self.resultTitle.place(anchor="center", relx=0.055, rely=0.13)

        self.resultHash = ctk.CTkTextbox(master=self.resultFrame,
            width=970,
            height=100,
            fg_color="#09131E",
            border_width=1,
            border_color="#29323D",
            corner_radius=8,
            scrollbar_button_color="#29323D",
            scrollbar_button_hover_color="#29323D",
            font=("Roboto", 14),
            text_color="#8EA5A5"
        )
        self.resultHash.place(anchor="center", relx=0.5, rely=0.6)
        self.resultHash.insert("1.0", "Hash-Wert wird hier angezeigt...")

        self.copyHash = ctk.CTkButton(master=self.resultFrame,
            text="Kopieren",
            image=ctk.CTkImage(dark_image=Image.open("app/icons/png/calculatorCopy.png"), size=(25, 25)),
            corner_radius=8,
            fg_color="#0639BF",
            text_color="#B6C6ED",
            border_width=1,
            border_color="#09276C",
            hover_color="#112758",
            font=("Roboto Medium", 14),
            width=100,
            height=20,
            command=lambda:clipboard.copy(hashValue)
        )
        self.copyHash.place(anchor="center", relx=0.92, rely=0.13)

        # mainFrame
        self.calculateHash =  ctk.CTkButton(master=self,
            text="Hash berechnen",
            width=195,
            height=40,
            fg_color="#07329B",
            border_width=1,
            border_color="#328EFB",
            hover_color="#1C3679",
            font=("Roboto Medium", 17.5),
            image=ctk.CTkImage(dark_image=Image.open('app/icons/png/flashSymbol.png'), size=(20, 20)),
            command=lambda:self.convertHash()
        )
        self.calculateHash.place(anchor="center", relx=0.112, rely=0.85)

        self.deleteEveryEntrys =  ctk.CTkButton(master=self,
            text="Alle Eingaben löschen",
            width=195,
            height=40,
            fg_color="#07329B",
            border_width=1,
            border_color="#328EFB",
            hover_color="#1C3679",
            font=("Roboto Medium", 17.5),
            image=ctk.CTkImage(dark_image=Image.open('app/icons/png/calculatorTrashCan.png'), size=(20, 20)),
            command=lambda:self.deleteEntrys()
        )
        self.deleteEveryEntrys.place(anchor="center", relx=0.88, rely=0.85)
        
        # tipButton
        self.tipFrame = ctk.CTkButton(master=self,
            fg_color="#0C161E",
            text="Hash-Funktionen sind Einwegfunktionen. Der ursprüngliche Text kann nicht aus dem Hash-Wert zurückgerechnet werden.",
            text_color="#8EA5A5",
            width=1025,
            height=60,
            corner_radius=8,
            border_width=2,
            border_color="#131B23",
            hover="disabled",
            image=ctk.CTkImage(dark_image=Image.open('app/icons/png/proTipIcon.png'), size=(35, 35)),
            font=("Segoe UI", 12),
        )
        self.tipFrame.place(anchor="center", relx=0.5032, rely=0.94)

    def clearEntry(self):
        self.entryField.delete(0.0, 'end')

    def resetButtonColors(self):
        self.MD5button.configure(fg_color="#08121C", border_color="#16202B")
        self.SHA1button.configure(fg_color="#08121C", border_color="#16202B")
        self.SHA224button.configure(fg_color="#08121C", border_color="#16202B")
        self.SHA256button.configure(fg_color="#08121C", border_color="#16202B")
        self.SHA384button.configure(fg_color="#08121C", border_color="#16202B")
        self.SHA512button.configure(fg_color="#08121C", border_color="#16202B")
        self.SHA3_224button.configure(fg_color="#08121C", border_color="#16202B")
        self.SHA3_256button.configure(fg_color="#08121C", border_color="#16202B")
        self.SHA3_384button.configure(fg_color="#08121C", border_color="#16202B")
        self.SHA3_512button.configure(fg_color="#08121C", border_color="#16202B")

    def changeButtonColor(self, button):
        global currentAlgorithm
        self.resetButtonColors()
        if button == "MD5":
            self.MD5button.configure(fg_color="#07329B", border_color="#328EFB")
        
        elif button == "SHA-1":
            self.SHA1button.configure(fg_color="#07329B", border_color="#328EFB")

        elif button == "SHA-224":
            self.SHA224button.configure(fg_color="#07329B", border_color="#328EFB")

        elif button == "SHA-256":
            self.SHA256button.configure(fg_color="#07329B", border_color="#328EFB")

        elif button == "SHA-384":
            self.SHA384button.configure(fg_color="#07329B", border_color="#328EFB")

        elif button == "SHA-512":
            self.SHA512button.configure(fg_color="#07329B", border_color="#328EFB")

        elif button == "SHA3-224":
            self.SHA3_224button.configure(fg_color="#07329B", border_color="#328EFB")

        elif button == "SHA3-256":
            self.SHA3_256button.configure(fg_color="#07329B", border_color="#328EFB")

        elif button == "SHA3-384":
            self.SHA3_384button.configure(fg_color="#07329B", border_color="#328EFB")

        elif button == "SHA3-512":
            self.SHA3_512button.configure(fg_color="#07329B", border_color="#328EFB")
        
        currentAlgorithm = str(button)

    def convertHash(self):
        global hashValue, currentAlgorithm
        textBox = self.entryField.get(0.0, 'end-1c').encode('utf-8')

        if len(currentAlgorithm) == 0:
            self.resultHash.delete(0.0, 'end')
            self.resultHash.insert("1.0", "Du hast kein Algorithmus ausgewählt...")
            return
        
        if currentAlgorithm == "MD5":
            hashValue = hashlib.md5(textBox).hexdigest()
        
        elif currentAlgorithm == "SHA-1":
            hashValue = hashlib.sha1(textBox).hexdigest()

        elif currentAlgorithm == "SHA-224":
            hashValue = hashlib.sha224(textBox).hexdigest()

        elif currentAlgorithm == "SHA-256":
            hashValue = hashlib.sha256(textBox).hexdigest()

        elif currentAlgorithm == "SHA-384":
            hashValue = hashlib.sha384(textBox).hexdigest()

        elif currentAlgorithm == "SHA-512":
            hashValue = hashlib.sha512(textBox).hexdigest()

        elif currentAlgorithm == "SHA3-224":
            hashValue = hashlib.sha3_224(textBox).hexdigest()

        elif currentAlgorithm == "SHA3-256":
            hashValue = hashlib.sha3_256(textBox).hexdigest()

        elif currentAlgorithm == "SHA3-384":
            hashValue = hashlib.sha3_384(textBox).hexdigest()

        elif currentAlgorithm == "SHA3-512":
            hashValue = hashlib.sha3_512(textBox).hexdigest()

        self.resultHash.delete(0.0, 'end')
        self.resultHash.insert("1.0", hashValue)

    def deleteEntrys(self):
        global currentAlgorithm
        currentAlgorithm = ''
        self.resetButtonColors()
        self.resultHash.delete(0.0, 'end')
        self.entryField.delete(0.0, 'end')
