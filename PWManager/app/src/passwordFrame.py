import customtkinter as ctk
import string, secrets, clipboard, json, os, uuid

from PIL import Image
from src.resourcePath import resource_path
from src.getData import get_data_path

nameLists =  [
"instagram", "google",
"apple", "gmail",
"telegram", "snapchat",
"tiktok", "facebook",
"discord", "youtube",
"netflix", "spotify",
"amazon","ebay",
"paypal"
]

FILE_PATH = get_data_path("passwords.json")

class passwordFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(master=parent,
            fg_color="#030D17",
            width=1058, 
            height=800,
            corner_radius=0,
            border_width=1,
            border_color="#212830"
        )
        self.totalAmountPasswords = 0

        #mainFrame
        self.title = ctk.CTkLabel(master=self,
            text="Passwörter",
            font=("Segoe UI", 22, "bold"),
            text_color="#EDECE5"
        )
        self.title.place(anchor="center", relx=0.07, rely=0.04)

        self.passwordText = ctk.CTkLabel(master=self,
            text="Verwalte deine gespeicherten Passwörter sicher und organisiert.",
            font=("Segoe UI", 14),
            text_color="#677073"
        )
        self.passwordText.place(anchor="center", relx=0.2, rely=0.07)

        # passwordsListFrame
        self.passwordsListFrame = ctk.CTkFrame(master=self,
            width=510,
            height=715,
            border_width=1,
            border_color="#232D38",
            fg_color="#0C161E",
            corner_radius=0
        )
        self.passwordsListFrame.place(anchor="center", relx=0.255, rely=0.53)

        # passwordsListFrame (SettingsFrame)
        self.passwordsListSettingsFrame = ctk.CTkFrame(master=self.passwordsListFrame,
            width=510,
            height=80,
            border_width=1,
            corner_radius=0,
            border_color="#232D38",
            fg_color="transparent",
        )
        self.passwordsListSettingsFrame.place(anchor="center", relx=0.5, rely=0.056)

        self.createNewEntry = ctk.CTkButton(master=self.passwordsListSettingsFrame,
            text="Neuer Eintrag",
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/plusButton.png"))),
            font=("Roboto Medium", 16),
            corner_radius=8,
            border_width=1,
            fg_color="#0639BF",
            text_color="#B6C6ED",
            border_color="#328EFB",
            hover_color="#112758",
            width=150,
            height=45,
            command=lambda:self.createNewPassword()
        )
        self.createNewEntry.place(anchor="center", relx=0.83, rely=0.5)

        # passwordsListFrame (totalAmountPasswords)
        self.passwordsListSavedFrame = ctk.CTkScrollableFrame(master=self.passwordsListFrame,
            width=480,
            height=635,
            border_width=1,
            corner_radius=0,
            border_color="#232D38",
            fg_color="transparent"
        )
        self.passwordsListSavedFrame.place(anchor="center", relx=0.5, rely=0.555)

        self.zeroEntries = ctk.CTkLabel(master=self.passwordsListSavedFrame,
            text="",
            image=ctk.CTkImage(dark_image=Image.open(resource_path('icons/png/zeroEntries.png')), size=(100, 100))
        )

        self.zeroEntriesText = ctk.CTkLabel(master=self.passwordsListSavedFrame,
            text="Noch keine Einträge vorhanden",
            font=("Segoe UI", 22),
            text_color="#EDECE5"
        )

        self.zeroEntriesTextInfo = ctk.CTkLabel(master=self.passwordsListSavedFrame,
            text="Speichere deine Passwörter sicher an einem Ort.",
            font=("Segoe UI", 14),
            text_color="#677073"
        )

        self.passwordsListSavedFrame.grid_columnconfigure(0, weight=1)
        self.passwordsListSavedFrame.grid_rowconfigure(0, weight=1)
        self.placeholder = ctk.CTkFrame(master=self.passwordsListSavedFrame,
            width=5,
            height=200,
            fg_color="transparent",
            border_width=0
        )
        self.placeholder.grid(row=0, column=0)
        self.zeroEntries.grid(row=1, column=0)
        self.zeroEntriesText.grid(row=2, column=0)
        self.zeroEntriesTextInfo.grid(row=3, column=0)

        # passwordInformationFrame
        self.passwordInformationFrame = ctk.CTkFrame(master=self,
            width=510,
            height=715,
            border_width=1,
            border_color="#232D38",
            fg_color="#0C161E",
            corner_radius=0,
        )
        self.passwordInformationFrame.place(anchor="center", relx=0.745, rely=0.53)

        self.informationtitle = ctk.CTkButton(master=self.passwordInformationFrame,
            text="",
            font=("Segoe UI", 22, "bold"),
            text_color="#EDECE5",
            fg_color="transparent",
            hover="disabled"
        )

        self.informationFrameDesign = ctk.CTkFrame(master=self.passwordInformationFrame,
            width=490,
            height=350,
            fg_color="transparent",
            border_width=0,
            corner_radius=0
        )

        self.usernameInformationDesign = ctk.CTkButton(master=self.informationFrameDesign,
            text="Benutzername / E-Mail",
            font=("Roboto", 14),
            width=490,
            height=87.5,
            corner_radius=0,
            fg_color="transparent",
            border_color="#232D38",
            border_width=1,
            hover="disabled",
            anchor="w",
            text_color="#677073"
        )

        self.usernameButton = ctk.CTkButton(master=self.usernameInformationDesign,
            text="",
            font=("Roboto", 12.5),
            width=250,
            height=50,
            corner_radius=8,
            fg_color="#09131E",
            border_color="#232D38",
            border_width=1,
            hover="disabled",
            anchor="center",
            text_color="#EDECE5"
        )

        self.passwordInformationDesign = ctk.CTkButton(master=self.informationFrameDesign,
            text="Passwort",
            font=("Roboto", 14),
            width=490,
            height=87.5,
            corner_radius=0,
            fg_color="transparent",
            border_color="#232D38",
            border_width=1,
            hover="disabled",
            anchor="w",
            text_color="#677073"
        )

        self.passwordButton = ctk.CTkButton(master=self.passwordInformationDesign,
            text="",
            font=("Roboto", 12.5),
            width=250,
            height=50,
            corner_radius=8,
            fg_color="#09131E",
            border_color="#232D38",
            border_width=1,
            hover="disabled",
            anchor="center",
            text_color="#EDECE5"
        )

        self.websiteInformationDesign = ctk.CTkButton(master=self.informationFrameDesign,
            text="Website",
            font=("Roboto", 14),
            width=490,
            height=87.5,
            corner_radius=0,
            fg_color="transparent",
            border_color="#232D38",
            border_width=1,
            hover="disabled",
            anchor="w",
            text_color="#677073"
        )

        self.websiteButton = ctk.CTkButton(master=self.websiteInformationDesign,
            text="",
            font=("Roboto", 12.5),
            width=250,
            height=50,
            corner_radius=8,
            fg_color="#09131E",
            border_color="#232D38",
            border_width=1,
            hover="disabled",
            anchor="center",
            text_color="#EDECE5"
        )

        self.notesInformationDesign = ctk.CTkButton(master=self.informationFrameDesign,
            text="Notizen",
            font=("Roboto", 14),
            width=490,
            height=87.5,
            corner_radius=0,
            fg_color="transparent",
            border_color="#232D38",
            border_width=1,
            hover="disabled",
            anchor="w",
            text_color="#677073"
        )

        self.notesButton = ctk.CTkButton(master=self.notesInformationDesign,
            text="",
            font=("Roboto", 12.5),
            width=250,
            height=50,
            corner_radius=8,
            fg_color="#09131E",
            border_color="#232D38",
            border_width=1,
            hover="disabled",
            anchor="center",
            text_color="#EDECE5"
        )

        self.copyButton = ctk.CTkButton(master=self.passwordInformationFrame,
            width=120,
            height=50,
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/calculatorCopy.png")), size=(25, 25)),
            text="Kopieren",
            font=("Roboto Medium", 16),
            corner_radius=8,
            border_width=1,
            fg_color="#0639BF",
            text_color="#B6C6ED",
            border_color="#328EFB",
            hover_color="#112758"
        )

        self.deleteButton = ctk.CTkButton(master=self.passwordInformationFrame,
            width=120,
            height=50,
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/calculatorTrashCan.png")), size=(22, 22)),
            text="Löschen",
            font=("Roboto Medium", 16),
            corner_radius=8,
            border_width=1,
            fg_color="#EE0707",
            text_color="#B6C6ED",
            border_color="#CE4444",
            hover_color="#802323"
        )

        data = self.load_passwords()

        for entry in data:
            self.createButton(
                entry["id"],
                entry["name"],
                entry["username"],
                entry["password"],
                entry["url"],
                entry["notes"]
            )
            self.totalAmountPasswords += 1
            self.checktotalAmountPasswords()


    def checktotalAmountPasswords(self):
        if self.totalAmountPasswords >= 1:
            try:
                if self.placeholder.winfo_exists():
                    self.placeholder.grid_forget()
                if self.zeroEntries.winfo_exists():
                    self.zeroEntries.grid_forget()
                if self.zeroEntriesText.winfo_exists():
                    self.zeroEntriesText.grid_forget()
                if self.zeroEntriesTextInfo.winfo_exists():
                    self.zeroEntriesTextInfo.grid_forget()
            except:
                pass

    def createNewPassword(self):
        newEntyFrame = ctk.CTkFrame(master=self,
            width=850,
            height=725,
            border_width=1,
            border_color="#232D38",
            fg_color="#0C161E",
            corner_radius=8
        )
        newEntyFrame.place(anchor="center", relx=0.5, rely=0.53)
        newEntyFrame.grab_set() # all interactions go to this frame
        newEntyFrame.focus() # sets the frame to the focus, not nessarcy but in case there's a bug

        titleText = ctk.CTkLabel(master=newEntyFrame,
            text="Neuen Eintrag erstellen",
            font=("Segoe UI", 18, "bold"),
            text_color="#EDECE5"
        )
        titleText.place(anchor="center", relx=0.15, rely=0.05)

        errorText = ctk.CTkLabel(master=newEntyFrame,
            text="",
            text_color="#F32334",
            font=("Roboto Medium", 16)
        )
        errorText.place(anchor="center", relx=0.5, rely=0.11)

        closeFrame = ctk.CTkButton(master=newEntyFrame,
            text="",
            image=ctk.CTkImage(dark_image=Image.open(resource_path('icons/png/closeButton.png')), size=(35, 35)),
            fg_color="transparent",
            hover_color="#232D38",
            width=40,
            height=40,
            command=lambda:closeFrame()
        )
        closeFrame.place(anchor="center", relx=0.95, rely=0.05)

        # generallyInformationFrame
        generallyInformationFrame = ctk.CTkFrame(master=newEntyFrame,
            width=400,
            height=500,
            fg_color="transparent",
            border_width=2,
            border_color="#232D38"
        )
        generallyInformationFrame.place(anchor="center", relx=0.26, rely=0.5)

        generallyTitleText = ctk.CTkLabel(master=generallyInformationFrame,
            text="Allgemeine Informationen",
            font=("Segoe UI", 15, "bold"),
            text_color="#EDECE5"
        )
        generallyTitleText.place(anchor="center", relx=0.265, rely=0.08)

        generallyNameText = ctk.CTkLabel(master=generallyInformationFrame,
            text="Name / Website *",
            font=("Segoe UI", 14),
            text_color="#EDECE5"
        )
        generallyNameText.place(anchor="center", relx=0.17, rely=0.15)

        nameEntry = ctk.CTkEntry(master=generallyInformationFrame,
            placeholder_text="z.B. Google, Amazon, Netflix",
            placeholder_text_color="#565C62",
            fg_color="#030D17",
            border_width=1,
            border_color="#212830",
            corner_radius=8,
            width=370,
            height=35,
            font=("Roboto", 13),
            text_color="#81868B"
        ) 
        nameEntry.place(anchor="center", relx=0.495, rely=0.21)

        generallyUsernameText = ctk.CTkLabel(master=generallyInformationFrame,
            text="Benutzername / E-Mail *",
            font=("Segoe UI", 14),
            text_color="#EDECE5"
        )
        generallyUsernameText.place(anchor="center", relx=0.22, rely=0.33)

        usernameEntry = ctk.CTkEntry(master=generallyInformationFrame,
            placeholder_text="z.B. max.mustermann@gmail.com",
            placeholder_text_color="#565C62",
            fg_color="#030D17",
            border_width=1,
            border_color="#212830",
            corner_radius=8,
            width=370,
            height=35,
            font=("Roboto", 13),
            text_color="#81868B"
        ) 
        usernameEntry.place(anchor="center", relx=0.495, rely=0.4)

        generallyPasswordText = ctk.CTkLabel(master=generallyInformationFrame,
            text="Passwort *",
            font=("Segoe UI", 14),
            text_color="#EDECE5"
        )
        generallyPasswordText.place(anchor="center", relx=0.12, rely=0.49)

        passwordEntry = ctk.CTkEntry(master=generallyInformationFrame,
            placeholder_text="Ein sicheres Passwort eingeben...",
            placeholder_text_color="#565C62",
            fg_color="#030D17",
            border_width=1,
            border_color="#212830",
            corner_radius=8,
            width=370,
            height=35,
            font=("Roboto", 13),
            text_color="#81868B"
        ) 
        passwordEntry.place(anchor="center", relx=0.495, rely=0.56)

        generatePasswordButton = ctk.CTkButton(master=generallyInformationFrame,
            width=370,
            height=50,
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/informationClosedIcon.png")), size=(20, 20)),
            text="Passwort generieren",
            font=("Roboto Medium", 16),
            corner_radius=8,
            border_width=1,
            fg_color="#0639BF",
            text_color="#B6C6ED",
            border_color="#328EFB",
            hover_color="#112758",
            command=lambda:generatePassword()
        )
        generatePasswordButton.place(anchor="center", relx=0.495, rely=0.75)

        # additonalInformationFrame
        additonalInformationFrame = ctk.CTkFrame(master=newEntyFrame,
            width=400,
            height=500,
            fg_color="transparent",
            border_width=2,
            border_color="#232D38"
        )
        additonalInformationFrame.place(anchor="center", relx=0.74, rely=0.5)

        additonalTitleText = ctk.CTkLabel(master=additonalInformationFrame,
            text="Zusätzliche Informationen",
            font=("Segoe UI", 15, "bold"),
            text_color="#EDECE5"
        )
        additonalTitleText.place(anchor="center", relx=0.265, rely=0.08)

        additonalLinkText = ctk.CTkLabel(master=additonalInformationFrame,
            text="Website / URL",
            font=("Segoe UI", 14),
            text_color="#EDECE5"
        )
        additonalLinkText.place(anchor="center", relx=0.14, rely=0.15)

        linkEntry = ctk.CTkEntry(master=additonalInformationFrame,
            placeholder_text="https://example.com",
            placeholder_text_color="#565C62",
            fg_color="#030D17",
            border_width=1,
            border_color="#212830",
            corner_radius=8,
            width=370,
            height=35,
            font=("Roboto", 13),
            text_color="#81868B"
        ) 
        linkEntry.place(anchor="center", relx=0.495, rely=0.21)

        additonalNotesText = ctk.CTkLabel(master=additonalInformationFrame,
            text="Notizen",
            font=("Segoe UI", 14),
            text_color="#EDECE5"
        )
        additonalNotesText.place(anchor="center", relx=0.10, rely=0.33)

        notesEntry = ctk.CTkEntry(master=additonalInformationFrame,
            placeholder_text="Notizen hinzufügen...",
            placeholder_text_color="#565C62",
            fg_color="#030D17",
            border_width=1,
            border_color="#212830",
            corner_radius=8,
            width=370,
            height=35,
            font=("Roboto", 13),
            text_color="#81868B"
        ) 
        notesEntry.place(anchor="center", relx=0.495, rely=0.4)

        cancelButton = ctk.CTkButton(master=newEntyFrame,
            width=150,
            height=45,
            text="Abbrechen",
            font=("Roboto Medium", 16),
            corner_radius=8,
            border_width=1,
            fg_color="#030D17",
            text_color="#B6C6ED",
            border_color="#212830",
            hover_color="#353C4B",
            command=lambda:closeFrame()
        )
        cancelButton.place(anchor="center", relx=0.11, rely=0.93)

        saveButton = ctk.CTkButton(master=newEntyFrame,
            width=150,
            height=45,
            image=ctk.CTkImage(dark_image=Image.open(resource_path("icons/png/savePassword.png")), size=(20, 20)),
            text="Speichern",
            font=("Roboto Medium", 16),
            corner_radius=8,
            border_width=1,
            fg_color="#0639BF",
            text_color="#B6C6ED",
            border_color="#328EFB",
            hover_color="#112758",
            command=lambda:saveThePassword()
        )
        saveButton.place(anchor="center", relx=0.888, rely=0.93)

        def closeFrame():
            newEntyFrame.grab_release()
            newEntyFrame.place_forget()
    

        def generatePassword():
            allChars = string.ascii_letters + string.digits + string.punctuation
            pw = ''
            for n in range(24):
                pw += secrets.choice(allChars)

            passwordEntry.delete(0, 'end')
            passwordEntry.insert(0, pw)

        def saveThePassword():
            global nameLists, totalAmountPasswords
            nameFull = nameEntry.get().lower().strip()
            nameFull = nameFull.replace(" ", "")

            username = usernameEntry.get().strip()

            password = passwordEntry.get().strip()

            url = linkEntry.get().strip()
            url = url.replace(" ", "")

            notes = notesEntry.get().strip()

            requiredText = ''

            if len(nameFull) == 0:
                requiredText += "Das Feld „Name / Website“ darf nicht leer sein.\n"
                
            if len(username) < 4:
                requiredText += "Dein Benutzername muss mindestens 4 Zeichen haben.\n" 

            if len(password) == 0:
                requiredText += "Das Feld „Passwort“ darf nicht leer sein.\n"
            
            errorText.configure(text=requiredText)

            if len(requiredText) > 1: pass
            else:
                self.totalAmountPasswords += 1
                self.checktotalAmountPasswords()

                new_entry = {
                    "id": str(uuid.uuid4()),
                    "name": nameFull,
                    "username": username,
                    "password": password,
                    "url": url,
                    "notes": notes
                }

                data = self.load_passwords()
                data.append(new_entry)
                self.save_passwords(data)

                self.createButton(new_entry["id"], nameFull, username, password, url, notes)
                closeFrame()
            
    def createButton(self, entry_id, enterName, username, password, url, notes):
        global nameLists, totalAmountPasswords
        checkImage = ''
        if enterName in nameLists:
            checkImage = ctk.CTkImage(dark_image=Image.open(resource_path(f"icons/png/appPngs/{enterName}.png")), size=(50,50 ))
        else:
            checkImage = ctk.CTkImage(dark_image=Image.open(resource_path(f"icons/png/appPngs/notInnamelists.png")), size=(50,50 ))
        variable = ctk.CTkButton(master=self.passwordsListSavedFrame,
                image=checkImage,
                text=f"{enterName}, {username}",
                width=510,
                height=50,
                anchor="w",
                corner_radius=0,
                fg_color="transparent",
                border_color="#232D38",
                hover_color="#112758",
                border_width=1,
                command=lambda: self.showInformationen(entry_id, enterName, username, password, url, notes, checkImage)
            )
        variable.grid(row=self.totalAmountPasswords, column=0)

    def load_passwords(self):
        if os.path.exists(FILE_PATH):
            with open(FILE_PATH, "r") as f:
                return json.load(f)
        return []

    def save_passwords(self, data):
        with open(FILE_PATH, "w") as f:
            json.dump(data, f, indent=4)

    def showInformationen(self, entry_id, name, username, password, url, notes, checkImage):
        nameDesigned = name[0:1].upper() + name[1:]

        self.informationtitle.place(anchor="center", relx=0.5, rely=0.08)
        self.informationFrameDesign.place(anchor="center", relx=0.5, rely=0.4)

        self.usernameInformationDesign.place(anchor="center", relx=0.5, rely=0.125)
        self.usernameButton.place(anchor="center", relx=0.7, rely=0.5)

        self.passwordInformationDesign.place(anchor="center", relx=0.5, rely=0.368)
        self.passwordButton.place(anchor="center", relx=0.7, rely=0.5)

        self.websiteInformationDesign.place(anchor="center", relx=0.5, rely=0.611)
        self.websiteButton.place(anchor="center", relx=0.7, rely=0.5)

        self.notesInformationDesign.place(anchor="center", relx=0.5, rely=0.854)
        self.notesButton.place(anchor="center", relx=0.7, rely=0.5)

        self.copyButton.place(anchor="center", relx=0.35, rely=0.9)
        self.copyButton.configure(command=lambda:self.copyUsernamePasswordDesigned(username, password))
        self.deleteButton.place(anchor="center", relx=0.60, rely=0.9)
        self.deleteButton.configure(command=lambda: self.deletePassword(entry_id))

        self.informationtitle.configure(image=checkImage, text=nameDesigned)

        self.usernameButton.configure(text=username, command=lambda:clipboard.copy(username))
        self.passwordButton.configure(text=password, command=lambda:clipboard.copy(password))
        if len(url) == 0:
            self.websiteButton.configure(text="Du hast kein Link eingefügt")
        else:
            self.websiteButton.configure(text=url)

        if len(url) == 0:
            self.notesButton.configure(text="Du hast keine Notiz hinzugefügt")
        else:
            self.notesButton.configure(text=notes)

    def copyUsernamePasswordDesigned(self, username, password):
        copy = ("Benutzername: " + str(username)
                + '\n' + "Passwort: " + str(password)
                + '\n' + "Hinweis: Gib deine Passwörter niemals an Dritte weiter!"
            )
        clipboard.copy(copy)
    
    def deletePassword(self, entry_id):
        data = self.load_passwords()

        data = [entry for entry in data if entry["id"] != entry_id]

        self.save_passwords(data)

        self.informationtitle.place_forget()
        self.informationFrameDesign.place_forget()
        self.usernameButton.place_forget()
        self.passwordButton.place_forget()
        self.websiteButton.place_forget()
        self.notesButton.place_forget()
        self.copyButton.place_forget()
        self.deleteButton.place_forget()

        self.refreshUI()

    def refreshUI(self):
        for widget in self.passwordsListSavedFrame.winfo_children():
            widget.destroy()

        self.totalAmountPasswords = 0

        data = self.load_passwords()

        for entry in data:
            self.createButton(
                entry["id"],
                entry["name"],
                entry["username"],
                entry["password"],
                entry["url"],
                entry["notes"]
            )
            self.totalAmountPasswords += 1

        self.checktotalAmountPasswords()