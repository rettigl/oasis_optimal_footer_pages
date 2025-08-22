import os

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from nomad.config import config

#myapi_entry_point = config.get_plugin_entry_point('oasis_optimal_footer_pages.apis:oasis_optimal_footer_pages')

app = FastAPI()

static_folder = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))
app.mount("/static", StaticFiles(directory=static_folder), name="static")