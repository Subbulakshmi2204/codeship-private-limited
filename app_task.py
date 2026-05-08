from flask import Flask, render_template,request

app = Flask(__name__)

all_data = []

@app.route('/')

def home():
    return render_template('07-05-2026 personal_info.html')
    
@app.route('/submit',methods=['POST'])
def submit():
    
    name = request.form['name']
    age = request.form['age']
    city = request.form['city']
    phno = request.form['phno']
    gender = request.form['gender']
    
    data = { 'name':name,'age':age,'city':city,'phno':phno,'gender':gender}
    
    all_data.append(data)
    
    return render_template('07-05-2026 output.html',all_data=all_data)

if __name__ == '__main__':
    app.run(debug=True)
    