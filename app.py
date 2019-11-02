
"""main module from ehere exzcution should start"""
import json
import os

from flask import Flask, request
from flask_caching import Cache
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from parse_reponse import response

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["10 per minute", "1 per second"],
)

config = {
    "DEBUG": True,  # some Flask specific configs
    "CACHE_TYPE": "simple",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

#RATE_LIMIT_FUNCS = {'ip': lambda: get_remote_address}

app.config.from_mapping(config)
cache = Cache(app)


# endpoint to Recive request
@app.route("/rep.cal", methods=["POST"])
@limiter.limit("10000 per second")
def md5_json():
    try:
        request_payload = json.dumps(request.json)
        loaded_payloads = json.loads(request_payload)
        obj_response = response(**loaded_payloads)

        invalid_request = obj_response.validate_reposnse()

        if invalid_request is not None:
            return response_back(invalid_request)

        authenticate_request = obj_response.authenticate_reponse()

        if authenticate_request is True:
            list_score = obj_response.get_reputation_score()
            score = obj_response.calculate_reputation_score(list_score)
            reply_response = obj_response.preapare_response(score)
            return response_back(reply_response)
        return response_back(authenticate_request)
    except Exception as e:
        return response_back(str(e))

def response_back(messgae):
    return json.dumps(messgae)

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=False, threaded=True, )
