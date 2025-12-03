from django.shortcuts import redirect


def role_required(allowed_roles=[]):
    def decorator(functionality):
        # @wraps(functionality)
        def wrapper(request, *arg, **kwargs):
            if not request.user.is_authenticated:
                return redirect("login")
            if request.user.role not in allowed_roles:
                return redirect("no_access")

            return functionality(request, *arg, **kwargs)

        return wrapper

    return decorator
