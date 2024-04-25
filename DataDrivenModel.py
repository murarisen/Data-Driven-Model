# from crypt import methods
# from operator import methodcaller
import pickle
from flask import Flask,render_template,request
# from winreg import REG_WHOLE_HIVE_VOLATILE

model = pickle.load(open('model.pkl','rb'))
app=Flask(__name__,template_folder='template')
@app.route('/')
def index1():
    return render_template('index1.html')

@app.route('/predict',methods=['GET','POST'])
def predict():
    Flushing=int(request.form.get('Flushing1'))
    Discharge=int(request.form.get('Discharge1'))
    Pulse=int(request.form.get('Pulse1'))
    Duty=int(request.form.get('Duty1'))
    Recast=float(request.form.get('Recast1'))

    li=[Flushing,Discharge,Pulse,Duty,Recast]
    Circularity=model.predict([li])
    output=round(Circularity[0],2)
    #Recast=model.predict([li])
    #output=round(Recast[0],2)
    return render_template('index1.html',predict_text=f'Circularity for given inputs is {output}')




if __name__=='__main__':
    app.run(debug=True)    



