from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Event


def home(request):
    return render(request, "core/home.html")


class EventView(APIView):
    # GET /events/        - list all event names
    # GET /events/{name}/ - get count for a specific event
    def get(self, request, name=None):
        if name is None:
            names = list(Event.objects.values_list("name", flat=True))
            return Response(names)
        else:
            try:
                event = Event.objects.get(name=name)
                return Response({"name": event.name, "count": event.count})
            except Event.DoesNotExist:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    # PUT /events/{name}/ - create event (error if already exists)
    def put(self, request, name):
        if Event.objects.filter(name=name).exists():
            return Response({"error": "Already exists"}, status=status.HTTP_409_CONFLICT)
        event = Event.objects.create(name=name)
        return Response({"name": event.name, "count": event.count}, status=status.HTTP_201_CREATED)

    # POST /events/{name}/ - increment count (error if doesn't exist)
    def post(self, request, name):
        try:
            event = Event.objects.get(name=name)
            event.count += 1
            event.save()
            return Response({"name": event.name, "count": event.count})
        except Event.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)

    # DELETE /events/{name}/ - delete event
    def delete(self, request, name):
        try:
            Event.objects.get(name=name).delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Event.DoesNotExist:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)