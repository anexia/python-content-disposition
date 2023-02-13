from django.http import FileResponse
from rest_framework import viewsets
from rest_framework.decorators import action

from content_disposition import rfc5987_content_disposition

from .models import Photo
from .serializers import PhotoSerializer


class PhotoViewSet(viewsets.ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

    @action(
        detail=True,
        methods=["get"],
        http_method_names=["get"],
        url_path=r"download",
    )
    def download_route(self, request, pk=None):
        """
        Assuming that self.get_object() returns a model defining
        'name = models.CharField(...)', 'file = models.FileField(...)' and 'mime = models.CharField(...)'
        whereas 'mime' represents the correct mime_type related to 'file'
        """
        instance = self.get_object()

        response = FileResponse(
            open(instance.file.path, "rb").read(),
            content_type=instance.mime,
        )
        response["Content-Disposition"] = rfc5987_content_disposition(instance.file.name)

        return response
