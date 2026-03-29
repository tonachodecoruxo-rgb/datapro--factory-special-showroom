import json
import os

# Configuración
BASE_DIR = "Z:/"
OUTPUT_FOLDER = "00_DATAPRO_SHOWROOM"

def crear_muestras():
    # Nos aseguramos de que el showroom existe
    if not os.path.exists(os.path.join(BASE_DIR, OUTPUT_FOLDER)):
        os.makedirs(os.path.join(BASE_DIR, OUTPUT_FOLDER))

    # Recorremos todas las carpetas del 01 al 50
    for folder in os.listdir(BASE_DIR):
        if folder.startswith(("0", "1", "2", "3", "4", "5")) and os.path.isdir(os.path.join(BASE_DIR, folder)):
            
            # Buscamos el archivo JSON de datos (el gordo)
            for file in os.listdir(os.path.join(BASE_DIR, folder)):
                if file.endswith(".json") and "data_" in file:
                    path_completo = os.path.join(BASE_DIR, folder, file)
                    
                    with open(path_completo, 'r', encoding='utf-8') as f:
                        datos_completos = json.load(f)
                    
                    # EXTRAEMOS SOLO EL SAMPLE (Las primeras 5 líneas)
                    muestra = datos_completos[:5]
                    
                    # Creamos la carpeta del activo dentro del Showroom para GitHub
                    target_folder = os.path.join(BASE_DIR, OUTPUT_FOLDER, folder)
                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)
                    
                    # Guardamos la muestra
                    nombre_muestra = f"SAMPLE_{file}"
                    with open(os.path.join(target_folder, nombre_muestra), 'w', encoding='utf-8') as f:
                        json.dump(muestra, f, indent=4)
                    
                    # También copiamos el Dossier si existe
                    dossier_name = f"DOSSIER_{folder.split('_')[0]}.md"
                    dossier_path = os.path.join(BASE_DIR, folder, dossier_name)
                    if os.path.exists(dossier_path):
                        import shutil
                        shutil.copy(dossier_path, os.path.join(target_folder, dossier_name))
                        
                    print(f"✅ Muestra y Dossier preparados para: {folder}")

if __name__ == "__main__":
    crear_muestras()