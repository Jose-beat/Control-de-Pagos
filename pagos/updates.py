from .models import Pago
def act_tramite():
    pagos = Pago.objects.all()
    try:
        max_item = max(pagos, key=str)
        tramite_defect = int(str(max_item))
        tramite_defect =  tramite_defect + 1
    except:
        tramite_defect = 0
        #print(type(alumnos))
    #print(matricula_defect)
    return tramite_defect
