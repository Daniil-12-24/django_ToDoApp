from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello, world. This is my future To Do application.")

def tasks(request):
    return HttpResponse("Hello, world. This is tasks page.")

def users(request, name, age):
    return HttpResponse(f"""
    <h2>About the user:
    <p>Name - {name}</p>
    <p>Age - {age}</p>
""")
