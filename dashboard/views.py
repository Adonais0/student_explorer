from django.views.generic import View, TemplateView

# Create your views here.

class Dashboard(TemplateView):
    template_name = "dashboard/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super(Dashboard, self).get_context_data(**kwargs)
        return context

dashboard = Dashboard.as_view()