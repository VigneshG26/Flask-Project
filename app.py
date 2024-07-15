from flask import Flask, render_template



app = Flask(__name__)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products/<name>')
def products(name):
    return render_template('specific_products.html',cat = name)



if __name__ == '__main__':
    app.run(debug=True)