from rest_framework import generics
from rest_framework.response import Response

class FakeView(generics.GenericAPIView):

    def get(self, request):

        return Response(status=204)