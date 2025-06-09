from django.db import models
from django.utils import timezone

class ContactMessage(models.Model):
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Phone")
    subject = models.CharField(max_length=200, verbose_name="Subject")
    message = models.TextField(verbose_name="Message")
    created_at = models.DateTimeField(default=timezone.now)
    is_replied = models.BooleanField(default=False, verbose_name="Replied")
    
    def __str__(self):
        return f"{self.name} - {self.subject}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Contact Message"
        verbose_name_plural = "Contact Messages"

class QuoteRequest(models.Model):
    PROJECT_TYPES = [
        ('website', 'Website Development'),
        ('game', 'Game Development'),
        ('mobile', 'Mobile App Development'),
        ('django', 'Django Backend'),
        ('other', 'Other')
    ]
    
    BUDGET_RANGES = [
        ('5k-15k', '₹5,000 - ₹15,000'),
        ('15k-30k', '₹15,000 - ₹30,000'),
        ('30k-50k', '₹30,000 - ₹50,000'),
        ('50k-1l', '₹50,000 - ₹1,00,000'),
        ('1l+', '₹1,00,000+')
    ]
    
    name = models.CharField(max_length=100, verbose_name="Name")
    email = models.EmailField(verbose_name="Email")
    phone = models.CharField(max_length=15, verbose_name="Phone")
    company = models.CharField(max_length=100, blank=True, verbose_name="Company")
    project_type = models.CharField(max_length=20, choices=PROJECT_TYPES, verbose_name="Project Type")
    budget_range = models.CharField(max_length=20, choices=BUDGET_RANGES, verbose_name="Budget Range")
    description = models.TextField(verbose_name="Project Description")
    deadline = models.CharField(max_length=50, verbose_name="Deadline")
    features_needed = models.TextField(blank=True, verbose_name="Features Needed")
    created_at = models.DateTimeField(default=timezone.now)
    is_processed = models.BooleanField(default=False, verbose_name="Processed")
    
    def __str__(self):
        return f"{self.name} - {self.get_project_type_display()}"
    
    class Meta:
        ordering = ['-created_at']
        verbose_name = "Quote Request"
        verbose_name_plural = "Quote Requests"