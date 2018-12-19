from django.shortcuts import render
from django.http import HTTPResponse

# Create your views here.

def index(req) {
    return HTTPResponse('Hello World')
}
