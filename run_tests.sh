#!/bin/bash
set -e

# Installer les dépendances
pip install -r requirements.txt

# Exécuter les tests avec Pytest
pytest
