function changedFile(value) {
    alert('Selected file: ' + value);
};

var ws = new WebSocket("ws://localhost:8888/websocket");

var i = 0;

ws.onopen = function() {
    requestJSON();
};

function filter(meh) {
    titleValue = document.getElementById("titleInput").value;
    authorValue = document.getElementById("authorInput").value;
    categoryValue = document.getElementById("categoryInput").value;
    languageValue = document.getElementById("languageInput").value;
    fileClassValue = document.getElementById("fileClassInput").value;

    var ws = new WebSocket("ws://localhost:8888/websocket");

    ws.onopen = function() {
        if (titleValue!="") {
            ws.send("Filter Title " + titleValue)
        }
    };
};

function requestJSON() {
    ws.send("JSON Request");

    ws.onmessage = function(event) {
        receiveData(event);
    };
};

function receiveData(event) {
    if (event.data != "close") {
        var msg = JSON.parse(event.data)

        var x = document.getElementById("searcherTable").rows.length;

        console.log(x);

        var tableRef = document.getElementById("searcherTable");
        var newRow = tableRef.insertRow(x);

        var cellTitle = newRow.insertCell(0);
        var cellAuthor = newRow.insertCell(1);
        var cellCategory = newRow.insertCell(2);
        var cellLanguage = newRow.insertCell(3);
        var cellFileFormat = newRow.insertCell(4);
        var cellDownload = newRow.insertCell(5);

        var textTitle = document.createTextNode(msg["Title"]);
        var textAuthor = document.createTextNode(msg["Author"]);
        var textCategory = document.createTextNode(msg["Category"]);
        var textLanguage = document.createTextNode(msg["Language"]);
        var textFileFormat = document.createTextNode(msg["FileFormat"]);
        var textDownload = '<a href="/files/' + msg["Filename"] + '" download>Download</a>';

        var buttonDownload = document.createElement("BUTTON");
        buttonDownload.innerHTML = textDownload;

        buttonDownload.className = "buttonDownload";

        cellTitle.appendChild(textTitle);
        cellAuthor.appendChild(textAuthor);
        cellCategory.appendChild(textCategory);
        cellLanguage.appendChild(textLanguage);
        cellFileFormat.appendChild(textFileFormat);
        cellDownload.appendChild(buttonDownload);

        cellTitle.className = "left";

        if (i%2 == 0) {
            cellTitle.className = "rowWhite left";
            cellAuthor.className = "rowWhite";
            cellCategory.className = "rowWhite";
            cellLanguage.className = "rowWhite";
            cellFileFormat.className = "rowWhite";
            cellDownload.className = "rowWhite right";
            }
        else {
            cellTitle.className = "rowGray left";
            cellAuthor.className = "rowGray";
            cellCategory.className = "rowGray";
            cellLanguage.className = "rowGray";
            cellFileFormat.className = "rowGray";
            cellDownload.className = "rowGray right";
        };

        ws.send("next");

        ++i
    }

    else {
        ws.close();
        
        var x = document.getElementById("searcherTable").rows.length;

        var tableRef = document.getElementById("searcherTable");
        var newBlankRow = tableRef.insertRow(x);

        for (let i = 0; i < 6; i++) {
            var cell = newBlankRow.insertCell(i);
            cell.className = "endTable";
        }

        i = 0;
    }
}
