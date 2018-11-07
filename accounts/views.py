from django.shortcuts import render
from django.contrib import messages
from .forms import CustomUserForm
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
# Create your views here.


def register(request):

    variables = {
        'form':CustomUserForm
    }

    if request.POST:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            variables['mensaje'] = "Registro correcto"
        else:
            variables['mensaje'] = "Ha ocurrido un problema, revisa los errores"
            variables['form'] = form

    return render(request, 'accounts/register.html', variables)

def cambiar_pass(request):

    variables = {
        'form':PasswordChangeForm(request.user)
    }

    if request.POST:
        formulario = PasswordChangeForm(request.user, request.POST)
        if formulario.is_valid():
            user = formulario.save()
            update_session_auth_hash(request, user)
            variables['mensaje'] = "Cambios registrados"
        else:
            variables['mensaje'] = "Ha ocurrido un error"
            variables['form'] = formulario

    return render(request, 'accounts/cambiar_pass.html', variables)

