from django.shortcuts import redirect, reverse

def redirect_to_forum(req):
    return redirect(reverse('forum-home'))