import datetime
from HotelIFBA.models import Quarto, Estadia

def checar_disponibilidade(quarto, dataEntrada, dataSaida):
    quartos_list=[]
    estadia_list = Estadia.objects.filter(quarto=quarto)
    for estadia in estadia_list:
        if estadia.dataEntrada > dataSaida or estadia.dataSaida < dataEntrada:
            quartos_list.append(True)
        else:
            quartos_list.append(False)

    return all(quartos_list)