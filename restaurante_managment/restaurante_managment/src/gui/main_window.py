import tkinter as tk
from tkinter import ttk, messagebox
from src.database.db_manager import DBManager
from src.models.menu_item import MenuItem
from src.models.order import Order
from src.gui.reports import ReportGenerator

class MainWindow:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Gestión de Restaurante")
        self.db = DBManager()
        self.current_order = Order()
        self.setup_gui()

    def setup_gui(self):
        # Menu Frame
        menu_frame = ttk.LabelFrame(self.root, text="Gestión Menú")
        menu_frame.grid(row=0, column=0, padx=5, pady=5)
        
        # Menu Entry Fields
        ttk.Label(menu_frame, text="Nombre:").grid(row=0, column=0)
        self.name_entry = ttk.Entry(menu_frame)
        self.name_entry.grid(row=0, column=1)

        ttk.Label(menu_frame, text="Precio:").grid(row=1, column=0)
        self.price_entry = ttk.Entry(menu_frame)
        self.price_entry.grid(row=1, column=1)

        ttk.Label(menu_frame, text="Categoría:").grid(row=2, column=0)
        self.category_entry = ttk.Entry(menu_frame)
        self.category_entry.grid(row=2, column=1)

        ttk.Button(menu_frame, text="Añadir Plato", 
                  command=self.add_menu_item).grid(row=3, column=0, columnspan=2)

        # Order Frame
        order_frame = ttk.LabelFrame(self.root, text="Realizar Pedido")
        order_frame.grid(row=0, column=1, padx=5, pady=5)

        ttk.Button(order_frame, text="Añadir Plato al Pedido", 
                  command=self.add_item_to_order).grid(row=0, column=0, columnspan=2)

        ttk.Button(order_frame, text="Registrar Pedido", 
                  command=self.place_order).grid(row=1, column=0, columnspan=2)

        # Report Frame
        report_frame = ttk.LabelFrame(self.root, text="Reportes")
        report_frame.grid(row=1, column=0, padx=5, pady=5)

        ttk.Button(report_frame, text="Generar Reporte de Ventas", 
                  command=self.generate_sales_report).grid(row=0, column=0, columnspan=2)

    def add_menu_item(self):
        name = self.name_entry.get()
        price = self.price_entry.get()
        category = self.category_entry.get()
        
        try:
            price = float(price)
            item = MenuItem(name, price, category)
            self.db.add_menu_item(item)
            messagebox.showinfo("Éxito", "Plato añadido al menú")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    def add_item_to_order(self):
        name = self.name_entry.get()
        item = self.db.get_menu_item(name)
        if item:
            self.current_order.add_item(item)
            messagebox.showinfo("Éxito", "Plato añadido al pedido")
        else:
            messagebox.showerror("Error", "Plato no encontrado en el menú")

    def place_order(self):
        self.db.add_order(self.current_order)
        self.current_order = Order()
        messagebox.showinfo("Éxito", "Pedido registrado")

    def generate_sales_report(self):
        report_generator = ReportGenerator()
        report_generator.generate_sales_report()