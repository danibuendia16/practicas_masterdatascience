import flask
from joblib import load
import pandas as pd
import json
from werkzeug.exceptions import BadRequest

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return ""

@app.errorhandler(KeyError)
def handle_unexpected_error(error):
    status_code = 400
    response = {
        'error': {
            'type': 'Bad request',
            'message': 'Parametro invalido los parametros validos son [C_MNTH,C_WDAY,C_HOUR,C_VEHS,C_CONF,C_RCFG,C_WTHR,C_RSUR,C_RALN,C_TRAF,V_TYPE_1,V_TYPE_10,V_TYPE_11,V_TYPE_14,V_TYPE_16,V_TYPE_17,V_TYPE_18,V_TYPE_19,V_TYPE_20,V_TYPE_21,V_TYPE_22,V_TYPE_23,V_TYPE_24,V_TYPE_5,V_TYPE_6,V_TYPE_7,V_TYPE_8,V_TYPE_9,P_SEX_F,P_SEX_M,P_SAFE,P_AGE,A_VAGE]'
        }
    }

    return json.dumps(response), status_code

@app.errorhandler(BadRequest)
def handle_unexpected_error(error):
    status_code = 400
    response = {
        'error': {
            'type': 'Bad request',
            'message': error.description
        }
    }

    return json.dumps(response), status_code

@app.route('/predict', methods=['GET'])
def predict():
    input = dict(flask.request.args)

    validations = {
        'C_MNTH':[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        'C_WDAY': [1, 2, 3, 4, 5, 6, 7],
        'C_HOUR': [0, 1, 2, 3],
        'C_CONF': [1, 2, 3, 4, 5, 6, 21, 22, 23, 24, 25, 31, 32, 33, 34, 35, 36, 41, 42],
        'C_RCFG': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 13],
        'C_WTHR': [1, 2, 3, 4, 5, 6, 7, 8],
        'C_RSUR': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
        'C_RALN': [1, 2, 3, 4, 5, 6, 7],
        'C_TRAF': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19]
    }
    default_validation = ['C_MNTH','C_WDAY','C_HOUR','C_VEHS','C_CONF','C_RCFG','C_WTHR','C_RSUR','C_RALN','C_TRAF','V_TYPE_1','V_TYPE_10','V_TYPE_11','V_TYPE_14','V_TYPE_16','V_TYPE_17','V_TYPE_18','V_TYPE_19','V_TYPE_20','V_TYPE_21','V_TYPE_22','V_TYPE_23','V_TYPE_24','V_TYPE_5','V_TYPE_6','V_TYPE_7','V_TYPE_8','V_TYPE_9','P_SEX_F','P_SEX_M','P_SAFE','P_AGE','A_VAGE']
    for key,value in input.items():
        input[key] = [value]
        if key not in default_validation:
            raise KeyError()
        if key in validations:
            if int(value) not in validations[key]:
                message = f'El valor de {key} debe estar entre {validations[key]}'
                raise BadRequest(description=message)
        
    
    defaults = list(set(default_validation) - set(input.keys()))
   
    for key in defaults:
        input[key] = [None]
    
    print(input,flush=True)
    input_df = pd.DataFrame(input)
    model = load('./model.joblib')
    threshold = 0.075053

    output = {
        "prediccion" : 1 if model.predict_proba(input_df)[0][1] > threshold else 0,
        "probabilidad_fatalidad" : float(model.predict_proba(input_df)[0][1]),
        "probabilidad_no_fatalidad" : float(model.predict_proba(input_df)[0][0])

        
    }

    return output

app.run(host='0.0.0.0', port=5000)
