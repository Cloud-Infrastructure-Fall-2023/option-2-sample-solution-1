from flask import Flask, request, jsonify

app = Flask(__name__)

base_path = '/Users/lyk/Documents/CMU/23 Fall/14848/Project'

@app.route('/process_json', methods=['POST'])
def process_json():
    data = request.get_json()  # Get JSON data from the request

    # Process the JSON data as needed
    # You can access data['key'] to get specific values
    print("server received:", data)
    return jsonify({'message': 'Request processed successfully'}), 200

@app.route('/process_files', methods=['POST'])
def process_files():
    uploaded_files = request.files.getlist('file')

    for file in uploaded_files:
        print(file.filename)

    return jsonify({'message': 'Files processed successfully'}), 200


if __name__ == '__main__':
    app.run(debug=True, port=12345)