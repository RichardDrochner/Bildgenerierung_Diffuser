# Bildgenerierung_Diffuser
# README – Dokumentation der erhobenen Daten und generierten Bilder

## Projektbeschreibung

Dieses Repository enthält die im Rahmen der Abschlussarbeit erhobenen und erzeugten Forschungsdaten sowie zugehörige Logdateien. Ziel der Arbeit ist die nachvollziehbare Dokumentation und Analyse von Leistungs- und Generierungsprozessen bei der Erzeugung hochauflösender, KI-generierter Bilddaten.

Die Dokumentation orientiert sich an den Anforderungen guter wissenschaftlicher Praxis und den Empfehlungen zum Forschungsdatenmanagement (FDM).

---

## Art der Daten

Die vorliegenden Daten umfassen:

1. **Logdaten**

   * Performance- und Laufzeitlogs der Bildgenerierung
   * CSV-Dateien mit Zeitstempeln, Parametern (z. B. Steps, Seed) und Systemkennzahlen

2. **Bilddaten**

   * KI-generierte Bilddateien (z. B. *.webp*)
   * Motive: futuristische Campus- und urbane Szenarien
   * Unterschiedliche Generierungsparameter (Steps, Seeds, Detailgrad)

3. **Begleitende Metadaten**

   * Dateinamenkodierung zur Zuordnung von Parametern
   * Ordnerstruktur nach Datentyp und Experimentreihe

**Sprache:** Deutsch

**Wissenschaftliche Methode:**
Experimentelle Datenerhebung und vergleichende Analyse von System- und Modellparametern bei KI-gestützter Bildgenerierung.

---

## Datenursprung 

* **Autor:** Die Daten wurden vollständig selbst erhoben und generiert.
* **Drittquellen:** Keine externen Datensätze wurden verwendet.
* **Lizenz:** Apache License 2.0

  * Log- und Messdaten: CC BY 4.0 (sofern nicht anders angegeben)
  * Bilddaten: Nutzung ausschließlich zu wissenschaftlichen Zwecken im Rahmen der Abschlussarbeit

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

**Ordnerstruktur (Beispiel):**

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



