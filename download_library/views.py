#from django.shortcuts import render

# Create your views here.

#from django.shortcuts import render

# Create your views here.

'''from django.shortcuts import render, get_object_or_404
from .models import Category, File

def library_home(request):
    categories = Category.objects.all()
    return render(request, 'library_home.html', {'categories': categories})

def category_files(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    files = category.files.all()
    return render(request, 'category_files.html', {'category': category, 'files': files})


from django.shortcuts import render, get_object_or_404
from .models import Category, File, Customer

def customer_list(request):
    customers = Customer.objects.all()  # Get all customers
    return render(request, 'customer_list.html', {'customers': customers})

def library_home(request):
    categories = Category.objects.all()
    return render(request, 'library_home.html', {'categories': categories})

def customer_list(request):
    customers = Customer.objects.all()  # Get all customers
    return render(request, 'customer_list.html', {'customers': customers})

def category_files(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    customer_id = request.GET.get('customer_id')  # Retrieve customer ID from the query parameter if provided

    if customer_id:
        customer = get_object_or_404(Customer, id=customer_id)
        files = category.files.filter(customers=customer)
    else:
        files = category.files.all()  # Display all files if no customer is specified

    return render(request, 'category_files.html', {'category': category, 'files': files})

def customer_files(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    files = customer.files.all()  # Get all files associated with this customer
    return render(request, 'customer_files.html', {'customer': customer, 'files': files})

from django.shortcuts import render, get_object_or_404
from .models import Category, File, Customer

def customer_list(request):
    customers = Customer.objects.all()  # Get all customers
    return render(request, 'library/customer_list.html', {'customers': customers})

def customer_files(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    files = customer.files.all()  # Get all files associated with this customer
    return render(request, 'library/customer_files.html', {'customer': customer, 'files': files})

'''
from django.shortcuts import render, get_object_or_404 # type: ignore
from .models import Category, File, Customer

def library_home(request):
    categories = Category.objects.all()
    return render(request, 'library_home.html', {'categories': categories})

def category_files(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    files = category.files.all()  # Display all files for the category
    return render(request, 'category_files.html', {'category': category, 'files': files})

def customer_list(request):
    customer = Customer.objects.all()  # Get all customers
    return render(request, 'customer_list_template.html', {'customers': customer})

def customer_files(request, customer_id):
    customer = get_object_or_404(Customer, id=customer_id)
    files = customer.files.all()  # Get all files associated with this customer
    return render(request, 'customer_files_template.html', {'customer': customer, 'files': files})


