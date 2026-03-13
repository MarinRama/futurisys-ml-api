# Standards de développement et d’expérimentation ML

## 1. Objectif
Ce document définit les standards de développement, de versioning, de qualité logicielle
et d’expérimentation ML du projet `futurisys-ml-api`.

## 2. Git et gestion des branches
- `main` : branche stable, prête pour la production
- `feature/<nom-feature>` : développement d’une nouvelle fonctionnalité
- `fix/<nom-fix>` : correction de bug
- les développements se font sur des branches dédiées
- les fusions dans `main` se font via Pull Request

## 3. Conventions de commit
Format recommandé :
- `feat: ...`
- `fix: ...`
- `docs: ...`
- `ci: ...`
- `chore: ...`

Exemples :
- `feat: add FastAPI prediction endpoint`
- `ci: add GitHub Actions workflow`
- `docs: add deployment instructions`

## 4. Qualité du code
- code Python lisible et modulaire
- séparation claire entre API, logique métier, tests et configuration
- pas de secrets ni mots de passe en dur dans le code
- utilisation de variables d’environnement pour la configuration sensible

## 5. Tests
- les tests sont exécutés automatiquement via GitHub Actions
- chaque push et chaque pull request vers `main` déclenchent la CI
- tout code fusionné dans `main` doit passer les tests
- un test minimal doit toujours exister pour garantir le bon fonctionnement du pipeline

## 6. CI/CD
- la CI vérifie l’installation des dépendances et l’exécution des tests
- le déploiement continu s’effectue vers Hugging Face Spaces depuis la branche `main`
- la branche `main` est protégée pour empêcher les merges sans validation

## 7. Gestion des environnements
- `dev` : développement local
- `test` : exécution automatisée dans GitHub Actions
- `prod` : déploiement sur Hugging Face Spaces

Chaque environnement possède sa configuration propre via variables d’environnement.

## 8. Standards d’expérimentation ML
- les expériences doivent être traçables
- la version du modèle déployé doit être identifiable
- les features d’entrée du modèle doivent être documentées
- toute nouvelle version de modèle doit être testée avant déploiement
- les artefacts volumineux doivent être gérés proprement (ex: Git LFS si nécessaire)

## 9. Gestion des secrets
- les secrets GitHub sont stockés dans `Settings > Secrets and variables > Actions`
- les secrets Hugging Face sont stockés dans les réglages du Space
- aucune clé API ou token ne doit être versionné dans le dépôt