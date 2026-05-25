# Documentation Technique du Modèle de Machine Learning

# 1. Présentation du modèle

## Objectif

L’objectif du projet est de prédire le **risque de départ d’un employé (employee attrition)** à partir de données RH.

Le modèle de Machine Learning permet d’identifier les employés susceptibles de quitter l’entreprise afin de :

- réduire le turnover
- améliorer la rétention des employés
- accompagner les décisions RH
- détecter les signaux faibles de désengagement

Le modèle est exposé via une **API REST FastAPI** permettant une utilisation simple, reproductible et documentée.

---

# 2. Problématique métier

Le turnover employé représente un coût important pour les entreprises :

- coûts de recrutement
- perte de connaissances métier
- baisse de productivité
- temps de formation des nouveaux collaborateurs

L’objectif du modèle est donc de fournir une **probabilité de départ** afin d’aider les équipes RH à anticiper les risques.

---

# 3. Dataset utilisé

## Source

Le modèle repose sur un dataset RH utilisé dans le cadre du projet OpenClassrooms (P3/P4).

## Taille du dataset

- **1470 lignes**
- données structurées RH

## Nature des données

Les données contiennent :

### Informations démographiques

- âge
- genre
- statut marital

### Informations professionnelles

- département
- poste
- expérience
- ancienneté
- promotions

### Informations financières

- revenu mensuel
- augmentation salariale

### Satisfaction employé

- satisfaction environnement
- satisfaction travail
- satisfaction équipe
- équilibre vie professionnelle / personnelle

### Formation et évolution

- formations suivies
- distance domicile-travail
- niveau d’éducation

---

# 4. Variables utilisées par le modèle

Le modèle utilise les variables suivantes :

```text
age
genre
revenu_mensuel
statut_marital
departement
poste
nombre_experiences_precedentes
annee_experience_totale
annees_dans_l_entreprise
annees_dans_le_poste_actuel
satisfaction_employee_environnement
note_evaluation_precedente
satisfaction_employee_nature_travail
satisfaction_employee_equipe
satisfaction_employee_equilibre_pro_perso
note_evaluation_actuelle
heure_supplementaires
augementation_salaire_precedente
nombre_participation_pee
nb_formations_suivies
distance_domicile_travail
niveau_education
domaine_etude
frequence_deplacement
annees_depuis_la_derniere_promotion
annes_sous_responsable_actuel
```

Ces variables correspondent aux colonnes réellement attendues par le pipeline Machine Learning.

---

# 5. Architecture globale du système

Le flux complet de traitement est le suivant :

```text
Client
   ↓
API FastAPI
   ↓
Validation des données (Pydantic)
   ↓
Enregistrement PostgreSQL
   ↓
Chargement du modèle ML
   ↓
Prétraitement des données
   ↓
Prédiction
   ↓
Réponse API
```

---

# 6. Architecture du pipeline Machine Learning

Le modèle repose sur un pipeline Scikit-learn permettant d’automatiser les étapes de traitement des données.

Pipeline logique :

```text
Données d'entrée
      ↓
Imputation des valeurs manquantes
      ↓
Normalisation des variables numériques
      ↓
Encodage One-Hot des variables catégorielles
      ↓
Régression Logistique
      ↓
Prédiction
```

---

# 7. Prétraitement des données

Avant apprentissage et prédiction, les données passent par plusieurs transformations.

## Variables numériques

Les variables numériques sont :

- imputées en cas de valeurs manquantes
- standardisées

Prétraitements utilisés :

- `SimpleImputer(strategy="median")`
- `StandardScaler()`

---

## Variables catégorielles

Les variables catégorielles sont :

- imputées
- encodées

Prétraitements utilisés :

- `SimpleImputer(strategy="most_frequent")`
- `OneHotEncoder()`

---

# 8. Modèle utilisé

Le modèle utilisé est :

```python
LogisticRegression
```

## Pourquoi ce modèle ?

La régression logistique a été choisie pour plusieurs raisons :

### Interprétabilité

Le modèle reste relativement simple à expliquer et interpréter.

### Performance

Il fonctionne efficacement sur des datasets tabulaires structurés.

### Rapidité

Temps d’entraînement et de prédiction rapides.

### Probabilité de prédiction

Le modèle permet d’obtenir :

- une classe prédite
- une probabilité associée

Exemple :

```json
{
  "prediction": 1,
  "probability": 0.81
}
```

---

# 9. Performance du modèle

