from django.shortcuts import render
from django.views.generic import  TemplateView,DetailView,FormView,UpdateView,DeleteView
from .models import Post
from .forms import PostForm
from django.contrib import messages
from  django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View


# Create your views here.
class HomePageView(LoginRequiredMixin,TemplateView):

    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-id')
        return context
    

class PostDetailView(LoginRequiredMixin,DetailView):
    template_name = 'detail.html'
    model = Post
    
class AddPostView(LoginRequiredMixin,FormView):
    template_name ="addpost.html"
    form_class = PostForm
    success_url = '/home'
    
    
    def  dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    
    def form_valid(self, form):
        new_object = Post.objects.create(
            title = form.cleaned_data['title'],
            description = form.cleaned_data['description'],
            image = form.cleaned_data['image'],
            )
        messages.add_message(self.request, messages.SUCCESS, 'Content successfully uploaded.')
        return super().form_valid(form)
    

class ContactPageView(TemplateView):

    template_name = "contact.html"
    
class LandingPageView(TemplateView):

    template_name = "index.html"

    
class AboutpageView(TemplateView):
    template_name="about.html"
    
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    fields=['title','description','image']
    template_name = 'update.html'
    success_url ='/home'


class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = 'delete.html'
    success_url = '/home'
    
    
class Error404View(View):
    def get(self, request, exception=None):
        return render(request, '404.html')
