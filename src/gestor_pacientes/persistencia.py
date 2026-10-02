# MÓDULO PARA GUARDAR Y CARGAR DATOS
# Se encarga de la persistencia de los datos en formato JSON,
# incluyendo la lista de pacientes en espera y el historial de pacientes atendidos.
# También va a almacenar el siguiente id a asignar

# IMPORTACIONES
import json # para trabajar con archivos JSON
import os # evita FileNotFoundError
from .paciente import Paciente # permite trabajar con la clase Paciente

# Nombre del fichero
fichero_JSON = "hospital_data.json"

# AL INICIAR EL PROGRAMA
# Los datos deben cargarse automáticamente
def cargar_datos():
    if not os.path.exists(fichero_JSON): # No hay fichero del que recuperar el estado
        return [], [], 1 # Hospital inicialmente vacío

    try:
        with open(fichero_JSON, "r", encoding="utf-8") as fichero:
            estado_recuperado = json.load(fichero)

        pacientes_espera = [
            Paciente.from_dict(paciente)
            for paciente in estado_recuperado.get("pacientes_espera", [])
        ]

        pacientes_atendidos = [
            Paciente.from_dict(paciente)
            for paciente in estado_recuperado.get("pacientes_atendidos", [])
        ]

        id_siguiente_paciente = estado_recuperado.get("id_siguiente_paciente", 1)

        return pacientes_espera, pacientes_atendidos, id_siguiente_paciente

    except (json.JSONDecodeError, IOError, ValueError): # Manejo de posibles errores en lectura 
        return [], [], 1

# AL SALIR DEL PROGRAMA
# Se deben guardar los datos y cambios efectuados
def guardar_datos(pacientes_espera, pacientes_atendidos, id_siguiente_paciente):
    estado_recuperar = {
        "pacientes_espera": [paciente.to_dict() for paciente in pacientes_espera],
        "pacientes_atendidos": [paciente.to_dict() for paciente in pacientes_atendidos],
        "id_siguiente_paciente": id_siguiente_paciente
    }

    try:
        with open(fichero_JSON, "w", encoding="utf-8") as fichero:
            json.dump(estado_recuperar, fichero, indent=4, ensure_ascii=False)

    except IOError:
        print("Se ha producido un error en el guardado de datos. Inténtelo de nuevo.")
