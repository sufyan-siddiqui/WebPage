from flask import Flask, render_template, request

app=Flask(__name__)

@app.route("/")
def index():
   return render_template("index.html")

@app.route("/result", methods=["POST"])
def result():
    
    data = request.form.get("news-text")
    flag=True
    sources=["www.google.com", "www.youtube.com", "www.bbc.com", "www.newyorktimes.com"]
    return render_template("result.html", flag=flag, sources=sources, data=data)