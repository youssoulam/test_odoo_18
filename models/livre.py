# -*- coding: utf-8 -*-

from odoo import models, fields


class Livres(models.Model):
    _name = "gestion.bibliotheque.livre"
    _description = "Gestion des livres"

    name = fields.Char(string="Titre du livre", required=True)
    isbn = fields.Char(string="Code ISBN", required=True)
    maison_edition = fields.Char(string="Maison d'édition")
    annee_publication = fields.Integer(string="Année de pulication")
    auteur_id = fields.Many2one(
        "gestion.bibliotheque.auteur", string="Liste des auteurs", required=True
    )
