# # myapp/middleware.py

# from django.conf import settings

# class MockIPMiddleware:
#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
#         if settings.DEBUG:
#             request.META['REMOTE_ADDR'] =ip_address # Example IP address for testing
#         response = self.get_response(request)
#         return response
