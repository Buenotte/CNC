# 📋 CNC-Einrichteblatt & Werkzeug-Rüstplan (Agent 3: Setup-Sheet)
**Auftrag:** Auftrag 09 – Schnittdaten-Optimierung Edelstahl V4A *(1.4571)*  
**Kunde:** Krupp Maschinenteile GmbH, Duisburg *(Frank Lehmann, Produktionsleiter)*  
**Erstellt von:** Dipl.-Ing. Bujanovski *(Agent 3: NC-Safety- & Setup-Agent)*  
**Datum:** 24. Oktober 2026  
**Zielmaschine:** Haas VF-2 *(NGC-Steuerung, ISO-G-Code)*  
**NC-Programm:** `uebung_09_schnittdaten_check.nc` *(O1009)*  

---

## 1. Werkstück- & Spannmittel-Setup

| Parameter | Einstellwert | Erläuterung & Sicherheitshinweis |
| :--- | :--- | :--- |
| **Werkstoff** | **Edelstahl V4A (1.4571 / X6CrNiMoTi17-12-2)** | Hochzäher, austenitischer Edelstahl; neigt zu starker Kaltverfestigung. |
| **Rohteilmaße** | $85{,}0 \times 55{,}0 \times 15{,}0\,\text{mm}$ | Sägezuschnitt mit $2{,}5\,\text{mm}$ Aufmaß rundum. |
| **Fertigteilmaße** | $80{,}0 \times 50{,}0 \times 12{,}0\,\text{mm}$ | Planfräsen der Oberseite auf Fertigmaß $Z = 0{,}000\,\text{mm}$. |
| **Spannmittel** | Maschinenschraubstock mit gehärteten Stahlbacken | Backenbreite $125\,\text{mm}$, Spannkraft $70\,\text{Nm}$ Drehmoment. |
| **Parallelunterlagen ($h$)** | **Höhe $h = 32{,}0\,\text{mm}$** | Garantiert $3{,}0\,\text{mm}$ Spannrand und $+7{,}0\,\text{mm}$ Kollisionsreserve zu den Backen. |
| **Wackel-Probe (Fingerprobe)** | Zwingend durchführen | Nach Niederklopfen mit Schonhammer prüfen, ob beide Leisten spielfrei klemmen! |
| **Nullpunkt ($W / G54$)** | **$X0, Y0, Z0$ an fester Backe links hinten** | $Z0$ auf Fertigteil-Oberseite abnullen; Kantentaster-Kugelradius $+5{,}00\,\text{mm}$ verrechnen! |

---

## 2. Werkzeug- & Schnittdatenliste (Gedrosselte Sicherheitswerte)

> [!IMPORTANT]
> **Achtung Werkstatt:** Die Spindeldrehzahlen wurden vom Postprozessor via Auto-Speed-Clamp automatisch auf werkstoffgerechte Werte für Edelstahl gedrosselt! Keinesfalls an der Steuerung manuell auf $8.000\,\text{U/min}$ hochdrehen!

| Platz (T) | Werkzeug-Beschreibung | Durchmesser | Schneiden ($z$) | Schnittgeschw. ($v_c$) | Drehzahl ($S$) | Vorschub ($F$) | Kühlung |
| :---: | :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **`T01`** | **VHM-Schaftfräser Ø 10 mm** *(AlTiN-Beschichtung)* | $10{,}0\,\text{mm}$ | 4 | **$90\,\text{m/min}$** *(Maximalwert)* | **`S2865`** *(Auto-Speed-Clamp)* | **`F400`** *(Gedrosselt)* | **`M08`** *(Flutkühlung)* |
| **`T02`** | **VHM-Spiralbohrer Ø 6 mm** *(mit Innenkühlung)* | $6{,}0\,\text{mm}$ | 2 | **$66\,\text{m/min}$** *(Sicherheitswert)* | **`S3500`** | **`F280`** | **`M08`** *(Flutkühlung)* |

---

## 3. Schritt-für-Schritt-Einfahrprotokoll an der Maschine

1. **Schritt 1 (Luftschnitt in $Z +50\,\text{mm}$):**  
   Im G54-Nullpunktspeicher temporär $+50{,}0\,\text{mm}$ auf Z aufschlagen. Programm starten und Verfahrwege in der freien Luft visuell abgleichen.
2. **Schritt 2 (Einzelsatz `Single Block` mit 10 % Vorschub-Override):**  
   Z-Nullpunkt wieder auf $0{,}00\,\text{mm}$ zurücksetzen. Mit Einzelsatz-Taste jeden Befehl einzeln bestätigen und Restweganzeige *(Distance-to-go)* vor jedem Spanabtrag prüfen.
3. **Schritt 3 (Schnittbeobachtung & KSS-Druck):**  
   Auf silbrig-braune, lockere Kommaspäne achten. Bei Rauchentwicklung oder blauglühenden Spänen sofort Vorschub-Halt betätigen!

---

**Freigegeben zur Rüstung:** Dipl.-Ing. Bujanovski *(Agent 3: NC-Safety- & Setup-Agent)*  
**Datum:** 24. Oktober 2026
