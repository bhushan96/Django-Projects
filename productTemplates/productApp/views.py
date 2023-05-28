from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'productApp/index.html')

def electronics(request):
    product_dict = {
        'heading': "Electornics",
        'product1': "Mac",
        'image1': "images/mac.png",
        'product2': "IPhone",
        'image2': "images/iphone.jpg",
        'product3': "Dell",
        'image3': "images/dell.jpg",
    }
    return render(request, 'productApp/products.html', product_dict)

def toys(request):
    product_dict = {
        'heading': "Toys",
        'product1': "Remote Car",
        'image1': "images/remote-car.jpeg",
        'product2': "Drone",
        'image2': "images/drone.jpg",
        'product3': "Rocket Luncher",
        'image3': "images/rocket-launcher.jpg",
    }
    return render(request, 'productApp/products.html', product_dict)

def shoes(request):
    product_dict = {
        'heading': "Shoes",
        'product1': "Nike",
        'image1': "images/nike.jpeg",
        'product2': "Adidas",
        'image2': "images/adidas.jpeg",
        'product3': "Reebok",
        'image3': "images/reebok.jpeg",
    }
    return render(request, 'productApp/products.html', product_dict)
