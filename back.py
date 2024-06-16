from flask import Flask, render_template, request
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

client = Groq(api_key=os.environ.get("GROQ_API_KEY"))

app = Flask(__name__)

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


@app.route('/resposta', methods=['POST'])
def resposta():
    conteudo = 'Você é um medico com mais de 50 anos de experiencia'
    pergunta = request.form['pergunta']

    chat_completion = client.chat.completions.create(
        messages=[
            {"role": "system", "content": conteudo},
            {"role": "user", "content": pergunta},
            {"role": "assistant", "content": 'Ajude estudantes universitario da faculdade de medicina que fizerem perguntas'}
        ],
        model="llama3-8b-8192",
        temperature=0,
        max_tokens=1024,
        top_p=1,
        stop=None,
    )
    
    resposta = chat_completion.choices[0].message.content

    return render_template('chat.html', resposta=resposta, pergunta=pergunta)



if __name__ == '__main__':
    app.run(debug=True)
