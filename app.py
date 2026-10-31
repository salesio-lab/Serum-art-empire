import os
from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html') if os.path.exists('templates/index.html') else '''
    <html><body style="text-align:center;padding:50px;font-family:sans-serif">
    <h1>🎨 Serum Art Empire - LIVE!</h1>
    <h2>Welcome to Ruiru's Best Art Shop!</h2>
    <p>Your paintings are coming soon...</p>
    <p><a href="/static/">View Art</a></p>
    </body></html>
    '''

@app.route('/static/<path:filename>')
def static_files(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)
