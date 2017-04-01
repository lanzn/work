from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse 
from django.shortcuts import render_to_response
import mysql.connector 
from blog.models import smovie 
from django.shortcuts import get_object_or_404, render

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template import RequestContext

ONE_PAGE_OF_DATA = 4  
  
def index(rq):  
    try:  
        curPage = int(rq.GET.get('curPage', '1'))  
        print("hah")
        print(rq.GET.get('allPage', '1')) 
        print(type(rq.GET.get('allPage', '')))
        allPage = float(rq.GET.get('allPage','1'))  # 这个地方错了，注意到后台只输出了hah，然后就跳到
        print(allPage) 
        print(type(allPage))
        print("hee")
        pageType = str(rq.GET.get('pageType', ''))  
        print("lala")
    except ValueError:  
        curPage = 1  #这个地方了，所以又跟第一页一样了
        allPage = 1  
        pageType = ''  
  
    #判断点击了【下一页】还是【上一页】  
    if pageType == 'pageDown':  
        curPage += 1  
    elif pageType == 'pageUp':  
        curPage -= 1  
  
    startPos = (curPage - 1) * ONE_PAGE_OF_DATA  
    endPos = startPos + ONE_PAGE_OF_DATA  
    posts = smovie.objects.all()[startPos:endPos]  
  
    if curPage == 1 and allPage == 1: #标记1  
        allPostCounts = smovie.objects.count()  
        allPage = allPostCounts / ONE_PAGE_OF_DATA  
        remainPost = allPostCounts % ONE_PAGE_OF_DATA  
        if remainPost > 0:  
            allPage += 1  
  
    return render_to_response("index.html",{'posts':posts, 'allPage':allPage, 'curPage':curPage})
# def index(req):  
	# # db =  mysql.connector.connect(user="root",password="root",database="test",cursorclass = MySQLdb.cursors.DictCursor)
	# # cursor=db.cursor()
	# # cursor.execute('SELECT * FROM movies')
	# # names=[row[:] for row in cursor.fetchall()]
	# # db.close()
	# names=smovie.objects.all()
	# return render_to_response('index.html',{'names':names})
def extent(req,extent_id):
	#names=smovie.objects.all()
	name=get_object_or_404(smovie,pk=extent_id)
	return render_to_response('extent.html',{'name':name})
# def extent1(req):
	# names=smovie.objects.all()
	# return render_to_response('extent1.html',{'names':names})
# def extent2(req):
	# names=smovie.objects.all()
	# return render_to_response('extent2.html',{'names':names})
