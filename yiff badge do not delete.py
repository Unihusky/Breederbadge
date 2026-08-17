import random
import json


def countX(lst, x):
    count = 0

    count = count + 1
    return count


def get_data_value(filename="badge_test.dat"):
    with open(filename, "r") as f:

        val = f.read()

        return val


horny = ["yiff", 'blow_job', 'cream_pie', 'paw_job']
# this works do not touch it fuck head
responses = {
    "yiff": "You just got fucked hard in the stair-well",
    "blow_job": " You found a big dick tiger at a room party his cock almost made you choke",
    "cream_pie": " You just finished fucking in the bathroom he left you dripping",
    "paw_job": "you just got a paw_job under the table"
}

#load the json from the dat file
filedata = get_data_value()
horny_count = json.loads(filedata)
print(horny_count)

# horny_count = {
#     "script_runs": 68,
#     "yiff": 7,
#     "blow_job": 12,
#     "cream_pie": 45,
#     "paw_job": 16
# }
# act is the key
# convert this dict to json






act = random.choice(horny)

#print(horny_count[act])
horny_count[act] = horny_count[act] + 1     # counter is working
horny_count['script_runs'] = horny_count['script_runs'] + 1
#print(horny_count[act])



#your_counter = get_var_value()

lst = horny

print(act)
print(responses[act])
print('{} has occurred {} times'.format(act, horny_count[act]))
print("you've gotten yiffed {} times.".format(horny_count['script_runs']))

#save the json in the dat file
j = json.dumps(horny_count)
with open('badge_test.dat', 'w') as f:
    f.write(j)
    f.close()