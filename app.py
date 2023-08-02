from flask import Flask ,render_template

app = Flask(__name__)
post=[{'name':'School-'
       ,'title': 'BSF Sen Sec Red School',
       'post':"SILIGURI"
       },{'name':'UnderGrade-'
       ,'title': 'Institute of Engeernering and Management',
       'post':"Kolkata"
       }]

@app.route("/")
def hello_world():
    return render_template('Ankit.html',posts=post)


if(__name__=="__main__"):
   app.run(debug =True)