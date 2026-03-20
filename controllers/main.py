# -*- coding: utf-8 -*-
import json
from odoo import http
from odoo.http import request


def _json_response(payload, status=200):
    return request.make_response(
        json.dumps(payload, ensure_ascii=False),
        headers=[("Content-Type", "application/json")],
        status=status,
    )


class AuteurAPI(http.Controller):
    # GET: liste + détail
    @http.route(
        ["/api/auteurs", "/api/auteurs/<int:auteur_id>"],
        type="http",
        auth="user",
        methods=["GET"],
        csrf=False,
    )
    def get_auteurs(self, auteur_id=None, **params):
        Auteur = request.env["gestion.bibliotheque.auteur"].sudo()

        if auteur_id:
            rec = Auteur.browse(auteur_id)
            if not rec.exists():
                return _json_response({"error": "Auteur introuvable"}, status=404)

            return _json_response(
                {
                    "id": rec.id,
                    "name": rec.name,
                    "sexe": rec.sexe,
                    "livre_ids": rec.livre_ids.ids,
                }
            )

        # liste (optionnel: pagination)
        limit = int(params.get("limit", 50))
        offset = int(params.get("offset", 0))
        auteurs = Auteur.search([], limit=limit, offset=offset, order="id desc")

        return _json_response(
            {
                "count": len(auteurs),
                "results": [
                    {
                        "id": a.id,
                        "name": a.name,
                        "sexe": a.sexe,
                        "livre_ids": a.livre_ids.ids,
                    }
                    for a in auteurs
                ],
            }
        )

    # POST: création
    @http.route("/api/auteurs", type="json", auth="user", methods=["POST"], csrf=False)
    def create_auteur(self, **payload):
        # payload est le body JSON envoyé en type=json
        # Ex: {"name":"Victor Hugo","sexe":"male"}
        if not payload.get("name"):
            return {"error": "Le champ 'name' est obligatoire"}

        Auteur = request.env["gestion.bibliotheque.auteur"].sudo()
        rec = Auteur.create(
            {
                "name": payload.get("name"),
                "sexe": payload.get("sexe"),
            }
        )
        return {"id": rec.id, "name": rec.name, "sexe": rec.sexe}

    # PUT: modification
    @http.route(
        "/api/auteurs/<int:auteur_id>",
        type="json",
        auth="user",
        methods=["PUT"],
        csrf=False,
    )
    def update_auteur(self, auteur_id, **payload):
        Auteur = request.env["gestion.bibliotheque.auteur"].sudo()
        rec = Auteur.browse(auteur_id)
        if not rec.exists():
            return {"error": "Auteur introuvable"}

        vals = {}
        if "name" in payload:
            vals["name"] = payload["name"]
        if "sexe" in payload:
            vals["sexe"] = payload["sexe"]

        rec.write(vals)
        return {"id": rec.id, "name": rec.name, "sexe": rec.sexe}

    # DELETE: suppression
    @http.route(
        "/api/auteurs/<int:auteur_id>",
        type="json",
        auth="user",
        methods=["DELETE"],
        csrf=False,
    )
    def delete_auteur(self, auteur_id, **payload):
        Auteur = request.env["gestion.bibliotheque.auteur"].sudo()
        rec = Auteur.browse(auteur_id)
        if not rec.exists():
            return {"error": "Auteur introuvable"}

        rec.unlink()
        return {"success": True, "deleted_id": auteur_id}
