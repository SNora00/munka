function formatName() {
    var inputElem = document.getElementById('nevInput');
    var inputValue = inputElem.value;

    var formattedName = inputValue.replace(/(^|\s)\S/g, function (match) {
        return match.toUpperCase();
    });

    inputElem.value = formattedName;
}
