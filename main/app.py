import logging
from aiohttp import web
from main.routes import init_routes

logging.basicConfig(level=logging.ERROR, # show only error msgs
                    format='%(asctime)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S')

def init_app(argv=None) -> web.Application:
    app = web.Application()
    logging.basicConfig(level=logging.DEBUG)
    init_routes(app)
    return app


app = init_app()