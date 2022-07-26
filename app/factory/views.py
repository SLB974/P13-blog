"""factory upload management views"""

from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect, render

from factory.core.import_process import ImportProcessor


def upload_md_file(request):
    """Upload a file"""
    if request.method == 'POST':
        uploaded_file = request.FILES['md_file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        path = fs.path(name)
        processor = ImportProcessor(path)
        html_file = processor.process()
        return render(request, html_file)
    return render(request, 'factory/md_upload.html')


