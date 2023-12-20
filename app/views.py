from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import user
@api_view()
def hello_world(request):
    return Response({"message": "Hello, world!"})

@api_view(["POST"])
def create_user(request):
    data = request.data
    if len(data["username"]) <= 18 and len(data["username"]) <= 10:
        new_user = user(username = data["username"], password = data["password"])
        new_user.save()
        return Response({"message": "user created", "content": {"username": data["username"], "password": data["password"]}})
    return Response({"message": "failed to create user"})