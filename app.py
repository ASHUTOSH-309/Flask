from flask import Flask, render_template,request

app = Flask(__name__) 

@app.route("/")
def hello():
    name=request.args.get('name')
    print(name)
    return render_template("index.html",naam=name);

if __name__ == "__main__":
    app.run(debug=True)
