import os

def acortar_nombres_en_directorio(ruta, longitud_maxima):
    """
    Acorta los nombres de archivos y carpetas en un directorio dado si son más largos que la longitud máxima.
    
    :param ruta: Ruta del directorio donde se encuentran los archivos y carpetas.
    :param longitud_maxima: Longitud máxima permitida para los nombres.
    """
    try:
        for root, dirs, files in os.walk(ruta, topdown=False):
            # Acortar nombres de archivos
            for nombre in files:
                if len(nombre) > longitud_maxima:
                    nuevo_nombre = nombre[:longitud_maxima]
                    ruta_original = os.path.join(root, nombre)
                    ruta_nueva = os.path.join(root, nuevo_nombre)
                    os.rename(ruta_original, ruta_nueva)
                    print(f"Archivo renombrado: {ruta_original} -> {ruta_nueva}")
            
            # Acortar nombres de carpetas
            for nombre in dirs:
                if len(nombre) > longitud_maxima:
                    nuevo_nombre = nombre[:longitud_maxima]
                    ruta_original = os.path.join(root, nombre)
                    ruta_nueva = os.path.join(root, nuevo_nombre)
                    os.rename(ruta_original, ruta_nueva)
                    print(f"Carpeta renombrada: {ruta_original} -> {ruta_nueva}")
    
    except Exception as e:
        print(f"Error: {e}")

# Uso del script
directorio = "ruta/a/tu/directorio"  # Cambia esto por el camino de tu carpeta
longitud_maxima = 10  # Cambia esto según la longitud máxima deseada
acortar_nombres_en_directorio(directorio, longitud_maxima)
