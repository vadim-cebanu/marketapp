from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse, HttpResponseNotFound, Http404
import json
from django.utils.text import slugify
from .dummy_data import gadgets
from django.urls import reverse
from django.views import View

def start_page_view(request):
   return render(request, 'market_app/test.html')

def single_gadget_int_view(request,gadget_id):
   if len(gadgets) > gadget_id:
      new_slug= slugify(gadgets[gadget_id]["name"])
      new_url= reverse("gadget_slug_url", args=[new_slug])
      return redirect(new_url)
   return HttpResponseNotFound("not found by me")

class GadgetView(View):
   def  get(self, request, gadget_slug):
      gadget_match= None
      for gadget in gadgets:
          if slugify(gadget["name"]) == gadget_slug:
            gadget_match=gadget
         
      if gadget_match:
         return JsonResponse(gadget_match)
      raise Http404()
  
   
def single_gadget_post_view(request):
   if request.method == "POST":
      try:
        data = json.loads(request.body)
        print(f"received data : {data}")
        return JsonResponse({"response": "That's all"})
      except:
         return JsonResponse({"response": "That was nothing at all"})