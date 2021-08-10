from django.test import TestCase
from content.models import UserProfile
from django.contrib.auth import get_user_model
# Create your tests here.
class ContentTests(TestCase):
    def test_user_profile(self):
        db = get_user_model()
        tuser = db.objects.create_user(
            'testuser@user.com', 'username', 'firstname', 'password')
        testprofile = UserProfile.objects.create(user = tuser , image ='', teacher ='False')
        self.assertEqual(str(testprofile), "testuser@user.com")
