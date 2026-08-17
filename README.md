# Breederbadge 
# Persistent storage file location
DATA_FILE = Path("badge_test.dat")
# Configurable responses dictionary
RESPONSES = {
"yiff": "You just got fucked hard in the stair-well",
"blow_job": "You found a big dick tiger at a room party, his cock almost made you choke",
"cream_pie": "You just finished fucking in the bathroom, he left you dripping",
"paw_job": "You just got a paw_job under the table",
}
@dataclass
class BadgeState:
script_runs: int = 0
counts: dict[str, int] = field(
default_factory=lambda: {action: 0 for action in RESPONSES}
)
@classmethod
def load(cls, filepath: Path) -> "BadgeState":
"""Loads state from JSON file; defaults if missing or invalid."""
if not filepath.exists():
return cls()
try:
data = json.loads(filepath.read_text())
script_runs = data.get("script_runs", 0)
counts = {
action: data.get("counts", {}).get(action, data.get(action, 0))
for action in RESPONSES
}
return cls(script_runs=script_runs, counts=counts)
except (json.JSONDecodeError, OSError):
print("Warning: Could not parse badge data file. Starting fresh.")
return cls()
def save(self, filepath: Path) -> None:
"""Saves state back to JSON file."""
payload = {
"script_runs": self.script_runs,
"counts": self.counts,
}
filepath.write_text(json.dumps(payload, indent=2))
def trigger_random_action(self) -> tuple[str, str]:
"""Picks a random action, increments counters, and returns result."""
action = random.choice(list(RESPONSES.keys()))
self.counts[action] += 1
self.script_runs += 1
return action, RESPONSES[action]
def main():
badge = BadgeState.load(DATA_FILE)
action, message = badge.trigger_random_action()
print(action)
print(message)
print(f"{action} has occurred {badge.counts[action]} time(s).")
print(f"You've gotten yiffed {badge.script_runs} time(s).")
badge.save(DATA_FILE)
if __name__ == "__main__":
main()
📁 Repository File Structure Reference
DEFCON-Switch-Badge-Bolgy-Wolgy/
├── Hardware/
[cite_start]│ ├── DEFCON_Switch_Badge.kicad_pro # KiCad Project File [cite: 715]
[cite_start]│ ├── DEFCON_Switch_Badge.kicad_sch # Main Badge Schematic [cite: 715]
[cite_start]│ ├── DEFCON_Switch_Badge.kicad_pcb # PCB Layout & Edge.Cuts [cite: 715]
[cite_start]│ ├── Switch_Badge_Art.kicad_mod # Converted Silkscreen Footprint [cite: 715]
[cite_start]│ └── Gerbers/ # Manufacturing Drill/Gerber files [cite: 724]
├── Artwork/
│ ├── bolgy wolgy.JPG # Main Switch Parody Art
│ └── photo_2026-08-03_13-50-09.jpg # SAO Insertion Visual Target
├── Firmware/
[cite_start]│ ├── Bolgy_wolgy_code.py # Main Badge Execution Logic [cite: 715]
[cite_start]│ └── badge_test.dat # Persistent State Storage JSON [cite: 16]
[cite_start]└── README.md # Project Description & Specifications [cite: 715]
