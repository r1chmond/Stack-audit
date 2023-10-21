from django.shortcuts import render
from audits import apis
from audits.forms import SmartContractForm


# Create your views here.
def home(request):
    form = SmartContractForm()
    context = {}
    if request.method == "POST":
        form = SmartContractForm(request.POST)
        if form.is_valid():
            source = apis.get_source_from_hiro_api(form.cleaned_data["contract"])
            response = apis.get_response_from_openai(source)
            context['response'] = response

    context["form"] = form
    return render(request, 'home.html', context=context)
