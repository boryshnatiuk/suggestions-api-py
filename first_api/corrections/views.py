from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import JsonResponse

import requests
import xml.etree.ElementTree as Et


class Suggestions(APIView):
    @staticmethod
    def get_suggestions(q):
        url_path = "http://suggestqueries.google.com/complete/search?output=xml&lr=lang_en&q="
        response = requests.get(url_path+q)
        return Et.fromstring(response.text)

    def construct_suggestions(self, q):
        sg = self.get_suggestions(q)
        suggestions = []
        for suggestion in sg.iter('suggestion'):
            suggestions.append(suggestion.get('data'))
        return suggestions

    def get(self, request):
        q = request.query_params.get('q', None)
        suggestions = self.construct_suggestions(q)
        # return Response({"suggestions": suggestions})
        return JsonResponse({"suggestions": suggestions})
