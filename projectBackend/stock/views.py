import random
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import MyTokenObtainPairSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework import status
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from django.contrib.auth.models import User
from rest_framework_mongoengine import viewsets
from rest_framework.decorators import api_view
from .serializers import WatchListSerializer
from .models import WatchList


class MyObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = MyTokenObtainPairSerializer


class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer


class LOGIN(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        content = {'message': 'Welcome'}
        return Response(content)


class WatchListViewSet(viewsets.ModelViewSet):
    lookup_field = 'id'
    serializer_class = WatchListSerializer

    def get_queryset(self):
        return WatchList.objects.all()

    @api_view(['GET'])
    def get_object(self):
        user = User.objects.get(username=self.user)
        print(user)
        userId = user.id
        lists = WatchList.objects.filter(user=user)
        serializer = WatchListSerializer(lists, many=True)
        return Response(serializer.data)

    @api_view(['POST'])
    def add_symbol(self):
        serializer = WatchListSerializer(data=self.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    @api_view(['DELETE'])
    def del_symbol(self):
        item = self.data['watchlist']
        user = self.data['user']
        # user = User.objects.get(username=self.user)
        lists = WatchList.objects.filter(user=user, watchlist=item)
        lists.delete()
        return Response("Deleted")


class PriceDepth(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        depthScalper = []
        priceDepth = {'buy': [], 'sell': []}
        min = float(request.data['price']) - 5.5
        max = float(request.data['price'])

        curr = roundHalf(max)

        for i in range(0, 15):
            curr = curr - 0.05
            newEntry = {
                'price': round(curr, 2),
                'quantity': 0
            }
            depthScalper.append(newEntry)

        curr = roundHalf(max)

        for i in range(0, 15):
            newEntry = {
                'price': round(curr, 2),
                'quantity': 0
            }
            depthScalper.append(newEntry)
            curr = curr + 0.05
        iterator = 0
        while iterator < 5:
            index = random.randrange(0, 15)
            quantity = random.randrange(0, 1000)
            currDep = depthScalper[index]
            pb = priceDepth['buy']
            collision = list(filter(lambda pb: pb['price'] == currDep['price'], pb))
            if len(collision) > 0:
                continue
            currDep['quantity'] = quantity
            priceDepth['buy'].append(currDep)
            iterator = iterator + 1

        iterator = 0
        while iterator < 5:
            index = random.randrange(15, 29)
            quantity = random.randrange(0, 1000)
            currDep = depthScalper[index]
            ps = priceDepth['sell']
            collision = list(filter(lambda ps: ps['price'] == currDep['price'], ps))
            if len(collision) > 0:
                continue
            currDep['quantity'] = quantity
            priceDepth['sell'].append(currDep)
            iterator = iterator + 1
        return Response(priceDepth)


def roundHalf(num):
    return round(num * 2) / 2
