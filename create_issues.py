import subprocess
import json
import re

owner = 'kristoadv9-netizen'
project_id = '1'

# 1. Clean up old draft items
print("Cleaning up old draft items from the project...")
try:
    with open('items.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
        for item in data.get('items', []):
            item_id = item.get('id')
            if item_id:
                print(f"Deleting item {item_id}")
                subprocess.run(["gh", "project", "item-delete", project_id, "--owner", owner, "--id", item_id], capture_output=True)
except Exception as e:
    print(f"Error cleaning items: {e}")

# 2. Read tasks from ROADMAP.md
print("Reading ROADMAP.md...")
with open('ROADMAP.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()

tasks = []
current_level = ""
for line in lines:
    if line.startswith("## Nível"):
        current_level = line.replace("##", "").strip()
    match = re.search(r'- \[[x ]\] \*\*(Task \d+:)\*\* (.*)', line)
    if match:
        task_title = f"{match.group(1)} {match.group(2)}"
        tasks.append({'level': current_level, 'title': task_title})

print(f"Found {len(tasks)} tasks.")

# 3. Create Issues and add to Project
for i, task in enumerate(tasks):
    print(f"Creating Issue {i+1}/{len(tasks)}: {task['title']}")
    
    # Generate detailed body
    body = f"""## {task['title']}

**Categoria:** {task['level']}

### 📋 Passo a Passo para Conclusão
- [ ] **1. Planejamento:** Entender os requisitos da tarefa e o que precisa ser feito.
- [ ] **2. Criação:** Criar o arquivo `.py` na pasta correspondente.
- [ ] **3. Implementação:** Escrever a lógica principal (estruturas de controle, funções, classes, etc.).
- [ ] **4. Testes:** Testar o código rodando no terminal com diferentes cenários e inputs.
- [ ] **5. Refatoração:** Limpar o código, dar nomes melhores às variáveis e adicionar comentários explicativos.
- [ ] **6. Finalização:** Marcar esta issue como fechada e atualizar o `ROADMAP.md`!

*Boa sorte nos estudos!* 🚀
"""
    
    with open('temp_body.md', 'w', encoding='utf-8') as f:
        f.write(body)
        
    cmd_issue = [
        "gh", "issue", "create",
        "--title", task['title'],
        "--body-file", "temp_body.md"
    ]
    
    result = subprocess.run(cmd_issue, capture_output=True, text=True)
    if result.returncode == 0:
        issue_url = result.stdout.strip()
        print(f"Created issue: {issue_url}")
        
        # Add issue to project
        cmd_project = [
            "gh", "project", "item-add", project_id,
            "--owner", owner,
            "--url", issue_url
        ]
        res_proj = subprocess.run(cmd_project, capture_output=True, text=True)
        if res_proj.returncode != 0:
            print(f"Failed to add to project: {res_proj.stderr}")
    else:
        print(f"Failed to create issue: {result.stderr}")
        
print("All tasks created as Issues and added to the Project!")
