import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('winequality.csv', sep=';')

print("Información del DataFrame:")
print(df.info())
print("\nRevisar valores nulos en cada columna:")
print(df.isna().sum())

duplicados = df.duplicated().sum()
print(f"\nNúmero de filas duplicadas: {duplicados}")

#  eliminar duplicados 
df.drop_duplicates(inplace=True)

print("\nResumen estadístico (describe):")
print(df.describe())


corr_matrix = df.corr(numeric_only=True)  
print("\nMatriz de correlación:")
print(corr_matrix)

# matriz de correlación con un heatmap de Seaborn
plt.figure(figsize=(10, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Matriz de Correlación')
plt.show()

# Histograma de la variable 'quality'
plt.figure(figsize=(8, 5))
sns.histplot(data=df, x='quality', bins=8, kde=True)
plt.title('Distribución de la calidad del vino')
plt.xlabel('Quality')
plt.ylabel('Frecuencia')
plt.show()

#  Gráfico de dispersión entre 'alcohol' y 'quality'
plt.figure(figsize=(8, 5))
sns.scatterplot(data=df, x='alcohol', y='quality')
plt.title('Relación entre Alcohol y Calidad')
plt.xlabel('Alcohol')
plt.ylabel('Quality')
plt.show()

#  Boxplot de 'pH' categorizado por 'quality'
plt.figure(figsize=(8, 5))
sns.boxplot(data=df, x='quality', y='pH')
plt.title('Distribución de pH según la calidad del vino')
plt.xlabel('Quality')
plt.ylabel('pH')
plt.show()

