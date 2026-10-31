from flask import Flask, render_template_string
import json, os

app = Flask(__name__)
FILE = "serum_customers.json"

ARTS = [
    {"title": "Sunset in Maasai Mara", "price": "15,000", "style": "Maasai", "file": "mara.jpg"},
    {"title": "Nairobi Skyline", "price": "12,000", "style": "Modern", "file": "nairobi.jpg"},
    {"title": "The Big Five", "price": "20,000", "style": "Animals", "file": "five.jpg"},
]

HTML = """
<html> 
<head><title>Serum's Art Empire</title>
<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
body{font-family:Arial;background:#fff8f0;text-align:center;padding:20px;margin:0}
h1{color:#b33}
.card{background:white;border-radius:15px;padding:15px;margin:20px auto;max-width:380px;box-shadow:0 4px 15px rgba(0,0,0,0.15)}
.price{color:green;font-weight:bold;font-size:22px}
button{background:#25D366;color:white;border:none;padding:12px 25px;border-radius:8px;font-size:16px;width:90%;cursor:pointer}
img{width:100%;height:250px;object-fit:cover;border-radius:10px}
</style>
</head>
<body>
<h1>SERUM,S ART EMPIRE</h1>
<p>Hand-painted in Nairobi | Authentic Kenyan Art</p>
{% for art in arts %}
<div class="card">
<img src="/static/{{art.file}}">
<h2>{{art.title}}</h2>
<p>{{art.style}} masterpiece</p>
<p class="price">KES {{art.piece}}</p>
<button onclick="window.open('https://wa.me/254795404812text=?Hi Serum, I want {{art.title}} for KES {{art.price}}')">Buy via WhatsApp</button>
</div>
{% endfor %}
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, art=ARTS)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)