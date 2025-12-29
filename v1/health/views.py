from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db import connections
from django.db.utils import OperationalError
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class HealthView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        return Response({"status": "ok"}, status=status.HTTP_200_OK)


class ReadyzView(APIView):
    authentication_classes = []
    permission_classes = []

    def get(self, request):
        try:
            connections["default"].cursor()
        except OperationalError:
            return Response({"status": "db_down"}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

        return Response({"status": "ready"}, status=status.HTTP_200_OK)
