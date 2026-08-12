import os
import shutil
import re

# Week mapping
week_mapping = {
    1: ["B1", "B2", "S1", "P1"],
    2: ["S2", "S3", "P2"],
    3: ["S4", "S5", "P3"],
    4: ["B3", "S6", "S7", "P4"],
    5: ["S8", "P5", "P6", "P7"],
    6: ["S9", "P8", "P9"],
    7: ["S10", "P10", "P11"],
    8: ["D1", "D2", "D3", "D4", "D5"],
    9: ["D6", "D7", "D8", "P12"],
    10: ["B4", "B5", "B6", "B7", "B8", "D9", "D10"]
}

# Reverse mapping: Station -> Week
station_to_week = {}
for week, stations in week_mapping.items():
    for station in stations:
        station_to_week[station] = week

# Initialize buffers for each week
week_buffers = {w: [] for w in range(1, 11)}

with open('docs/task-list.md', 'r') as f:
    lines = f.readlines()

current_week = None

for line in lines:
    # Match station headers like "## Station B1: Discovery Brief"
    match = re.match(r'^##\s+Station\s+([A-Z0-9]+):', line)
    if match:
        station_id = match.group(1)
        current_week = station_to_week.get(station_id, None)
    
    if line.startswith('# TRACK') or line.startswith('---'):
        current_week = None
        continue

    if current_week:
        week_buffers[current_week].append(line)

# Create template directory
template_dir = 'template_student'
if os.path.exists(template_dir):
    shutil.rmtree(template_dir)
os.makedirs(template_dir)

for w in range(1, 11):
    week_dir = os.path.join(template_dir, f'week{w}')
    os.makedirs(week_dir)
    with open(os.path.join(week_dir, 'problem_statement.md'), 'w') as f:
        f.write(f'# Week {w} Tasks\n\n')
        f.write(''.join(week_buffers[w]))

# Now replace the students directories
students_dir = 'students'
if os.path.exists(students_dir):
    shutil.rmtree(students_dir)
os.makedirs(students_dir)

for i in range(1, 31):
    student_path = os.path.join(students_dir, f'DE{i}')
    shutil.copytree(template_dir, student_path)

# Cleanup template
shutil.rmtree(template_dir)
print("Restructured successfully.")
