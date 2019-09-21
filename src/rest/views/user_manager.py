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
            if serializer.create(serializer.validated_data):
                return Response({'status': 'ok'}, status=201)
            else:
                return Response({'status': 'User exist!'}, status=400)
        return Response({'status': 'Bad data!'}, status=400)

    @staticmethod
    def get(request):
        login = request.headers.get('login')
        password = request.headers.get('password')
        user = User.objects.get(login=login, password=password)

        serializer = UserSerializer(user)
        return Response(serializer.data, status=200)
