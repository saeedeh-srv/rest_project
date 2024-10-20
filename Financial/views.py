from .models import FinancialRecord,FinancialProjectInput
from .serializers import FinancialRecordSerializers,FinancialProjectInputSerializer
from rest_framework import generics


class FinancialListCreateView(generics.ListCreateAPIView):
    """

    """
    serializer_class = FinancialRecordSerializers

    def get_queryset(self):
        user = self.request.user
        return FinancialRecord.objects.filter(who_created=user).order_by('-price')

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(who_created=self.request.user)



class FinancialProjectInputView(generics.ListCreateAPIView):
    """
    a class to show Input financial
    """
    serializer_class = FinancialProjectInputSerializer
    def get_queryset(self):
        user=self.request.user
        return FinancialProjectInput.objects.filter(who_created=user)
    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(who_created=self.request.user)

