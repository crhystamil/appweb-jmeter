from flask import Flask, render_template, request
import random

app = Flask(__name__)

# Página de inicio
@app.route('/')
def home():
    return render_template('home.html')

# Página de productos
@app.route('/products')
def products():
    # Genera una lista de productos aleatorios
    products = [f'Producto {i}' for i in range(1, random.randint(2, 10))]
    return render_template('products.html', products=products)

# Página de contacto
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Aquí podrías agregar lógica para guardar la información o enviarla a algún lugar
        return render_template('contact.html', success=True)
    return render_template('contact.html', success=False)

if __name__ == '__main__':
    app.run(debug=True)

