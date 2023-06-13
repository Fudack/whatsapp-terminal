import sys
import pyttsx3

file_path = sys.argv[1]

# Leer el contenido del archivo
with open(file_path, 'r') as file:
    lines = file.readlines()

if lines:
    last_message = lines[-2] if len(lines) >= 2 else lines[-1]
    last_message = last_message.strip()

    # Inicializar el motor de síntesis de voz
    engine = pyttsx3.init()

    # Configurar las propiedades de la voz
    engine.setProperty('rate', 150)  # Velocidad de habla (palabras por minuto)

    # Leer el último mensaje en voz alta
    engine.say(last_message)
    engine.runAndWait()
else:
    print('No hay mensajes guardados en el archivo.')

import sys
import pyttsx3
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

file_path = sys.argv[1]

# Inicializar el motor de síntesis de voz
engine = pyttsx3.init()

# Configurar las propiedades de la voz
engine.setProperty('rate', 150)  # Velocidad de habla (palabras por minuto)


class FileModifiedEventHandler(FileSystemEventHandler):
    def __init__(self):
        super().__init__()

    def on_modified(self, event):
        if event.src_path == file_path:
            read_last_message()

def read_last_message():
    # Leer el contenido del archivo
    with open(file_path, 'r') as file:
        lines = file.readlines()

    if lines:
        last_line = lines[-1]
        if last_line.startswith('remitente:'):
            remitente = last_line[len('remitente:'):].strip()
            contenido_line = lines[-2] if len(lines) >= 2 else lines[-1]
            if contenido_line.startswith('contenido:'):
                contenido = contenido_line[len('contenido:'):].strip()

                # Leer el último mensaje en voz alta
                message = f'Remitente: {remitente}\nContenido: {contenido}'
                engine.say(message)
                engine.runAndWait()


if __name__ == "__main__":
    # Leer el último mensaje al iniciar el script
    read_last_message()

    # Crear un observador de cambios en el directorio
    event_handler = FileModifiedEventHandler()
    observer = Observer()
    observer.schedule(event_handler, path=file_path, recursive=False)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()

    observer.join()
