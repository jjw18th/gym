from django.contrib import admin

# Register your models here.
from products.models import Products
from products.models import Batches
from products.models import Diet
from products.models import Message
from products.models import Recipe
from products.models import Faq
admin.site.register(Products)
admin.site.register(Message)
admin.site.register(Diet)
admin.site.register(Batches)
admin.site.register(Recipe)
admin.site.register(Faq)
