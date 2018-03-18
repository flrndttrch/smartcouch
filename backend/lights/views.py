# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Create your views here.
from django.shortcuts import render, get_object_or_404, get_list_or_404

from lights.models import LightingHistory, Lighting


def index(request):
    latest_lighting_list = get_list_or_404(LightingHistory.objects.order_by('-activation_date'))[:5]
    context = {'latest_lighting_list': latest_lighting_list}
    return render(request, 'lights/index.html', context)

def detail(request, lighting_id):
    lighting = get_object_or_404(Lighting, pk=lighting_id)
    return render(request, 'lights/detail.html', {'lighting': lighting})

# class LatestLightingView(DetailView):
#     model = LightingHistory
#     # context_object_name = 'lighting_history'
#     # queryset = LightingHistory.objects.order_by('-activation_date')
#
#     def get(self, request):
#         try:
#             latest = LightingHistory.objects.order_by('-activation_date').first()
#             # latest_serialized = serializers.serialize('json', [latest], ensure_ascii=False)[1:-1]
#         except LightingHistory.DoesNotExist:
#             return Http404("No Lighting activated yet.")
#         return render(request, 'polls/detail.html', {'latest': latest})