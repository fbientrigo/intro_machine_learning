# Proyecto 1: Ley de Hubble

## Descripción
En este proyecto, utilizamos un modelo de **regresión lineal** para explorar la **Ley de Hubble**, que describe la relación entre la distancia a una galaxia y su velocidad de recesión. El objetivo es estimar la **constante de Hubble** a partir de datos simulados de supernovas tipo Ia, que nos permitirán calcular las distancias y las velocidades de recesión de galaxias.

Trabajamos con un **dataset simulado** que nos permite obtener resultados esperados sin necesidad de una limpieza exhaustiva de datos, enfocándonos en el análisis y la construcción del modelo.

Origen del dataset: [Kaggle: Ley de Hubble](https://www.kaggle.com/datasets/austinhinkel/hubble-law-astronomy-lab/data)

## La Ley de Hubble

La **Ley de Hubble** es un concepto clave en la cosmología moderna, ya que establece que las galaxias se alejan de nosotros a una velocidad proporcional a su distancia. Esta relación se expresa como:

$$
v = H_0 \cdot d
$$

Donde:
- **$v$** es la **velocidad de recesión** (en km/s).
- **$d$** es la **distancia** a la galaxia (en megaparsecs, Mpc).
- **$H_0$** es la **constante de Hubble**, que mide la tasa de expansión del universo en km/s/Mpc.

Esta ley es fundamental para entender la expansión del universo y se basa en el **corrimiento al rojo** ("redshift") de la luz emitida por galaxias distantes.

## Metodología

### 1. Cálculo de la Distancia
Las supernovas tipo Ia son utilizadas como **velas estándar** debido a su magnitud absoluta constante. La distancia a una galaxia puede calcularse utilizando la magnitud aparente ($m$) observada y la magnitud absoluta ($M$) de estas supernovas, con la fórmula:

$$
d = 10^{\frac{m - M + 5}{5}}
$$

Donde $d$ es la distancia en parsecs.

### 2. Cálculo de la Velocidad de Recesión
La **velocidad de recesión** de una galaxia se determina a partir de su **redshift** ($z$), utilizando la relación:

$$
v = z \cdot c
$$

Donde $c$ es la velocidad de la luz (300,000 km/s).

### 3. Regresión Lineal
Una vez calculadas las distancias y las velocidades, realizamos una **regresión lineal** entre ambas variables. La pendiente de esta regresión corresponde a la **constante de Hubble** ($H_0$).

## Implementación

1. **Cargar y procesar los datos**: Se parte de un dataset con las magnitudes aparentes y los valores de redshift de las supernovas.
2. **Transformación de los datos**: Convertimos la magnitud aparente en distancias y el redshift en velocidades.
3. **Separación de datos**: Dividimos los datos en conjuntos de entrenamiento y prueba para evaluar el modelo.
4. **Entrenamiento del modelo**: Utilizamos un modelo de **regresión lineal** para ajustar la relación entre la distancia y la velocidad de recesión.
5. **Evaluación del modelo**: Calculamos métricas como el **Mean Squared Error (MSE)** y el **R²** para medir la calidad del modelo.

## Ejecución del Proyecto

Sigue estos pasos para ejecutar el proyecto en tu entorno local:

1. Clona el repositorio.
2. Instala las dependencias requeridas:
   ```bash
   pip install -r requirements.txt
