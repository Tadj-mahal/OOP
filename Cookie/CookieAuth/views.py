from django.shortcuts import render, redirect
from django.contrib.auth import authenticate
from django.http import JsonResponse

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            response = redirect(f'/user?username={username}&password={password}')
            response.set_cookie('session_token', 'abc123xyz456', secure=True, httponly=True)
            return response

    return render(request, 'base.html')

def user_view(request):
    session_token = request.COOKIES.get('session_token')

    if session_token == 'abc123xyz456':
        username = request.GET.get('username')
        password = request.GET.get('password')
        return JsonResponse({'username': username, 'password': password})

    return JsonResponse({'message': 'Unauthorized'}, status=401)