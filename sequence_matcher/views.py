from django.shortcuts import render
from django.shortcuts import HttpResponse
from .alignment import align
from .models import Sequence
from django.utils import timezone

def sequence_matcher(request):
    if request.method == 'POST':
        sequence = request.POST.get('info', None).upper()
        protein, index = align(sequence)
        seq, created = Sequence.objects.get_or_create(title = sequence, index = index, protein = protein)
        seq.timestamp = timezone.now()
        seq.save()
    data = Sequence.objects.all().order_by('timestamp').reverse()
    sequence_dict = {'sequences':data}
    return render(request, 'sequence_matcher.html', sequence_dict)
