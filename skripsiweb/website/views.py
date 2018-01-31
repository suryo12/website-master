from django.views import generic
from .models import NodeID

class IndexView(generic.ListView):
    template_name = 'skripsiweb/base.html'

    def get_queryset(self):
        return NodeID.objects.all()


class DetailView(generic.DetailView):
    model = NodeID
    template_name = 'skripsiweb/detail.html'

