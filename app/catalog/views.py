"""Catalog upload management views"""

from django.core.files.storage import FileSystemStorage
from django.shortcuts import render


def upload_md_file(request):
    """Upload a file"""
    if request.method == 'POST':
        uploaded_file = request.FILES['md_file']
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        url = fs.url(name)
        return render(request, 'catalog/md_upload.html', {'url': url})
    return render(request, 'catalog/md_upload.html')


