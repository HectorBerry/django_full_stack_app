from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from base.models import Room, Topic
from .serializers import RoomSerializer, TopicSerializer

@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET /api',
        'GET, POST /api/rooms',
        'GET /api/rooms/:id',
        'POST /api/rooms/create/',
        'GET /api/rooms/delete/:id'
    ]
    return Response(routes)

@api_view(['GET', 'POST'])
def getRooms(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getRoom(request, pk):
    room = Room.objects.get(id=int(pk))
    serializer = RoomSerializer(room, many=False)
    return Response(serializer.data)
    
@api_view(['POST'])
def createTopic(request):
    if request.method == 'POST':
        serializer = TopicSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_405_NOT_ALLOWED)

@api_view(['POST'])
def createNewRoom(request):
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    return Response(serializer.errors, status=status.HTTP_405_NOT_ALLOWED)



@api_view(['GET'])
def deleteRoom(request, pk):
    room = Room.objects.get(id=int(pk))
    if request.method == 'GET':
        room.delete()
        return Response(status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)