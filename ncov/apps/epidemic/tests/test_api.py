from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class EpidemicAPITestCase(APITestCase):
    def setUp(self) -> None:
        pass

    def test_get_epidemic_api(self):
        _url = reverse("api:epidemic:index")
        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
