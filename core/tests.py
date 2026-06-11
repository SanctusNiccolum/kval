from django.test import Client, TestCase

class TestPing(TestCase):
    def test(self):
        client = Client()
        response = client.get('/ping/')
        self.assertEqual(response.status_code, 200)
