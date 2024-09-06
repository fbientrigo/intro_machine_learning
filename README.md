# intro_machine_learning

Repositorio con scripts y ejercicios para la clase de **Introducción a Machine Learning**, que ofrece ejemplos detallados y explicados paso a paso. Este repositorio está diseñado para enseñar conceptos fundamentales de Machine Learning a través de la práctica y la experimentación con varios datasets, implementando técnicas modernas en **Python** usando bibliotecas como **TensorFlow**, **Scikit-learn**, **KerasTuner**, entre otras.

# Requisitos
Este repositorio requiere Python 3.10 y las siguientes bibliotecas:

- tensorflow
- keras-tuner
- sklearn
- matplotlib
- numpy
- pandas

# Instalación
Se recomienda crear un entorno virtual en la carpeta con
```bash
python -m pip install venv
python -m venv env
```

El entorno virtual permite hacer modificaciones manteniendo el python del sistema limpio, luego se puede activar en Windows
```powershell
env\Scripts\activate
```
O en Linux
```bash
source env/Scripts/activate
```
Una vez activado:

Y luego instalar las librerias
```bash
python -m pip install -r requirements.txt
```

## Contenido del Repositorio

### 1. Datasets
Este repositorio incluye scripts que trabajan con varios datasets, tales como:

- **MNIST**: El clásico dataset de dígitos escritos a mano, utilizado para entrenar modelos de clasificación de imágenes.
- **Hipparcos**: Datos del catálogo de estrellas, usados para técnicas de clasificación y reducción de dimensionalidad.
- **Custom datasets**: Implementaciones para generar datos de ejemplo, usar clases desbalanceadas, y aplicar técnicas de oversampling.

### 2. Algoritmos de Machine Learning
El repositorio incluye implementaciones y ejemplos de los siguientes algoritmos:

- **Regresión Lineal y Regresión Logística**
- **Árboles de Decisión y Random Forest**
- **Support Vector Machines (SVM)**
- **K-Nearest Neighbors (kNN)**
- **Redes Neuronales Densas**
- **Boosting (AdaBoost)**
  
### 3. Técnicas Avanzadas
- **Reducción de Dimensionalidad**: Aplicación de PCA, t-SNE, y Isomap para la visualización y reducción de dimensionalidad.
- **Oversampling y manejo de clases desbalanceadas** usando SMOTE y técnicas manuales.
- **Hyperparameter Tuning** con **KerasTuner** para la optimización de modelos.
- **Visualización**: Gráficos de precisión, pérdida, ROC y matrices de confusión para análisis de resultados.


