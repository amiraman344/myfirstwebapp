import datetime
from flask import Flask, render_template
app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
# @app.route('/more')
# def more():
#     return render_template("more.html")

# @app.route('/')
# def form():
#     return render_template("form.html")

# @app.route('/hello', methods=["POST"])
# def hello():
#     name=request.form.get("name")
#     return render_template("hello.html", name=name)



#-----------------for connecting two pages


#-------------------TO find Is it new_year
# @app.route('/')
# def index():
#     now= datetime.datetime.now()
#     new_year=now.month ==1 and now.day ==1
#     new_year=True
#     return render_template("index.html", new_year=new_year)

#------------------------for loop for not repeating the same Html code
# @app.route('/')
# def index():
#     names=["amir","iqra"]
#     return render_template("index.html",names=names)
#--------------------------hello world
# @app.route('/<string:name>')
# def hello(name):
#     name= name.capitalize()
#     return f"hello, {name}"



