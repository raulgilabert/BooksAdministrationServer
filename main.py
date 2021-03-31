import tornado.ioloop
import tornado.web

import os
import sqlite3

import mainWeb
import searcher


class Application(tornado.web.Application):
    def __init__(self):
        base_dir = os.path.dirname(__file__)
        settings = {
            'template_path': os.path.join(base_dir, "templates"),
            'static_path': os.path.join(base_dir, "static"),
            'debug': True,
            "xsrf_cookies": False,
        }

        tornado.web.Application.__init__(self, [
            tornado.web.url(r"/", mainWeb.Main),
            tornado.web.url(r"/searcher", searcher.Searcher),
            tornado.web.url(r"/files/(.*)", tornado.web.StaticFileHandler,
                            {"path": os.path.join(base_dir, "static/uploads")})
        ], **settings)


if __name__ == '__main__':
    base = sqlite3.connect("base.db")
    cursor = base.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS data (Title TEXT, Author TEXT,
                    Language TEXT, Category TEXT, Format TEXT, File TEXT)""")

    try:
        os.mkdir("static/uploads/")
    except FileExistsError:
        pass

    Application().listen(8888)
    tornado.ioloop.IOLoop.instance().start()
