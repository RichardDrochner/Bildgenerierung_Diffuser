# Bildgenerierung_Diffuser

## Projektbeschreibung

Dieses Repository enthält die im Rahmen der Bachelorarbeit im Studiengang Wirtschaftsinformatik an der Hochschule für Technik und Wirtschaft Berlin (HTW Berlin) erhobenen und erzeugten Forschungsdaten sowie zugehörige Logdateien.

Ziel der Arbeit ist das Erstellen einer Nutzungs- und Leistungsdokumentation für den Verleih von GPU-gestützten Laptops an Studierende der HTW Berlin. Das Projekt dient als Einstiegsszenario für Studierende, um erste praktische Erfahrungen mit GPU-beschleunigten Anwendungen zu sammeln, sowie zur Evaluation der Leistungsfähigkeit der Leihgeräte unter realistischen Nutzungsszenarien (z. B. KI-Bildgenerierung).

Die Datenerhebung und -auswertung erfolgte eigenständig durch den Autor im Rahmen der Bachelorarbeit. Die Dokumentation orientiert sich an den Anforderungen guter wissenschaftlicher Praxis sowie an den Empfehlungen zum Forschungsdatenmanagement (FDM).

---

## Art der Daten

Die vorliegenden Daten umfassen:

1. **Logdaten**

   * Performance- und Laufzeitlogs der Bildgenerierung
   * CSV-Dateien mit Zeitstempeln, Ausführungsdauer, Hardwareauslastung und Parametern der Testläufe

2. **Bilddaten**

   * KI-generierte Bilddateien (z. B. *.webp*)
   * Zweck: reproduzierbare Belastungs- und Funktionstests der GPU-Hardware
   * Motive: futuristische Campus- und urbane Szenarien
   * Unterschiedliche Generierungsparameter (Steps, Seeds, Detailgrad)

3. **Begleitende Metadaten**

   * Dateinamenkodierung zur Zuordnung von Parametern
   * Ordnerstruktur nach Datentyp und Experimentreihe

**Sprache:** Deutsch

**Wissenschaftliche Methode:**
Experimentelle Datenerhebung zur Leistungsbewertung von GPU-gestützten Leihlaptops sowie Erstellung einer praxisorientierten Nutzungsdokumentation für Studierende.

---

## Datenursprung 

* **Autor:** Die Daten wurden vollständig selbst erhoben und generiert.
* **Drittquellen:** Keine externen Datensätze wurden verwendet.
* **Lizenz:

* Code, Log- und Messdaten: Apache License 2.0

* Generierte Bilddaten: Apache License 2.0 (wissenschaftliche Nutzung im Rahmen der Abschlussarbeit)

---

## Zeitraum der Datenerhebung

* Datenerhebung und Bildgenerierung: siehe Zeitstempel in den Logdateien
* Datenaufbereitung und Analyse: im Anschluss an die Generierungsphase im Rahmen der Abschlussarbeit

---

## Datenformate und -umfang

* **Logdateien:**

  * CSV (*.csv*)
  * Größe: wenige KB bis MB

* **Bilddateien:**

  * WebP (*.webp*)
  * Größe: abhängig von Auflösung und Detailgrad (mehrere MB pro Bild)

---

## Eingesetzte Werkzeuge

* KI-Bildgenerierungssoftware (Diffusionsmodell, lokal ausgeführt)
* Skripte zur Protokollierung der Performance-Daten
* Tabellenkalkulations- bzw. Analysewerkzeuge zur Auswertung der CSV-Dateien

(Es wurden ausschließlich Werkzeuge genutzt, die lokal oder im Rahmen der Arbeit verfügbar waren.)

---

## Qualitätssicherung

* Plausibilitätsprüfung der Logdaten (Vollständigkeit, konsistente Zeitstempel)
* Vergleich mehrerer Generierungsdurchläufe mit identischen Parametern
* Nachvollziehbare Benennung der Bilddateien zur eindeutigen Zuordnung

---

## Datenschutz und Rechte

* Es wurden **keine personenbezogenen oder sensiblen Daten** erhhoben.
* Die generierten Bilder stellen keine realen Personen dar.
* Urheberrecht an allen Daten und Bildern liegt beim Autor.

---

## Ablageort und Struktur

**Ordnerstruktur:**

```
/
├─ Logs/
│  └─ perf_log_diffuser.csv
├─ Diffuser Images/
│  ├─ campus_sunset_*.webp
│  └─ urban_futuristic_*.webp
└─ README.md
```

**Dateibenennung:**

* Enthält Informationen zu Motiv, Steps, Seed und ggf. Iteration

**Aufbewahrung:**

* Speicherung lokal und in gesichertem Repository
* Aufbewahrungsdauer gemäß Prüfungs- und Hochschulvorgaben

---

## Hinweise zur Nachnutzung

Die vorliegenden Daten und Dateien stehen unter der **Apache License, Version 2.0**. Eine Nachnutzung, Veränderung und Weiterverbreitung ist im Rahmen dieser Lizenz zulässig, sofern die Lizenzbedingungen eingehalten werden.

Die Daten dienen primär der Nachvollziehbarkeit und Reproduzierbarkeit der Bachelorarbeit im Studiengang Wirtschaftsinformatik an der HTW Berlin.

---

## Kontakt

Bei Rückfragen zur Struktur, Nutzung oder Interpretation der Daten wenden Sie sich bitte an den Autor der Bachelorarbeit (HTW Berlin, Wirtschaftsinformatik).



