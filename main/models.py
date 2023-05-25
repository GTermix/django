from django.db import models


class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Category(BaseModel):
    name = models.CharField(max_length=100)
    desc = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "category"
        verbose_name_plural = "categories"
        db_table = "Category"


class ProductInventory(BaseModel):
    quantity = models.PositiveIntegerField()

    class Meta:
        db_table = "Inventory"


class Discount(BaseModel):
    name = models.CharField(max_length=150)
    desc = models.TextField(null=True, blank=True)
    percent = models.DecimalField(max_digits=4, decimal_places=2)
    active = models.BooleanField(default=True, blank=True)

    class Meta:
        db_table = "Discount"


class Product(BaseModel):
    name = models.CharField(max_length=200)
    desc = models.TextField()
    sku_code = models.CharField(max_length=20)
    images = models.ImageField(upload_to='images/')
    price = models.DecimalField(max_digits=20, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    inventory = models.OneToOneField(ProductInventory, on_delete=models.CASCADE)
    discount = models.ForeignKey(Discount, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "Product"
