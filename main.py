import os
import tkinter as tk
from src.db import inicializar_bd
from src.vista import InventarioApp

def main():
    if "DB_NAME" not in os.environ:
        os.environ["DB_NAME"] = "inventario.db"

    # Inicializa la base de datos de forma transparente
    inicializar_bd()
    
    # Arranca la ventana de Tkinter
    root = tk.Tk()
    app = InventarioApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()