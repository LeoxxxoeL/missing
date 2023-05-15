window.onload = function () {
    addtable();
}
$(function () {
    passdate();
});
var itemdata
function passdate() {
    var request_event = $.ajax
        ({
            url: "/passdata",
            type: "GET",
            dataType: 'json',
            success: function (response) {
                console.log(response)
                itemdata = response
                // $('#deviceSN').text(response);
            }, // success
            error: function () {
                console.log("Error!, EventDetect failed");
            } // error

        }); // end of request the events
}
function addtable() {
    var table = document.getElementById("table");
    for (var i = 0; i < itemdata.length; i++) {
        var tr = document.createElement("tr");
        table.appendChild(tr);
        for (var j = 1; j < 7; j++) {
            var xh = document.createElement("td");
            xh.innerHTML = itemdata[i][j];
            tr.appendChild(xh);
        }
    }
}

