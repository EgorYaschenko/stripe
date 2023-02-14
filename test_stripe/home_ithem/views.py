import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from django.shortcuts import render, HttpResponse,loader
from django.views.generic import TemplateView
from .models import Item

stripe.api_key=settings.STRIPE_SECRET_KEY
class SuccessView(TemplateView):
    template_name = "home_item/success.html"




class CancelView(TemplateView):
    template_name = "home_item/cancel.html"

class CreateCheckoutSessionView(View):
    def post(self, request, *args, **kwargs):
        item_id = self.kwargs["pk"]

        item = Item.objects.get(id=item_id)

        YOUR_DOMAIN = "http://127.0.0.1:8000"
        checkout_session = stripe.checkout.Session.create(
            payment_method_types=['card'],
            line_items=[
                {
                    'price_data': {
                        'currency': 'usd',
                        'unit_amount': item.price,
                        'product_data': {
                            'name': item.name

                        },
                    },
                    'quantity': 1,
                },
            ],
            metadata={
                "item_id": item.id
            },
            mode='payment',
            success_url=YOUR_DOMAIN + '/success/',
            cancel_url=YOUR_DOMAIN + '/cancel',
        )
        return JsonResponse({
            'id': checkout_session.id
        })


def Index(request):
    template = loader.get_template('home_item/index.html')
    data=Item.objects.all()
    context = {
        'data': data,

    }

    return HttpResponse(template.render(context, request))







def item_index(request,id):
    template = loader.get_template('home_item/item.html')
    data=Item.objects.get(pk=id)
    context = {
        'data': data,
        "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY,
    }

    return HttpResponse(template.render(context, request))



# Create your views here.
