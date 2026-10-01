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

    # BUSCAR UN PACIENTE
    def buscar_paciente(self, id_busqueda):
        for paciente in self.pacientes_espera:
            if paciente.id == id_busqueda:
                return paciente
                
        return None

    # ELIMINAR UN PACIENTE
    def eliminar_paciente(self, id_busqueda):
        paciente_buscado = self.buscar_paciente(id_busqueda)
        encontrado = True
        if paciente_buscado is None:
            encontrado = False
        else:
            self.pacientes_espera.remove(paciente_buscado)
        
        return encontrado

    # LISTAR PACIENTES EN ESPERA
    def listar_pacientes_espera(self):
        return self.pacientes_espera

    # LISTAR PACIENTES POR PRIORIDAD
    def listar_por_prioridad(self):
        # La máxima prioridad es 5
        return sorted(self.pacientes_espera, key = lambda x: (-x.prioridad, x.id)) 

    # ATENDER AL SIGUIENTE PACIENTE
    def atender_paciente(self):
        # En caso de no haber paciente que atender
        if not self.pacientes_espera:
            return None
            
        # En caso de haber pacientes en espera
        paciente_atender = self.listar_por_prioridad()[0]

        self.pacientes_espera.remove(paciente_atender)
        self.historial_atendidos.append(paciente_atender)

        return paciente_atender

    # CONSULTAR EL HISTORIAL
    def consultar_historial(self):
        return self.historial_atendidos

    # MOSTRAR ESTADÍSTICAS
    def mostrar_estadisticas(self):
        # Edad media de todos los pacientes registrados
        pacientes_registrados = self.pacientes_espera + self.historial_atendidos
        if pacientes_registrados:
            edad_media = round(sum(paciente.edad for paciente in pacientes_registrados) / len(pacientes_registrados),2)
        else:
            edad_media = None

        # Pacientes en espera por prioridad
        prioridades = {i: 0 for i in range(1, 6)}
        for paciente in self.pacientes_espera:
            prioridades[paciente.prioridad] += 1

        texto = (
            f"Pacientes en espera: {len(self.pacientes_espera)}\n"
            f"Pacientes atendidos: {len(self.historial_atendidos)}\n"
            f"Edad media: {edad_media}\n"
            )
        
        # Mostrar prioridades de máxima prioridad a mínima
        for k, v in reversed(prioridades.items()):
            texto += f"Prioridad {k}: {v}\n"
    
        return texto
