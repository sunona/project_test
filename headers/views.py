# -*- coding: utf-8 -*-
import datetime
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpRequest
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.template.loader import render_to_string
from django.core.context_processors import csrf
import httplib

def headers(request):
    #conn = httplib.HTTPConnection('www.yandex.ru')
    #conn.request('GET','/')
    #res = conn.getresponse()
    #print(res)
    return render_to_response('headers/headers.html',
                              {'a':100},
                               context_instance=RequestContext(request))                                
    

                               