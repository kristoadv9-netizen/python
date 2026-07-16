import subprocess
import re

roadmap_path = 'ROADMAP.md'
owner = 'kristoadv9-netizen'
project_id = '1'

with open(roadmap_path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

tasks = []
for line in lines:
    # Match lines like: - [ ] **Task 02:** Calculadora básica...
    match = re.search(r'- \[[x ]\] \*\*(Task \d+:)\*\* (.*)', line)
    if match:
        task_title = f"{match.group(1)} {match.group(2)}"
        tasks.append(task_title)

print(f"Found {len(tasks)} tasks.")

for i, task in enumerate(tasks):
    print(f"Adding task {i+1}/{len(tasks)}: {task}")
    cmd = [
        "gh", "project", "item-create", project_id,
        "--owner", owner,
        "--title", task
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Failed to add task: {result.stderr}")
    
print("Done adding tasks to project.")
