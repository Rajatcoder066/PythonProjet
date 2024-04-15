from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
from datetime import datetime
from home.models import Contact
from home.models import Registration
from home.models import Upload
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login
from django.template.loader import get_template
from xhtml2pdf import pisa

# Create your views here.
def index(request):
        context={'products' : Upload.objects.all()}
        return render(request,'index.html',context)
        #return HttpResponse("Hello welcome the routing page")
def about(request):
        #return HttpResponse("This is about page")
        return render(request,'about.html')
def services(request):
        #return HttpResponse("This is Service page")
        return render(request,'services.html')
def contact(request):
        if request.method=='POST':
                name=request.POST.get('name')
                email=request.POST.get('email')
                subject=request.POST.get('subject')
                message=request.POST.get('message')
                contact=Contact(name=name,email=email,subject=subject,message=message,date=datetime.today())
                contact.save()
        #return HttpResponse("This is contact page")

        return render(request,'contact.html')
def reg(request):
        if request.method=='POST':
                 name=request.POST.get('name')
                 email=request.POST.get('email')
                 password=request.POST.get('password')
                 phone=request.POST.get('phone')
                 Data=Registration(name=name,email=email,password=password,phone=phone,date=datetime.today())
                 Data.save()
                 messages.success(request, 'Your message has been sent!')
        return render(request,'reg.html')
def login(request): 
        if request.method=="POST":
                reg=Registration.objects.all()
                email = request.POST.get('email')
                password = request.POST.get('password')
                print(email, password)
                
                Registration = authenticate(email=email, password=password)

                if Registration is not None:
            # A backend authenticated the credentials
                        login(request, Registraion)
                        return redirect("index")

                else:
            # No backend authenticated the credentials
                         return render(request, 'login.html')
        return render(request, 'login.html')
def data(request):
         if request.method=='POST':
                 name=request.POST.get('name')
                 url=request.POST.get('url')
                 price=request.POST.get('price')
                 offer=request.POST.get('offer')
                 description=request.POST.get('description')
                 spec=request.POST.get('spec')
                 category=request.POST.get('category')
                 uploadData=Upload(name=name,url=url,price=price,offer=offer,description=description,spec=spec,category=category,date=datetime.today())
                 uploadData.save()
                 messages.success(request, 'Your message has been sent!')
         return render(request,'data.html')
def product_detail(request, pk):
    product = get_object_or_404(Upload, pk=pk)
    context = {'product': product}
    return render(request,'product_detail.html',context)
def kart(request,pk):
    product = get_object_or_404(Upload, pk=pk)
    context = {'product': product}
    return render(request,'kart.html',context)
def order(request,pk):
        product = get_object_or_404(Upload, pk=pk)
        context = {'product': product}
        return render(request,'order.html',context)
def contin(request,pk):
    product = get_object_or_404(Upload, pk=pk)
    context = {'product': product}
    return render(request,'continue.html',context)
                        

def download(request):

    # Define the context data to render the template
    context = {'my_data': 'Hello, world!'}

    # Get the HTML template to convert
    template = get_template('continue.html')
    html = template.render(context)

    # Define the output PDF file name
    pdf_file = 'my_output.pdf'

    # Convert the HTML to PDF using xhtml2pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename=my_output.pdf'

    # Create a PDF object and convert the HTML to PDF
    pisa.CreatePDF(html, dest=response)

    # If we need to generate a PDF file instead of returning the response
    # uncomment the following lines instead of the previous one
    # with open(pdf_file, 'w+b') as pdf_file:
    #     pisa.CreatePDF(html, dest=pdf_file)

    return response
