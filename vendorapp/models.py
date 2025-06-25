from django.db import models
from django.contrib.auth.models import User

class VendorRegistration(models.Model):
    # Step 1: General Information
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True)
    supplier_name = models.CharField(max_length=255)
    supplier_alias = models.CharField(max_length=255, blank=True)
    address1 = models.CharField(max_length=255)
    address2 = models.CharField(max_length=255, blank=True)
    address3 = models.CharField(max_length=255, blank=True)
    city = models.CharField(max_length=100)
    pin_code = models.CharField(max_length=10)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    mobile = models.CharField(max_length=15)
    landline = models.CharField(max_length=15, blank=True)
    fax = models.CharField(max_length=50, blank=True)
    email = models.EmailField()
    alt_email = models.EmailField(blank=True)
    
    products_offered = models.TextField()
    product_category = models.CharField(max_length=100)

    # Step 2: Legal / Statutory
    pan_no = models.CharField(max_length=20)
    gst_no = models.CharField(max_length=30)
    gst_type = models.CharField(max_length=50)
    msme_certificate = models.FileField(upload_to='uploads/mse_certificates/', null=True, blank=True)

    
    msme_no = models.CharField(max_length=50, blank=True)
    
    msme_valid_date = models.DateField(null=True, blank=True)
    gem_no = models.CharField(max_length=50, blank=True)
    

    # Step 3: Financial Info
    bank_name = models.CharField(max_length=100)
    bank_code = models.CharField(max_length=20)
    bank_city = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=15)
    account_no = models.CharField(max_length=30)
    account_type = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=20)
   
    # Step 4 skipped - assumed to be product info already included

    # Step 5: Declaration
    declaration = models.BooleanField(default=False)
    additional_notes = models.TextField(blank=True)

    # System Fields
    is_approved = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)
    STATUS_CHOICES = (
        ('Pending', 'Pending'),
        ('Accepted', 'Accepted'),
        ('Rejected', 'Rejected'),
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.supplier_name

