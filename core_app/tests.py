import unittest
import json
from django.test import TestCase, Client
from django.urls import reverse


class ApiTest(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    # Url of list working
    def test_list(self):
        response = self.client.get(reverse("tasks:list-create-task"))
        self.assertEqual(response.status_code, 200)
        # print(json.dumps(response.json(), indent=2, sort_keys=True))
        self.assertIsInstance(response.json(), list)

    # Creation of an object
    def test_create_task(self):
        data = {
            "day": "2022-08-01",
            "reminder": False,
            "text": "Learn testing"
        }
        res = self.client.post(reverse("tasks:list-create-task"), data=data)
        val = dict(res.json())
        del val["id"]
        # The returned data must be the same as the send data
        self.assertEqual(val, data)
        # The created data must be appear when we call listing url
        listing = self.client.get(reverse("tasks:list-create-task"))
        #print(json.dumps(listing.json(), indent=2, sort_keys=True))
        self.assertIn(res.json(), listing.json())

    def test_create_task_exist(self):
        data = {
            "day": "2022-08-01",
            "reminder": False,
            "text": "Learn testing"
        }
        self.client.post(reverse("tasks:list-create-task"), data=data)
        res2 = self.client.post(reverse("tasks:list-create-task"), data=data)
        self.assertEqual(res2.status_code, 400)

    # Creation of an object
    def test_rud_task(self):
        data = {
            "day": "2022-08-01",
            "reminder": False,
            "text": "Learn testing"
        }
        res = self.client.post(reverse("tasks:list-create-task"), data=data)
        task_id = res.json()['id']

        r_response = self.client.get(reverse("tasks:rud-task", kwargs={"task_id":task_id}))
        
        # data returned is the previous data created
        self.assertEqual(r_response.status_code, 200)
        self.assertEqual(r_response.json(), dict(**data, **{"id":task_id}))
        
        #delete task
        d_response = self.client.delete(
            reverse("tasks:rud-task", kwargs={"task_id": task_id}))
        # no error on the delete
        self.assertEqual(d_response.status_code, 204)
        # try to retrieve again  
        d_response = self.client.get(
            reverse("tasks:rud-task", kwargs={"task_id": task_id}))
        self.assertNotEqual(d_response.status_code, 200)
