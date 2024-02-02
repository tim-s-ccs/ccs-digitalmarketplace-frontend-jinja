import os
import re
from datetime import datetime

from typing import Any

from flask import Flask, render_template_string, render_template, request, Blueprint
from jinja2 import ChoiceLoader, PackageLoader, FileSystemLoader, PrefixLoader

from dmutils.external import external as external_blueprint
from dmutils.formats import datetimeformat


def parse_document_upload_time(data):
    match = re.search(r"(\d{4}-\d{2}-\d{2}-\d{2}\d{2})\..{2,3}$", data)
    if match:
        return datetime.strptime(match.group(1), "%Y-%m-%d-%H%M")


def create_app():
    app = Flask(__name__)

    app.jinja_loader = ChoiceLoader(
        [
            PrefixLoader(
                {
                    "govuk_frontend_jinja": PackageLoader("govuk_frontend_jinja"),
                    "digitalmarketplace_frontend_jinja": FileSystemLoader(
                        searchpath=os.path.join(
                            os.path.dirname(__file__),
                            "../digitalmarketplace_frontend_jinja/templates"
                        )
                    )
                }
            ),
            FileSystemLoader(
                searchpath=os.path.join(
                    os.path.dirname(__file__),
                    "templates"
                )
            )
        ]
    )

    # For the urls in the header and footer
    app.register_blueprint(external_blueprint)

    # Filters for some of the components
    app.add_template_filter(datetimeformat)
    app.add_template_filter(parse_document_upload_time)

    main = Blueprint('main', __name__)

    @main.get("/")
    def index() -> str:
        return "Hello there"

    app.register_blueprint(main)

    @app.post("/component/<string:component>")
    def component(component: str) -> Any:
        data: Any = request.get_json()
        # Render the component using the data provided
        # component is the hyphenated component name e.g. character-count
        # data['macro_name'] is the camelcased name e.g. CharacterCount
        # data['params] are the params that will be passed to the macro
        # Returns an html response that is just the template in question - no wrapping <html>, <body> elements etc
        return render_template_string(
            f"""
            {{% from "digitalmarketplace_frontend_jinja/components/{component}/macro.html" import digitalmarketplace{data['macro_name']} %}}
            {{{{ digitalmarketplace{data['macro_name']}({data["params"]}) }}}}
            """
        )

    @app.post("/layout/<string:layout>")
    def layout(layout: str) -> Any:
        data: Any = request.get_json()
        # Render the layout template using the data provided
        return render_template(f"digitalmarketplace_frontend_jinja/layouts/{layout}.html", **data.get('params', {}))

    @app.post("/error/<string:error>")
    def error_page(error: str) -> Any:
        data: Any = request.get_json()
        # Render the error template using the data provided
        return render_template(f"digitalmarketplace_frontend_jinja/errors/{error}.html", **data.get('params', {}))

    return app
