from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=10)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.name


class PcPart(models.Model):
    parts = [
        ('CPU', 'Processor'),
        ('GPU', 'Graphics Card'),
        ('RAM', 'Memory'),
        ('SSD', 'Solid State Drive'),
        ('HDD', 'Hard Disk Drive'),
        ('MB', 'Motherboard'),
        ('CASE', 'Cases')
    ]

    part = models.CharField(max_length=10, choices=parts)
    name = models.CharField(max_length=120)
    manufacturer = models.CharField(max_length=120)
    price = models.FloatField()
    stock = models.IntegerField()
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return f"{self.part} - {self.name} ({self.manufacturer}) - ${self.price} (Stock: {self.stock})"

    @property
    def image_url(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url

class Specs(models.Model):
    pc_part = models.ForeignKey(PcPart, on_delete=models.CASCADE, related_name='specs')
    details = models.TextField()

    def __str__(self):
        return f"{self.pc_part.name} Specifications {self.details}"

class Review(models.Model):
    pc_part = models.ForeignKey(PcPart, on_delete=models.CASCADE, related_name='reviews')
    review = models.TextField()
    reviewer = models.CharField(max_length=120)
    rating = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)], default=0)
    review_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.pc_part.name} - Review by {self.reviewer} (Rating: {self.rating})"

class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='orders')
    date_ordered = models.DateField(auto_now_add=True)
    completed = models.BooleanField(default=False)
    transaction_id = models.CharField(max_length=100, null=True)

    @property
    def get_cart_total(self):
        orderitems = self.items.all()
        total = sum([item.get_total for item in orderitems])
        return total

    @property
    def get_cart_items(self):
        orderitems = self.items.all()
        total = sum([item.quantity for item in orderitems])  # Summing the quantity of each item
        return total

    def __str__(self):
        return f"{self.customer} - {self.date_ordered}"


class OrderItem(models.Model):
    pc_part = models.ForeignKey(PcPart, on_delete=models.CASCADE, related_name='order_items')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField()
    date_added = models.DateField(auto_now_add=True)

    @property
    def get_total(self):
        total = self.pc_part.price * self.quantity
        return total

    def __str__(self):
        return f"{self.order} - {self.date_added}"

class ShippingAddress(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True)
    address = models.CharField(max_length=200, null=False)
    city = models.CharField(max_length=200, null=False)
    state = models.CharField(max_length=200, null=False)
    zip_code = models.CharField(max_length=200, null=False)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.address

