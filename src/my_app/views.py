from django.shortcuts import render
from django.http import HttpResponse
from .forms import LinksForm
# from .utils import gen_url
from .models import Link
from django.http import HttpResponseRedirect


# Create your views here.
def test_view(request):
    if request.method == 'POST':
        if not Link.objects.filter(old_link = request.POST['link'] ):
            Link.objects.create(
                old_link = request.POST['link'] )
    form = LinksForm()
    links = Link.objects.all().order_by("-id")
    return render(request, "my_app/test.html", context = {"form":form, "links":links})  



def redirect_view(request, new_link):

    link = Link.objects.filter(new_link = new_link).last()
    
    return HttpResponseRedirect(link.old_link)
    
