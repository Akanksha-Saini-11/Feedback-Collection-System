from django.urls import path
from . import views

urlpatterns = [
    path("", views.FeedbackListView.as_view(), name="feedback_list"),
    path("feedback/add/", views.FeedbackCreateView.as_view(), name="feedback_add"),
    path("feedback/<int:pk>/", views.FeedbackDetailView.as_view(), name="feedback_detail"),
    path("feedback/<int:pk>/edit/", views.FeedbackUpdateView.as_view(), name="feedback_edit"),
    path("feedback/<int:pk>/delete/", views.FeedbackDeleteView.as_view(), name="feedback_delete"),
]