from django import forms


from .models import Categoria

class CategoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = ('nombre', 'descripcion',)
from .models import Pelicula

class PeliculaForm(forms.ModelForm):

    class Meta:
        model = Pelicula
        fields = ('nombre', 'sinopsis','anio','productor','categoria',)
