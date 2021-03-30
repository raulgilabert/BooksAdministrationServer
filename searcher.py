import tornado.websocket

import sqlite3
import json


class Searcher(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Open")

    def on_message(self, message):
        if message == "JSON Request":
            self.firstSendJSON()

        if message == "next":
            try:
                self.sendJSON()
            except IndexError:
                self.write_message("close")

    def on_close(self):
        print("Close")

    def firstSendJSON(self):
        print("Received JSON request")

        base = sqlite3.connect("base.db")
        cursor = base.cursor()

        cursor.execute("SELECT * FROM data ORDER BY Title ASC")

        self.data = cursor.fetchall()
        self.i = 0

        self.sendJSON()

    def sendJSON(self):
        dat = self.data[self.i]

        JSONToSend = {
            "Title": dat[0],
            "Author": dat[1],
            "Language": dat[2],
            "Category": dat[3],
            "FileFormat": dat[4],
            "Filename": dat[5]
        }

        JSONToSendDumped = json.dumps(JSONToSend)

        self.write_message(JSONToSendDumped)

        self.i += 1
