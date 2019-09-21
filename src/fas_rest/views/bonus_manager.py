from rest_framework.response import Response
from rest_framework.views import APIView

from rest.models import Bonus
from fas_rest.serialisers import BonusSerializer


class BonusManager(APIView):
    @staticmethod
    def post(request):
        data = request.data
        serializer = BonusSerializer(data=data)
        print(serializer.is_valid())
        print(serializer.errors)
        #serializer.create(serializer.validated_data)

        return Response({'status': 'ok'}, status=200)

    @staticmethod
    def update(request):
        data = request.data
        serializer = BonusSerializer(data)
        bonus = Bonus.objects.get(bonus_code=serializer.validated_data.bonus_code)
        serializer.update(bonus, serializer.validated_data)

        return Response({'status': 'ok'}, status=200)