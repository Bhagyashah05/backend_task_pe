from flask import Flask, jsonify
from models import db
from utils import get_eligible_topics

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///learning.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/api/learning-path/<int:learner_id>', methods=['GET'])
def learning_path(learner_id):
    eligible_topics = get_eligible_topics(learner_id)
    return jsonify(eligible_topics)

if __name__ == '__main__':
    app.run(debug=True)
