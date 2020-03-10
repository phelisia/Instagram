from django.shortcuts import render
from django.http  import HttpResponse
import datetime as dt
from django.utils import timezone 
from django.http  import HttpResponse,Http404
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Image, Profile, Comment
from .forms import *

# Create your views here.
# @login_required(login_url='/profile')
# def welcome(request):

def signup(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('welcome')
    else:
        form = RegisterForm()
    return render(request , 'registration/registration_form.html', {'form': form})

@login_required(login_url='logout')
def welcome(request):
    image = Image.objects.all()
    return render(request, 'welcome.html', {'images': image})

@login_required(login_url='/profile')
def search_results(request):
    if 'username' in request.GET and request.GET["username"]:
        search_term = request.GET.get("username")
        searched_users = User.objects.filter(username = search_term)
        message = f"{search_term}"
        profile_pic = User.objects.all()
        return render(request, 'search.html', {'message':message, 'results':searched_users, 'profile_pic':profile_pic})
    else:
        message = "You haven't searched for any term"
        return render(request, 'all-pics/search.html', {'message':message})
            
def profile(request):
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
            return render(request, 'profile.html', {})

    return render(request, 'all-pics/profile.html', {})
def ImageCreateView(request):
    # template_name = 'all-pics/create.html'
    if request.method == 'POST':
        form = ImageForm(request.POST,request.FILES)
        if form.is_valid():
            image = form.save(commit=False)
            author = request.user
            image.save()
            messages.success(request, f'Your post has been created successfully!!')
            return redirect('posts')
    else:
        form = ImageForm()
    context = {
        "form":form,
    }
    return render(request, 'all-pics/create.html', context)
def ImageDeleteView(DeleteView):
    template_name = 'all-pics/delete.html'

    def get_object(self):
        id_=self.kwargs.get("id")
        return get_object_or_404(Post, id=id_)

    def get_success_url(self):
        return reverse('all-pics:post_list')
