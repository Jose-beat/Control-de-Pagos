from .models  import Alumno
from admin.grados_carreras.models import Grados_carreras
GRUPOS = [
    ('A','a'),
    ('B','b'),
    ('C','c'),
    ('D','d'),
    ('E','e'),
    ('F','f'),
    ('G','g'),
    ('H','h'),
    ('I','i'),
    ('J','j'),
]

def act_matricula():
    alumnos = Alumno.objects.all()
    try:
        max_item = max(alumnos, key=str)
        matricula_defect = int(str(max_item))
        matricula_defect =  matricula_defect + 1
    except:
        matricula_defect = 0
        #print(type(alumnos))
    #print(matricula_defect)
    return matricula_defect

def act_Grados_Carreras(idGrado):
    grados_carreras = Grados_carreras.objects.all()
    numero_grupos = 0
    try:
        for i in grados_carreras:
            numero_grupos = i.cantidad_grupos
        
        return GRUPOS[0:numero_grupos]
    except:
        pass

        
