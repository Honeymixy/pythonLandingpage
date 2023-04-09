from django.urls import path


from .views import HomePageView,ContactPageView,AboutpageView,PostDetailView,AddPostView,PostUpdateView,PostDeleteView,LandingPageView,Error404View

urlpatterns = [
    path('',LandingPageView.as_view(),name='index'),
    path('home/',HomePageView.as_view(),name='home'),
    path('detail/<int:pk>/',PostDetailView.as_view(),name='detail'),
    path('contact/',ContactPageView.as_view(),name='contact'),
    path('about/',AboutpageView.as_view(),name='about'),
    path('post/',AddPostView.as_view(),name='post'), 
    path('detail/<int:pk>/update/', PostUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/delete/', PostDeleteView.as_view(), name='delete'),
    path('404/', Error404View.as_view(), name='error_404'),

 
]


