# Import necessary modules
from flask import Flask, render_template, redirect, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import SQLAlchemyError

# Create Flask application instance
app = Flask(__name__)

# Configure SQLAlchemy to use MySQL database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root:vicky2003@localhost/vicky'
db = SQLAlchemy(app)

# Define Account model
class Account(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    balance = db.Column(db.Float, default=0.0)

    def __repr__(self):
        return f'<Account {self.name}>'

# Define function to transfer money
def transfer_money(from_account_id, to_account_id, amount):
    try:
        # Start the transaction
        db.session.begin()

        # Update the balances
        from_account = Account.query.get(from_account_id)
        to_account = Account.query.get(to_account_id)

        if from_account.balance >= amount:
            from_account.balance -= amount
            to_account.balance += amount

            # Commit the transaction
            db.session.commit()
            return True, "Transaction successful."
        else:
            return False, "Insufficient balance."

    except SQLAlchemyError as e:
        # Rollback the transaction in case of any error
        db.session.rollback()
        return False, str(e)

# Define Flask routes and views
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transfer', methods=['POST'])
def transfer():
    from_account_id = request.form.get('from_account_id')
    to_account_id = request.form.get('to_account_id')
    amount = float(request.form.get('amount'))

    success, message = transfer_money(from_account_id, to_account_id, amount)

    if success:
        return redirect('/')
    else:
        return render_template('error.html', message=message)

# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)
