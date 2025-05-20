import unittest
import json
from trackerApp import app

class TaskTrackerTest(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_add_task(self):
        response = self.client.post('/tasks', json={'title': 'Test Task'})
        self.assertEqual(response.status_code, 201)

    def test_get_tasks(self):
        response = self.client.get('/tasks')
        self.assertEqual(response.status_code, 200)

    def test_delete_task(self):
        self.client.post('/tasks', json={'title': 'Temp'})
        response = self.client.delete('/tasks/1')
        self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
