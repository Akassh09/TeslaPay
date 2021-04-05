from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()

class Transaction(models.Model):
    made_by = models.ForeignKey(User, related_name='transactions', on_delete=models.CASCADE)
    made_on = models.DateTimeField(auto_now_add=True)
    amount = models.IntegerField()
    order_id = models.CharField(max_length=100,unique=True,null=True,blank=True)
    checksum = models.CharField(max_length=100,null=True,blank=True)

    def save(self, *args, **kwargs):
        if self.order_id and self.made_on and self.id:
            self.order_id = self.made_on.strftime('TeslaPay%Y%m%dODR') +  str(self.id)
        return super().save(*args, **kwargs)

