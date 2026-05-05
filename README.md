## Hinweis
Dieses Projekt haben wir als Team zusammen gemacht um unsere Skills in der Softwareentwicklung zu zeigen
Es ist ein Portfolio Projekt und nicht für den echten Einsatz gedacht

*MITGLIEDER/AUFGABENTEILUNG*
- Max
    - Ganze GUI Gestaltung
    - passwordFrame.py
    - checkerFrame.py
- Morrison
    - generatorFrame.py
    - calculatorFrame.py
    - Speicherung durch JSON Dateien

**PASSWÖRTER: passwordFrame.py**
- Speichert Passwörter mit UI lokal in JSON Datei
- Optional können Notizen oder Links hinzugefügt werden (Links sind nicht anklickbar)
- Falls App Name z.B. Instagram Google Apple Gmail Telegram Snapchat Tiktok Facebook Discord Youtube Netflix Spotify Amazon Ebay Paypal dann wird ein passendes Icon angezeigt sonst ein ? Icon

**GENERATOR: generatorFrame.py**
- Erstellt starke und zufällige Passwörter
- Standard Analyse
- Speichert die letzten 5 generierten Passwörter ältestes wird ersetzt
- Auswahl von Zeichenarten
- Sonderzeichen können mit Slider hinzugefügt werden

**PASSWORTER-CHECKER: checkerFrame.py**
- Überprüft eingegebenes Passwort
- Standard Analyse
- Sicherheitsbewertung basierend auf geleakten Datenbanken über API von HIBP
- Überprüft wie lange ein Computer bräuchte um das Passwort zu hacken mit library -> zxcvbn
- Gibt Empfehlung zur Verbesserung
- Speichert die letzten 5 geprüften Passwörter ältestes wird ersetzt

**HASH-RECHNER: calculatorFrame.py**
- Wandelt Text oder einzelne Wörter in Hashes um
- Unterstützt MD5 SHA-1 SHA-224 SHA-256 SHA-384 SHA-512 SHA3-224 SHA3-256 SHA3-384 SHA3-512
- Speichert keine Daten

# Disclaimer:
- Alle Daten werden nur lokal auf dem eigenen Rechner gespeichert
- Internetverbindung wird für API Calls benötigt
- pwmanagerdev ist für den Start über Visual Studio Code gedacht
- pwmanager ist nur für die Erstellung der .exe Version gedacht da dabei zusätzliche Dateien erstellt wurden und Build Komponenten erzeugt werden (startet nicht über Visual Studio Code)
