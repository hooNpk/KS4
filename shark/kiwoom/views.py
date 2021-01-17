from django.shortcuts import render
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from kiwoom_module import Kiwoom
from django.http import HttpResponse
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QAxContainer import *
from PyQt5.QtCore import *

app = 'ABC'
kiwoom = 'DEFAULT'

def index(request):
    global app
    global kiwoom
    app = QApplication([""])
    kiwoom = Kiwoom()
    kiwoom.comm_connect()
    return HttpResponse("GET REQUEST to LOGIN")

def today(request):
    codes = kiwoom.get_all_codes_names()
    print(codes)
    return HttpResponse("This is for returning today's information")

def trading(request):
    print(request)
    return HttpResponse("Request for Trading:::::")
