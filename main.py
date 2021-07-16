from flask import Flask, render_template
app = Flask(__name__)
# @app.route("/")
@app.route('/')
def index():
    return render_template("index.html")
@app.route("/yanwei")
def yanwei():
    return "Hello, Yanwei"
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
    # app.run( port=80, debug=True)
#   We made two new changes
#render_template將會找尋html檔案傳送給使用者