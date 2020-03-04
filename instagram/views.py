from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.http  import HttpResponse,Http404
from django.shortcuts import render


# Create your views here.
def welcome(request):
    return render(request,'welcome.html')
def image_of_day(request):
    date = dt.date.today()
    return render(request, 'all-pics/today-image.html', {"date": date,})
    
def convert_dates(dates):

    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day  
def past_days_image(request,past_date):
        # Converts data from the string Url
    try:
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(news_of_day)

    return render(request, 'all-pics/past-image.html', {"date": date})