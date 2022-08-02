from django.utils.translation import gettext_lazy as _
from django.shortcuts import render

VIEW_ERRORS = {
    404:{"title": _("Page not found"),
         "content": _("The page you are looking for does not exist."),},
    500:{"title": _("Internal server error"),
         "content":_("An error has occurred")},
    403:{"title": _("Permission denied"),
         "content":_("You do not have permission to access this page")},
    400:{"title": _("Bad request"),
         "content": _("The request is invalid")},    
}

def error_view_handler(request, exception, status):
    return render(request, template_name='errors.html',
                  status = status,
                  context={'error': exception,
                           'status': status,
                           'title': VIEW_ERRORS[status]["title"],
                           'content': VIEW_ERRORS[status]["content"]})
    
def error_404_view_handler(request, exception=None):
    return error_view_handler(request, exception, 404)

def error_500_view_handler(request, exception=None):
    return error_view_handler(request, exception, 500)

def error_403_view_handler(request, exception=None):
    return error_view_handler(request, exception, 403)

def error_400_view_handler(request, exception=None):
    return error_view_handler(request, exception, 400)
