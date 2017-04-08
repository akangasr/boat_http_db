import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from boats.models import Boat

def index(request):
    return HttpResponse("Boats")

@csrf_exempt  # local use
def add_boats(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
    else:
        return HttpResponse("Error: Expected boat data in HTTP POST request body", status=400)
    count_change = 0
    count_add = 0
    try:
        for jarnro, item in data.items():
            try:
                # change
                b = Boat.objects.get(jarnro=jarnro)
                for k, v in item:
                    setattr(b, k, v)
                b.save()
                count_change += 1
            except:
                # add
                b = Boat(**item, jarnro=jarnro)
                b.save()
                count_add += 1
    except Exception as e:
        return HttpResponse("Error: {}".format(e), status=400)
    return HttpResponse("Changed {}, added {}".format(count_change, count_add), status=200)

@csrf_exempt  # local use
def list_boats(request):
    if request.method == "POST":
        data = json.loads(request.body.decode("utf-8"))
    else:
        return HttpResponse("Error: Expected boat data in HTTP POST request body", status=400)
    boats = Boat.objects.filter(**data)
    retu = list()
    for boat in boats:
        ret = dict()
        ret["kayttoonottovuosi"] = boat.kayttoonottovuosi
        ret["maxnopeus"] = boat.maxnopeus
        ret["vene_malli"] = boat.vene_malli
        ret["vene_merkki"] = boat.vene_merkki
        ret["ruonkopituus"] = boat.runkopituus
        ret["maxleveys"] = boat.maxleveys
        retu.append(ret)
    return HttpResponse(json.dumps(retu))

