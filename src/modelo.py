from abc import ABC, abstractmethod

class Entidad(ABC):
    def _init_(self, id_entidad: int = None):
        self._id = id_entidad

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        self._id = value

    @abstractmethod
    def mostrar_detalle(self) -> str:
        pass

class Producto(Entidad):
    def _init_(self, nombre: str, precio: float, stock: int, id_producto: int = None):
        super()._init_(id_producto)
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, value):
        if not value or not isinstance(value, str) or len(value.strip()) == 0:
            raise ValueError("El nombre no puede estar vacío.")
        self._nombre = value.strip()

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("El precio debe ser mayor o igual a 0.")
        self._precio = float(value)

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("El stock debe ser un entero mayor o igual a 0.")
        self._stock = value

    def mostrar_detalle(self) -> str:
        id_str = f"ID: {self.id}" if self.id else "ID: Nuevo"
        return f"Producto [{id_str}] -> {self.nombre} | Precio: ${self.precio:.2f} | Stock: {self.stock} uds."