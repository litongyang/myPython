
from django.template import loader, Context
import django.http as http
from . import models
from django.shortcuts import HttpResponseRedirect,Http404,HttpResponse,render_to_response
#import Interface.Interface_web.models as models

# Create your views here.

def archive(request):
    posts = models.InterfacePost.objects.all()
    t = loader.get_template("archive.html")
    c = Context({'posts': posts})
    names = "ssss"
    return http.HttpResponse(t.render(c))
   # return render_to_response("archive.html",locals())