var input = $(".file_");
var preview = $(".preview");
var button = $("input[type='submit']");

$().ready(function() {
    input.change(change_preview);

    if (preview.text() == "...") {
        button.prop("disabled", true);
    }
    else {
        button.prop("disabled", false);
    }
})

function change_preview() {
    var file = input[0].files[0];
    if (file) {
        preview.text(file.name);
        button.prop("disabled", false);
    }

    else {
        preview.text("...");
        button.prop("disabled", true);
    }
    };
