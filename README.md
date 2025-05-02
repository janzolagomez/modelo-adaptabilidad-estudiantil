# Predicción del Nivel de Adaptabilidad Digital de Estudiantes

Este proyecto de aprendizaje automático tiene como objetivo predecir el nivel de adaptabilidad de los estudiantes al entorno digital (Bajo, Moderado o Alto) utilizando datos demográficos, tecnológicos y educativos. Fue desarrollado como parte de mi formación en análisis de datos aplicado a la educación.

🎯 Objetivo del proyecto

Construir un modelo que, a partir de datos como edad, dispositivo, tipo de conexión a internet y condiciones financieras, sea capaz de predecir con alta precisión el nivel de adaptabilidad digital de un estudiante.

🧐 Dataset

El conjunto de datos incluye 1205 registros de estudiantes con las siguientes variables:

Gender, Age, Education Level, Institution Type, IT Student

Location, Load-shedding, Financial Condition

Internet Type, Network Type, Class Duration, Self Lms, Device

Adaptivity Level (variable objetivo)

Fuente del dataset: Kaggle: Student Adaptability Dataset

⚙️ Metodología

Preprocesamiento de datos:

Limpieza, codificación categórica, separación de variables

Entrenamiento de modelos:

Random Forest

Regresión Logística

**Validación cruzada y búsqueda de hiperparámetros (GridSearchCV)

Evaluación de métricas:

Accuracy, Precision, Recall, F1-score

Matriz de confusión

Selección del mejor modelo

Predicción con nuevos datos

📈 Resultados

🔍 Mejor modelo: Random Forest (F1-score: 0.91)

⚒️ Modelo guardado: mejor_modelo_adaptabilidad.pkl

📊 Factores más importantes para la predicción:

Duración de clases (0 horas)

Género

Condición financiera

Tipo de conexión y dispositivo

📝 Recomendaciones educativas

Asegurar acceso a tecnología y conexión adecuada

Personalizar duración de clases virtuales

Diseñar estrategias según edad y género

Brindar apoyo a estudiantes con desventaja económica
