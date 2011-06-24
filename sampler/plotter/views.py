# Create your views here.



from django.shortcuts import *
from django.utils import simplejson
import json
import math

def index(request):
  return render_to_response('index.html')

def query(request):
  try:
    params = request.REQUEST
    lo, hi, gran = int(params.get("lo")), int(params.get("hi")), int(params.get("granularity"))
    f = open('/home/pratik/grp/sampler/plotter/input.txt', 'r')
    LIMIT, i = 20*gran, 0
    labels, points = [], []
    for n in f:
      if lo <= i and i <= hi:
        points.append( n[:-1] )
        labels.append( i )
      i += 1
    if hi-lo > LIMIT:
      _points = []
      _labels = []
      step = (hi - lo) / LIMIT
      for z in xrange(0, len(points), step):
         _points.append( points[z] )
         _labels.append( labels[z] )
      labels = _labels
      points = _points
    req = {"labels" : labels, "points" : points}
    return HttpResponse(simplejson.dumps(req), mimetype="application/json")
  except:
    return HttpResponse("Something went wrong")
