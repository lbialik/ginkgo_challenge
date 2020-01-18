from django.shortcuts import render
from django.shortcuts import HttpResponse
from .alignment import align
from .models import Sequence

def sequence_matcher(request):
    return render(request, 'sequence_matcher.html', {})

def submit(request):
    if request.method == 'POST':
        sequence = request.POST.get('info', None)
        protein, index = align(sequence)
        seq = Sequence()
        seq.index = index
        seq.protein = protein
        seq.title = sequence
        seq.save()
    return render(request, 'sequence_matcher.html', {})