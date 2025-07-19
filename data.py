from app import app
from models import db, Topic, LearnerProgress

with app.app_context():
    db.drop_all()
    db.create_all()

    t1 = Topic(id=1, title='Intro to AI', prerequisite_ids=[])
    t2 = Topic(id=2, title='Machine Learning', prerequisite_ids=[1])
    t3 = Topic(id=3, title='Deep Learning', prerequisite_ids=[2])
    t4 = Topic(id=4, title='NLP Basics', prerequisite_ids=[2])
    t5 = Topic(id=5, title='Advanced NLP', prerequisite_ids=[4])

    db.session.add_all([t1, t2, t3, t4, t5])

    p1 = LearnerProgress(learner_id=1, topic_id=1, status='Completed', score=95.0)
    p2 = LearnerProgress(learner_id=1, topic_id=2, status='Completed', score=90.0)
    p3 = LearnerProgress(learner_id=1, topic_id=4, status='In Progress', score=65.0)

    db.session.add_all([p1, p2, p3])
    db.session.commit()

