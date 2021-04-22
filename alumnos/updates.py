from .models  import Alumno

def act_matricula():
    alumnos = Alumno.objects.all()
    max_item = max(alumnos, key=str)
    matricula_defect = int(str(max_item))
    matricula_defect =  matricula_defect + 1
    #print(matricula_defect)
    return matricula_defect
