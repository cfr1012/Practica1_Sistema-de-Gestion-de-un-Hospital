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

    # REGISTRAR UN PACIENTE
    def registrar_paciente(self, nombre, edad, prioridad, motivo_consulta):
        paciente_nuevo = Paciente(
            id = self.id_siguiente_paciente,
            nombre = nombre,
            edad = edad,
            prioridad = prioridad,
            motivo_consulta = motivo_consulta
        )
        # Una vez registrado el paciente, le añadimos a la lista de espera 
        # y actualizamos el id para el siguiente registro
        self.pacientes_espera.append(paciente_nuevo)
        self.id_siguiente_paciente += 1
        
        return paciente_nuevo
