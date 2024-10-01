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

if __name__ == "__main__":
    app.run(debug=True, port=5001)