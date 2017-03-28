from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from django.shortcuts import render_to_response
import mysql.connector 
from blog.models import smovie 
def index(req):  
	# db =  mysql.connector.connect(user="root",password="root",database="test",cursorclass = MySQLdb.cursors.DictCursor)
	# cursor=db.cursor()
	# cursor.execute('SELECT * FROM movies')
	# names=[row[:] for row in cursor.fetchall()]
	# db.close()
	names=smovie.objects.all()
	return render_to_response('index.html',{'names':names})
def extent1(req):
	names=smovie.objects.all()
	return render_to_response('extent1.html',{'names':names})
def extent2(req):
	names=smovie.objects.all()
	return render_to_response('extent2.html',{'names':names})
	