from django.shortcuts import render
from django.shortcuts import HttpResponse

def sequence_matcher(request):
    return render(request, 'sequence_matcher.html', {})

def submit(request):
    if request.method == 'POST':
        sequence = request.POST.get('info', None)
        text = "<H1>{}</H1>".format(sequence)
        return HttpResponse(text)
    else:
        return render(request, 'sequence_matcher.html', {})