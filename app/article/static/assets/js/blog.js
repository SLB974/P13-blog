$(document).ready(function() {
    enlight_menu();
    $(".darkon").click(darkon_click);
    $(".darkoff").click(darkoff_click);
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
    $(".darkon").css("display", "none");
    $(".darkoff").css("display", "block");
    document.body.setAttribute("data-theme", "dark");
};

function darkoff_click() {
    $(".darkoff").css("display", "none");
    $(".darkon").css("display", "block");
    document.body.removeAttribute("data-theme");
};