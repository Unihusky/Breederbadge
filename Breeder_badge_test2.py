from pathlib import Path
import json
import random


# Single source of truth for all potential badge responses
RESPONSES = {
    "yiff": "You just got fucked hard in the stair-well",
    "blow_job": " You found a big dick tiger at a room party his cock almost made you choke",
    "cream_pie": " You just finished fucking in the bathroom he left you dripping",
    "paw_job": "you just got a paw_job under the table"
}

ACTIONS = list(RESPONSES.keys())

BADGE_DATA_FILE = "badge.dat"

# We use a Badge throughout the script, so lets make sure it's a first class object
class Badge:
    # This __init__ function is called whenever we initialize a new badge.
    def __init__(self):
        self.possible_actions = ACTIONS
        # For each possible action, lets initialize to 0
        self.actions_performed = {action: 0 for action in self.possible_actions}
        self.script_runs = 0

    def increment_action(self, action):
        self.actions_performed[action] += 1
        self.script_runs += 1

    def perform_action(self):
        action = random.choice(self.possible_actions)
        self.increment_action(action)
        return (action, RESPONSES[action])

    def get_action_count(self, action):
        return self.actions_performed[action]

    def get_run_count(self):
        return self.script_runs

    def save(self):
        with open(BADGE_DATA_FILE, 'w') as f:
            f.write(json.dumps(self.__dict__))


# Returns a Badge object representing the current state of the badge
def initialize_or_load_badge_data():
    badge_object = {}
    if Path(BADGE_DATA_FILE).exists():
        with open(BADGE_DATA_FILE, 'r') as f:
            badge_dict = json.loads(f.read())
            badge_object = Badge(**badge_dict)
    else:
        badge_object = Badge()
    return badge_object

# Let's load up the badge data
badge = initialize_or_load_badge_data()

# Perform an action from this badge's possible actions
action, response = badge.perform_action()

print(action)
print(response)
print(f"{action} has occurred {badge.get_action_count(action)} times")
print(f"you've gotten yiffed {badge.get_run_count()} times.")

badge.save()

