from datetime import datetime
from typing import List, Dict
from .menu_item import MenuItem

class Order:
    IVA = 0.21

    def __init__(self):
        self.items: List[MenuItem] = []
        self.date = datetime.now()
        self.total = 0.0
    
    def add_item(self, item: MenuItem):
        self.items.append(item)
        self.calculate_total()
    
    def calculate_total(self):
        subtotal = sum(item.price for item in self.items)
        self.total = subtotal * (1 + self.IVA)
    
    def to_dict(self) -> Dict:
        return {
            "date": self.date.isoformat(),
            "items": [item.name for item in self.items],
            "total": self.total
        }