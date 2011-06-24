# Create your views here.



from django.shortcuts import *
from django.utils import simplejson
import json

def index(request):
  return render_to_response('index.html')

def query(request):
  try:
    params = request.REQUEST
    lo, hi = int(params.get("lo")), int(params.get("hi"))
    f = open('/home/pratik/grp/sampler/plotter/input.txt', 'r')
    LIMIT, i = 20, 0
    
    labels, points = [], []
    for n in f:
      i += 1
      if lo <= i and i <= hi:
        points.append( n[:-1] )
        labels.append( i )
    
    req = {"labels" : labels, "points" : points}
    return HttpResponse(simplejson.dumps(req), mimetype="application/json")
  except:
    return HttpResponse("Something went wrong")
