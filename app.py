
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Witaj w moim API!"

@app.route('/hello', methods=['GET'])
def hello():
    name = request.args.get('name')
    return f"Hello {name}!" if name else "Hello!"

@app.route('/api/v1.0/predict', methods=['GET'])
def predict():
    try:
    
        num1 = float(request.args.get('num1'))
        num2 = float(request.args.get('num2'))
        
        suma = num1 + num2
        prediction = 1 if suma > 5.8 else 0
        
        return jsonify({
            "prediction": prediction,
            "features": {
                "num1": num1,
                "num2": num2
            }
        })
        
    except (TypeError, ValueError):
        return jsonify({"error": "nieodpowiednie parametry. Podaj numeryczne wartosci dla num1 and num2."}), 400

if __name__ == '__main__':
    app.run(debug=True)


#do sprawdzenia działania programu - różne opcje

res = requests.get("http://127.0.0.1:5000/api/v1.0/predict?num1=3&num2=4")
print(res.json()) 

res = requests.get("http://127.0.0.1:5000/api/v1.0/predict?num1=2&num2=3")
print(res.json())

res = requests.get("http://127.0.0.1:5000/api/v1.0/predict")
print(res.json())

res = requests.get("http://127.0.0.1:5000/api/v1.0/predict?num1=abc&num2=4")
print(res.json())

