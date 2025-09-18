from typing import Optional
import logging

logger = logging.getLogger(__name__)

class NotificationServer:
    def __init__(self, user_contact: dict[str, str]):
        """
        user_contact = {
            "phone": "user_number",
            "email": "email_address",
            "telegramm": "user_telegram"
        }
        Словарь, содержащий контакты пользовател
        """
        self.user_contact = user_contact
        
    def send_email(self, message: str) -> bool:
        try:
            #Здесь должен быть код отправки сообщения по email
            #Например какой-нибудь SMPT сервер
            logger.info("Отправка сообщения по Email")
            return True
        except Exception as err:
            logger.error(f"Ошибка отправки сообщения по Email - {err}")
            return False  
        
    def send_sms(self, message: str) -> bool:
        try:
            #Здесь должен быть код отправки сообщения по SMS
            logger.info("Отправка сообщения по SMS")
            return True
        except Exception as err:
            logger.error(f"Ошибка отправки сообщения по SMS - {err}")
            return False  
        
    def send_telegram(self, message: str) -> bool:
        try:
            #Здесь должен быть код отправки сообщения по Telegram
            logger.info("Отправка сообщения по Telegram")
            return True
        except Exception as err:
            logger.error(f"Ошибка отправки сообщения по Telegram - {err}")
            return False        
        
    def send(self, message: str) -> bool:
        """Общая функция для отправки сообщения 

        Args:
            message (str): Сообщение, которое необходимо отправить
        """
        
        if self.send_email(message):
            logger.info("Сообщение успешно отправлено по Email")
            return True
        logger.warning("Не удалось отправить по Email, попытка отправки по SMS...")
        if self.send_sms(message):
            logger.info("Сообщение успешно отправлено по SMS")
            return True
        logger.warning("Не удалось отправить по SMS, попытка отправки по Telegram...")
        if self.send_telegram(message):
            logger.info("Сообщение успешно отправлено по Telegramm")
            return True
        logger.error("Не удалось отправить сообщение!")
        return False
        
            
        