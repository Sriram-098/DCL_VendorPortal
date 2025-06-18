from django.shortcuts import render
from django.http import HttpResponse
from .models import VendorRegistration
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime

@csrf_exempt  # For testing only; remove in production and use csrf_token in HTML
def register(request):
    if request.method == "POST":
        print("PAN NO from form:", request.POST.get('pan_no'))

        try:
            VendorRegistration.objects.create(
                # Step 1: General Info
                supplier_name=request.POST.get('supplier_name'),
                supplier_alias=request.POST.get('supplier_alias', ''),
                address1=request.POST.get('address1'),
                address2=request.POST.get('address2', ''),
                address3=request.POST.get('address3', ''),
                city=request.POST.get('city'),
                pin_code=request.POST.get('pin_code'),
                state=request.POST.get('state'),
                country=request.POST.get('country'),
                mobile=request.POST.get('mobile'),
                landline=request.POST.get('landline', ''),
                fax=request.POST.get('fax', ''),
                email=request.POST.get('email'),
                alt_email=request.POST.get('alt_email', ''),
                proprietor_name=request.POST.get('proprietor_name'),
                group_name=request.POST.get('group_name', ''),
                holding_company=request.POST.get('holding_company', ''),
                subsidiary=request.POST.get('subsidiary', ''),
                established_year=request.POST.get('established_year'),
                contact_person=request.POST.get('contact_person'),
                designation=request.POST.get('designation', ''),
                department=request.POST.get('department', ''),
                ownership_type=request.POST.get('ownership_type'),
                business_nature=request.POST.get('business_nature'),
                scst_indicator=request.POST.get('scst_indicator', ''),
                women_enterprise=request.POST.get('women_enterprise', ''),
                application_type=request.POST.get('application_type'),
                products_offered=request.POST.get('products_offered'),
                product_category=request.POST.get('product_category'),

                # Step 2: Statutory Info
                pan_no=request.POST.get('pan_no'),
                gst_no=request.POST.get('gst_no'),
                gst_type=request.POST.get('gst_type'),
                nsic_no=request.POST.get('nsic_no', ''),
                mse_no=request.POST.get('mse_no', ''),
                approved_vendor_of=request.POST.get('approved_vendor_of', ''),
                nsic_valid_date=request.POST.get('nsic_valid_date') or None,
                mse_valid_date=request.POST.get('mse_valid_date') or None,
                gem_no=request.POST.get('gem_no', ''),
                nsic_permanent=request.POST.get('nsic_permanent', ''),
                ssi_permanent=request.POST.get('ssi_permanent', ''),
                iso9000=request.POST.get('iso9000', ''),
                iso14000=request.POST.get('iso14000', ''),
                iso18000=request.POST.get('iso18000', ''),
                cin_no=request.POST.get('cin_no', ''),

                # Step 3: Financial Info
                bank_name=request.POST.get('bank_name'),
                bank_code=request.POST.get('bank_code'),
                bank_city=request.POST.get('bank_city'),
                branch_name=request.POST.get('branch_name'),
                ifsc=request.POST.get('ifsc'),
                account_no=request.POST.get('account_no'),
                account_type=request.POST.get('account_type'),
                payment_type=request.POST.get('payment_type'),
                turnover_year1=request.POST.get('turnover_year1'),
                turnover_amt1=request.POST.get('turnover_amt1'),
                turnover_year2=request.POST.get('turnover_year2'),
                turnover_amt2=request.POST.get('turnover_amt2'),
                turnover_year3=request.POST.get('turnover_year3'),
                turnover_amt3=request.POST.get('turnover_amt3'),

                # Step 4: Declaration
                declaration=request.POST.get('declaration') == 'on',
                additional_notes=request.POST.get('additional_notes', '')
            )
            return HttpResponse("Registration successful!")

        except Exception as e:
            return HttpResponse(f"❌ Error while saving: {str(e)}", status=500)

    return render(request, "register.html")




def startingpage(request):
    return render(request,"startingpage.html")

def instructionpage(request):
    return render(request,"instructionpage.html")

def instructionregisteruser(request):
    return render(request,"instructionregisteruser.html")


    
