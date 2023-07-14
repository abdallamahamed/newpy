from django.shortcuts import render,get_object_or_404
from .models import cources,category,post,postcategory,Price_Plans,Recommendations
from .models import home_interface
from .models import contact_information
from .models import contact_data
from django.http import HttpResponse
from django.core.mail import send_mail
from .models import my_contact
from django.contrib import messages
from django.http import HttpResponseRedirect
from base import models

# Create your views here.
#pofolia pages
def list_page(request):
    obj=cources.objects.all()
    oo=category.objects.all()
    nn=Recommendations.objects.all()
    return render(request, 'portfolio-2-col.html',{'obj':obj,'oo':oo,'nn':nn})

def detail_page(request,id):
    obj=get_object_or_404(cources,pk=id)
    return render(request, 'portfolio-single.html',{'obj':obj,})



#home ...............................................
def ama(request):
    obj=home_interface.objects.all()
    opp=cources.objects.all()
    ll=Price_Plans.objects.all()
    nn=Recommendations.objects.all()

    return render(request, 'home.html',{'obj':obj,'opp':opp,'ll':ll,'nn':nn,})
    
#....................................................


#posts pages
def list_post(request):
    ww=postcategory.objects.all()
    ww=post.objects.all()

    return render(request, 'blog-2-col.html',{'ww':ww,'ww':ww, })

def detail_post(request,id):
    ww=get_object_or_404(post,pk=id)
    
    
    return render(request, 'blog-post.html',{'ww':ww,})


# contect page 
    
def contact(request):
    if request.method =='POST':
        name = request.POST['fname']
        email = request.POST['femail']
        phone = request.POST['fphone']
        message = request.POST['fmessage']
        ins = my_contact(magac=name, iimel=email, number=phone, fikrad=message)
        ins.save()
        print('saved')
        return render(request, 'sucsess.html')
    bb = contact_information.objects.first()
    context = {'bb':bb}
    return render(request, 'contact.html',context)






#history page
from .models import work_history,educational_history

def history(request):
    e=work_history.objects.all()
    r=educational_history.objects.all()
    
    context = {'r':r, 'e':e}

    return render(request, 'history.html', context)