# -*- coding: utf-8 -*-

{
    "name": "Gestion Bibliothèque",
    "sequence": -1000,
    "version": "18.0.1.0.0",
    "category": "TP",
    "summary": "TP1 Module ERP Odoo Gestion Bibliothèque",
    "description": """ L'objectif principal du module est de créer une application
    permettant de gérer mes bibliothèques dans les universités au Sénégal.
    1. Gestion des Livres 
    2. Gestion des Auteurs 
    3. Gestion des Exemplaires
    """,
    "author": "Youssoupha LAM",
    "company": "CRD 2026",
    "maintainer": "Equipe IT CRD 2026",
    "website": "https://uadb.edu.sn/",
    "depends": ["base", "website"],
    "data": [
        "security/ir.model.access.csv",
        "views/auteur.xml",
        "views/livre.xml",
        "views/menu.xml",
    ],
    # "images": ["static/description/banner.jpg"],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": True,
}
