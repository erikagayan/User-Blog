from django.http import JsonResponse
from django.views import View
import re
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

email_verification_results = {}


@method_decorator(csrf_exempt, name="dispatch")
class EmailVerificationView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        email = data.get("email")

        if email is None:
            return JsonResponse({"error": "No email provided"}, status=400)

        is_valid = re.match(r"[^@]+@[^@]+\.[^@]+", email) is not None

        email_verification_results[email] = is_valid
        return JsonResponse({"email": email, "is_valid": is_valid})


class EmailResultView(View):
    def get(self, request, *args, **kwargs):
        email = request.GET.get("email")
        result = email_verification_results.get(email)
        if result is None:
            return JsonResponse({"error": "Email not found"}, status=404)
        return JsonResponse({"email": email, "is_valid": result})
