from django.test import TestCase

class BasicTest(TestCase):

    def test_1_equal_1(self):
        self.assertEqual(1, 1)
