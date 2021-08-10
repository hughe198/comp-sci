from django.test import TestCase
from django.conf import settings
# Create your tests here.
class ContentTests(TestCase):

    def test_debug_mode(self):
        debugsetting = settings.DEBUG
        print(debugsetting)
        self.assertFalse(debugsetting)
        #tests run with debug set to false, to reflect production server.
