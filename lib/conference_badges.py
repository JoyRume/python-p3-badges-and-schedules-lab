

def badge_maker(name):
    return f"Hello, my name is {name}."

def batch_badge_creator(names):
    return [badge_maker(name) for name in names]

def assign_rooms(speakers):
    return [f"Hello, {speaker}! You'll be assigned to room {index + 1}!" for index, speaker in enumerate(speakers)]

def printer(speakers):
    badges = batch_badge_creator(speakers)
    room_assignments = assign_rooms(speakers)
    for badge in badges:
        print(badge)
    for assignment in room_assignments:
        print(assignment)
