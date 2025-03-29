from flask import Flask ,request, jsonify ,make_response
from query_engine import translate_query, process_query, validate_query, convert_to_pseudo_sql
import base64
app = Flask('__name__')

# Lightweight authentication as required (Basic Auth)
def check_auth(username, password):
    return username == 'user' and password == 'pass'

def requires_auth(f):
    from functools import wraps
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return f(*args, **kwargs)
    return decorated

def authenticate():
    message = {'message': "Authenticate please"}
    resp = make_response(jsonify(message), 401)
    resp.headers['WWW-Authenticate'] = 'Basic realm="Login Required"'
    return resp

@app.route('/query', methods=['POST'])
@requires_auth
def query():
    data = request.get_json()
    query_text = data.get('query')

    if not query_text:
        return jsonify({"error": "Query text is required"}), 400

    category, price = translate_query(query_text)
    results = process_query(category, price)

    return jsonify({"results": results})

@app.route('/explain', methods=['POST'])
@requires_auth
def explain():
    data = request.get_json()
    query_text = data.get('query')

    if not query_text:
        return jsonify({"error": "Query text is required"}), 400

    category, price = translate_query(query_text)
    explanation = {
        "category_filter": category,
        "price_filter": price,
        "pseudo_sql": convert_to_pseudo_sql(query_text)
    }

    return jsonify({"explanation": explanation})

@app.route('/validate', methods=['POST'])
@requires_auth
def validate():
    data = request.get_json()
    query_text = data.get('query')

    if not query_text:
        return jsonify({"error": "Query text is required"}), 400

    is_valid = validate_query(query_text)
    return jsonify({"is_valid": is_valid})

if __name__ == '__main__':
    app.run(debug=True)
