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
    C1 = C1.upper()
    C2 = C2.upper()

    cards = [["H2", "D2", "C2", "S2"],
            ["H3", "D3", "C3", "S3"],
            ["H4", "D4", "C4", "S4"],
            ["H5", "D5", "C5", "S5"], 
            ["H6", "D6", "C6", "S6"],
            ["H7", "D7", "C7", "S7"], 
            ["H8", "D8", "C8", "S8"], 
            ["H9", "D9", "C9", "S9"], 
            ["HT", "DT", "CT", "ST"], 
            ["HJ", "DJ", "CJ", "SJ"], 
            ["HQ", "DQ", "CQ", "SQ"], 
            ["HK", "DK", "CK", "SK"], 
            ["HA", "DA", "CA", "SA"]]
    key1 = 0
    key2 = 0

    for row in cards:
        for card in row:
            if C1 == card:
                key1 = 1
    for row in cards:
        for card in row:
            if C2 == card:
                key2 = 1


    if key1 == key2 == 1:
        players = request.form['players']
        players = int(players)
        A1, A2, A3 = testing_pcalc.main_function(C1, C2, players)   
        return render_template('results.html', procent_over=A1, hand_strength=A2, split=A3)
        #redirect('/input')
    else:
        return render_template('input.html')

@app.route('/input', methods = ['POST'])
def input():
    return render_template('input.html')
    
 

if __name__ == '__main__':
   app.run(debug = True)
