from flask import Flask, request, redirect, render_template
import testing_pcalc
app = Flask(__name__)
@app.route('/', methods = ['GET'])
def get_input():
    return render_template('input.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    C1 = request.form['card1']
    C2 = request.form['card2']
    players = request.form['players']
    players = int(players)
    A1, A2, A3 = testing_pcalc.main_function(C1, C2, players)   
    return render_template('results.html', procent_over=A1, hand_strength=A2, split=A3)
    #redirect('/input')

@app.route('/input', methods = ['POST'])
def input():
    return render_template('input.html')
    
 

if __name__ == '__main__':
   app.run(debug = True)
