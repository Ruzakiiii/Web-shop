from django.db import models

# Create your models here.
class Categories(models.Model):
    category_name = models.CharField(max_length=20)

    def __str__(self):
        return self.category_name

class Products(models.Model):
    product_name = models.CharField(max_length=50)
    product_price = models.IntegerField()
    product_des = models.CharField(max_length=880)
    product_cotegory = models.ForeignKey(Categories, on_delete=models.CASCADE, null=True, blank=True)
    product_image = models.ImageField(null=True, blank=True)


    def __str__(self):
        return self.product_name


class Cart(models.Model):
    user_id = models.IntegerField()
    product_name = models.ForeignKey(Products,on_delete=models.CASCADE, null=True, blank=True)
    product_count = models.IntegerField()

    def __str__(self):
        return str(self.user_id)


class Sales(models.Model):
    sale_name = models.CharField(max_length=70)
    sale_percent = models.IntegerField()
    sale_product = models.ManyToManyField(Products)

    def __str__(self):
        return self.sale_name