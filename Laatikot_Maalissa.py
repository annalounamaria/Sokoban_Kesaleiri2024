def are_all_boxes_in_goals():
    all_goals = len(goals);
    boxes_in_goal = 0;
    for box in boxes:
        for goal in goals:
            if(box.y == goal.y and box.x == goal.x):
                boxes_in_goal += 1
                print("laatikko maalissa")
    if(boxes_in_goal == all_goals):
        print("Voitto!")
        return True
