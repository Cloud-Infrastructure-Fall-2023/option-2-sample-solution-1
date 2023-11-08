from flask import Flask, render_template, request, jsonify
import base64
import requests
import mimetypes

app = Flask(__name__)

file_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/send_files', methods=['POST'])
def send_files():
    files = request.files.getlist('files[]') 

    global file_data
    file_data = []
    file_names = []
    for file in files:
        file_name = file.filename
        file_contents = file.read() 
        file_names.append(file_name)
        file_data.append({'name': file_name, 'contents': file_contents})
        
    response = {'message': 'Files received successfully', 'filenames': file_names}

    return jsonify(response)

@app.route('/construct_indices', methods=['POST'])
def construct_indices():
    response = {'message': 'Inverted indices constructed successfully'}
    return jsonify(response)

@app.route('/load_engine', methods=['POST'])
def load_engine():
    target_url = 'http://127.0.0.1:12345/process_files'
    files = []

    for file in file_data:
        mime_type, _ = mimetypes.guess_type(file['name'])
        print("filename:", file['name'])
        print("file type:", mime_type)
        print("file contents:", file['contents'])
        files.append(('file', (file['name'], file['contents'], mime_type or 'application/octet-stream')))
        print(files)
    return jsonify({'message': 'success'})
    response = requests.post(target_url, files=files)

    if response.status_code == 200:
        return jsonify({'message': 'success'})

    else:
        return jsonify({'message': "failure"})
    

@app.route('/top_n', methods=['POST'])
def top_n():
    response = {'message': 'Top-N executed successfully'}
    return jsonify(response)

@app.route('/search_term_input', methods=['POST'])
def search_term_input():
    target_url = 'http://127.0.0.1:12345/process_json'

    term = request.form.get('search_term')
    data = {'term': term}
    return jsonify({'message': "search term input executed", 'execution_time': 10})
    response = requests.post(target_url, json=data)
    print("after post")

    if response.status_code == 200:
        return jsonify({'message': str(response.json()), 'execution_time': 10})
    else:
        return jsonify({'message: failure'})


@app.route('/top_n_input', methods=['POST'])
def top_n_input():
    target_url = 'http://127.0.0.1:12345/process_json'

    number = request.form.get('n')
    data = {'number': number}
    print("data is", data)
    return jsonify({'message': "top n input executed"})
    response = requests.post(target_url, json=data)

    if response.status_code == 200:
        return jsonify({'message': str(response.json())})
    else:
        return jsonify({'message: failure'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
