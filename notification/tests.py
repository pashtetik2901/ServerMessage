from django.test import TestCase, Client
from unittest.mock import patch, Mock
from notification.service import NotificationServer


class SendNotification(TestCase):
    def setUp(self):
        self.client = Client()
        
    @patch("notification.service.NotificationServer.send")
    def test_send_success(self, mock_send: Mock):
        mock_send.return_value = True
        
        response = self.client.post(
            "/send-notification/", 
            data='{"user_contact": {"email": "user@example.com"}, "message": "Hello"}',
            content_type="application/json",
        )
        
        self.assertEqual(response.status_code, 200)
        self.assertIn("Данные успешно отправлены", response.json().get("detail", ""))
        
    @patch("notification.service.NotificationServer.send")
    def test_send_unluck(self, mock_send: Mock):
        mock_send.return_value = False
        
        response = self.client.post(
            "/send-notification/", 
            data='{"user_contact": {"email": "user@example.com"}, "message": "Hello"}',
            content_type="application/json",
        )
        
        self.assertEqual(response.status_code, 500)
        self.assertIn("Данные не отправлены", response.json().get("detail", ""))
        
    def test_send_wrong_json(self):
        response = self.client.post(
            "/send-notification/", 
            data='Bad_ample.com"}, "message": "Hello"}',
            content_type="application/json",
        )
        
        self.assertEqual(response.status_code, 400)
        self.assertIn("Некорректный запрос", response.json().get("error", ""))
        
    def test_send_fail(self):
        response = self.client.post(
            "/send-notification/", 
            data='{"message": "Hello"}',
            content_type="application/json",
        )
        
        self.assertEqual(response.status_code, 400)
        self.assertIn("Недостаточно данных.", response.json().get("detail", ""))
        
        
