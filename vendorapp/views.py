from django.shortcuts import render
from django.http import HttpResponse
from .models import VendorRegistration
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime
from django.contrib import messages
from django.shortcuts import render, redirect, get_object_or_404
from .models import VendorRegistration
from django.contrib.auth.decorators import user_passes_test
from django.core.exceptions import PermissionDenied
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.models import User
import re
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required


# For testing only; remove in production and use csrf_token in HTML
def register(request):
    if request.method == "POST":
        print("PAN NO from form:", request.POST.get('pan_no'))
        supplier_name = request.POST.get("supplier_name")
        supplier_alias = request.POST.get("supplier_alias", "")
        address1 = request.POST.get("address1")
        address2 = request.POST.get("address2", "")
        address3 = request.POST.get("address3", "")
        city = request.POST.get("city")
        pin_code = request.POST.get("pin_code")
        state = request.POST.get("state")
        country = request.POST.get("country")
        mobile = request.POST.get("mobile")
        landline = request.POST.get("landline", "")
        fax = request.POST.get("fax", "")
        email = request.POST.get("email")
        alt_email = request.POST.get("alt_email", "")
        
        products_offered = request.POST.get("products_offered")
        product_category = request.POST.get("product_category")

        # Step 2: Statutory Info
        pan_no = request.POST.get("pan_no")
        gst_no = request.POST.get("gst_no")
        gst_type = request.POST.get("gst_type")
        
        msme_certificate = request.FILES.get('mse_certificate')

        msme_no = request.POST.get("mse_no", "")
        
        msme_valid_date = request.POST.get("mse_valid_date") or None
        gem_no = request.POST.get("gem_no", "")
        

        # Step 3: Financial Info
        bank_name = request.POST.get("bank_name")
        bank_code = request.POST.get("bank_code")
        bank_city = request.POST.get("bank_city")
        branch_name = request.POST.get("branch_name")
        ifsc = request.POST.get("ifsc")
        account_no = request.POST.get("account_no")
        account_type = request.POST.get("account_type")
        payment_type = request.POST.get("payment_type")
        
        
        # Step 4: Declaration
        declaration = request.POST.get("declaration") == "on"
        additional_notes = request.POST.get("additional_notes", "")
        
        # Check if the vendor name already exists
        if VendorRegistration.objects.filter(supplier_name=supplier_name).exists():
            print("error comes")
            messages.error(request, "Username already exists")
            return render(request, 'register.html', {'prefill': request.POST,'current_step': 0 })
                # Check if the email already exists
        if VendorRegistration.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'register.html', {'prefill': request.POST})

        # Validate mobile number format
        if not re.match(r'^[6-9]\d{9}$', mobile):
            messages.error(request, "Invalid mobile number")
            return render(request, 'register.html', {'prefill': request.POST})

        # Validate PAN format
        pan_regex = r'^[A-Z]{5}[0-9]{4}[A-Z]$'
        if not re.match(pan_regex, pan_no):
            messages.error(request, "Invalid PAN format")
            return render(request, 'register.html', {'prefill': request.POST})

        # Validate GST if provided
        gst_regex = r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}[Z]{1}[A-Z\d]{1}$'
        if gst_no and not re.match(gst_regex, gst_no):
            messages.error(request, "GST number is not valid")
            return render(request, 'register.html', {'prefill': request.POST})

        # Validate IFSC code
        if not re.match(r'^[A-Z]{4}0[A-Z0-9]{6}$', ifsc):
            messages.error(request, "Invalid IFSC format")
            return render(request, 'register.html', {'prefill': request.POST})

        # Validate Account Number (should be 9 to 18 digits)
        if not re.fullmatch(r'^\d{9,18}$', account_no):
            messages.error(request, "Invalid account number. It should be 9 to 18 digits.")
            return render(request, 'register.html', {'prefill': request.POST})

        # Basic alphanumeric check for MSME number
        if not re.match(r'^[A-Za-z0-9/-]+$', msme_no):
            messages.error(request, "Invalid MSME Registration Number format.")
            return render(request, 'register.html', {'prefill': request.POST})

        # Basic alphanumeric check for GeM number
        if not re.match(r'^[A-Za-z0-9/-]+$', gem_no):
            messages.error(request, "Invalid GeM Registration Number format.")
            return render(request, 'register.html', {'prefill': request.POST})
        
        if VendorRegistration.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return render(request, 'register.html', {'prefill': request.POST})
        
        if VendorRegistration.objects.filter(pan_no=pan_no).exists():
            messages.error(request, "PAN already exists")
            return render(request, 'register.html', {'prefill': request.POST})
        
        if gst_no and VendorRegistration.objects.filter(gst_no=gst_no).exists():
            messages.error(request, "GST number already exists")
            return render(request, 'register.html', {'prefill': request.POST})
        
        if VendorRegistration.objects.filter(gem_no=gem_no).exists():
            messages.error(request, "GeM registration number already exists")
            return render(request, 'register.html', {'prefill': request.POST})
        
        if VendorRegistration.objects.filter(msme_no=msme_no).exists():
            messages.error(request, "MSME registration number already exists")
            return render(request, 'register.html', {'prefill': request.POST})
        
        if VendorRegistration.objects.filter(account_no=account_no).exists():
            messages.error(request, "Bank account number already exists")
            return render(request, 'register.html', {'prefill': request.POST})

        


        try:
            VendorRegistration.objects.create(
                supplier_name=supplier_name,
                supplier_alias=supplier_alias,
                address1=address1,
                address2=address2,
                address3=address3,
                city=city,
                pin_code=pin_code,
                state=state,
                country=country,
                mobile=mobile,
                landline=landline,
                fax=fax,
                email=email,
                alt_email=alt_email,
                
                products_offered=products_offered,
                product_category=product_category,
                pan_no=pan_no,
                gst_no=gst_no,
                gst_type=gst_type,
                
                msme_certificate=msme_certificate,
                msme_no=msme_no,
                
                msme_valid_date=msme_valid_date,
                gem_no=gem_no,
                
                bank_name=bank_name,
                bank_code=bank_code,
                bank_city=bank_city,
                branch_name=branch_name,
                ifsc=ifsc,
                account_no=account_no,
                account_type=account_type,
                payment_type=payment_type,
                
                declaration=declaration,
                additional_notes=additional_notes
)

            return HttpResponse("Registration successful!")

        except Exception as e:
            return HttpResponse(f"❌ Error while saving: {str(e)}", status=500)

    return render(request, "register.html")




