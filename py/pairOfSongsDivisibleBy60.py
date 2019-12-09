# In a list of songs, the i-th song has a duration of time[i] seconds. 

# Return the number of pairs of songs for which their total duration in seconds is divisible by 60.  Formally, we want the number of indices i < j with (time[i] + time[j]) % 60 == 0.

# Example 1:

# Input: [30,20,150,100,40]
# Output: 3
# Explanation: Three pairs have a total duration divisible by 60:
# (time[0] = 30, time[2] = 150): total duration 180
# (time[1] = 20, time[3] = 100): total duration 120
# (time[1] = 20, time[4] = 40): total duration 60
# Example 2:

# Input: [60,60,60]
# Output: 3
# Explanation: All three pairs have a total duration of 120, which is divisible by 60.

def diviBy60(time):
    # result = 0

    # for i in range(len(time)):
    #     cur_song = time[i]
    #     for j in range(i+1, len(time)):
    #         pair_song = time[j]
    #         if (cur_song + pair_song) % 60 == 0:
    #             result += 1
    # good solution, but quadratic, which I already knew, now try to optimize

    # my idea now is to first get the total sum
    # now I will use this sum to set some sort of max for my loops
    # now I will do hash searches

    # return result

    # copied this answer, which made no sense at first glance
    # after studying, I realize it's basically a variation of 2-sum
    # store values as they appear based on their % 60
    # now look for the target, if the target matches, increment by how many times it matches
    # else: set the value in the dict, either to 1, or increment it
    # res = 0
    # mp = dict()
    # for tm in time:
    #     tm = tm % 60
    #     target = (60 - tm) % 60
    #     if target in mp:
    #         res += mp[target] # this isn't just an INCREMENT, because if target appeared twice previously, then both match
    #     mp[tm] = mp.get(tm, 0) + 1 # this basically says, give me mp[tm] if it exists, otherwise give me 0.. and then INCREMENT
    
    # return res

    # trying to do it myself now

    result = 0
    prev_songs_dict = dict()

    for song in time:
        song = song % 60
        target = (60 - song) % 60
        if target in prev_songs_dict:
            result += prev_songs_dict[target]
        prev_songs_dict[song] = prev_songs_dict.get(song, 0) + 1
    
    return result


result = diviBy60([30,20,150,100,40])
print('hi')