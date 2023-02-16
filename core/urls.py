from django.urls import path
from core import views
from .views import PostCreateView,PostDeleteView,PostUpdateView,PostDetailview,Homeview
urlpatterns = [
    path('',Homeview.as_view(),name="index"),
    path('article/<int:pk>',PostDetailview.as_view(),name='article'),
    path('type/<str:type_name>', views.CategoryView,name='category'),
    path('type/Buy', views.Buy,name='Buy'),
    path('type/Rent', views.Rent,name='Rent'),
    path('subcategory/<str:subty_name>', views.SubcategoryView,name='subcategory'),
    path('search_results', views.search_results,name='search-results'),
    path('contact', views.contactus, name='contact')
]