# Trabajo Final
# Analisis de Datos con NumPy, Pandas y Matplotlib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# ========================
# 1. CREACION DEL DATASET
# ========================
data = {
    "Producto" : ["Pendrive 32GB", "Pendrive 64GB", "Pendrive 128GB", "Memoria RAM 8GB", "Memoria RAM 16GB",
                  "Memoria RAM 32GB", "SSD 256GB", "SSD 512GB", "SSD 1TB", "Tarjeta SD 64GB"],
    "Precio"   : [25, 45, 80, 120, 220, 380, 150, 280, 450, 35],
    "Cantidad" : [15, 10, 6, 5, 3, 2, 8, 4, 2, 12],
    "Ciudad"   : ["Lima", "Cusco", "Arequipa", "Trujillo", "Lima", "Piura", "Lima", "Cusco", "Arequipa", "Lima"]
}


# Convertir a DataFrame
df = pd.DataFrame(data)

# Mostrar el DataFrame completo
print("=== DATASET DE VENTAS MEMORIKIGS ===")
print(df)

# Exportar a CSV
df.to_csv("ventas_memorikigs.csv", index=False)
print("\nDataset exportado a ventas_memorikigs.csv")

# Importar desde CSV
df = pd.read_csv("ventas_memorikigs.csv")
print("\nDataset importado desde ventas_memorikigs.csv")
print(df)

# ==========================
# 2. MANIPULACION CON PANDAS
# ==========================

# Crear columna Ventas = Precio x Cantidad
df["Ventas"] = df["Precio"] * df["Cantidad"]

# Mostrar DataFrame con la nueva columna
print("\n=== DATAFRAME CON COLUMNA VENTAS ===")
print(df)

# Calcular estadisticas
promedio_ventas = df["Ventas"].mean()
venta_maxima    = df["Ventas"].max()
venta_minima    = df["Ventas"].min()
suma_ventas     = df["Ventas"].sum()

print("\n=== ESTADISTICAS ===")
print("Promedio de ventas:", promedio_ventas)
print("Venta maxima      :", venta_maxima)
print("Venta minima      :", venta_minima)
print("Suma total ventas :", suma_ventas)

# ========================
# 3. FILTRADO DE DATOS
# ========================
# Ventas en Lima
ventas_lima = df[df["Ciudad"] == "Lima"]
print("\n=== VENTAS EN LIMA ===")
print(ventas_lima)

# Productos con ventas mayores a 1000
ventas_mayor_1000 = df[df["Ventas"] > 1000]
print("\n=== PRODUCTOS CON VENTAS MAYORES A 1000 ===")
print(ventas_mayor_1000)

# Productos con cantidad mayor a 5
cantidad_mayor_5 = df[df["Cantidad"] > 5]
print("\n=== PRODUCTOS CON CANTIDAD MAYOR A 5 ===")
print(cantidad_mayor_5)

# ========================
# 4. CALCULOS CON NUMPY
# ========================
# Convertir columna Ventas a array NumPy
ventas_numpy = df["Ventas"].to_numpy()
print("\n=== CALCULOS CON NUMPY ===")
print("Array de ventas:", ventas_numpy)
print("Media           :", np.mean(ventas_numpy))
print("Desv. estandar :", np.std(ventas_numpy))
print("Valor maximo   :", np.max(ventas_numpy))
print("Valor minimo   :", np.min(ventas_numpy))


# ========================
# 5. VISUALIZACION CON MATPLOTLIB
# ========================
# Grafico de barras - ventas por producto
colores_barras = ["#F62222", "#1BD0C4", "#19ABCC", "#21A769", "#FFDA60", 
                  '#DDA0DD', "#2ADCB0", '#F7DC6F', "#A54ECB", "#50E1FE"]
plt.figure(figsize=(10, 6))
plt.bar(df["Producto"], df["Ventas"], color=colores_barras, alpha=0.8)
plt.title("Ventas por Producto")
plt.xlabel("Producto")
plt.ylabel("Ventas (S/.)")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico_barras.png")
plt.show()


# Grafico de linea - cantidad vendida por producto
plt.plot(df["Producto"], df["Cantidad"], color="red", marker="o", linestyle="--")
plt.title("Cantidad Vendida por Producto")
plt.xlabel("Producto")
plt.ylabel("Cantidad")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("grafico_linea.png")
plt.show()

# Grafico de pastel - distribucion de ventas por ciudad
ventas_ciudad = df.groupby("Ciudad")["Ventas"].sum()
plt.pie(ventas_ciudad, labels=ventas_ciudad.index, autopct="%1.1f%%")
plt.title("Distribucion de Ventas por Ciudad")
plt.savefig("grafico_pastel.png")
plt.show()

