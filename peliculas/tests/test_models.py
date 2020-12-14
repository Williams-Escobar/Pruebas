from django.test import TestCase
from peliculas.models import Pelicula, Categoria

class CategoriaModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Categoria.objects.create(nombre = 'Titulo para la pelicula',
                                descripcion = 'Texto de prueba de la sinopsis de la pelicula',)
        pass

    def test_titulo_max_length(self):
        pelicula=Categoria.objects.get(id=1)
        max_length = Categoria._meta.get_field('nombre').max_length
        self.assertEquals(max_length,50)
    pass

class PeliculaModelTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        categoria = Categoria.objects.create()
        Pelicula.objects.create(nombre = 'Titulo para la pelicula',
                               sinopsis = 'Texto de prueba de la sinopsis de la pelicula',
                               anio = 2020,
                                productor = 'Texto de prueba de la sinopsis de la pelicula',
                                categoria = categoria)
        pass
    def test_titulo_label(self):
        pelicula=Pelicula.objects.get(id=1)
        field_label = pelicula._meta.get_field('sinopsis').verbose_name
        self.assertEquals(field_label,'sinopsis')

    def test_titulo_max_length(self):
        pelicula=Pelicula.objects.get(id=1)
        max_length = Pelicula._meta.get_field('nombre').max_length
        self.assertEquals(max_length,80)

    def test_fecha_creacion_label (self):
        publicacion = Pelicula.objects.get(id=1)
        field_label = publicacion._meta.get_field('fecha_Creacion').verbose_name
        self.assertEquals(field_label,'Creado')