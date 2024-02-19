from django.shortcuts import HttpResponse,render
import random 
from django.contrib.auth.models import User

def index(request):
    person_list = ["HARI","RAM",'SHYAM',"NIRMAL","GITA"]

    users = User.objects.all()
    next_person_list = [
        {
            'username':"ram",
            'address':"JHAPA",
            'job':"STUDENT"
        }
        ,
        {
            'username':"shyam",
            'address':"BIRATNAGAR",
            'job':"WAITER"
        },
        {
            'username':"hari",
            'address':"ITHARI",
            'job':"ENGINEER"
        },
    ]
    context ={
        'users':users,
        'data':"HELLO",
        'person_list':person_list,
        'next_person_list':next_person_list
    }
    return render(request,'index.html',context)

def test(request):
    return HttpResponse("THIS IS TEST")

def view_profile(request,username,):
    user = username
    person_list = [
        {
            'username':"ram",
            'address':"JHAPA",
            'job':"STUDENT"
        }
        ,
        {
            'username':"shyam",
            'address':"BIRATNAGAR",
            'job':"WAITER"
        },
        {
            'username':"hari",
            'address':"ITHARI",
            'job':"ENGINEER"
        },
    ]
    for person in person_list:
        if person['username'] == user:
            return HttpResponse(f"THIS IS Profile of {person['username']} and his address is {person['address']}. He/She is {person['job']} . ")
        
    return HttpResponse("Profile not found")


def square(request,number):
    result = number*number
    return HttpResponse(f"The Square of <p>{number}<p> is <strong>{result}</strong>.")

    
def multiply(request,num1,num2):
    result = num1*num2
    return HttpResponse(f"The product of {num1} and {num2} is {result}")


def register(request):
    # username = request.GET.get('username')
    # full_name = request.GET.get('full_name')
    data = None
    if request.method == "POST":
        username = request.POST.get('username')
        full_name = request.POST.get('full_name')
        # object created and inserted to database
        
        if (username is not None and username != "" ):
            data = f"Your username is {username}"
        else :
            data = f"You haven't entered username"

    
    context = {
        'data':data,
    }
    return render(request,'register.html',context)