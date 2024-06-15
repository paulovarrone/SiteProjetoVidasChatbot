from flask import Flask, render_template, request

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/quem_somos')
def quem_somos():
    return render_template('quem_somos.html')

@app.route('/chat')
def ajuda():
    return render_template('chat.html')

@app.route('/contato')
def contato():
    return render_template('contato.html')

if __name__ == '__main__':
    app.run(debug=True)