# PROGRAMA PRINCIPAL
# Fichero que se encarga de la gestión de pacientes de un hospital 
# Implementación mediante consola

# IMPORTACIONES
from src.hospital import Hospital
from src.persistencia import cargar_datos, guardar_datos

# OPCIONES DEL MENÚ
def mostrar_menu():
    print("\n" + "=" * 50)
    print("GESTOR DE PACIENTES")
    print("=" * 50)
    print("1. Registrar paciente")
    print("2. Buscar paciente")
    print("3. Eliminar paciente")
    print("4. Listar pacientes en espera")
    print("5. Listar pacientes por prioridad")
    print("6. Atender al siguiente paciente")
    print("7. Consultar historial")
    print("8. Mostrar estadísticas")
    print("0. Guardar y salir")

# CÓDIGO MAIN
# Se encarga de la ejecución del programa.
# Muestra el menú y gestiona la opción seleccionada por el usuario.    
def main():

    # Cargar los datos del estado guardado
    pacientes_espera, pacientes_atendidos, id_siguiente = cargar_datos()

    # Creación del Hospital con los datos cargados
    hospital = Hospital(pacientes_espera, pacientes_atendidos, id_siguiente)
