inventario = [
    {"producto": "Laptop", "precio": 800, "stock": 5, "categoria": "Electrónicos"},
    {"producto": "Ratón", "precio": 20, "stock": 50, "categoria": "Electrónicos"},
    {"producto": "Libro Python", "precio": 35, "stock": 15, "categoria": "Libros"},
    {"producto": "Monitor", "precio": 200, "stock": 8, "categoria": "Electrónicos"},
    {"producto": "Teclado", "precio": 60, "stock": 25, "categoria": "Electrónicos"}
]

# 1. Filtrar productos de categoría "Electrónicos"
productos_electronicos = [
    item for item in inventario if item["categoria"] == "Electrónicos"
]
print("--- Productos Electrónicos ---")
for producto in productos_electronicos:
    print(producto)
print("\n")

# 2. Ordenar por precio descendente
inventario_ordenado_precio = sorted(
    inventario, key=lambda x: x["precio"], reverse=True
)
print("--- Inventario Ordenado por Precio (Descendente) ---")
for producto in inventario_ordenado_precio:
    print(producto)
print("\n")

# 3. Calcular valor total del inventario electrónico
valor_total_electronicos = sum(
    item["precio"] * item["stock"]
    for item in productos_electronicos  # Usamos la lista ya filtrada
)
print(
    f"--- Valor Total del Inventario Electrónico: ${valor_total_electronicos} ---"
)
print("\n")

# 4. Encontrar el producto más caro
producto_mas_caro = max(inventario, key=lambda x: x["precio"])
print("--- Producto Más Caro ---")
print(producto_mas_caro)
print("\n")