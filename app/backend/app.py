from flask import Flask, jsonify, request

app = Flask(__name__)

# Define a route for the root URL
@app.route('/')
def hello_world():
    return 'Hello, World!'

# Define a route that returns JSON data
@app.route('/data', methods=['GET'])
def get_data():
    data = {'message': 'This is data from the backend'}
    return jsonify(data)

# Define a route to receive data from the client
@app.route('/post', methods=['POST'])
def post_data():
    content = request.json
    print(content)  # Process the data as needed
    return jsonify({'status': 'success', 'data': content})

if __name__ == '__main__':
    app.run(debug=True)
