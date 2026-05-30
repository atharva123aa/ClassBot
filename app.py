from  flask import Flask,render_template, request,redirect,url_for
import json as j
import os 




app=Flask(__name__) 
#will help as i dont want repeiting it
def load_data():
    with open('data.json','r') as f:
        return j.load(f)
def save_data():
    with open('data.json', 'w') as f:
        j.dump(data,f) 

@app.route('/')
def home():
    data=load_data()   
    if data['class_name'] =='':
        return redirect(url_for('setup'))
        return redirect(url_for('chat'))#TODO:ADD ONE THING SYNC IN RETURN REDIRECCT IN WHICH YOU CAN SYNC THAT IF MY OTHER FLASK APP SCT
@app.route('/setup',methods=['GET', 'POST'])
def setup():
    if request.method =='POST':
        tname=request.form.get('teacher')
        cname =request.form.get('classname')
        data=load_data()
       data['teacher_name'] =tname
       data['class_name']=cname
       save_data(data)
    return redirect(url_for('add_students'))
    
    return render_template('setup.html')
@app.route('/add', methods=  ['GET', 'POST'])
def add_students():
    data=load_data() 
    if request.method== 'POST':
        sname= request.form.get('sname')
        roll=request.form.get('roll')
        gender = request.form.get('gender')
        data['students'].append({
            'name': sname,
            'roll_no':int(roll),
            'gender'  :gender 
        })
        save_data(data)
        return  redirect(url_for('add_students'))
        return render_template('add.html', students=data['students'])

#todo to add  a auto appender so i dont have to rewrite

@app.route('/chat', methods=['GET' ,'POST])
def chat():
    data=load_data()
    rly= None
    if request.method=='POST':
        msg=request.form.get('msg')
        from bot import respond#todo:Add  define respond model in bot.py 
        rly=respond(msg,data)
    return render_template('chat.html', rly=rly, classinfo=data)

if__name__== '__main__':
    
    app.run(debug=True)
            



