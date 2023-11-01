from main.controller import test, screenshot, getHtml, selenium_screenshot, selenium_console_command


def init_routes(app):
    app.router.add_post('/test', test)
    app.router.add_post('/screenshot', screenshot)
    app.router.add_post('/getHtml', getHtml)

    app.router.add_post('/selenium_screenshot', selenium_screenshot)
    app.router.add_post('/selenium_console_command', selenium_console_command)