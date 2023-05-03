from django.db import models


class Customer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100, null=True, blank=True)
    contact = models.OneToOneField(to='Contact', on_delete=models.CASCADE)
    address = models.ForeignKey(to="Address", on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"


class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to="product/", null=True)
    in_stock = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.title} - {self.price}"


class Order(models.Model):
    customer = models.ForeignKey(to=Customer, on_delete=models.CASCADE, related_name="orders")
    product = models.ManyToManyField(to=Product, related_name="orders")
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer} - {self.total_price}"


class Contact(models.Model):
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.email}"


class Address(models.Model):
    UZB = 'uzb'
    RUS = 'rus'
    TRK = 'trk'
    QZK = 'qzk'
    TJK = 'tjk'

    COUNTRIES = (
        (UZB, "Uzbekistan"),
        (RUS, "Russia"),
        (TRK, "Turkmenistan"),
        (QZK, "Qozoqistan"),
        (TJK, "Tojikistan")
    )

    street = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    zipcode = models.CharField(max_length=15)
    country = models.CharField(max_length=20, choices=COUNTRIES, default=UZB)

    def __str__(self):
        return f"{self.street}, {self.city}, {self.country}"
