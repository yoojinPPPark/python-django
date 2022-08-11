from django.shortcuts import render, HttpResponse, redirect

# def index(request):
# 	return render(request, 'core/index.html')

def index(request):
    return HttpResponse("http response 테스트")

arr = [1,2,3,4,5]

def test2(request):
  return HttpResponse(arr)

json = {
  "a": "1",
  "b": "2",
  "c": "3",
  "d": arr,
}

def test3(request):
  return HttpResponse(json)
