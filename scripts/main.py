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

# GESTIÓN DE LAS OPCIONES DEL MENÚ
# Bucle principal el menú - Se repite hasta que el usuario decida salir
    while True:
        mostrar_menu()

        opcion = input("Selecciona una opción, insertando el número: ").strip()

        if opcion == "1":
            break
        elif opcion == "2":
            break
        elif opcion == "3":
            break
        elif opcion == "4":
            break
        elif opcion == "5":
            break
        elif opcion == "6":
            break
        elif opcion == "7":
            break
        elif opcion == "8":
            break
        elif opcion == "0":
            break
        else:
            break
