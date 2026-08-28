from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    bmi = None
    category = None
    recommendation = None
    
    if request.method == 'POST':
        try:
            weight = float(request.form.get('weight'))
            height_cm = float(request.form.get('height'))
            goal = request.form.get('goal')
            diet = request.form.get('diet')
            location = request.form.get('location')
            injury = request.form.get('injury')
            
            height_m = height_cm / 100
            bmi = round(weight / (height_m ** 2), 1)
            
            if bmi < 18.5:
                category = "Underweight"
            elif 18.5 <= bmi < 25:
                category = "Normal weight"
            elif 25 <= bmi < 30:
                category = "Overweight"
            else:
                category = "Obese"
                
            recommendation = {
                'goal': goal,
                'diet': diet,
                'location': location,
                'injury': injury,
                'category': category
            }
        except ValueError:
            pass
            
    return render_template('calculator.html', bmi=bmi, category=category, rec=recommendation)

@app.route('/myths')
def myths():
    return render_template('myths.html')

@app.route('/challenges')
def challenges():
    selected_muscle = request.args.get('muscle', 'chest')
    selected_level = request.args.get('level', 'beginner')
    selected_env = request.args.get('environment', 'gym')
    
    return render_template('challenges.html', 
                           muscle=selected_muscle, 
                           level=selected_level, 
                           env=selected_env)

@app.route('/muscle')
def muscle():
    return render_template('muscle.html')

if __name__ == '__main__':
    app.run(debug=True)
