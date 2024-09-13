from django.shortcuts import render
from django.http import JsonResponse
from django.apps import apps
from django.views.decorators.csrf import csrf_exempt
from .models import Mononucleotides, Dinucleotides, Trinucleotides, Tetranucleotides, Pentanucleotides, Hexanucleotides
from ssr.forms import InputForm
import json

def home(request):
    return render(request, 'index.html', {'title': 'Home', 'message': 'Welcome to the homepage!'})

def index(request):
    return render(request, 'index.html')

@csrf_exempt
def analysis(request):
    return render(request, 'analysis.html')

def contact(request):
    return render(request, 'contact.html')

def documentation(request):
    return render(request, 'documentation.html')

def gallery(request):
    return render(request, 'gallery.html')

@csrf_exempt
def result(request):
    form = InputForm(request.POST or None)
    
    if request.method == 'POST':
        if form.is_valid():
            ssr_type = form.cleaned_data['ssrtype']
            chromosome = form.cleaned_data['chromosome']
            start = form.cleaned_data['start']
            end = form.cleaned_data['end']

            try:
                model_class = apps.get_model('ssr', ssr_type.lower() + 's')
                objects = model_class.objects.filter(
                    Chromosome=chromosome,
                    Start__gte=start,
                    End__lte=end
                ).values('ID', 'Chromosome', 'SSRtype', 'SSRsequence', 'Size', 'Start', 'End')

                context = {
                    'objects': list(objects),
                    'form': form
                }
                return render(request, 'result.html', context)
            except LookupError:
                form.add_error(None, 'The specified SSR model does not exist!')
            except Exception as e:
                form.add_error(None, str(e))

   # return render(request, 'result.html', {'form': form, 'objects':})
   
@csrf_exempt
def result_view(request, id, chromosome, ssrtype, ssrsequence, size, start, end):
    context = {
        'id': id,
        'chromosome': chromosome,
        'ssrtype': ssrtype,
        'ssrsequence': ssrsequence,
        'size': size,
        'start': start,
        'end': end,
    }
    return render(request, 'result.html', context)

@csrf_exempt
def analyze(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            response_data = {
                'success': True,
                'received_data': data
            }
            return JsonResponse(response_data)
        except json.JSONDecodeError:
            return JsonResponse({'success': False, 'message': 'Invalid JSON'}, status=400)
    else:
        return JsonResponse({'success': False, 'message': 'Only POST requests are allowed'}, status=405)
