from django.views.generic import DetailView, TemplateView
from rest_framework import mixins, generics
from graph.serializers import MemberSerializer
from .models import Member


class MainView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(MainView, self).get_context_data(**kwargs)
        context.update({
            'usernames': list(map(lambda mem: str(mem.github_username), Member.objects.all())),
        })
        return context


class MemberDetailView(DetailView):
    model = Member
    slug_url_kwarg = "username"
    slug_field = "github_username"

    def get_context_data(self, **kwargs):
        context = super(MemberDetailView, self).get_context_data(**kwargs)
        context.update({
            'usernames': list(map(lambda mem: str(mem.github_username), Member.objects.all())),
            })
        return context


class MemberRetrieveView(generics.RetrieveAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    lookup_field = 'github_username'
    lookup_url_kwarg = 'username'
