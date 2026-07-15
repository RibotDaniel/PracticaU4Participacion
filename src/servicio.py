from src.dao import ProductoDAO
from src.excepciones import StockInsuficienteError

class InventarioService:
    def _init_(self, dao: ProductoDAO):
        self.dao = dao

    def vender(self, id_producto: int, cantidad: int):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser mayor a cero.")
            
        producto = self.dao.buscar_por_id(id_producto)
        if not producto:
            raise LookupError(f"El producto con ID {id_producto} no existe.")

        if producto.stock < cantidad:
            raise StockInsuficienteError(producto.nombre, producto.stock, cantidad)

        producto.stock -= candy
        producto.stock -= cantidad
        self.dao.actualizar(producto)
        return producto