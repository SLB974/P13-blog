$(document).ready(function() {
    enlight_menu();
    $(".darkon").click(darkon_click);
    $(".darkoff").click(darkoff_click);
    dark_mode_check();
})

function enlight_menu() {
        var path=window.location.pathname;

        switch(path){

            case '/home/':
                $(".home").addClass("enlighted");
                break;

            case '/home/category/':
                $(".category").addClass("enlighted");
                break;

            case '/home/article/':
                $(".article").addClass("enlighted");
                break;

            case '/home/tutorial/':
                $(".tuto").addClass("enlighted");
                break;

            case '/home/oops/':
                $(".oops").addClass("enlighted");
                break;
        }

}

function darkon_click() {
    localStorage.setItem("data-theme", "dark");
    $(".darkon").css("display", "none");
    $(".darkoff").css("display", "block");
    dark_mode_check();
};

function darkoff_click() {
    localStorage.removeItem("data-theme");
    $(".darkoff").css("display", "none");
    $(".darkon").css("display", "block");
    dark_mode_check();
};

function dark_mode_check() {

if (localStorage.getItem("data-theme") == "dark") {
    document.body.setAttribute("data-theme", "dark");
} else {
    document.body.removeAttribute("data-theme");
}
}