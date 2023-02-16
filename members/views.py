from django.views import generic    
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.contrib.auth.models import User

class UserregistrationForm(generic.CreateView):
    form_class=UserCreationForm
    queryset = User.objects.all()
    template_name='registration/register.html'
    success_url=reverse_lazy('login')