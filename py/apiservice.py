# Dockerfile with FROM PYTHON with onbuild
# requirements.txt with Flask
# file below saved as api.py
# CMD python api.py inside Dockerfile
# docker-compose.yml file to build the service.. port, build from Dockerfile, volume mapping, port mapping


from flask import Flask, render_template, request, abort

app = Flask(__name__)

@app.route('/', METHODS=['GET'])
def index():
    # check if title exists in json
    if not request.json or not 'title' in request.json:
        abort(400)
    else:
        return ['title mirror', request.json['title']]

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=80)