from flask import Flask, request

app = Flask(__name__)

@app.route("/receive_data", methods=["POST"])
def receive_data():
    data = request.form["data"]
    try:
        with open("data.txt", "a") as file:
            file.write(data + "\n")
        return "Data received successfully", 200
    except Exception as error:
        return str(error), 500

@app.route("/get_data", methods=["POST"])
def get_data():
    try:
        with open("data.txt", "r") as file:
            data = file.read()
            if not data:
                return "No data found", 404
            return data, 200
    except FileNotFoundError:
        return "File not found", 404
    except Exception as error:
        return str(error), 500

if __name__ == "__main__":
    app.run(debug=True, port=5001)