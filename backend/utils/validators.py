def validate_topic(topic):

    if not topic:
        return False

    if len(topic.strip()) < 3:
        return False

    return True


def validate_roadmap(roadmap):

    if not roadmap:
        return False

    if len(roadmap.strip()) < 20:
        return False

    return True


def validate_text(value):

    if not value:
        return False

    if len(value.strip()) == 0:
        return False

    return True