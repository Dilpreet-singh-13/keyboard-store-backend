from django.db import models

class Switch(models.Model):
    type_choices = [
        ("linear", "linear"),
        ("tactile", "tactile"),
        ("clicky", "clicky")
    ]
    
    name = models.CharField(max_length=200, blank=False, unique=True)
    description = models.TextField(blank=True)
    switch_type = models.CharField(max_length=100, choices=type_choices, default='linear', blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.name

class Keyboard(models.Model):
    type_choices = [
        ("mechanical", "mechanical"),
        ("membrane", "membrane")
    ]

    name = models.CharField(max_length=200, blank=False, unique=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=False)
    description = models.TextField(blank=True)
    keyboard_type = models.CharField(max_length=200, blank=False, choices=type_choices, default='mechanical')
    weight = models.FloatField(null=True,blank=True)
    connectivity_options = models.CharField(max_length=200, blank=True, help_text="Comma-separated values like 'Bluetooth, 2.4GHz, USB-C'")
    switch = models.ForeignKey(Switch, on_delete=models.SET_NULL, related_name='switch', blank=True, null=True)

    def __str__(self):
        return self.name