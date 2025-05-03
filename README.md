# 🎓 Predicción del Nivel de Adaptabilidad Digital de Estudiantes

Este proyecto de aprendizaje automático tiene como objetivo **predecir el nivel de adaptabilidad digital de los estudiantes** (Bajo, Moderado o Alto), utilizando datos demográficos, educativos y tecnológicos. Fue desarrollado como parte de mi formación en **análisis de datos aplicado a la educación**.

👉 **[Ver la app en línea](https://modelo-adaptabilidad-estudiantil-uqx3zwnupbhrg2mvfvggng.streamlit.app/)**

---

## 🎯 Objetivo del Proyecto

Construir un modelo predictivo que, a partir de variables como:

- Edad
- Dispositivo utilizado
- Tipo de conexión a internet
- Condición económica
- Experiencia con tecnología

sea capaz de **estimar con alta precisión** el nivel de adaptación digital de un estudiante en entornos virtuales.

---

## 📊 Dataset Utilizado

- **Nombre del dataset:** [Student Adaptability Dataset – Kaggle](https://www.kaggle.com/datasets)
- **Total de registros:** 1205 estudiantes
- **Variable objetivo:** `Adaptivity Level` (Bajo, Moderado, Alto)

### 🧩 Variables predictoras:

- `Gender`, `Age`, `Education Level`, `Institution Type`, `IT Student`
- `Location`, `Load-shedding`, `Financial Condition`
- `Internet Type`, `Network Type`, `Class Duration`, `Self Lms`, `Device`

---

## ⚙️ Metodología de Trabajo

### 1. **Preprocesamiento de datos**
- Limpieza y codificación de variables categóricas (OneHotEncoder)
- División en conjuntos de entrenamiento y prueba
- Análisis exploratorio

### 2. **Entrenamiento de modelos**
- Regresión Logística
- Random Forest Classifier (mejor rendimiento)

### 3. **Optimización**
- Validación cruzada
- Búsqueda de hiperparámetros con GridSearchCV

### 4. **Evaluación**
- Accuracy, Precision, Recall, F1-score
- Matriz de confusión
- Interpretación de importancia de variables

---

## ✅ Resultados Obtenidos

| Modelo          | F1-score |
|-----------------|----------|
| Random Forest   | **0.91** |
| Regresión Logística | 0.86     |

- 🔍 **Mejor modelo seleccionado:** Random Forest
- 💾 **Modelo guardado:** `mejor_modelo_adaptabilidad.pkl`

---

## 📌 Factores más relevantes para la predicción

1. Duración de clases virtuales
2. Género del estudiante
3. Condición económica del hogar
4. Tipo de dispositivo utilizado
5. Tipo de conexión a internet

---

## 📝 Recomendaciones Educativas Derivadas

- **Asegurar acceso a tecnología** y conectividad adecuada en entornos vulnerables.
- **Personalizar la duración de las clases** según los recursos y capacidades de los estudiantes.
- **Diseñar estrategias diferenciadas** por edad y género.
- **Brindar apoyo específico** a quienes se encuentran en desventaja económica o tecnológica.

---

## 🚀 Tecnologías Utilizadas

- `Python 3`
- `Streamlit`
- `Scikit-learn`
- `Pandas`
- `Joblib`
- `Git & GitHub`

---

## 📂 Estructura del Proyecto

├── app.py # Aplicación Streamlit
├── mejor_modelo_adaptabilidad.pkl # Modelo entrenado
├── requirements.txt # Dependencias del proyecto
├── README.md # Documentación
└── Predicción de Adaptabilidad.ipynb # Notebook de desarrollo y análisis


---

## 👨‍💻 Autor

**Janzolagomez**  
Investigador en comunicación, educación y tecnología  
[LinkedIn](https://www.linkedin.com/in/janzolagomez) • [GitHub](https://github.com/janzolagomez)

---

> Proyecto realizado como evidencia práctica de análisis predictivo educativo con despliegue web en la nube.
