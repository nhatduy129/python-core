from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import threading
import time

def background_task():
    print("Starting background task...")
    time.sleep(5)  # Simulate some work
    print("Background task completed!")

class HelloView(APIView):
    def get(self, request):
        # Start background thread
        thread = threading.Thread(target=background_task)
        thread.start()
        
        return Response({
            'message': 'Hello, World!',
            'background_task': 'Started'
        })
