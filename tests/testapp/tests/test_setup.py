from django.apps import apps
from django.conf import settings
from django.test import SimpleTestCase
from testapp.models import Photo


class TestSetup(SimpleTestCase):
    def test_installed_apps(self):
        self.assertIn("content_disposition", settings.INSTALLED_APPS)

    def test_models(self):
        self.assertIs(apps.get_model("testapp", "Photo"), Photo)
