from django.db import models

class guest_nm(models.Model):
    guest_name = models.CharField(max_length=255)
    guest_respond = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.guest_name} - {self.guest_respond}"