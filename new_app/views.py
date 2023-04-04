from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class SampleView(APIView):
    def post(self, request):
        out_data = [
            {"Name":"Surya",
            "Age":25},
            {"Name":"Nikhil",
            "Age":28},
            {"Name":"Ashu",
            "Age":60},
        ]
        return Response(out_data)
