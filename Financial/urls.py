from django.urls import path
from .views import FinancialListCreateView,FinancialProjectInputView

app_name = 'financial'

urlpatterns = [
    path('list/create/', FinancialListCreateView.as_view(), name='list_create_financial_record'),
    path('list/inpute/create/', FinancialProjectInputView.as_view(), name='list_create_input_financial_project')
]
