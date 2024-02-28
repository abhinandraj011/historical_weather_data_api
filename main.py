from flask import Flask, render_template
#webframe work as mangager for multiple pages in a website and responsible

app= Flask(__name__)# we created a website object and now we have to connect html with website object
@app.route("/")# when home is called the tutorial.html is rendered
def home():
    return render_template("home.html") #tutorial.html should be in a specfic folder called templates
@app.route("/api/v1/<station>/<date>")
def about(station,date):
    temperature=23
    return{"station": station,
           "date": date,
           "temerature": temperature
           }
if __name__ =="__main__":
    app.run(debug=True)
