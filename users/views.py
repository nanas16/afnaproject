from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User

from .models import Biodata
from .forms import UserForms, BiodataForms
# ---------------------------------------------------------- Tabel User ----------------------------------------------------------#

def is_operator(user):
    if user.groups.filter(name='Operator').exists():
        return True
    else:
        return False

@login_required
@user_passes_test(is_operator)
def users(request):
    template_name = "user/tabel_users.html"
    list_user = User.objects.all()
    context = {
        'title':'tabel users',
        'list_user':list_user
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_detail(request, id):
    template_name = "user/user_detail.html"
    user_info = User.objects.get(id=id)
    bio = Biodata.objects.get(user=user_info)
    context = {
        'title': 'User',
        'user_info': user_info,
        'bio': bio
    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_edit(request, id):
    template_name = "user/user_edit.html"
    user_info = User.objects.get(id=id)
    bio = Biodata.objects.get(user=user_info)

    if request.method == "POST":
        forms_user = UserForms(request.POST, instance=user_info)
        forms_bio = BiodataForms(request.POST, instance=bio)
        if forms_user.is_valid() and forms_bio.is_valid():
            test = forms_user.save(commit=False)
            test.is_active = True
            test.save()
            forms_bio.save()
            return redirect(users)
    else:
        forms_user = UserForms(instance=user_info)
        forms_bio = BiodataForms(instance=bio)

    context = {
        'title': 'Edit User',
        'user_info': user_info,
        'bio': bio,

        'forms_user': forms_user,
        'forms_bio': forms_bio,

    }
    return render(request, template_name, context)

@login_required
@user_passes_test(is_operator)
def user_hapus(request, id):
    User.objects.get(id=id).delete()
    return redirect(users)
# ------------------------------------------------------------- end --------------------------------------------------------------#