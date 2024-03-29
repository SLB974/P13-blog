
from django.contrib.auth import get_user_model
from django.contrib.auth import login as log_in
from django.shortcuts import redirect, render
from django.urls import reverse

# from .forms import CustomUserCreationForm, UserForm
from .forms import RegisterForm, UserForm

User = get_user_model()


def signup(request):
    if request.method == "GET":
        form = RegisterForm
        return render(request, 'account/signup.html',{'form':form})
    
    form = RegisterForm(request.POST)
    if form.is_valid():
        user = form.save()
        log_in(request, user, backend='allauth.account.auth_backends.AuthenticationBackend')
        return redirect(reverse('home'))
        
    
    username=request.POST['username']
    email=request.POST['email']
    password1=request.POST['password1']
    password2=request.POST['password2']
    context = {"message":"Tous les champs sont obligatoires.", "advice":"Vérifiez votre saisie.", "form":form}

    
    if User.objects.filter(username=username).exists():
        context["message"]="Le nom de l'utilisateur est déjà attribué."
        context["advice"]="Choisissez un autre nom d'utilisateur."
        
    elif User.objects.filter(email=email).exists():
        context["message"]="Cet e-mail est déjà attribué à un utilisateur existant."
        context["advice"]="Choisissez une autre adresse e-mail."
        
    elif password1 != password2:
        context["message"]="Les mots de passe ne correspondent pas."


    elif len(password1) < 8:
        context["message"]="Le mot de passe doit contenir au moins 8 caractères."
        context["advice"]="Choisissez un autre mot de passe."
        
    else:
        context["message"]="Il persiste des erreurs."
        context["advice"]= form.errors.as_text()
        
   
    return render(request, 'account/signup.html', context)
