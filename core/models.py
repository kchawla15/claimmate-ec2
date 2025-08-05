from django.db import models
from django.contrib.auth.models import User

class WarrantyItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    store_name = models.CharField(max_length=100)
    product_type = models.CharField(max_length=100)
    warranty_duration_days = models.PositiveIntegerField(null=True, blank=True)
    purchase_date = models.DateField()
    receipt_file = models.FileField(upload_to='receipts/', null=True, blank=True)


    def expiry_date(self):
        if self.warranty_duration_days and self.purchase_date:
            from datetime import timedelta
            return self.purchase_date + timedelta(days=self.warranty_duration_days)
        return None

    def __str__(self):
        return f"{self.store_name} - {self.product_type}"
