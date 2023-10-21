from django.shortcuts import render

from audits.forms import SmartContractForm


# Create your views here.
def home(request):
    form = SmartContractForm()
    if request.method == "post":
        pass
    return render(request, 'home.html', context={"form": form})