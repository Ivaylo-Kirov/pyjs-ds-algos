# asteroid_data = {
# "t_per_blast_move": 10,
# "asteroids": [
# {
# "offset": 0,
# "t_per_asteroid_cycle": 2
# },{
# "offset": 1,
# "t_per_asteroid_cycle": 3
# },{
# "offset": 3,
# "t_per_asteroid_cycle": 4
# },{
# "offset": 1,
# "t_per_asteroid_cycle": 2
# }]
# }
import requests
import json

data = requests.get('https://gist.githubusercontent.com/anonymous/83dbd1bcd9684cc8757d/raw/d5035345880ea5f4e5bf1c34d8a444e0c9746a04/v3_chart.json')
asteroid_data = data.json()

# return expects a json array
# accelerations add up
# t_per_blast_move is when Eschaton blows up
# t_per_asteroid_cycle is how many moves asteroid needs to cycle
# offset refers to where asteroid is currently (0 means it's in our way, 1 means it was in our way 1 move ago)
#   as a result, (t_per_asteroid_cycle - offset) should represent how many Ts until it hits us

def calc_escape_route(asteroid_data):
    '''returns a safe course in json that can be plugged into a frigade in order to escape Eschaton'''
    result = []
    cur_frigate_pos = 0
    cur_velocity = 0
    cur_t = 0
    destroyed_belts = 0
    looking_for_escape = True
    asteroids = asteroid_data["asteroids"]

    while looking_for_escape:
        print(f't={cur_t} p={cur_frigate_pos} v={cur_velocity}')

        # 8682 is current and velocity is 100 so I should now be able to go to
        # 8781 if I decel.. or 8782 if I coast..or 8783 if I accel

        # calcs (i.e. should I accel, stay, or decel) - decisions get result.append()
        # e.g. 1 should be represented as cur_velocity += 1
        # only asteroids we care about are asteroids[cur_frigate_pos +- cur_velocity]
        # and for those asteroids, we only care if we can move forward (i.e. avoid a hit based on t_per_asteroid_cycle - offset)
        # otherwise consider staying and check current asteroid, and if that will hit us too, then back up

        # let's try a basic check to accel, which is always ideal
        target_asteroid_index = cur_frigate_pos + cur_velocity
        target_asteroid_offset = asteroids[target_asteroid_index]["offset"] + cur_t + 1
        target_asteroid_cycle = asteroids[target_asteroid_index]["t_per_asteroid_cycle"]
        
        if cur_frigate_pos + cur_velocity - 1 < 0:
            cur_asteroid_index = 0
        else:
            cur_asteroid_index = cur_frigate_pos + cur_velocity - 1
        cur_asteroid_offset = asteroids[cur_asteroid_index]["offset"] + cur_t + 1
        cur_asteroid_cycle = asteroids[cur_asteroid_index]["t_per_asteroid_cycle"]
        

        if cur_velocity > 0 and (cur_asteroid_offset) % cur_asteroid_cycle != 0 and cur_asteroid_cycle != 1:
            result.append(0)
        else:
            # can use this to check if we are about to hit (asteroid_offset + cur_t) % asteroid_cycle
            if (target_asteroid_offset) % target_asteroid_cycle != 0 and target_asteroid_cycle != 1:
                result.append(1)
                cur_velocity += 1
                # accel if frigate will not hit
            elif (cur_asteroid_offset) % cur_asteroid_cycle != 0 and cur_asteroid_cycle != 1:
                # could not accel, so is it safe to stay course?
                result.append(0)
            else:
                # could not accel, could not stay course, so must decel
                # if I hit something here, I will never know, using my version
                result.append(-1)
                cur_velocity -= 1

        cur_t += 1
        cur_frigate_pos += cur_velocity

        # misunderstood this, each t_per_blast_move iteration, makes the following belt explode..so in this scenario
        # if cur_t % t_per_blast_move == 0 then increment destroyed belts
        if cur_t % asteroid_data["t_per_blast_move"] == 0:
            destroyed_belts += 1
            
        if cur_frigate_pos <= destroyed_belts:
            print("You have been consumed by the blast")
            break
        
        if cur_frigate_pos + cur_velocity + 1 >= len(asteroids):
            print('Frigate has escaped')
            result.append(1)
            break

    return result

result = calc_escape_route(asteroid_data)

with open('data.json', 'w') as f:
    json.dump(result, f)
print('hi')

# cycle of 1 I believe means that it must be skipped