from rest_framework import status
from rest_framework.reverse import reverse
from rest_framework.test import APITestCase


class EpidemicAPITestCase(APITestCase):
    def setUp(self) -> None:
        self.epidemic_data = {
            "name": "湖北省",
            "province": "湖北省",
            "add_suspect": 1154,
            "cumulative_suspect": 6169,
            "new_diagnosis": 4823,
            "cumulative_diagnosis": 51986,
            "added_death": 116,
            "cumulative_death": 1318,
            "published_at": "2020-02-13",
        }

    def test_get_epidemic_api(self):
        _url = reverse("api:epidemic:index")
        res = self.client.get(_url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_post_a_epidemic_api(self):
        _url = reverse("api:epidemic:index")
        res = self.client.post(_url, data=self.epidemic_data)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertEqual(res.json(), self.epidemic_data)
        res = self.client.post(_url, data=self.epidemic_data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
