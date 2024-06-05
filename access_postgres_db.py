from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sde:sde@salesiqgen2.cygagau4oro0.us-west-2.rds.amazonaws.com:5432/next_gen'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Define your models based on the existing database schema
class HGPositions(db.Model):
    __tablename__ = 'hg_positions'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    hierarchy_level= db.Column(db.Integer)
    
# Routes to display details of first 10 rows of hg_positions table
@app.route('/')
def display_positions():
    positions = HGPositions.query.with_entities(HGPositions.name,HGPositions.hierarchy_level).all()
    return render_template('positions.html', positions=positions)

if __name__ == '__main__':
    app.run(debug=True)
