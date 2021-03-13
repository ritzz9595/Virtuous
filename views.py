import django.core.mail
from datetime import date, timedelta
import datetime
from django.core.files.storage import FileSystemStorage
from django.forms import forms, DateInput
import mysql.connector
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.shortcuts import render
from mysql.connector import Error
from mysql import connector

def index(request):
    return render(request,'index.html')