# Create your views here.


from django.shortcuts import *
def index(request):
  return render_to_response('index.html')

def query(request):
  return render_to_response('index.html')
  
