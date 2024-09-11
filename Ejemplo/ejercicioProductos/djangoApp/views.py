from django.shortcuts import render

# Create your views here.
def index(request):
    categorias = ['Electronica', 'Juguetes', 'Ropa']
    return render(request, 'djangoApp/index.html', {'categorias': categorias})

def productos(request, categoria):
    producto_data = {
        'Electronica': ['Mac', 'Iphone' 'Playstation'],
        'Juguetes': ['Auto', 'Paleta de Futbol', 'Figura de Accion'],
        'Ropa': ['Pantalones', 'Chaqueta', 'Camisa']}
    productos = producto_data.get(categoria, [])
    return render(request, 'djangoApp/productos.html', {'categoria': categoria, 'productos': productos})
