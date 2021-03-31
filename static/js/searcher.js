function changedFile(value) {
    alert('Selected file: ' + value);
};

// JSON listener and rows writer
function jsonListener() {
    // Converts string output to array
    data = JSON.parse(this.responseText);
    
    i = 0;

    // Loop viewing all the data received from the server
    data.forEach(element => {
        var x = document.getElementById("searcherTable").rows.length;

        // Get table
        var tableRef = document.getElementById("searcherTable");

        // Create row
        var newRow = tableRef.insertRow(x);

        // Create cells for the data
        var cellTitle = newRow.insertCell(0);
        var cellAuthor = newRow.insertCell(1);
        var cellCategory = newRow.insertCell(2);
        var cellLanguage = newRow.insertCell(3);
        var cellFileFormat = newRow.insertCell(4);
        var cellDownload = newRow.insertCell(5);

        // Create text to show in cells
        var textTitle = document.createTextNode(element[0]);
        var textAuthor = document.createTextNode(element[1]);
        var textCategory = document.createTextNode(element[2]);
        var textLanguage = document.createTextNode(element[3]);
        var textFileFormat = document.createTextNode(element[4]);

        // Create download button
        var textDownload = '<a href="/files/' + element[5] + '" download>Download</a>';
        var buttonDownload = document.createElement("BUTTON");
        buttonDownload.innerHTML = textDownload;

        buttonDownload.className = "buttonDownload";

        // Set text to cells
        cellTitle.appendChild(textTitle);
        cellAuthor.appendChild(textAuthor);
        cellCategory.appendChild(textCategory);
        cellLanguage.appendChild(textLanguage);
        cellFileFormat.appendChild(textFileFormat);
        cellDownload.appendChild(buttonDownload);

        // Set style to cells
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
    });

    // Create last row of cells 
    var x = document.getElementById("searcherTable").rows.length;

    var tableRef = document.getElementById("searcherTable");
    var newBlankRow = tableRef.insertRow(x);

    for (let i = 0; i < 6; i++) {
        var cell = newBlankRow.insertCell(i);
        cell.className = "endTable";
    }
}

// Request data without filters to server
httpRquest = new XMLHttpRequest();
httpRquest.addEventListener("load", jsonListener);
httpRquest.open("GET", "./searcher");
httpRquest.send();

