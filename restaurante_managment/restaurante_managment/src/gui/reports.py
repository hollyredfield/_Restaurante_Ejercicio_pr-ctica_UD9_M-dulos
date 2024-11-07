import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from src.database.db_manager import DBManager

class ReportGenerator:
    def __init__(self):
        self.db = DBManager()

    def generate_sales_report(self):
        self.db.cursor.execute('''
            SELECT items 
            FROM orders
        ''')
        data = self.db.cursor.fetchall()
        
        if not data:
            print("No data found in the orders table.")
            return
        
        items = [item for sublist in data for item in sublist[0].split(',')]
        item_counts = Counter(items)
        
        if not item_counts:
            print("No items found in the orders.")
            return
        
        items = list(item_counts.keys())
        counts = list(item_counts.values())
        
        print(f"Items: {items}")
        print(f"Counts: {counts}")
        
        plt.figure(figsize=(10, 6))
        sns.barplot(x=items, y=counts)
        plt.title('Cantidad de Platos Vendidos')
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()