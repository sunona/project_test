# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect, Http404, HttpResponse, HttpRequest
from django.shortcuts import render_to_response, get_object_or_404, redirect
from django.template import RequestContext
from django.core.context_processors import csrf
import requests
import lxml.html as html
from multiprocessing import Pool
from multiprocessing.dummy import Pool as ThreadPool
from models import Url

# must be installed packages requests, lxml
def get_title(url):
    response = requests.get(url)
    parsed_body = html.fromstring(response.text)
    response_list = parsed_body.xpath('//title/text()')
    title = response_list[0]
    return title

def headers(request):
    urls = ['http://yandex.ru', 'http://ru.wikipedia.org', 'http://python.org']

    # Make the Pool
    pool = ThreadPool(3)

    # Open the urls in their own threads
    title_list = pool.map(get_title, urls)
    return render_to_response('headers/headers.html',
                              {'title_list': title_list},
                               context_instance=RequestContext(request))


                               