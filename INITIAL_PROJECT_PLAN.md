# Agentic Project Plan IO Protocol

This document outlines a portable, AI-friendly workflow for project planning that works seamlessly across AI tools (Cursor, OpenAI, Claude, etc.). It ensures every agentic workflow creates a structured project plan and reads/writes it using a consistent Python interface.

---

## ✅ JSON Schema (project\_plan.json)

```json
{
  "project_id": "abc123",
  "name": "Refactor Authentication System",
  "created_at": "2025-07-04T12:00:00Z",
  "steps": [
    {
      "id": "STEP-001",
      "description": "Extract logic to service object",
      "complete": false,
      "dependencies": [],
      "assigned_to": "AI",
      "step_type": "refactor",
      "metadata": {}
    }
  ],
  "metadata": {
    "initiator": "bjorn",
    "ai_generated": true
  }
}
```

---

## ✅ Python Module: `project_plan_io.py`

```python
import json
from pathlib import Path
from typing import Dict, Any

PLAN_PATH = Path("project_plan.json")

def save_project_plan(plan: Dict[str, Any], path: Path = PLAN_PATH):
    path.write_text(json.dumps(plan, indent=2))

def load_project_plan(path: Path = PLAN_PATH) -> Dict[str, Any]:
    return json.loads(path.read_text())

def get_status_summary(path: Path = PLAN_PATH) -> str:
    plan = load_project_plan(path)
    steps = plan.get("steps", [])
    total = len(steps)
    complete = sum(1 for step in steps if step.get("complete"))
    return f"{complete}/{total} steps complete"

def mark_step_complete(step_id: str, path: Path = PLAN_PATH):
    plan = load_project_plan(path)
    for step in plan["steps"]:
        if step["id"] == step_id:
            step["complete"] = True
    save_project_plan(plan, path)
```

---

## ✅ Usage Conventions

* After plan generation, AI should call:

  ```python
  save_project_plan(plan_dict)
  ```

* When querying plan status, call:

  ```python
  get_status_summary()
  ```

* When marking steps complete:

  ```python
  mark_step_complete("STEP-001")
  ```

---

## ✅ Goals

* ✅ Cross-AI compatibility via consistent Python I/O
* ✅ Eliminates parsing logic inside AI responses
* ✅ Supports step dependency graphs and metadata

---

## 🧠 Optional Enhancements

* Version history / changelog
* Auto-generated `step_id`
* Notifications via event bus
* Export to markdown / HTML for visual review

---

Let me know if you want to integrate this into Cursor workflows, VSCode, or a web UI!
