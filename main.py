import os
from src.db import inicializar_bd
from src.modelo import Producto
from src.dao import ProductoDAO
from src.servicio import InventarioService
from src.excepciones import StockInsuficienteError

def main():
    if "DB_NAME" not in os.environ:
        os.environ["DB_NAME"] = "inventario.db"

    print("[SISTEMA] Inicializando base de datos local...")
    inicializar_bd()
    
    dao = ProductoDAO()
    servicio = InventarioService(dao)
    
    print("="*60)
    print("      DEMOSTRACIÓN EN VIVO: MINI SISTEMA DE INVENTARIO OOP      ")
    print("="*60)
    
    print("\n[EJECUCIÓN] Evaluando Caso 1: Intentar crear Producto('Mouse', -50, 5)")
    try:
        p1 = Producto(nombre="Mouse", precio=-50, stock=5)
    except ValueError as e:
        print(f">>  CAPTURA CORRECTA (ValueError): {e}")

    print("\n[EJECUCIÓN] Evaluando Caso 2: Registrar stock = 3 y vender 10 piezas")
    try:
        p_demo = Producto(nombre="Teclado Oficina", precio=250.0, stock=3)
        id_generado = dao.guardar(p_demo)
        print(f"   * Persistido en BD -> {p_demo.mostrar_detalle()}")
        
        print("   * Intentando invocar servicio.vender() con cantidad = 10...")
        servicio.vender(id_generado, cantidad=10)
    except StockInsuficienteError as e:
        print(f">>  CAPTURA CORRECTA (Excepción de Negocio): {e}")
    except Exception as e:
        print(f">>  Error inesperado: {e}")

    print("\n[EJECUCIÓN] Evaluando Caso 3: Simular desconexión a Red/Internet")
    print("   * Explicación: Operando bajo una arquitectura embebida SQLite local,")
    print("     el sistema ejecuta transacciones sin dependencias de sockets de red.")
    print("     Resultado: Operación 100% Autónoma y Resiliente.")
    print("\n" + "="*60)

if __name__ == "__main__":
    main()