from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import User
from rest.serialisers import UserSerializer


class UserManager(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'status': 'ok'}, status=201)
        return Response({'status': 'Bad data!'}, status=400)

    @staticmethod
    def update(request):
        data = request.data
        serializer = UserSerializer(data)
        return Response(serializer.data, status=200)