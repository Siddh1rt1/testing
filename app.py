from flask import Flask, request, render_template, jsonify, json
app = Flask(__name__)

import os, random
import jinja2
import argparse
import re
import time

SenCut = True
global_input = "Merz"
global_timer = 2
global_words = 2
check_1=0
check_2=0
check_3=0
check_4=0
option="normal"
option2="send"
classic_var=0
status = "html"

@app.route('/')
def index():
  global check_1
  check_1="checked"
  return render_template('index.html',val1="Merz", val2="10", timer=global_timer, timer_variable=global_timer, input_variable = global_input, words_variable = global_words, checked1="checked", checked2=check_2, checked3=check_3, checked4=check_4)

@app.route('/_stuff', methods= ['GET'])
def stuff():
    cpu=round(getCpuLoad())
    ram=round(getVmem())
    disk=round(getDisk())
    return jsonify(cpu=cpu, ram=ram, disk=disk)

@app.route('/background_process_test', methods= ['GET', 'POST'])
def setstatusold():
    status= "statusisserver"
    return status



@app.route('/getStatus')
def get_status():
    global status
    batus=status
    return jsonify(batus)



@app.route('/', methods=['POST'])
def my_form_post():

    global status
    status="server"
    in_text = request.form['text']
    global global_input
    global_input=str(in_text)
    print("log")
    in_words = request.form['text3']
    global global_words 
    global_words= int(in_words)
    
   

    global option
    option = request.form['radio']

    if option == 0 :
      option="normal"
    else:
      print("option=0")

    global check_1
    if str(option)in"normal":
      check_1 = "checked"
    else:
      check_1 = ""

    global check_2
    if str(option)in"Oneliner":
      check_2 = "checked"
    else:
      check_2 = ""

    global check_3
    if str(option)in"Klassisch":
      check_3 = "checked"
    else:
      check_3 = ""

    global check_4
    if str(option)in"Aggro":
      check_4 = "checked"
    else:
      check_4 = ""

  

    with open("data/out.csv", "r+") as himmel:
      top = himmel.read()

    if (str(in_text) not in str(top)):
      return render_template('index.html', data="Missing Data - 'Menschen' Eike hat über "+in_text+"noch keinen Witz geschrieben.", timer_variable=global_timer, input_variable = global_input, words_variable = global_words, checked1=check_1, checked2=check_2, checked3=check_3, checked4=check_4)

    else:
      timer = request.form['text2']
      
      
      set_global_timer(timer)
     
      out_result=('')
      x_ticker=int(timer)
      status = "train"
      for x in range(x_ticker):
        print (x)
        x=x+1
        import train 
        from train import dataset, model, predict 
        #train.predict(dataset,model,text)
        #besult= train.train(dataset,model,args)
        text_result= train.predict(option ,dataset , model, in_text, next_words=global_words) 
        print(text_result)

        if option in "Aggro":
          text_result = text_result.upper()
        else:
          print("noupper")
        
        out_result=out_result+text_result+" \n"
    status="html"
    return render_template('index.html',data=out_result+str(global_timer), timer_variable=global_timer, input_variable = global_input, words_variable = global_words, checked1=check_1, checked2=check_2, checked3=check_3, checked4=check_4)

def checkboxes():
   print("yes")   





def set_global_timer(timer):
  global global_timer
  global_timer= timer

def set_timer(timer):
  timer=int(timer)
  timer=str(timer)
  
  print(timer.isdecimal())
  if timer>20:
        timer=20
  else: print("timer")
  if timer<1:
        timer=1
  else: print("timer")
  timer=int(timer)
  return timer

if __name__ == '__main__':
  import argparse
  app.run(debug=True)
  
