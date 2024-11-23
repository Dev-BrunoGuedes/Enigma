from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Dicionário com respostas corretas para cada fase, agora mapeando para números
enigma_phases = {
    "index": {"resposta": "obrigado", "proxima": "378129837128937129873198273918"},         # Fase 1 → 2
    "378129837128937129873198273918": {"resposta": "1995", "proxima": "812937198237918273918273918273"},                # Fase 2 → 3
    "812937198237918273918273918273": {"resposta": "peixe", "proxima": "928374928374982374982374982374"},               # Fase 3 → 4
    "928374928374982374982374982374": {"resposta": "skript", "proxima": "192837192837192837192837192837"},              # Fase 4 → 5
    "192837192837192837192837192837": {"resposta": "algoaqui", "proxima": "283719283719283719283719283719"},            # Fase 5 → 6
    "283719283719283719283719283719": {"resposta": "enzorabelo", "proxima": "374928374928374928374928374928"},          # Fase 6 → 7
    "374928374928374928374928374928": {"resposta": "burmesedays", "proxima": "192847192847192847192847192847"},         # Fase 7 → 8
    "192847192847192847192847192847": {"resposta": "sideshowbob", "proxima": "827364827364827364827364827364"},         # Fase 8 → 9
    "827364827364827364827364827364": {"resposta": "trevas", "proxima": "918273918273918273918273918273"},             # Fase 9 → 10
    "918273918273918273918273918273": {"resposta": "carro", "proxima": "fim"},            # Última fase
}

@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return processa_fase('index')  # Tratar 'index' como a primeira fase

@app.route('/<fase>', methods=['GET', 'POST'])
def processa_fase(fase):
    if fase not in enigma_phases:
        return "Fase não encontrada!", 404

    if request.method == 'POST':
        resposta = request.form.get('resposta')
        if resposta == enigma_phases[fase]["resposta"]:
            proxima_fase = enigma_phases[fase]["proxima"]
            return redirect(url_for('processa_fase', fase=proxima_fase))
        return redirect(url_for('processa_fase', fase=fase) + "?erro=1")

    erro = request.args.get('erro')
    return render_template(f'{fase}.html', erro=erro)

@app.route('/fim')
def fim():
    return render_template('fim.html')  # Página final

if __name__ == "__main__":
    app.run(debug=True)