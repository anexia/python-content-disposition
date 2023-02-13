from django.apps import apps
from django.conf import settings
from django.test import SimpleTestCase
from testapp.models import Photo


class TestSetup(SimpleTestCase):
    def test_models(self):
        self.assertIs(apps.get_model("testapp", "Photo"), Photo)
