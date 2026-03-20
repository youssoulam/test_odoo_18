# -*- coding: utf-8 -*-

from odoo import models, fields


class Auteurs(models.Model):
    _name = "gestion.bibliotheque.auteur"
    _description = "Liste des auteurs"

    name = fields.Char(string="NOM et Prénom", required=True)
    sexe = fields.Selection(
        [("male", "Masculin"), ("female", "Féminin")], string="Sexe"
    )
    livre_ids = fields.One2many(
        string="Liste des livres",
        comodel_name="gestion.bibliotheque.livre",
        inverse_name="auteur_id",
        required=False,
    )
