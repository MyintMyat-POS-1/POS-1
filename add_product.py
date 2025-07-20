from flask import request, redirect, url_for

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        stock = request.form['stock']
        conn = get_db_connection()
        conn.execute('INSERT INTO products (name, price, stock) VALUES (?, ?, ?)', (name, price, stock))
        conn.commit()
        conn.close()
        return redirect(url_for('dashboard'))
    return render_template('add_product.html')
