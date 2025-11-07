from django.urls import reverse_lazy
from django.views import generic
from .models import Feedback
from .forms import FeedbackForm

class FeedbackListView(generic.ListView):
    model = Feedback
    template_name = "feedback_app/feedback_list.html"
    context_object_name = "feedback_list"
    paginate_by = 10

class FeedbackDetailView(generic.DetailView):
    model = Feedback
    template_name = "feedback_app/feedback_detail.html"
    context_object_name = "feedback"

class FeedbackCreateView(generic.CreateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "feedback_app/feedback_form.html"
    success_url = reverse_lazy("feedback_list")

class FeedbackUpdateView(generic.UpdateView):
    model = Feedback
    form_class = FeedbackForm
    template_name = "feedback_app/feedback_form.html"
    success_url = reverse_lazy("feedback_list")

class FeedbackDeleteView(generic.DeleteView):
    model = Feedback
    template_name = "feedback_app/feedback_confirm_delete.html"
    success_url = reverse_lazy("feedback_list")