# CLASE PACIENTE
# Representa un paciente del sistema con atributos de id, nombre, edad, prioridad y motivo de consulta
class Paciente:

    # CONSTRUCTOR
    def __init__(self, id, nombre, edad, prioridad, motivo_consulta):
        # Validación de los atributos del paciente antes de asignarlos
        self._validar_id(id)
        self._validar_nombre(nombre)
        self._validar_edad(edad)
        self._validar_prioridad(prioridad)
        self._validar_motivo_consulta(motivo_consulta)

        # Solo cuando son válidos, asignación de los atributos al objeto creado
        self.id = id
        self.nombre = nombre
        self.edad = edad
        self.prioridad = prioridad
        self.motivo_consulta = motivo_consulta

    # FUNCIONES INTERNAS DE VALIDACIÓN
    # Validación del id
    def _validar_id(self, id):
        if not isinstance(id, int) or id <= 0:
            raise ValueError("El ID asignado debe ser un número de tipo entero y positivo")

    # Validación del nombre
    def _validar_nombre(self, nombre):
        if not isinstance(nombre, str) or nombre.strip() == "":
            raise ValueError("El nombre debe ser texto y este no puede estar vacío")

    # Validación de la edad
    def _validar_edad(self, edad):
        if not isinstance(edad, int) or not (0 <= edad <= 120):
            raise ValueError("La edad debe ser un número de tipo entero entre 0 y 120")

    # Validación de la prioridad
    def _validar_prioridad(self, prioridad):
        if not isinstance(prioridad, int) or not (1 <= prioridad <= 5):
            raise ValueError("La prioridad debe ser un número de tipo entero entre 1 y 5")

    # Validación del motivo de consulta
    def _validar_motivo_consulta(self, motivo_consulta):
        if not isinstance(motivo_consulta, str) or motivo_consulta.strip() == "":
            raise ValueError("El motivo de consulta debe ser texto y este no puede estar vacío")

    # REPRESENTACIÓN LEGIBLE EN FORMATO CADENA  
    def __str__(self):
        return f"""Paciente de id "{self.id}": 
                    con nombre {self.nombre}, 
                    edad de {self.edad} años, 
                    prioridad {self.prioridad} 
                    y motivo de consulta: {self.motivo_consulta}"""
        
    # CONVERTIR PACIENTE A DICCIONARIO PARA ALMACENARLO EN JSON
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "edad": self.edad,
            "prioridad": self.prioridad,
            "motivo_consulta": self.motivo_consulta
        }

    # CONVERTIR DICCIONARIO A PACIENTE DESDE UN JSON
    @staticmethod
    def from_dict(data):
        return Paciente(
            id = data["id"],
            nombre = data["nombre"],
            edad = data["edad"],
            prioridad = data["prioridad"],
            motivo_consulta = data["motivo_consulta"]
        )