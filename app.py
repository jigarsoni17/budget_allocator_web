from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

def allocate_budget(salary):
    categories = {
        "Essentials": {
            "Rent/Mortgage": 0.24,
            "Utilities and Bills": 0.06,
            "Groceries": 0.10,
            "Transportation": 0.10,
        },
        "Savings": {
            "Emergency Fund": 0.10,
            "Vacation Savings": 0.05,
            "Special Occasion Fund": 0.05,
        },
        "Investments": {
            "Retirement Accounts": 0.10,
            "Stock Market or Mutual Funds": 0.06,
            "Bonds or Other Securities": 0.04,
        },
        "Discretionary Spending": {
            "Dining Out and Social Activities": 0.05,
            "Hobbies and Entertainment": 0.05,
        }
    }

    allocated_budget = {}
    for category, subcategories in categories.items():
        allocated_budget[category] = {subcategory: salary * percentage for subcategory, percentage in subcategories.items()}
    return allocated_budget

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/allocate', methods=['POST'])
def allocate():
    try:
        salary = float(request.form['salary'])
        allocated_budget = allocate_budget(salary)
        return jsonify(allocated_budget)
    except ValueError:
        return jsonify({'error': 'Please enter a valid number for the salary.'}), 400

if __name__ == '__main__':
    app.run(debug=True)
