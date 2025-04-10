from django.shortcuts import render, redirect
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def pdf(request):
    return render(request, 'pdf.html')

def manual(request):
    return render(request, 'manual.html', {"scopes" : [1,2,3]})

def results(request):
    if request.method == 'POST':

        if request.FILES.get('file'):
            pdf_file = request.FILES.get('file')

            if not pdf_file.name.endswith('.pdf'):
                messages.error(request, 'File is not PDF type')
                return redirect('index')

            results = f"you uploaded {request.FILES.get('file')}, and you should reduce your carbon footprint by x and y"
            context = {
                'results': results
            }

        elif request.POST.get('scope1') and request.POST.get('scope2') and request.POST.get('scope3') and request.POST.get('profit'):
            
            scopes = [request.POST.get('scope1'), request.POST.get('scope2'), request.POST.get('scope3')]
            profit = request.POST.get('profit')
            
            results = f"you selected {scopes[0]} and {scopes[1]} and {scopes[2]} and profit {profit}, and you should reduce your carbon footprint by x and y"
            context = {
                'results': results
            }
    else:
        return redirect('index')
    return render(request, 'results.html', context)
