from django_seed import Seed
from alumnos.models import Alumno
seeder = Seed.seeder()

seeder.add_entity(Alumno, 1,{
    'matricula': 18460642,
    'nombre' : 'Jose Juan',
    'apellidos' : 'Gomez Lopez',
    'domicilio' : '4 Norte #4',
    'telefono' : '2491201514',
    'grado': 8,
    'email': 'jj786908@gmail.com',
    'beca ': 100,
})

seeder.execute()