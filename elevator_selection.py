def nearest_lift(curr_pos, min):
    if(curr_pos < min):
        min = curr_pos
        return True
    return False


def get_lift(mydest, n): # assumptions-> mydest -> 'mypos': '3', 'dir': 'up'  || of dictionaries having lift statuses like status, current postion and direction
    fl = 0
    min = n[0]['current_pos']
    for i in range(len(n)):
        current = n[i]['current_pos']
        status = n[i]['status']
        pos = abs(current - mydest['mypos'])
        if(current == mydest['mypos']):    #if my position is same as any one of the elevators
            return n[i]
        if(status == "idle"):              #if there's any idle elevator nearby
            if(nearest_lift(pos, min)):
                min, fl = pos, i
        elif(status == "not-idle"):        
        #here we have choice-> we can give preference to the idle elevators or we can decide upon the non idle elevbators based on their direction, here I will let the code decide
            lift_direction = n[i]['dir']
            if(lift_direction == 'Up' and mydest['mypos'] > current):  #if the elevator is coming up and I'm above the elevator it can be chosen
                if(nearest_lift(pos, min)):
                    min, fl = pos, i
            if(lift_direction == 'Down' and mydest['mypos'] < current): #if the elevator is coming down and I'm below the elevator it can be chosen
                if(nearest_lift(pos, min)):
                    min, fl = pos, i
    return n[fl]  


mydest ={"mypos":6, "dir":"Up"}

n1 = [{"name":"A","status":"not-idle", "current_pos":4, "dir":"Up"},{"name":"B","status":"not-idle", "current_pos":2, "dir":"Up"},{"name":"C","status":"not-idle", "current_pos":5, "dir":"Down"}]  #this sample is based on all elevators busy ie not idle

n2 = [{"name":"A","status":"not-idle", "current_pos":4, "dir":"Up"},{"name":"B","status":"not-idle", "current_pos":2, "dir":"Up"},{"name":"C","status":"idle", "current_pos":5, "dir":"none"}]     #this sampple has only one idle ie C is idle and is nearest

n3 = [{"name":"A","status":"not-idle", "current_pos":4, "dir":"Up"},{"name":"B","status":"not-idle", "current_pos":2, "dir":"Up"},{"name":"C","status":"idle", "current_pos":3, "dir":"none"}]     #this sampple has only one idle ie C is idle but is far away


print(get_lift(mydest,n1))
print(get_lift(mydest,n2))
print(get_lift(mydest,n3))


 
