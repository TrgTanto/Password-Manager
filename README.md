## Hinweis
dieses projekt haben wir als team gemacht um unsere skills in der softwareentwicklung zu zeigen
es ist ein portfolio-projekt und nicht für den echten einsatz gedacht

*MITGLIEDER/AUFGABENTEILUNG*
- Maximilian Paschedag
    - ganze GUI (Gestaltung)
    - passwordFrame.py
    - checkerFrame.py
- Morrison May
    - generatorFrame.py
    - calculatorFrame.py
    - speicherung durch json dateien

**PASSWÖRTER: passwordFrame.py**
- speichert passwörter mit schöner ui (lokal in json datei)
- falls nötig kann man notizen hinzufügen oder links (nicht anklickbar)
- falls appname == Instagram, Google, Apple,
                   Gmail, Telegram, Snapchat,
                   Tiktok, Facebook, Discord,
                   Youtube, Netflix, Spotify,
                   Amazon, ebay, Paypal     -> perfektes icon, ansonsten ? icon

**GENERATOR: generatorFrame.py**
- starke und zufällge passwörter erstellen
- präzise standard analyse
- speichert die 5 letzten passwörter die generiert wurden (falls neues passwort ältestes geht weg)
- auswahl von zeichenarten
- sonderzeichen können mit slider addiert werden

**PASSWORTER-CHECKER: checkerFrame.py**
- überprüft eingegebenes passwort
- präzise standard analyse
- extra sicherheitsbewertung mit häufigkeit von echten geleakten datenbanken -> API call HIBP
- überprüft wie lange ein pc ca bräuchte um das passwort zu hacken -> library: zxcvbn
- empfehlungen was in der analyse fehlt
- speichert die 5 letzten passwörter die generiert wurden (falls neues passwort ältestes geht weg)

**HASH-RECHNER: calculatorFrame.py**
- kann text oder einzelnes wort sofort in einem beliebigen algorithmus (MD5, SHA-1, SHA-224,
                                                                       SHA-256, SHA-384, SHA-512,
                                                                       SHA3-224, SHA3-256, SHA3-384, SHA3-512)
- umgewandelt werden
- speichert nix

# disclaimer:
- alle daten werden nicht online gespeichert sondern bloß lokal auf seinen eigenen rechner
- app benötigt internet verbindung zwecks API call
- pwmanagerdev ist für den start per visual studio code (https://code.visualstudio.com/download) gedacht
- pwmanager ist für den start per exe (pwmanager/app/dist/main.exe) gedacht und kann nicht mit visual studio code gestartet werden
