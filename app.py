from flask import Flask, render_template, request

app = Flask(__name__)

import pickle

model = pickle.load(open(r'model.pkl', 'rb'))

@app.route('/')
def helloworld():
    return render_template("index.html")

@app.route('/login', methods=['POST'])
def login():
    try:
        # Retrieve form values
        a = int(request.form["cs"])
        b = int(request.form["ag"])
        c = int(request.form["tn"])
        d = int(request.form["bl"])
        e = int(request.form["pd"])
        f = int(request.form["cd"])
        g = int(request.form["ac"])
        h = int(request.form["sl"])
        i = request.form["location"]
        j = request.form["gender"]

        # Validate if all form fields are filled
        if any(value is None for value in [a, b, c, d, e, f, g, h, i, j]):
            return render_template("index.html", y="Please enter all values.")

        
        i1, i2 = 0, 0
        if i == "germany":
            i1, i2 = 1, 0
        elif i == "spain":
            i1, i2 = 0, 1

       
        j1 = 1 if j == "male" else 0

       
        k = [[a, b, c, d, e, f, g, h, i1, i2, j1]]

       
        output = model.predict(k)

        if output == 1:
            return render_template("index.html", y="Yes, the customer will leave the Bank")
        else:
            return render_template("index.html", y="No, the customer will not leave the Bank")

    except Exception as e:
        return render_template("index.html", y=f"Please Enter Values")

if __name__ == '__main__':
    app.run(debug=False)
    
