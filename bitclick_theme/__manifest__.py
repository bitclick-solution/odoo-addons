# Copyright 2026 Bitclick Solutions S.L.U.
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl).
{
    "name": "Bitclick: tema de marca",
    "summary": "Colores, tipografía y forma del sistema de diseño 2026 de Bitclick en el backend y el login",
    "version": "19.0.1.0.0",
    "category": "Hidden/Tools",
    "author": "Bitclick Solutions S.L.U.",
    "website": "https://bitclick.solutions",
    "license": "LGPL-3",
    "depends": ["web"],
    "assets": {
        # Antes que las de Odoo: las suyas son !default y respetan las nuestras.
        "web._assets_primary_variables": [
            ("prepend", "bitclick_theme/static/src/scss/primary_variables.scss"),
        ],
        "web.assets_backend": [
            "bitclick_theme/static/src/scss/fonts.scss",
            "bitclick_theme/static/src/scss/backend.scss",
        ],
        "web.assets_frontend": [
            "bitclick_theme/static/src/scss/fonts.scss",
            "bitclick_theme/static/src/scss/login.scss",
        ],
    },
    "installable": True,
}
