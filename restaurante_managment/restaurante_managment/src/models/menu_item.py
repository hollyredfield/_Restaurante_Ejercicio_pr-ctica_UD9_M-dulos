class MenuItem:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = price
        self.category = category
        self.validate()
    
    def validate(self):
        if not self.name or not isinstance(self.name, str):
            raise ValueError("Nombre inválido")
        if not isinstance(self.price, (int, float)) or self.price <= 0:
            raise ValueError("Precio inválido")
        if not self.category or not isinstance(self.category, str):
            raise ValueError("Categoría inválida")