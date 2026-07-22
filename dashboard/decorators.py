from django.shortcuts import redirect


def instructor_required(view_func):

    def wrapper(request, *args, **kwargs):

        if not request.user.is_authenticated:
            return redirect("instructor_login")

        if request.user.role.lower() != "instructor":
            return redirect("login")

        return view_func(request, *args, **kwargs)

    return wrapper