from django.db import models


class Task(models.Model):

    PRIORITY_CHOICES = [
        ("High", "High"),
        ("Medium", "Medium"),
        ("Low", "Low"),
    ]

    CATEGORY_CHOICES = [
        ("School", "School"),
        ("Personal", "Personal"),
        ("Work", "Work"),
        ("Others", "Others"),
    ]

    STATUS_CHOICES = [
        ("Pending", "Pending"),
        ("Completed", "Completed"),
    ]

    title = models.CharField(max_length=200)

    description = models.TextField(
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=100,
        choices=CATEGORY_CHOICES,
        default="Personal"
    )

    priority = models.CharField(
        max_length=20,
        choices=PRIORITY_CHOICES,
        default="Medium"
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="Pending"
    )

    due_date = models.DateField(
        blank=True,
        null=True
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return self.title