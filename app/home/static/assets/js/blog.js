function enlight_menu() {
    /* var menu = document.getElementById('home');
        menu.classList.add('enlighted'); */
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

$(document).ready(function() {
    enlight_menu();
})