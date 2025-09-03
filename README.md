# 📊 Análisis de Ciberseguridad Global (2015-2024)

Este proyecto analiza un dataset de incidentes de ciberseguridad globales entre 2015 y 2024.  
Se utiliza **Python (pandas, matplotlib, seaborn, sklearn)** en un **Jupyter Notebook** para explorar patrones, pérdidas económicas, industrias afectadas y vulnerabilidades.

---

## 🔎 Análisis Realizados

### 1. Carga y exploración inicial
- Se cargó el archivo `Global_Cybersecurity_Threats_2015-2024.csv` en un DataFrame.
- Se revisó el tamaño, columnas y primeras filas para entender la estructura.

### 2. Agrupaciones y métricas
Usando `groupby` + `agg`:
- **Pérdidas financieras por tipo de ataque** → DDoS y Phishing son los más costosos.
- **Usuarios afectados por industria** → IT, Banca y Salud lideran en impacto.
- **Pérdida promedio por país** → Alemania, Australia y EE.UU. encabezan la lista.
- **Tiempo de resolución por defensa** → Firewall resultó ligeramente más eficiente.
- **Vulnerabilidades más comunes** → Zero-day, Ingeniería social y Software sin parches.

### 3. Visualizaciones
Se generaron gráficos en **matplotlib** para:
- Pérdidas económicas por ataque.
- Usuarios afectados por industria.
- Promedio de pérdidas por país.
- Tiempos de resolución por defensa.
- Vulnerabilidades más frecuentes.

### 4. Correlaciones
Se construyó una **matriz de correlación** entre:
- Pérdidas financieras
- Usuarios afectados
- Tiempo de resolución  

👉 Resultado: No existe correlación lineal fuerte entre estas variables.

### 5. Clustering
- Se aplicó **KMeans (3 clusters)** sobre las variables numéricas.
- Reducción de dimensionalidad con **PCA** para graficar en 2D.
- Identificados 3 grupos:
  1. **Incidentes pequeños** → bajo impacto, más frecuentes.
  2. **Incidentes medianos** → impacto moderado.
  3. **Incidentes grandes** → pocos casos pero con enormes pérdidas o usuarios afectados.

---

## 🚀 Conclusiones
- Los ataques más frecuentes no siempre son los más costosos.
- Algunas industrias son más vulnerables que otras (IT y banca destacan).
- No hay correlación directa entre pérdidas económicas, usuarios afectados y tiempo de resolución.
- El clustering permite diferenciar **tres tipos de incidentes** con perfiles distintos, útil para diseñar **estrategias de mitigación diferenciadas**.

---

## 🛠️ Librerías usadas
- pandas  
- matplotlib  
- seaborn  
- scikit-learn  

---
