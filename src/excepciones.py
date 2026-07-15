class StockInsuficienteError(Exception):
    def _init_(self, nombre_producto: str, stock_actual: int, cantidad_solicitada: int):
        self.message = f"Operación Inválida: El producto '{nombre_producto}' posee stock de {stock_actual} uds, insuficiente para suplir {cantidad_solicitada} uds."
        super()._init_(self.message)