from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    prerequisite_ids = db.Column(db.PickleType) 

class LearnerProgress(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    learner_id = db.Column(db.Integer)
    topic_id = db.Column(db.Integer, db.ForeignKey('topic.id'))
    status = db.Column(db.String(20)) 
    score = db.Column(db.Float)
