from django.db import models

# Create your models here.
from form_demos2.web.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_TASKS = 3
    name = models.CharField(max_length=50)

    profile_image = models.ImageField(null=True, blank=True, upload_to='persons')

    def __str__(self):
        return self.name


class Todo(models.Model):
    text = models.CharField(null=False, blank=False, max_length=25, validators=(validate_text,))
    priority = models.IntegerField(null=False, blank=False, validators=(ValueInRangeValidator(1, 25),))
    is_done = models.BooleanField(null=False, blank=False, default=False)

    assignee = models.ForeignKey(Person, on_delete=models.RESTRICT)

