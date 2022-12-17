from django.shortcuts import render
from django.http import HttpResponse

from foodlovers.apps.vendor.models import Vendor

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``
from django.contrib.gis.db.models.functions import Distance


#GET THE LATITUDE AND LONGITUDE FROM SESSION
def get_or_set_current_location(request):
    if 'lat' and 'lng' in request.session:
        lat = request.session['lat']
        lng = request.session['lng']
        print(request.session['lat'], request.session['lng'])
        return lng, lat
    elif 'lat' and 'lng' in request.GET:
        print('sd:', request.session)
        lat = request.GET.get('lat')
        lng = request.GET.get('lng')
        request.session['lat'] = lat
        request.session['lng'] = lng
        return lng, lat
    else:
        return None


def home(request):
    popularvendors= Vendor.objects.filter(is_featured=True)
    lat=''
    lng=''
    print(get_or_set_current_location(request))
    if get_or_set_current_location(request) is not None:
        lat = request.session['lat']
        lng = request.session['lng']
        pnt = GEOSGeometry('POINT(%s %s)' % (get_or_set_current_location(request)))
        print('pnt:', pnt)
        vendors = Vendor.objects.filter(user_profile__location__distance_lte=(pnt, D(km=1000))).annotate(distance=Distance("user_profile__location", pnt)).order_by("distance")

        for v in vendors:
            v.kms = round(v.distance.km, 1)
    else:
        vendors = Vendor.objects.filter(is_approved=True, user__is_active=True)[:8]
    context = {
        'vendors': vendors,
        'popularvendors': popularvendors,
        'lat':lat,
        'lng':lng
    }
    return render(request, 'home.html', context)