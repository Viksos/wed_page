from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import guest_nm

def index(request):
    
    template = loader.get_template('guest_login/home.html')
    context = {
        'images' :['sala','my_2','my_1','kwiaty'],
        'static' : ['style_wed']
    }
    
    return( HttpResponse(template.render(context,request)))


def user_input(request):
    #if request.POST['submit'] == 'add_object':
    # Both ways to deal with it
    
        
    if request.method == 'POST':
        patient_name = request.POST.get('name')
        if 'bd_button' in request.POST:
            will_be = '1'
        else:
            will_be = '0'
    
        # Create a new patient entry in the database using the Patient model
        patient = guest_nm(guest_name=patient_name,guest_respond = will_be)
        patient.save()

        template = loader.get_template('guest_login/ty.html')
        context = {
    #    'images' :['sala','my_2','my_1','kwiaty'],
    #    'static' : ['style_wed']
    }
        
        
        return( HttpResponse(template.render(context,request)))
        #return HttpResponse("Data successfully inserted!")
    else:
        return HttpResponse("Invalid request method.")