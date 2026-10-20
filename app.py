import io
from contextlib import redirect_stdout
from flask import Flask, render_template, request, jsonify
import arithmatic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate_route():
    try:
        a = int(request.form['topNumber'])
        b = int(request.form['botNumber'])
    except (KeyError, ValueError):
        return jsonify(error='Please enter valid whole numbers.')

    op = request.form.get('operation', '')

    if a < 0 or b < 0:
        return jsonify(error='Negative numbers are not supported.')
    if op in ('-', '/') and a < b:
        return jsonify(error='For subtraction and division, the first number must be >= the second.')
    if op == '/' and b == 0:
        return jsonify(error='Cannot divide by zero.')

    buf = io.StringIO()
    try:
        with redirect_stdout(buf):
            arithmatic.calculate(a, b, op)
    except Exception as e:
        return jsonify(error=f'{type(e).__name__}: {e}')

    return jsonify(output=buf.getvalue())

if __name__ == '__main__':
    app.run(debug=True)