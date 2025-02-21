from flask import Flask, render_template, request
import random

app = Flask(__name__)

def generate_lottery(rows, balls, max_num=50):
    """Generate lottery numbers based on rows and balls."""
    if rows <= 0 or balls <= 0 or balls > max_num:
        return "Invalid input! Rows and balls must be positive, and balls <= " + str(max_num)
    result = []
    for _ in range(rows):
        numbers = sorted(random.sample(range(1, max_num + 1), balls))
        result.append(numbers)
    return result

@app.route('/', methods=['GET', 'POST'])
def index():
    """Handle the homepage and form submission."""
    if request.method == 'POST':
        try:
            rows = int(request.form['rows'])
            balls = int(request.form['balls'])
            result = generate_lottery(rows, balls)
            if isinstance(result, str):
                return render_template('results.html', result=result, error=True)
            return render_template('results.html', result=result, error=False)
        except ValueError:
            return render_template('results.html', result="Please enter valid numbers!", error=True)
    return render_template('index.html')

@app.route('/about')
def about():
    """Display the about page."""
    return render_template('index.html', show_about=True)

# Remove the app.run() line to avoid using the development server
# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
