import tkinter as tk
from tkinter import messagebox
from src.dao import ProductoDAO
from src.servicio import InventarioService
from src.modelo import Producto

class InventarioApp:
    def __init__(self, root):
        self.root = root
        self.root.title("UPVT - Sistema de Inventario")
        self.root.geometry("500x450")
        self.root.configure(bg="#f5f5f5")
        
        self.dao = ProductoDAO()
        self.servicio = InventarioService(self.dao)
        
        # Título
        tk.Label(root, text="Gestión de Inventario (POO)", font=("Arial", 16, "bold"), bg="#f5f5f5", fg="#333").pack(pady=10)
        
        # Formulario
        frame = tk.LabelFrame(root, text=" Registrar Producto ", padx=10, pady=10, bg="#f5f5f5")
        frame.pack(pady=10, fill="x", padx=20) # 👈 Corregido aquí: padx en lugar de px
        
        tk.Label(frame, text="Nombre:", bg="#f5f5f5").grid(row=0, column=0, sticky="w")
        self.txt_nombre = tk.Entry(frame)
        self.txt_nombre.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Precio:", bg="#f5f5f5").grid(row=1, column=0, sticky="w")
        self.txt_precio = tk.Entry(frame)
        self.txt_precio.grid(row=1, column=1, pady=5, padx=5)
        
        tk.Label(frame, text="Stock Inicial:", bg="#f5f5f5").grid(row=2, column=0, sticky="w")
        self.txt_stock = tk.Entry(frame)
        self.txt_stock.grid(row=2, column=1, pady=5, padx=5)
        
        tk.Button(frame, text="Guardar Producto", command=self.guardar_producto, bg="#4CAF50", fg="white").grid(row=3, columnspan=2, pady=10)
        
        # Operación de Venta
        frame_venta = tk.LabelFrame(root, text=" Simular Venta (Excepciones) ", padx=10, pady=10, bg="#f5f5f5")
        frame_venta.pack(pady=10, fill="x", padx=20) # 👈 Corregido aquí también: padx en lugar de px
        
        tk.Label(frame_venta, text="ID Producto:", bg="#f5f5f5").grid(row=0, column=0, sticky="w")
        self.txt_id_venta = tk.Entry(frame_venta)
        self.txt_id_venta.grid(row=0, column=1, pady=5, padx=5)
        
        tk.Label(frame_venta, text="Cantidad:", bg="#f5f5f5").grid(row=1, column=0, sticky="w")
        self.txt_cant_venta = tk.Entry(frame_venta)
        self.txt_cant_venta.grid(row=1, column=1, pady=5, padx=5)
        
        tk.Button(frame_venta, text="Ejecutar Venta", command=self.vender_producto, bg="#008CBA", fg="white").grid(row=2, columnspan=2, pady=10)

    def guardar_producto(self):
        try:
            nombre = self.txt_nombre.get()
            precio = float(self.txt_precio.get())
            stock = int(self.txt_stock.get())
            
            nuevo_prod = Producto(nombre, precio, stock)
            id_generado = self.dao.guardar(nuevo_prod)
            
            messagebox.showinfo("Éxito", f"Producto registrado.\nID Asignado: {id_generado}")
            self.txt_nombre.delete(0, tk.END)
            self.txt_precio.delete(0, tk.END)
            self.txt_stock.delete(0, tk.END)
        except ValueError as e:
            messagebox.showerror("Error de Validación", f"Atrapado por POO:\n{e}")

    def vender_producto(self):
        try:
            id_prod = int(self.txt_id_venta.get())
            cantidad = int(self.txt_cant_venta.get())
            
            prod_actualizado = self.servicio.vender(id_prod, cantidad)
            messagebox.showinfo("Venta Exitosa", f"Venta realizada.\nNuevo stock de {prod_actualizado.nombre}: {prod_actualizado.stock}")
        except Exception as e:
            messagebox.showerror("Error de Negocio", f"Excepción Controlada:\n{e}")