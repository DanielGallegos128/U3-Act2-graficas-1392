import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
# Daniel Gallegos   NC=1392
# Problema 5: Ecommerce (Nombre, usuarios activos en millones, envío gratis disponible, año)
amz = ['Amazon', 310, True, 1994]
ali = ['Aliexpress', 150, True, 2010]
ml  = ['Mercado Libre', 108, True, 1999]
ebg = ['eBay', 133, False, 1995]
shk = ['Shopee', 200, True, 2015]
lista_de_tiendas = [amz,ali,ml,ebg,shk]
df_tiendas = pd.DataFrame(lista_de_tiendas,columns=["Nombre","Cantidad","Envio_gratis","Año"])
print(df_tiendas)
plt.plot(df_tiendas["Nombre"],df_tiendas["Cantidad"])
plt.title("Grafica tiendas online 1392")
plt.xlabel("Nombre de las tiendas")
plt.ylabel("Cantidad de usuarios")
plt.show()
# Creamos una grafica de puntos
plt.scatter(df_tiendas["Nombre"],df_tiendas["Cantidad"])
plt.title("Grafica de puntos tiendas online 1392")
plt.show()
# Grafica de barras
plt.bar(df_tiendas["Nombre"],df_tiendas["Cantidad"])
plt.title("Grafica de barras tiendas online 1392")
plt.xlabel("Las Tiendas")
plt.ylabel("Cantidad Usuarios")
# Mostrar grafica
plt.show()
# Ordenar la grafica de barras de manera descendente
# de la mas grande a la pequeña
df_rs_ordenar = df_tiendas.sort_values("Cantidad",ascending=False)
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"])
plt.title("Grafica tiendas online 1392")
plt.show()
# Coloreando la grafica
plt.bar(df_rs_ordenar["Nombre"],df_rs_ordenar["Cantidad"],
        color=["b","g","c","m","y","r"])
plt.title("Grafica tiendas online 1392")
plt.show()
# Grafica de pastel
# plt.plot(df_redes_sociales["Nombre"],df_redes_sociales["Cantidad"])
plt.pie(df_tiendas["Cantidad"],labels=df_tiendas["Nombre"])
plt.title("Grafica de pie tiendas online 1392")
plt.show()