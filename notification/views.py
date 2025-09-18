from django.shortcuts import render
from django.http import JsonResponse, HttpRequest
from django.views.decorators.http import require_POST
from django.views.decorators.csrf import csrf_exempt
from .service import NotificationServer
import json

@csrf_exempt
@require_POST
def send_notification(request: HttpRequest):
    try:
        data: dict = json.loads(request.body)
        user_contact = data.get("user_contact", {})
        message = data.get("message", "")
        
        if not user_contact or not message:
            return JsonResponse(
                {
                    "detail": "Недостаточно данных."
                },
                status=400
            )
            
        notifier = NotificationServer(user_contact)
        
        success = notifier.send(message)
        
        if success:
            return JsonResponse(
                {
                    "detail": "Данные успешно отправлены"
                }
            )
        else:
            return JsonResponse(
                {
                    "detail": "Данные не отправлены"
                },
                status=500
            )
    except json.JSONDecodeError:
        return JsonResponse({"error": "Некорректный запрос"}, status=400)
    
    except Exception as e:
        return JsonResponse({"error": f"Ошибка сервера: {str(e)}"}, status=500)


