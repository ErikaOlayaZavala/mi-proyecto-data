import pandas as pd
import sqlite3 # Librería para bases de datos
import os

def cargar_a_sqlite(df):
    # 1. Conectar al archivo que creaste en DBeaver
    # Asegúrate de que el nombre coincida exactamente con el de tu carpeta
    conexion = sqlite3.connect('mi_base_datos.db')
    
    try:
        # 2. Enviar el DataFrame a una tabla llamada 'ventas_totales'
        # if_exists='replace' sirve para que si la tabla ya existe, la actualice
        df.to_sql('ventas_totales', conexion, if_exists='replace', index=False)
        print("¡Datos cargados exitosamente en la base de datos! 🚀")
    except Exception as e:
        print(f"Hubo un error al cargar: {e}")
    finally:
        # 3. Cerrar la conexión siempre (buena práctica Senior)
        conexion.close()

if __name__ == "__main__":
    archivo = 'ventas.csv'
    if os.path.exists(archivo):
        df_leido = pd.read_csv(archivo)
        print("Datos leídos del CSV correctamente.")
        
        # Llamamos a la nueva función de carga
        cargar_a_sqlite(df_leido)
    else:
        print("No se encontró el archivo CSV.")