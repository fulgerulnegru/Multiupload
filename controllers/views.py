from django.shortcuts import render_to_response,redirect
from django.template import RequestContext, Context
from django.http import HttpResponse,Http404,HttpResponseRedirect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth.views import login
from django.contrib.auth import login as auth_login
from django.views.decorators.csrf import *
import os
import Image
import StringIO
#din site
from controllers.models import *
from controllers.forms import *
from settings import *

def home(request):
    return render_to_response("home.html")


def upload(request):
    if request.method == "POST":
        form = ImageUploadForm(request.POST,request.FILES)
    else:
        form=ImageUploadForm()
    return render_to_response("upload.html",RequestContext(request,{'form':form}))



@csrf_exempt
def upload_file(request):
    if request.method == "POST":
        print request.FILES
        print request.FILES.getlist('pic')
        im = Image.open(request.FILES['pic'])
        ImageAttachment.objects.create(image=request.FILES['pic'])
        #im.save('static/upload'+str(request.FILES['pic'])) 
        #fd = open('%s/%s' % (MEDIA_ROOT, filename), 'wb')
        #fd.write(im['content'])
        #fd.close()
        #im.save(PATH_OF_IMAGE_TO_BE_PALETTED, "PNG")
    return render_to_response("home.html")
