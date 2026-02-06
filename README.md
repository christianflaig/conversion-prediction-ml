# Conversion Prediction with Machine Learning

## Problem
Ziel dieses Projekts ist es, vorherzusagen, ob ein Website-Besucher
mit hoher Wahrscheinlichkeit einen Kauf tätigt.

## Data
Da keine echten Nutzerdaten verfügbar waren, wurde ein synthetischer
Datensatz mit 10.000 Beobachtungen erstellt.
Die Features repräsentieren typische Nutzerverhaltensdaten:
- Age
- Time on site
- Pages visited
- Returning user

## Model
Als Modell wurde eine logistische Regression verwendet, da sie
probabilistische Vorhersagen ermöglicht und gut interpretierbar ist.

## Evaluation
Das Modell wurde mit Accuracy, Precision, Recall und F1-Score bewertet.
Der Fokus lag auf Recall, da verpasste Käufer höhere Kosten verursachen
als falsche Ansprachen.

## Structure
- data.py: Datengenerierung
- model.py: Training & Prediction
- evaluation.py: Modellbewertung
- main.py: Orchestrierung

## Notes
Dieses Projekt dient als Lern- und Portfolio-Projekt und legt den Fokus
auf saubere Struktur, Nachvollziehbarkeit und realistische Evaluation.