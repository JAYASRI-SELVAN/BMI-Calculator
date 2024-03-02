from flask import Flask, render_template, request

app = Flask(__name__)

def calculate_bmi(height, weight):
    height_in_meters = height / 100
    bmi = weight / (height_in_meters ** 2)
    return round(bmi, 2)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        height = float(request.form['height'])
        weight = float(request.form['weight'])
        bmi = calculate_bmi(height, weight)
        return render_template('index.html', bmi=bmi, height=height, weight=weight)

    return render_template('index.html', bmi=None, height=None, weight=None)

if __name__ == '__main__':
    app.run(debug=True)
