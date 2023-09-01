from django.shortcuts import render
import requests
from .models import Coderdata
# Create your views here.
def savingandviewing(request):
    url='https://codeforces.com/api/user.ratedList'
    resp=requests.get(url)
    data=resp.json()
    cop=data["result"].copy()
    for users in cop:
        if users.get("organization", {}) != "IIT Kharagpur":
            data["result"].remove(users)
    return render(request, 'blog/home.html', {'data': data})
