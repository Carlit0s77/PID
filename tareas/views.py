from django.shortcuts import render, redirect, get_object_or_404
from .forms import ArrendatarioForm
from .models import Arrendatario
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, 'home.html')

# listar


def arrendatarios(request):
    arrendatarios = Arrendatario.objects.all()
    return render(request, 'arrendatarios.html', {
        'arrendatarios': arrendatarios
    })

# crear

@login_required
def crear_arrendatario(request):
    # metodo get -- muestra info
    if request.method == 'POST':
        return render(request, 'crear_arrendatario.html', {
            'form': ArrendatarioForm
        })
        # metodo post -- entra datos
    else:
        try:
            form = ArrendatarioForm(request.POST)
            nuevo_arrendatario = form.save(commit=False)
            nuevo_arrendatario.user = request.user
            nuevo_arrendatario.save()
            return redirect('arrendatarios')
        except:
            return render(request, 'crear_arrendatario.html', {
                'form': ArrendatarioForm,
                'error': 'Please provider valide data'
            })


# detalle arrendatario , update
@login_required
def arrendatario_datalle(request, arrendatario_id):
    if request.method == 'POST':
        arrendatario = get_object_or_404(Arrendatario, pk=arrendatario_id)
        form = ArrendatarioForm(instance=arrendatario)
        return render(request, 'arrendatario_detalle.html', {
            'arrendatario': arrendatario,
            'form': form
        })
    else:
        try:
            arrendatario = get_object_or_404(Arrendatario, pk=arrendatario_id)
            form = ArrendatarioForm(request.POST, instance=arrendatario)
            form.save()
            return redirect('arrendatarios')
        except ValueError:
            return render(request, 'arrendatario_detalle.html', {
                'arrendatario': arrendatario,
                'form': form,
                'error': "Error al actualizar , datos incorrectos"
            })

# eliminar

@login_required
def delete_arrendatario(request, arrendatario_id):
    arrendatario = get_object_or_404(Arrendatario, pk=arrendatario_id)
    arrendatario.delete()
    return redirect('arrendatarios')

