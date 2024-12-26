from django.http import JsonResponse
from .ai_model import analyze_sentiment

def analyze_text(request):
    text = request.GET.get("text", "")
    if text:
        result = analyze_sentiment(text)
        return JsonResponse(result, safe=False)
    return JsonResponse({"error": "No text provided"}, status=400)

