# MÓDULO PARA GUARDAR Y CARGAR DATOS
# Se encarga de la persistencia de los datos en formato JSON,
# incluyendo la lista de pacientes en espera y el historial de pacientes atendidos.
# También va a almacenar el siguiente id a asignar

# IMPORTACIONES
import json # para trabajar con archivos JSON
import os # evita FileNotFoundError
from .paciente import Paciente # permite trabajar con la clase Paciente

