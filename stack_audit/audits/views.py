from django.shortcuts import render
from audits import openai_api
from audits.forms import SmartContractForm


# Create your views here.
def home(request):
    form = SmartContractForm()
    context = {}
    if request.method == "POST":
        form = SmartContractForm(request.POST)
        response = openai_api.get_response(form)
        context['response'] = response

    context["form"] = form
    return render(request, 'home.html', context=context)
