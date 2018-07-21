from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from .models import SourceSite

class StandardFileTestCase(TestCase):
    """Parsing the cpp standard."""

    def setUp(self):
        """Parse this file."""
        self.Souce = SourceSite(website="file://./SourceSites/fixtures/std.html")

    def test_model_can_create_a_bucketlist(self):
        """Test the bucketlist model can create a bucketlist."""
        old_count = Bucketlist.objects.count()
        self.bucketlist.save()
        new_count = Bucketlist.objects.count()
        self.assertNotEqual(old_count, new_count)
