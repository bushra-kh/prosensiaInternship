import random

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def total_value(self):
        return self.price * self.quantity

    def __str__(self):
        return f"{self.name} ::- Qty: {self.quantity}, Value: {self.total_value():.1f}"

class PerishableProduct(Product):
    def __init__(self, name, price, quantity, expiry_days):
        super().__init__(name, price, quantity)
        self.expiry_days = expiry_days

    def total_value(self):
        value = super().total_value()
        if self.expiry_days < 5:
            value *= 0.8  # 20% discount
        return value

    def __str__(self):
        return f"{self.name} ::- Qty: {self.quantity}, Value: {self.total_value():.1f} (Perishable, {self.expiry_days} days left)"

class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, product):
        self.products.append(product)

    def list_inventory(self):
        for idx, prod in enumerate(self.products, 1):
            print(f"{idx}. {prod}")

    def search_by_name(self, term):
        results = list(filter(lambda p: term.lower() in p.name.lower(), self.products))
        for prod in results:
            print(prod)
        return results

    def restock_randomly(self, min_qty=1, max_qty=10):
        for prod in self.products:
            add_qty = random.randint(min_qty, max_qty)
            prod.quantity += add_qty

    def export_summary(self, filename="inventory_report.txt"):
        with open(filename, "w") as f:
            for idx, prod in enumerate(self.products, 1):
                f.write(f"{idx}. {prod}\n")

# Example usage
if __name__ == "__main__":
    inv = Inventory()
    inv.add_product(Product("Apple", 5.0, 10))
    inv.add_product(PerishableProduct("Milk", 4.0, 5, expiry_days=3))

    print("Inventory:")
    inv.list_inventory()

    print("\nSearch 'milk':")
    inv.search_by_name("milk")

    inv.restock_randomly()
    print("\nAfter restocking:")
    inv.list_inventory()

    inv.export_summary()
    print("\nInventory summary exported to inventory_report.txt")