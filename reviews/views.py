from django.shortcuts import render
from django.views.generic import ListView,CreateView,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Comment
from .forms import CommentForm
from apartments.models import Apartment
# Create your views here.

class CommentList(LoginRequiredMixin,ListView):
    model = Comment
    template_name = 'reviews/list_comments.html'
    context_object_name = 'comments'

class CommentAdd(LoginRequiredMixin,CreateView):
    form_class= CommentForm
    model = Comment
    success_url = "/"
    redirect_field_name = "next"

    template_name = 'reviews/add_comment.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        apartment_id = self.request.POST.get('apartment')  # Use get() to avoid KeyError
        apartment_ins = Apartment.objects.get(pk=apartment_id)  # Use get() to retrieve a single instance
        obj.apartment = apartment_ins
        return super().form_valid(form)

        
    