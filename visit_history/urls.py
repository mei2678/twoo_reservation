from django.urls import path
from .views import VisitHistoryView

urlpatterns = [
    path('<int:user_id>', VisitHistoryView.as_view(),
         name='visit-history-list')
]