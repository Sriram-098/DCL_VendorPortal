from django.db import models

class VendorRegistration(models.Model):
    # Step 1: General Information
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
    proprietor_name = models.CharField(max_length=255)
    group_name = models.CharField(max_length=255, blank=True)
    holding_company = models.CharField(max_length=255, blank=True)
    subsidiary = models.CharField(max_length=255, blank=True)
    established_year = models.IntegerField()
    contact_person = models.CharField(max_length=255)
    designation = models.CharField(max_length=100, blank=True)
    department = models.CharField(max_length=100, blank=True)
    ownership_type = models.CharField(max_length=100)
    business_nature = models.CharField(max_length=100)
    scst_indicator = models.CharField(max_length=50, blank=True)
    women_enterprise = models.CharField(max_length=10, blank=True)
    application_type = models.CharField(max_length=50)
    products_offered = models.TextField()
    product_category = models.CharField(max_length=100)

    # Step 2: Legal / Statutory
    pan_no = models.CharField(max_length=20)
    gst_no = models.CharField(max_length=30)
    gst_type = models.CharField(max_length=50)
    nsic_no = models.CharField(max_length=50, blank=True)
    mse_no = models.CharField(max_length=50, blank=True)
    approved_vendor_of = models.CharField(max_length=255, blank=True)
    nsic_valid_date = models.DateField(null=True, blank=True)
    mse_valid_date = models.DateField(null=True, blank=True)
    gem_no = models.CharField(max_length=50, blank=True)
    nsic_permanent = models.CharField(max_length=10, blank=True)
    ssi_permanent = models.CharField(max_length=10, blank=True)
    iso9000 = models.CharField(max_length=10, blank=True)
    iso14000 = models.CharField(max_length=10, blank=True)
    iso18000 = models.CharField(max_length=10, blank=True)
    cin_no = models.CharField(max_length=30, blank=True)

    # Step 3: Financial Info
    bank_name = models.CharField(max_length=100)
    bank_code = models.CharField(max_length=20)
    bank_city = models.CharField(max_length=100)
    branch_name = models.CharField(max_length=100)
    ifsc = models.CharField(max_length=15)
    account_no = models.CharField(max_length=30)
    account_type = models.CharField(max_length=20)
    payment_type = models.CharField(max_length=20)
    turnover_year1 = models.IntegerField()
    turnover_amt1 = models.CharField(max_length=50)
    turnover_year2 = models.IntegerField()
    turnover_amt2 = models.CharField(max_length=50)
    turnover_year3 = models.IntegerField()
    turnover_amt3 = models.CharField(max_length=50)

    # Step 4 skipped - assumed to be product info already included

    # Step 5: Declaration
    declaration = models.BooleanField(default=False)
    additional_notes = models.TextField(blank=True)

    # System Fields
    is_approved = models.BooleanField(default=False)
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.supplier_name

