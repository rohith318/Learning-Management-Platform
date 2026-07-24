from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import UserForm
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.hashers import make_password
from .models import User


def user_list(request):

    search = request.GET.get("search", "")

    users = User.objects.all()

    if search:
        users = users.filter(
            username__icontains=search
        )

    paginator = Paginator(users, 5)

    page_number = request.GET.get("page")

    users = paginator.get_page(page_number)

    return render(
        request,
        "accounts/user_list.html",
        {
            "users": users,
            "search": search,
        },
    )

def add_user(request):
    if request.method == "POST":
        form = UserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect("user_list")

    else:
        form = UserForm()

    return render(
        request,
        "accounts/user_form.html",
        {
            "form": form,
            "title": "Add User",
        },
    )


def edit_user(request, pk):
    user = get_object_or_404(User, pk=pk)

    if request.method == "POST":
        form = UserForm(request.POST, instance=user)

        if form.is_valid():
            form.save()
            return redirect("user_list")

    else:
        form = UserForm(instance=user)

    return render(
        request,
        "accounts/user_form.html",
        {
            "form": form,
            "title": "Edit User",
        },
    )


def delete_user(request, pk):
    user = get_object_or_404(User, pk=pk)
    user.delete()

    return redirect("user_list")



def forgot_password(request):

    if request.method == "POST":

        username = request.POST.get("username")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if new_password != confirm_password:
            messages.error(request, "Passwords do not match.")
            return redirect("forgot_password")

        try:
            user = User.objects.get(username=username)

            user.password = make_password(new_password)
            user.save()

            messages.success(request, "Password changed successfully.")

            return redirect("user_login")

        except User.DoesNotExist:

            messages.error(request, "Username not found.")

            return redirect("forgot_password")

    return render(request, "registration/forgot_password.html")


