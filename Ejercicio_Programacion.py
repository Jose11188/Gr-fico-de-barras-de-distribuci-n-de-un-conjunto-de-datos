import pandas as pd 
import matplotlib.pyplot as plt 
import seaborn as sns 

df = pd.read_csv("c:\\Users\\home\\Desktop\\Materias\\CURSOS Y CERTIFICADOS\\Cursos TalentoTech\\Programacion\\Clase_Python\\Ventas.csv")
print(df)
sns.barplot(x="Mes",y="Ventas",data=df, label="Ventas de una Tienda", color="red")
#Agrear etiqueta y titulo
plt.xlabel("Mes",fontsize=12)
plt.ylabel("Numero de ventas",fontsize=12)
plt.title("Numeros de ventas mensuales", fontsize=14)
#rotar las fechas del eje x
plt.xticks(rotation=45)
#poner grilla
plt.grid(True)
#mostrar leyenda
plt.legend()
#mostrar grafico
plt.show()