# ========================
# 6.ANALISIS DE RESULTADOS
# ========================
print("\n=== ANALISIS DE RESULTADOS ===")
print("1. Producto con mayores ventas :", df.loc[df["Ventas"].idxmax(), "Producto"])
print("2. Ciudad con mayor volumen    :", ventas_ciudad.idxmax())
print("3. Promedio de ventas          :", round(np.mean(ventas_numpy), 2))
print("4. Variacion en ventas         :", round(np.std(ventas_numpy), 2), "- hay variacion significativa")
print("5. Producto a promocionar mas  :", df.loc[df["Ventas"].idxmin(), "Producto"])


# ====================================
# NUEVO DATASET - 30 productos, 5 ciudades, 30 regiones
# ====================================

data2 = {
    "Producto" : [
        "Pendrive 32GB",    "Pendrive 64GB",     "Pendrive 128GB",
        "Memoria RAM 8GB",  "Memoria RAM 16GB",  "Memoria RAM 32GB",
        "SSD 256GB",        "SSD 512GB",         "SSD 1TB",
        "Tarjeta SD 64GB",  "Pendrive 32GB",     "Memoria RAM 8GB",
        "SSD 256GB",        "Pendrive 64GB",     "SSD 1TB",
        "Memoria RAM 16GB", "Tarjeta SD 64GB",   "Pendrive 128GB",
        "SSD 512GB",        "Memoria RAM 32GB",  "Pendrive 32GB",
        "SSD 256GB",        "Memoria RAM 8GB",   "Pendrive 64GB",
        "SSD 1TB",          "Tarjeta SD 64GB",   "Memoria RAM 16GB",
        "Pendrive 128GB",   "SSD 512GB",         "Memoria RAM 32GB"
    ],
    "Precio" : [
        25,  45,  80, 120, 220, 380, 150, 280, 450,  35,
        25, 120, 150,  45, 450, 220,  35,  80, 280, 380,
        25, 150, 120,  45, 450,  35, 220,  80, 280, 380
    ],
    "Cantidad" : [
        15, 10,  6,  5,  3,  2,  8,  4,  2, 12,
        18,  7, 11, 13,  1,  4, 20,  9,  3,  2,
        16,  6,  8, 14,  2, 11,  5,  7,  4,  3
    ],
    "Ciudad" : [
        "Lima",      "Cusco",         "Arequipa",
        "Trujillo",  "Lima",          "Piura",
        "Lima",      "Cusco",         "Arequipa",
        "Lima",      "Trujillo",      "Chiclayo",
        "Huancayo",  "Lima",          "Ica",
        "Huaraz",    "Cajamarca",     "Puno",
        "Tarapoto",  "Tacna",         "Moquegua",
        "Tumbes",    "Pucallpa",      "Iquitos",
        "Chachapoyas", "Huanuco",     "Cerro de Pasco",
        "Abancay",   "Ayacucho",      "Huancavelica"
    ],
    "Region" : [
        "Lima",          "Cusco",          "Arequipa",
        "La Libertad",   "Lima",           "Piura",
        "Lima",          "Cusco",          "Arequipa",
        "Lima",          "La Libertad",    "Lambayeque",
        "Junin",         "Lima",           "Ica",
        "Ancash",        "Cajamarca",      "Puno",
        "San Martin",    "Tacna",          "Moquegua",
        "Tumbes",        "Ucayali",        "Loreto",
        "Amazonas",      "Huanuco",        "Pasco",
        "Apurimac",      "Ayacucho",       "Huancavelica"
    ]
}


df2 = pd.DataFrame(data2)
df2["Ventas"] = df2["Precio"] * df2["Cantidad"]

print("\n=== NUEVO DATASET (30 registros, 5 ciudades base, 30 regiones) ===")
print(df2)

# Exportar nuevo dataset a CSV
df2.to_csv("ventas_memorikigs_nuevo.csv", index=False)
print("\nNuevo dataset exportado a ventas_memorikigs_nuevo.csv")

# Histograma de ventas (COLOR VERDE)
ventas_numpy2 = df2["Ventas"].to_numpy()
plt.hist(ventas_numpy2, bins=10, color='#27AE60', alpha=0.75, edgecolor='black')
plt.title("Histograma de Ventas")
plt.xlabel("Ventas (S/.)")
plt.ylabel("Frecuencia")
plt.tight_layout()
plt.savefig("grafico_histograma.png")
plt.show()


# Grafico de dispersion - Precio vs Cantidad
plt.scatter(df2["Precio"], df2["Cantidad"])
plt.title("Precio vs Cantidad")
plt.xlabel("Precio (S/.)")
plt.ylabel("Cantidad")
plt.tight_layout()
plt.savefig("grafico_dispersion.png")
plt.show()

print("\nGraficos guardados!")
