# CLASE HOSPITAL
# Representa la clase encargada de la gestión del flujo de pacientes.
# Controla el registro de pacientes, la lista de espera y el servicio de atención, el historial y las estadísticas del mismo.

# IMPORTACIONES
from .paciente import Paciente #Importamos la clase Paciente para poder crear y manejar objetos de este tipo

class Hospital:

    # CONSTRUCTOR
    def __init__(self, pacientes_espera = None, historial_atendidos = None, id_siguiente_paciente=1):
        # Si no se arranca el programa desde un estado inicial, se crean listas vacías
        self.pacientes_espera = pacientes_espera if pacientes_espera is not None else []
        self.historial_atendidos = historial_atendidos if historial_atendidos is not None else []
        self.id_siguiente_paciente = id_siguiente_paciente 
