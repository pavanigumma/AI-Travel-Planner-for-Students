from flask import Flask, render_template, request
from itinerary_generator import generate_itinerary
from budget_calculator import calculate_budget

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    itinerary = None
    budget_details = None

    if request.method == 'POST':
        destination = request.form['destination']
        budget = request.form['budget']
        days = request.form['days']
        interests = request.form['interests']

        itinerary = generate_itinerary(destination, budget, days, interests)
        budget_details = calculate_budget(budget, days)

    return render_template('index.html', 
                           itinerary=itinerary,
                           budget_details=budget_details)

if __name__ == "__main__":
    app.run(debug=True)
