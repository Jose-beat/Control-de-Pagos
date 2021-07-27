from .models  import Alumno

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
