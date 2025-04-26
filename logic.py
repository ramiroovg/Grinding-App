#Velocidades de corte y avance para fresadoras CNC
# Este script calcula la velocidad de corte y el avance por minuto para fresadoras CNC 
# basándose en el diámetro de la herramienta, la velocidad del husillo (RPM), 
# el avance por diente y el número de dientes de la herramienta.
from tkinter import messagebox


# Definición de la función calcular_velocidades_cnc
def calcular_velocidades_cnc(diametro_herramienta, rpm, avance_por_diente, numero_dientes):
    velocidad_corte = (3.1416 * diametro_herramienta * rpm) / 1000  # en m/min
    avance_por_minuto = avance_por_diente * numero_dientes * rpm  # en mm/min
    return velocidad_corte, avance_por_minuto

def calcular_area_salida(velocidad_entrada, area_entrada, velocidad_salida,):
    area_salida = (velocidad_entrada * area_entrada / velocidad_salida)  # en mm2
    return area_salida
