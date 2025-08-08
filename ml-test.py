import joblib
import numpy as np
import sklearn

model = joblib.load('./model/insurance-ml.pkl')
sc_x   = joblib.load('./model/scaler_x.pkl')
sc_y   = joblib.load('./model/scaler_y.pkl')

print("Scikit-learn version:", sklearn.__version__)
print(f"sc_x mean: {sc_x.mean_}, scale: {sc_x.scale_}")
print(f"sc_y mean: {sc_y.mean_}, scale: {sc_y.scale_}")

edad = int(input("Ingrese la edad del asegurado: "))

edad_sc        = sc_x.transform(np.array([[edad]]))
pred_sc        = model.predict(edad_sc)
pred_original  = sc_y.inverse_transform(pred_sc) * 1000

print(f'El precio del seguro para {edad} años es de: $ {pred_original[0][0]:.2f}')
