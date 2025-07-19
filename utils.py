from models import Topic, LearnerProgress

def get_eligible_topics(learner_id):
    progress = LearnerProgress.query.filter_by(learner_id=learner_id).all()
    progress_map = {p.topic_id: p.status for p in progress}

    all_topics = Topic.query.all()
    eligible = []

    for topic in all_topics:
        if progress_map.get(topic.id) in ['In Progress', 'Completed']:
            continue

        if all(progress_map.get(pid) == 'Completed' for pid in topic.prerequisite_ids or []):
            eligible.append({
                'id': topic.id,
                'title': topic.title,
                'prerequisites': topic.prerequisite_ids
            })

    return eligible
