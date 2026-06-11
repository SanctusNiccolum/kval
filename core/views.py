from django.shortcuts import redirect, render
from django.http import HttpResponse


def test(request):
    return HttpResponse("OK")

def error_404_view(request, exception=None):
    return redirect('/admin/')

# class TestVeiw:
#      def get(self, request, *args, **kwargs):
#         self.object = None
#         render(request, 'myapp/index.html',)