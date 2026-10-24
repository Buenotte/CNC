# 📩 Kundenauftrag: Hessen Automotive GmbH (Auftrag 16: Meisterprüfung – 5-Punkte-Endabnahme & Zertifikat)

**Auftraggeber:** Dipl.-Ing. Bernd Schäfer (Leiter Qualitätssicherung)  
**Unternehmen:** Hessen Automotive GmbH  
**Empfänger:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
**Zielmaschine:** **GroB G550 5-Achs-Bearbeitungszentrum (Siemens Sinumerik ONE)**  
**Vereinbartes Budget:** **490,00 € netto** (583,10 € brutto)  

---

## Auftrags-Briefing des Kunden:

# 📩 Kundenauftrag: Übung 16: Die komplette 5-Punkte-Endabnahme im Simulator vor der Auslieferung an den Online-Kunden (Meister-Prüfung)
**Auftrags-Kategorie:** 16 (Unabhängiges Sicherheits-Audit & G-Code-Zertifizierung)
**Auftragnehmer:** Dipl.-Ing. Bujanovski – Freiberufliches Ingenieurbüro für CAD/CAM-Fertigungstechnik & Postprozessor-Entwicklung  
**Status:** Aktiv / Bereit zur Bearbeitung

---

## 1. Das Original-Auftragsbriefing des Kunden

So sieht eine typische hochbezahlte Anfrage aus, wenn ein Automobilzulieferer oder Maschinenbauer ein externes Sicherheits-Audit vor dem Serienanlauf verlangt:

> **Von:** Dipl.-Ing. Bernd Schäfer *(Leiter Qualitätssicherung)* `<b.schaefer@hessen-automotive.de>`  
> **An:** Dipl.-Ing. Bujanovski `<kontakt@ingenieurbuero-bujanovski.de>`  
> **Datum:** 30. Oktober 2026, 15:00 Uhr  
> **Betreff:** Externes Sicherheits-Audit & Crash-Prüfprotokoll für 5 Serienprogramme  
>
> Sehr geehrter Herr Kollege Dipl.-Ing. Bujanovski,  
> 
> als Tier-1-Zulieferer der Automobilindustrie in Frankfurt am Main dürfen wir neue Fräsprogramme erst auf unseren 500.000-Euro-5-Achs-Zentren freigeben, wenn ein unabhängiges, ingenieurmäßiges Sicherheits-Audit durchgeführt wurde *(Vier-Augen-Prinzip nach IATF 16949)*.  
> 
> **Aufgabenstellung:**  
> Unterziehen Sie unser CNC-Programm der vollständigen **5-Stufen-Meisterprüfung**:  
> 1. Verifikation von Werkstück-Nullpunkt `G54` und Rohteilabmessungen am 3D-Simulator.  
> 2. Mathematische Z-MIN-Prüfung gegen Schraubstock-Crash und Ermittlung der Mindest-Werkzeugauskraglänge $L_{\text{min}}$.  
> 3. Vollständiger Scan auf Eilgangfehler *(keine `G00`-Bewegungen unterhalb $Z \le 0$!)*.  
> 4. Schnittdaten-Plausibilität: Rechtslauf `M03`, Drehzahl $S > 0$, Vorschub $F > 0$ vor erstem Materialeintauchen, Kühlmittel `M08`.  
> 5. Sicherer 2-Stufen-Rückzug `G53 Z0.` vor Tischfahrt `G53 Y0.`.  
> 6. Generierung des zertifizierten Prüfprotokolls und Einrichteblatts (PDF) mit Haftungsfreigabeklausel.  
> 
> **Vergütung:**  
> Pauschal **490,00 € netto** pro auditierter Baugruppe.  
> 
> Wir freuen uns auf Ihren detaillierten Prüfbericht!  
> 
> Mit besten Grüßen  
> **Dipl.-Ing. Bernd Schäfer** – Automotive Zerspanungs-Cluster Hessen GmbH, Frankfurt am Main

---

## 2. Bearbeitungshinweise für diesen Auftrag
* **Zuständiger Agent für Angebot:** `Agent 4` (Backoffice-Agent) – siehe `ANGEBOT_DIPL_ING_BUJANOVSKI.md` in diesem Ordner.
* **Zuständiger Agent für Umsetzung:** `Agent 2` (Postprocessor-Coder-Agent) für Code- & .cps-Modifikationen.
* **Zuständiger Agent für Prüfung & Freigabe:** `Agent 3` (NC-Safety- & Setup-Agent) für Crash-Prüfung und Einrichteblatt.

