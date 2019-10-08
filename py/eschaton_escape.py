# Ivaylo Kirov - Sep. 18, 2019
import requests
import json

data = requests.get('https://gist.githubusercontent.com/anonymous/83dbd1bcd9684cc8757d/raw/d5035345880ea5f4e5bf1c34d8a444e0c9746a04/v3_chart.json')
asteroid_data = data.json()

def calc_escape_route(asteroid_data):
    '''returns a safe course in json that can be plugged into a frigate in order to escape Eschaton'''
    print(f'goal is {len(asteroid_data["asteroids"])}')
    for i in range(1, 150):
        ideal_speed = i
        result, cur_frigate_pos, cur_velocity, cur_t, destroyed_belts, looking_for_escape, asteroids = [], 0, 0, 1, 0, True, asteroid_data["asteroids"]
        while looking_for_escape:
            
            #print(f't={cur_t} p={cur_frigate_pos} v={cur_velocity}')

            if cur_frigate_pos == 0:
                if asteroids[0]["offset"] + cur_t == 0:
                    result.append(0)
                    cur_t += 1
                    continue
                else:
                    result.append(1)
                    cur_velocity += 1
                    cur_t += 1
                    cur_frigate_pos += cur_velocity
                    continue

            decel_target = asteroids[cur_frigate_pos + cur_velocity - 2]
            cur_target = asteroids[cur_frigate_pos + cur_velocity - 1]
            boost_target = asteroids[cur_frigate_pos + cur_velocity]

            # prioritize decel
            if cur_velocity > ideal_speed and (decel_target["offset"] + cur_t) % decel_target["t_per_asteroid_cycle"] != 0 and decel_target["t_per_asteroid_cycle"] != 1:
                result.append(-1)
                cur_velocity += -1
            else:
                if (cur_target["offset"] + cur_t) % cur_target["t_per_asteroid_cycle"] != 0 and cur_target["t_per_asteroid_cycle"] != 1:
                    result.append(0)
                    #print('the ship coasts: a=0')
                elif (decel_target["offset"] + cur_t) % decel_target["t_per_asteroid_cycle"] != 0 and decel_target["t_per_asteroid_cycle"] != 1:
                    result.append(-1)
                    cur_velocity += -1
                    #print('the ship decelerates: a=-1')
                elif (boost_target["offset"] + cur_t) % boost_target["t_per_asteroid_cycle"] != 0 and boost_target["t_per_asteroid_cycle"] != 1:
                    result.append(1)
                    cur_velocity += 1
                    #print('the ship accelerates: a=1')
                else:
                    print(f'failed for speed {ideal_speed} at {cur_frigate_pos} with velocity {cur_velocity}')
                    break
            
            cur_t += 1
            cur_frigate_pos += cur_velocity

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
#with open('data.json', 'w') as f:
    #json.dump(result, f)
print('hi')

