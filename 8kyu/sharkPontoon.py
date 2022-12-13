def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):

    if dolphin:
        shark_speed = shark_speed / 2

    shark_speed=  shark_distance - pontoon_distance 
    youSpeed = pontoon_distance / you_speed
    
    return "Alive!" if youSpeed > shark_speed else "Shark Bait!"

    
print(shark(12, 50, 4, 8, True))
