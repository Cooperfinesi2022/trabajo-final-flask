from flask import Flask, request, render_template
import joblib
import numpy as np

# cargar modelo y scalers
model = joblib.load('./model/insurance-ml.pkl')
sc_x   = joblib.load('./model/scaler_x.pkl')
sc_y   = joblib.load('./model/scaler_y.pkl')

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None

    # si el usuario envía el formulario, calcular la predicción puntual
    if request.method == 'POST':
        seguros = int(request.form['seguros'])
        # escalar, predecir y desescalar
        seguros_sc    = sc_x.transform([[seguros]])
        pred_sc       = model.predict(seguros_sc)
        pred_original = sc_y.inverse_transform(pred_sc) * 1000
        result        = round(pred_original[0][0], 2)

    # preparar datos para el gráfico: predicción vs número de seguros
    # aquí usamos un rango de 0 a 10; ajústalo según tu dominio
    seguros_range = list(range(0, 11))
    seguros_sc_all    = sc_x.transform(np.array(seguros_range).reshape(-1, 1))
    preds_sc_all      = model.predict(seguros_sc_all)
    preds_original_all = sc_y.inverse_transform(preds_sc_all) * 1000
    prices = [round(p[0], 2) for p in preds_original_all]

    return render_template(
        'index.html',
        result=result,
        seguros_range=seguros_range,
        prices=prices
    )

if __name__ == '__main__':
    app.run(debug=True)
