from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return '''
        <h1>velkommen til denne nettsiden</h1>
        <p><a href="https://www.vg.no/">Gå til VG</a></p>
        <p><a href="/aboutme/sebastian">Les mer om meg</a></p>
        <p><a href="/aboutbike/sebastian">Les mer om sykkel</a></p>
        <p><a href="/aboutlife/sebastian">Les mer om livet</a></p>
    '''

@app.route('/aboutme/<navn>')
def aboutme(navn):
    return f'''
        <h1>Om meg</h1>
        <p>Hei, jeg heter {navn}.</p>
        <a href="/">Tilbake til forsiden</a>
    '''

@app.route('/aboutbike/<navn>')
def aboutbike(navn):
    return f'''
        <h1>Om sykkel</h1>
        <p>Hei, jeg heter {navn}. Her skriver jeg om sykler.</p>
        <a href="/">Tilbake til forsiden</a>
    '''

@app.route('/aboutlife/<navn>')
def aboutlife(navn):
    return f'''
        <h1>Om livet</h1>
        <p>Hei, jeg heter {navn}. Her skriver jeg om livet.</p>
        <a href="/">Tilbake til forsiden</a>
    '''

if __name__ == "__main__":
    app.run()

