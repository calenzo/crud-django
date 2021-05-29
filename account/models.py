from django.db import models

class Category(models.Model):

    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "{} {}".format(self.id, self.name)

class Transaction(models.Model):

    id = models.BigAutoField(primary_key=True)
    date = models.DateTimeField(auto_now=True)
    description = models.CharField(max_length=255)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    comments = models.TextField(null=True, blank=True)

    def __str__(self):
        return "{} {}".format(self.id, self.description)