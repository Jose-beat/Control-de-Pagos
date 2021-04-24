from .models  import Reportes

def act_idReporte():

    reportes = Reportes.objects.all()
    try:
        max_item = max(reportes, key=str)
        id_defect = int(str(max_item))
        id_defect += 1
    except:
        id_defect = 0
    print(id_defect)
    return id_defect
