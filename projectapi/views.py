from django.shortcuts import render


from projects.models import Project
from .serializers import Projectser
from django.http import HttpResponse
from rest_framework import viewsets, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

class ProjectList(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = Projectser
@api_view(['GET', 'PUT', 'DELETE'])
def Project_detail(request, id):
    try:
        projects = Project.objects.get(id=id)
    except projects.DoesNotExist:
        return HttpResponse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Projectser(projects)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = Projectser(projects, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        Projectser.delete()
        return HttpResponse(status=status.HTTP_204_NO_CONTENT)