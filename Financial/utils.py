from .models import FinancialRecord, FinancialProjectInput
from Projects.models import Project

def get_related_models():
    return {
        'financial_record': FinancialRecord,
        'project': Project,
    }