import pandas
from flask import Flask, render_template
#webframe work as mangager for multiple pages in a website and responsible
import pandas as pd

stations=pd.read_csv("data_small/stations.txt",skiprows=17)
stations = stations[["STAID","STANAME                                 "]]


app= Flask(__name__)# we created a website object and now we have to connect html with website object
@app.route("/")# when home is called the tutorial.html is rendered
def home():
    return render_template("home.html",data=stations.to_html()) #tutorial.html should be in a specfic folder called templates
@app.route("/api/v1/<station>/<date>")
def about(station,date):
    filename = "data_small/TG_STAID"+str(station).zfill(6)+".txt"
    df=pd.read_csv(filename, skiprows=20, parse_dates=["    DATE"])
    temperature= df.loc[df['    DATE'] == date]['   TG'].squeeze() / 10
    return{"station": station,
           "date": date,
           "temerature": temperature
           }
if __name__ =="__main__":
    app.run(debug=True)
