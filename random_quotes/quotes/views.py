from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from quotes.models import Quote


class QuoteView(View):

    def get(self, request, *args, **kwargs):
        quote = Quote.objects.order_by("?").first()
        data = {
            "quote":quote
        }
        return render(request, "quotes/quotes.html", context=data)

quote_view = QuoteView.as_view()
