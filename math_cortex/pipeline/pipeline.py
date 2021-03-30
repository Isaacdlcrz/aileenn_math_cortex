import json
from ..exceptions import InternalServerError
from flask import Blueprint, jsonify, request
from .pipeline_utility import convolve_2_dfs, predictions
import pandas as pd

#Blueprint Configuration
pipeline_bp = Blueprint('pipeline_bp', __name__)

# All routes have '/pipeline' as a prefix as declared on __init__.py

@pipeline_bp.route("", methods=['POST'])
def get_conv():
    try:
        body = json.loads(request.get_data())
        """{
                data1: {
                    tag: tag,
                    data: data
                },
                data2: {
                    tag: tag,
                    data: data
                }
           }"""
        df1 = pd.DataFrame(body['data1']['data'])
        df2 = pd.DataFrame(body['data2']['data'])
        return jsonify((convolve_2_dfs(df1, df2, body['data1']['tag'], body['data2']['tag'])).tolist())
    except Exception as e:
        if hasattr(e, 'message'):
            print("Ex message", e.message)
        else:
            print("Ex", e)
        raise InternalServerError
        
@pipeline_bp.route("/predictions", methods=['POST'])
def get_pred():
    try:
        body = json.loads(request.get_data())
        """{
                "tag_x": [Arreglo de fechas]
                "tag_y": [Arreglo de valores]
           }"""
        df1 = pd.DataFrame(body)
        
        return predictions(df1)
    except Exception as e:
        if hasattr(e, 'message'):
            print("Ex message", e.message)
        else:
            print("Ex", e)
        raise InternalServerError
