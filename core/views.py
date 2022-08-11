from django.shortcuts import render, HttpResponse, JsonResponse, redirect

# def index(request):
# 	return render(request, 'core/index.html')

def index(request):
    return HttpResponse("http response 테스트")

def test2(request):
  return JsonResponse("json response 테스트")

json = {
  "a": "1",
  "b": "2",
  "c": "3",
}

def test3(request):
  return JsonResponse(json)