Les performances doivent être évaluées après entraînement.

Exemple de métriques attendues :

| Métrique | Valeur |
|----------|--------|
| Accuracy | XX % |
| Precision | XX % |
| Recall | XX % |
| F1-score | XX % |
| ROC-AUC | XX % |

Ces métriques permettent d’évaluer :

- la robustesse du modèle
- sa capacité de généralisation
- son efficacité métier

---

# 10. API de prédiction

Le modèle est exposé via FastAPI.

Endpoint principal :

```http
POST /predict
```

Exemple de requête :

```json
{
  "age": 26,
  "genre": "M",
  "revenu_mensuel": 2000,
  "statut_marital": "Célibataire",
  "departement": "Consulting",
  "poste": "Consultant",
  "nombre_experiences_precedentes": 2,
  "annee_experience_totale": 4,
  "annees_dans_l_entreprise": 1,
  "annees_dans_le_poste_actuel": 2,
  "satisfaction_employee_environnement": 3,
  "note_evaluation_precedente": 4,
  "satisfaction_employee_nature_travail": 3,
  "satisfaction_employee_equipe": 4,
  "satisfaction_employee_equilibre_pro_perso": 3,
  "note_evaluation_actuelle": 4,
  "heure_supplementaires": "Oui",
  "augementation_salaire_precedente": "11 %",
  "nombre_participation_pee": 1,
  "nb_formations_suivies": 3,
  "distance_domicile_travail": 12,
  "niveau_education": 3,
  "domaine_etude": "Infra & Cloud",
  "frequence_deplacement": "Occasionnel",
  "annees_depuis_la_derniere_promotion": 1,
  "annes_sous_responsable_actuel": 2
}
```

Exemple de réponse :

```json
{
  "prediction": 0,
  "probability": 0.12,
  "interpretation": "Faible risque d’attrition"
}
```

Documentation interactive :

```text
http://localhost:8000/docs
```

---

# 11. Validation des données

La validation est assurée par **Pydantic**.

Elle garantit :

- présence des champs requis
- conformité des types
- réduction des erreurs d’exécution

Exemple d’erreur :

```json
{
  "detail": "validation error"
}
```

HTTP :

```text
422 Unprocessable Entity
```

---

# 12. Traçabilité via PostgreSQL

Toutes les interactions avec le modèle transitent par PostgreSQL.

Les objectifs sont :

- enregistrer les inputs
- enregistrer les outputs
- assurer la traçabilité des échanges
- faciliter l’audit du modèle

Les tables permettent notamment :

- d’analyser les prédictions produites
- de reproduire les traitements
- de surveiller le comportement du modèle

---

# 13. Tests et fiabilité

Le projet inclut des tests unitaires et fonctionnels.

Résultats actuels :

- **13 tests passés**
- **97 % de couverture**

Les tests couvrent :

### API

- `/`
- `/health`
- `/predict`

### Validation

- payload invalide
- payload incomplet
- JSON vide

### Erreurs HTTP

- `404`
- `405`
- `422`

### Modèle

- logique de prédiction
- cohérence des réponses

### Performance

- temps de réponse API inférieur au seuil défini

---

# 14. Maintenance du modèle

Le protocole recommandé de mise à jour est :

## Étape 1 — Réentraîner le modèle

Réentraîner le modèle sur un dataset mis à jour.

---

## Étape 2 — Remplacer le modèle

Remplacer :

```text
models/attrition_model.joblib
```

---

## Étape 3 — Vérifier les performances

Contrôler :

- Accuracy
- Precision
- Recall
- F1-score
- ROC-AUC

---

## Étape 4 — Vérifier les tests

Exécuter :

```bash
pytest
```

---

## Étape 5 — Vérifier la couverture

```bash
pytest --cov=app --cov-report=html
```

Objectif recommandé :

> couverture supérieure à 90 %

---

## Étape 6 — Déploiement

Pousser les changements sur GitHub.

La CI/CD déclenche :

- exécution automatique des tests
- validation du code
- déploiement Hugging Face

---

# 15. Limites actuelles

Le projet présente certaines limites :

- absence de monitoring du drift
- pas de versioning avancé des modèles
- pas d’authentification API
- absence de monitoring métier

---

# 16. Améliorations futures

Les évolutions envisagées :

- ajout de Docker
- monitoring des performances du modèle
- versioning des modèles
- authentification API
- suivi des métriques de production
- monitoring temps réel