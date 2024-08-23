from django.db import models

class WasteImage(models.Model):
    image = models.ImageField(upload_to='uploads/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    plastic_percentage = models.FloatField(null=True, blank=True)
    metal_percentage = models.FloatField(null=True, blank=True)
    # Add fields for other waste types as needed
