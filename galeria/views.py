# from django.shortcuts import render, redirect
# from .models import Galeria
# from .forms import GaleriaForm

# def home(request):
#     galerie = Galeria.objects.all()
#     return render(request, 'galeria/home.html', {'galerie': galerie})


# def create_galeria(request):
#     if request.method == "POST":
#         form = GaleriaForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('home')
#     else:
#         form = GaleriaForm()
#     return render(request, 'galeria/create_galeria.html', {'form': form})


# Create your views here.
