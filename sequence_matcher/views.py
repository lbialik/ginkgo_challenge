from django.shortcuts import render

def sequence_matcher(request):
    return render(request, 'sequence_matcher.html', {})