def is_admin(user):
    if user.is_superuser:
        return True
    
def not_authorized(request):
    return render(request, 'not_authorized.html')
  # Or use is_staff if you prefer

@user_passes_test(is_admin, login_url='/not-authorized/')
def admin_dashboard(request):
    vendors = VendorRegistration.objects.all().order_by('-id')
    return render(request, 'admin-dashboard.html', {'vendors': vendors})

from django.core.mail import send_mail
from django.conf import settings
import random
import string

def generate_password(length=8):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

@user_passes_test(is_admin, login_url='/not-authorized/')
def update_status(request, vendor_id, new_status):
    vendor = get_object_or_404(VendorRegistration, id=vendor_id)
    vendor.status = new_status
    vendor.save()

    # Send email if Accepted
    if new_status == "Accepted" and vendor.user is None:
        username = vendor.email.split('@')[0]
        password = generate_password()
        print("accepted")

        user = User.objects.create_user(
            username=username,
            email=vendor.email,
            password=password,
            first_name=vendor.supplier_name
        )
        vendor.user = user
        vendor.save()

        # Send Email
        subject = "Vendor Account Approved - DCL Portal"
        message = f"""
        Dear {vendor.supplier_name},

        Your registration has been approved.

        Login Credentials:
        Username: {user.username}
        Password: {password}

        You can now access the homepage using the link below:
        http://127.0.0.1:8000/register/

        Regards,  
        DCL Vendor Portal Team
        """

        send_mail(subject, message, settings.EMAIL_HOST_USER, [vendor.email])

    if new_status == 'Rejected':
        subject = "Vendor Registration Rejected"
        message = f"""
Dear {vendor.supplier_name},

We regret to inform you that your vendor registration has been rejected.

If you have any queries or believe this was a mistake, please contact our support.

Best Regards,
DCL Vendor Registration Team
"""
        send_mail(subject, message, settings.EMAIL_HOST_USER, [vendor.email])

    return redirect('admin-dashboard')



def startingpage(request):
    
    return render(request,"startingpage.html")

def instructionpage(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        print(username,password)
        print("received")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")  # success → redirect to instructions
        else:
            return render(request, "instructionpage.html", {"error": "Invalid credentials"})
    
    return render(request,"instructionpage.html")

def instructionregisteruser(request):
    return render(request,"instructionregisteruser.html")

@login_required
def home(request):
    return render(request,"home.html")




    
