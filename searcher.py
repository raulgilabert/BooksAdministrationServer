import tornado.web

import sqlite3
import json


class Searcher(tornado.web.RequestHandler):
    def get(self):
        base = sqlite3.connect("base.db")
        cursor = base.cursor()

        cursor.execute("SELECT * FROM data")

        data = cursor.fetchall()

        dataToSend = json.dumps(data)

        print(dataToSend)

        self.write(dataToSend)
