from flask import Flask, render_template

app = Flask(__name__)



@app.route('/play')
def rename():
    return render_template("index.html", num=3, color="blue")

@app.route('/play/<int:num>')
def second(num):
    return render_template("index.html", num=num, color="green")

@app.route('/play/<string:color>/<int:num>')
def third(color, num):
    return render_template("index.html", color=color, num=num) 



if __name__=="__main__":
    app.run(debug=True)