import os

from django.core.files import File
from django.test import TestCase
from rest_framework.status import HTTP_200_OK
from testapp.models import Photo


def load_test_image(name):
    directory = os.path.dirname(__file__)
    file = os.path.join(directory, "test_images", name)
    return open(file, "rb")


class TestApi(TestCase):
    def setUp(self):
        super().setUp()

        with load_test_image("TestA.jpg") as file:
            self.photo = Photo.objects.create(name="photo1", mime="image/jpeg")
            self.photo.file.save("TestA.jpg", file)

    def test_download(self):
        """Assert the resulting FileResponse contains the expected Content-Disposition"""
        response = self.client.get(path=f"/api/photo/{self.photo.pk}/download/")
        self.assertEqual(HTTP_200_OK, response.status_code)

        # check response
        self.assertEqual(
            f'inline; filename="{self.photo.file.name}"',
            response.get("Content-Disposition"),
        )
