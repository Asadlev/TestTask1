from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Product, Lessons, Group
# Create your views here.


class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        data = ([{'id': product.id, 'name': product.name, 'lessons_count': product.lesson_set.count()} for product in products])
        return Response(data)


class LessonsForProductALIVew(APIView):
    def get(self, request, product_id):
        user = request.user
        product = Product.objects.get(id=product_id)

        if user.objects is product:
            lessons = Lessons.objects.filter(product=product)
            data = [{ 'id': lesson.id, 'title': lesson.title, 'video': lesson.video } for lesson in lessons]
            return Response(data)











