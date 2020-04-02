from flask import Flask, request, redirect, render_template
app = Flask(__name__)
@app.route('/', methods = ['GET'])
def get_input():
    print("/input")
    return render_template('input.html')

@app.route('/handle_data', methods=['POST'])
def handle_data():
    C1 = request.form['card1']
    C2 = request.form['card2']
    print(C1, C2)
    return redirect('/input')

@app.route('/input', methods = ['POST'])
def input():
    print("cards: ")
    return render_template('input.html')
    
 

if __name__ == '__main__':
   app.run(debug = True)

print(handle_data())