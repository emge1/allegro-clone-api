from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from v1.accounts.serializers.register import RegisterSerialiser


class RegisterView(APIView):
    authentication_classes = ()
    permission_classes = ()

    @staticmethod
    def post(request):
        """
        Register a new user
        """
        serializer = RegisterSerialiser(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"message": "User registered successfully!"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
