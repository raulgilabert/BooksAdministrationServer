import tornado.web
import sqlite3


class Main(tornado.web.RequestHandler):
    def get(self):
        self.render("main.html")

    def post(self):
        file = self.request.files["file"][0]
        filename = file["filename"]

        print("received file " + filename)

        with open("static/uploads/" + filename, "wb") as f:
            f.write(file["body"])

            f.close()

        title = self.get_argument("title")
        author = self.get_argument("author")
        category = self.get_argument("category")
        language = self.get_argument("language")

        dotPos = 0
        i = 0
        for char in filename:
            if char == ".":
                dotPos = i

            i += 1

        fileFormat = filename[dotPos + 1:]

        data = (title, author, language, category, fileFormat, filename)

        print("Inserting data: ", data)

        base = sqlite3.connect("base.db")
        cursor = base.cursor()

        cursor.execute("INSERT INTO data (Title, Author, Language, Category, Format, File) VALUES(?, ?, ?, ?, ?, ?)",
                       data)

        base.commit()

        self.get()
