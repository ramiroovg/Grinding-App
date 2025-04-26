import tkinter as tk
from tkinter import ttk, messagebox
# Este script crea una interfaz gráfica de usuario (GUI) para una aplicación de herramientas utilizadas en grinding.
# La aplicación incluye una calculadora CNC y una herramienta adicional para calcular el flujo de pipa.


#aqui se define la función que se encarga de realizar el cálculo de velocidades CNC 
# y actualizar los resultados en la interfaz gráfica.
def crear_calculadora_cnc(tab):
    from logic import calcular_velocidades_cnc
    

    # Definición de la función calcular para realizar el cálculo de velocidades CNC
    def calculara(entry_diametro, entry_rpm, entry_avance, entry_dientes, resultado_vc, resultado_f, calcular_velocidades_cnc):

        try:
            diametro_herramienta = float(entry_diametro.get())
            rpm = float(entry_rpm.get())
            avance_por_diente = float(entry_avance.get())
            numero_dientes = int(entry_dientes.get())

            velocidad_corte, avance_por_minuto = calcular_velocidades_cnc(
            diametro_herramienta, rpm, avance_por_diente, numero_dientes
            )

            resultado_vc.config(text=f"Velocidad de corte (Vc): {velocidad_corte:.2f} m/min")
            resultado_f.config(text=f"Avance por minuto (F): {avance_por_minuto:.2f} mm/min")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")
    
    """Crea la calculadora CNC en la pestaña especificada."""
    tk.Label(tab, text="Diámetro de la herramienta (mm):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_diametro = tk.Entry(tab)
    entry_diametro.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(tab, text="Velocidad del husillo (RPM):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_rpm = tk.Entry(tab)
    entry_rpm.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(tab, text="Avance por diente (mm):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_avance = tk.Entry(tab)
    entry_avance.grid(row=2, column=1, padx=10, pady=5)

    tk.Label(tab, text="Número de dientes:").grid(row=3, column=0, padx=10, pady=5, sticky="e")
    entry_dientes = tk.Entry(tab)
    entry_dientes.grid(row=3, column=1, padx=10, pady=5)

    resultado_vc = tk.Label(tab, text="Velocidad de corte (Vc):")
    resultado_vc.grid(row=5, column=0, columnspan=2, pady=5)

    resultado_f = tk.Label(tab, text="Avance por minuto (F):")
    resultado_f.grid(row=6, column=0, columnspan=2, pady=5)

    tk.Button(
        tab,
        text="Calcular",
        command=lambda: calculara(entry_diametro, entry_rpm, entry_avance, entry_dientes, resultado_vc, resultado_f, calcular_velocidades_cnc)
    ).grid(row=4, column=0, columnspan=2, pady=10)


# Aqui se define la función crear_calculadora_flujo que se encarga de crear una
#  herramienta para hacer cálculos de flujo de pipa en la pestaña especificada.
def crear_calculadora_flujo(tab):
    from logic import calcular_area_salida
    
    def calcular():
        try:
            area_entrada = float(entry_area1.get())
            velocidad_entrada = float(entry_v1.get())
            velocidad_salida = float(entry_v2.get())


            area_salida = calcular_area_salida(velocidad_entrada, area_entrada, velocidad_salida,)

            resultado_vc.config(text=f"Area de Salida (mm2): {area_salida:.2f} mm2")
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese valores numéricos válidos.")


    tk.Label(tab, text="Area de Entrada (mm2):").grid(row=0, column=0, padx=10, pady=5, sticky="e")
    entry_area1 = tk.Entry(tab)
    entry_area1.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(tab, text="Velocidad de Entrada (M/s):").grid(row=1, column=0, padx=10, pady=5, sticky="e")
    entry_v1 = tk.Entry(tab)
    entry_v1.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(tab, text="Velocidad de Salida (M/s):").grid(row=2, column=0, padx=10, pady=5, sticky="e")
    entry_v2 = tk.Entry(tab)
    entry_v2.grid(row=2, column=1, padx=10, pady=5)

    tk.Button(
        tab,
        text="Calcular",
        command=lambda: calcular()
    ).grid(row=4, column=0, columnspan=2, pady=10)
    resultado_vc = tk.Label(tab, text="Area de Salida (mm2):")
    resultado_vc.grid(row=5, column=0, columnspan=2, pady=5)

    #tk.Button(root, text="Calcular", command=calcular).grid(row=4, column=0, columnspan=2, pady=10)

    




def crear_herramienta_extra(tab):
    """Crea la calculadora en la pestaña especificada."""
    tk.Label(tab, text="Herramienta de cálculo en construcción").pack(pady=20)
    # Aquí puedes agregar más widgets y lógica para la calculadora





# Configuración de la ventana principal
root = tk.Tk()
root.title("Aplicación de Herramientas Ingeniería")
root.geometry("600x400")


# Crear el contenedor de pestañas
notebook = ttk.Notebook(root)
notebook.pack(expand=True, fill="both")

# Crear las pestañas
tab_calculadora_cnc = ttk.Frame(notebook) #Crea la pestaña de calculadora CNC
tab_flujo_pipa = ttk.Frame(notebook)#Crea la pestaña de flujo de pipa
tab_herramienta_extra = ttk.Frame(notebook)

# Agregar las pestañas al contenedor
notebook.add(tab_calculadora_cnc, text="Calculadora CNC") #Crea la pestaña de calculadora CNC
notebook.add(tab_flujo_pipa, text="Calculadora de Flujo de Pipa") #Crea la Pestaña de flujo de pipa
notebook.add(tab_herramienta_extra, text="Herramienta Extra") #Crea la pestaña de herramienta extra

# Agregar contenido a las pestañas
crear_calculadora_cnc(tab_calculadora_cnc)
crear_calculadora_flujo(tab_flujo_pipa)
crear_herramienta_extra(tab_herramienta_extra)




# Iniciar la aplicación
root.mainloop()