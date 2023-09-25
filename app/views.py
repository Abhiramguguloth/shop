from django.shortcuts import render, redirect
from django.views import View
from .models import Customer, Product, Cart
from .forms import CustomerRegistrationForm, CustomerProfileForm
from django.contrib import messages
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


#def home(request):
# return render(request, 'app/home.html') p

class ProductView(View):
 def get(self, request):
    totalitem = 0
    tops = Product.objects.filter(category='TP')
    jeans = Product.objects.filter(category='JS')
    mobiles = Product.objects.filter(category='M')
    toys = Product.objects.filter(category='TY')
    electronics = Product.objects.filter(category='EL')
    laptops = Product.objects.filter(category='LP')
    if request.user.is_authenticated:
	    totalitem = len(Cart.objects.filter(user=request.user))
    return render(request, 'app/home.html', {'tops':tops, 'jeans':jeans, 'mobiles':mobiles, 'toys':toys, 'electronics':electronics, 'laptops':laptops, 'totalitem':totalitem})
  

#def product_detail(request):
# return render(request, 'app/productdetail.html')

#def change_password(request):
# return render(request, 'app/changepassword.html')

#def login(request):
 #return render(request, 'app/login.html')

#def customerregistration(request):
#return render(request, 'app/customerregistration.html')

class CustomerRegistrationView(View):
 def get(self, request):
    form = CustomerRegistrationForm()
    return render(request, 'app/customerregistration.html', {'form':form})
 
 def post(self, request):
    form = CustomerRegistrationForm(request.POST)
    if form.is_valid():
      messages.success(request, 'Registration Completed Successfully...')
      form.save()
    return render(request, 'app/customerregistration.html', {'form':form}) 
 
 def clean_password1(self):
    password1 = self.cleaned_data.get('password1')
    
    if not re.search(r'[!@#$%^&*(),.?":{}|<>]', password1):
        raise forms.ValidationError("Password must contain at least one special character.")
        
    if not re.search(r'\d', password1):
        raise forms.ValidationError("Password must contain at least one number.")

    if not re.search(r'[A-Z]', password1):
        raise forms.ValidationError("Password must contain at least one capital letter.")

    if not re.search(r'[a-z]', password1):
        raise forms.ValidationError("Password must contain at least one small letter.")

    return password1


@method_decorator(login_required, name='dispatch')
class ProfileView(View):
	def get(self, request):
		form = CustomerProfileForm()
		return render(request, 'app/profile.html', {'form':form, 'active':'btn-success'})
		
	def post(self, request):
		form = CustomerProfileForm(request.POST)
		if form.is_valid():
			user = request.user
			name  = form.cleaned_data['name']
			locality = form.cleaned_data['locality']
			city = form.cleaned_data['city']
			state = form.cleaned_data['state']
			zipcode = form.cleaned_data['zipcode']
			reg = Customer(user=user, name=name, locality=locality, city=city, state=state, zipcode=zipcode)
			reg.save()
			messages.success(request, 'Congratulations!! Profile Updated Successfully.')
		return render(request, 'app/profile.html', {'form':form, 'active':'btn-dark'})

