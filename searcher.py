import tornado.websocket

import sqlite3
import json


class Searcher(tornado.websocket.WebSocketHandler):
    def open(self):
        print("Open")

        self.filters = {
            "Title": "",
            "Author": "",
            "Category": "",
            "Language": "",
            "Format": ""
        }

    def on_message(self, message):
        if message == "JSON Request":
            self.firstSendJSON(self.filters)

        elif message == "next":
            self.sendJSON()

        elif message[:6] == "Filter":
            dataToFilter = message[7:]

            category = ""
            i = 7

            for char in dataToFilter:
                i += 1
                if char == " ":
                    break
                else:
                    category += char

            filterData = message[i:]

            self.filters[category] = filterData

            print(category + " with data " + filterData)

            self.firstSendJSON(self.filters)

    def on_close(self):
        print("Close")

    def firstSendJSON(self, filters):
        print("Received JSON request")

        base = sqlite3.connect("base.db")
        cursor = base.cursor()

        if filters["Title"] != "":
            cursor.execute("SELECT * FROM data WHERE Title LIKE '%" + filters["Title"] + "%'")
        else:
            cursor.execute("SELECT * FROM data")

        self.data = cursor.fetchall()
        self.i = 0

        self.sendJSON()

    def sendJSON(self):
        try:
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

        except IndexError:
            self.write_message("close")
            print("exception")
            pass

