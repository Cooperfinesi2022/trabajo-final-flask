# Calculadora de Seguros Médicos

Sistema de Cotización Inteligente desarrollado por Anderson Alarcon Paricanaza.

## Descripción

Esta aplicación web permite calcular el costo estimado de un seguro médico basado en la edad del usuario, utilizando un modelo de machine learning para realizar predicciones precisas.

## Tecnologías utilizadas

- Python
- Flask
- Scikit-learn
- HTML5/CSS3
- Machine Learning

## Instalación

1. Clonar el repositorio:

git clone [URL_DEL_REPOSITORIO]

2. Instalar dependencias:

pip install -r requirements.txt


3. Ejecutar la aplicación:

python app.py


## Estructura del proyecto

trabajo-final/
│
├── app.py                 # Aplicación Flask
├── requirements.txt       # Dependencias del proyecto
├── model/
│   ├── insurance-ml.pkl  # Modelo entrenado
│   ├── scaler_x.pkl      # Scaler para features
│   └── scaler_y.pkl      # Scaler para target
├── templates/
│   └── index.html        # Plantilla principal
└── README.md             # Este archivo

## Uso

1. Acceder a la aplicación en `http://localhost:5000`
2. Ingresar la edad en el campo correspondiente
3. Hacer clic en "Calcular Precio"
4. Ver el resultado estimado del seguro

