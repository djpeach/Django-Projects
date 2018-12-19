from django.shortcuts import redirect, reverse


def redirect_to_blog(req):
    return redirect(reverse('blog:read-list'))
