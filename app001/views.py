# Create your views here.
from django.http import HttpResponse, Http404
from .models import Departamento, Habilidad, Empleado
from django.shortcuts import get_object_or_404, get_list_or_404, render


# devuelve el listado de empresas
def index(request):
    departamentos = get_list_or_404(Departamento.objects.order_by("nombre"))
    """ output = ", ".join([d.nombre for d in departamentos])
    return HttpResponse(output) """
    context = {'lista_departamentos': departamentos}
    return render(request, 'index.html', context)


# devuelve los datos de un departamento
def detail(request, departamento_id):
    departamento = Departamento.objects.get(pk=departamento_id)
    #  output = ", ".join([str(departamento.id), departamento.nombre, str(departamento.telefono)])
    """ output = f"{departamento.id}, {departamento.nombre},{departamento.telefono}"
    return HttpResponse(output)"""
    context = {'departamento': departamento}
    return render(request, 'detail.html', context)


# devuelve los empleados de un departamento
def empleados(request, departamento_id):
    departamento = get_object_or_404(Departamento, pk=departamento_id)
    """output = ', '.join([e.nombre for e in departamento.empleado_set.all()])
    return HttpResponse(output)"""
    empleados = departamento.empleado_set.all()
    context = {'departamento': departamento, 'empleados': empleados}
    return render(request, 'empleados.html', context)


# devuelve los detalles de un empleado
def empleado(request, empleado_id):
    """ empleado = Empleado.objects.get(pk=empleado_id)
    datos_empleado = f"{empleado.id}, {empleado.nombre}, {empleado.fecha_nacimiento}, {empleado.antiguedad}, {empleado.departamento.nombre}"
    habilidades = ', '.join([h.nombre for h in empleado.habilidades.all()])
    output = f"{datos_empleado} // Habilidades: {habilidades}"
    return HttpResponse(output)"""
    empleado = get_object_or_404(Empleado, pk=empleado_id)
    habilidades = empleado.habilidades.all()
    context = { "empleado": empleado, "habilidades": habilidades}
    return render(request, 'empleado.html',context)


def habilidad(request, habilidad_id):
    habilidad =get_object_or_404(Habilidad, pk=habilidad_id)
    empleados = habilidad.empleado_set.all()
    context = {'empleados':empleados, 'habilidad': habilidad}
    return render(request, 'habilidad.html',context)
