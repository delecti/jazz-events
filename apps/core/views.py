from .models import Event
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView


def home(request):
    names = Event.objects.values_list("name", flat=True).distinct()
    events = [{"name": n, "count": Event.objects.filter(name=n).count()} for n in names]
    return render(request, "core/home.html", {"events": events})


class EventView(APIView):
    renderer_classes = [JSONRenderer]
    parser_classes = [JSONParser]

    # GET /events/        - list all event names with counts
    # GET /events/{name}/ - get count for a specific event name
    def get(self, request, name=None):
        if name is None:
            names = Event.objects.values_list("name", flat=True).distinct()
            events = [{"name": n, "count": Event.objects.filter(name=n).count()} for n in names]
            return Response(events)
        else:
            count = Event.objects.filter(name=name).count()
            if count == 0:
                return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
            return Response({"name": name, "count": count})

    # PUT /events/{name}/ - create first occurrence of an event name (error if already exists)
    def put(self, request, name):
        if Event.objects.filter(name=name).exists():
            return Response({"error": "Already exists"}, status=status.HTTP_409_CONFLICT)
        Event.objects.create(name=name)
        return Response({"name": name, "count": 1}, status=status.HTTP_201_CREATED)

    # POST /events/{name}/ - add one more occurrence (error if doesn't exist)
    def post(self, request, name):
        if not Event.objects.filter(name=name).exists():
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        Event.objects.create(name=name)
        count = Event.objects.filter(name=name).count()
        return Response({"name": name, "count": count})

    # DELETE /events/{name}/ - delete all occurrences of an event name
    def delete(self, request, name):
        deleted, _ = Event.objects.filter(name=name).delete()
        if deleted == 0:
            return Response({"error": "Not found"}, status=status.HTTP_404_NOT_FOUND)
        return Response(status=status.HTTP_204_NO_CONTENT)