from django.http import HttpResponse
from django.shortcuts import render
from .models import ThreeDModel
from django.views.static import serve
from model3DView import settings


def home(request):
    models = ThreeDModel.objects.all()
    context = {
        'models': models
    }
    return render(request, 'home.html', context)


def render_3d_model(request, model_id):
    model = ThreeDModel.objects.get(id=model_id)
    model_file_path = model.file.url

    file_extension = model_file_path.split('.')[-1].lower()

    context = {
        'model_id': model.id,
        'model_file_path': model_file_path,
        'model_name': model.name,
        'file_extension': file_extension
    }

    return render(request, 'model_viewer.html', context)


def serve_3d_model_file(request, model_id):
    model = ThreeDModel.objects.get(id=model_id)
    model_file_path = model.filePath

    return serve(request, model_file_path, document_root=settings.MEDIA_ROOT)
