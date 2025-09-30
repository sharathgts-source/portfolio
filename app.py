from flask import Flask, render_template, request, redirect, flash

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Required for flashing messages

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')

    # For now, just simulate storing or emailing it
    print(f"New message from {name} ({email}): {message}")
    flash('Thank you for reaching out!')

    return redirect('/')

if __name__ == '_main_':
    app.run(debug=True, port=8000)