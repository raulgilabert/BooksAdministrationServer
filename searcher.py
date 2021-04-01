import tornado.web

import sqlite3
import json


class Searcher(tornado.web.RequestHandler):
    def get(self):
        applyFilter = self.get_argument("filter")

        base = sqlite3.connect("base.db")
        cursor = base.cursor()

        if applyFilter == "no":
            cursor.execute("SELECT * FROM data ORDER BY Title ASC")

        else:
            titleFilter = self.get_argument("Title")
            authorFilter = self.get_argument("Author")
            categoryFilter = self.get_argument("Category")
            languageFilter = self.get_argument("Language")
            fileFormatFilter = self.get_argument("Format")

            sqlRequest = "SELECT * FROM data"

            changed = False

            if titleFilter != "None":
                if not changed:
                    sqlRequest += " WHERE"

                sqlRequest += " Title LIKE '%" + titleFilter + "%' AND"
                changed = True

            if authorFilter != "None":
                if not changed:
                    sqlRequest += " WHERE"

                sqlRequest += " Author LIKE '%" + authorFilter + "%' AND"
                changed = True

            if categoryFilter != "None":
                if not changed:
                    sqlRequest += " WHERE"

                sqlRequest += " Category LIKE '%" + categoryFilter + "%' AND"
                changed = True

            if languageFilter != "None":
                if not changed:
                    sqlRequest += " WHERE"

                sqlRequest += " Language LIKE '%" + languageFilter + "%' AND"
                changed = True

            if fileFormatFilter != "None":
                if not changed:
                    sqlRequest += " WHERE"

                sqlRequest += " Format LIKE '%" + fileFormatFilter + "%' AND"
                changed = True

            if changed:
                sqlRequest = sqlRequest[:-3]

            sqlRequest += " ORDER BY Title ASC"

            print(sqlRequest)

            cursor.execute(sqlRequest)

        data = cursor.fetchall()

        dataToSend = json.dumps(data)

        print(dataToSend)

        self.write(dataToSend)
