from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
monthly_challange = {
    "january": "January is the first month of the year.",
    "February": "February is the second month of the year.",
    "march": "March is the third month of the year.",
    "april": "April is the fourth month of the year.",
    "may": "May is the fifth month of the year.",
    "june": "June is the sixth month of the year.",
    "july": "July is the seventh month of the year.",
    "august": "August is the eighth month of the year.",
    "september": "September is the ninth month of the year.",
    "october": "October is the tenth month of the year.",
    "november": "November is the eleventh month of the year.",
    "december": "December is the twelfth month of the year."
}

def index(request):
    month_list = ""
    months = list(monthly_challange.keys())
    
    for month in months:
        capitlaized_month = month.capitalize()
        month_path = reverse("month-challange", args=[month])
        month_list += f"<li><a href=\"{month_path}\">{capitlaized_month}</a></li>"
    response_data = f"<ul>{month_list}</ul>"
    return HttpResponse(response_data) 

def monthly_challanges_By_num(request, month):
    months = list(monthly_challange.keys())
    if month > len(months):
        return HttpResponseNotFound("Invalid month")
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challange", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def  monthly_challanges(request, month):
    try:
        challange_text = monthly_challange[month]
    except:
        return HttpResponseNotFound("<h1>Invalid month</h1>")
    response_data = f"<h1>{challange_text}</h1>"
    return HttpResponse(response_data)
   