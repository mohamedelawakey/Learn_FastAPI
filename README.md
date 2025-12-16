# FastAPI Repo

Purpose: learn `FastAPI` quickly via small, runnable examples. Each file exposes its own `app`.

---

## Quick Start

#### 1) Clone & enter
```bash
git clone https://github.com/mohamedelawakey/Learn_FastAPI.git
cd <YOUR_REPO_FOLDER>
```

#### 2) (Optional) create venv
```bash
python -m venv .venv && . .venv/bin/activate
# Windows (CMD): .\.venv\Scripts\activate
# Windows (PowerShell): .\.venv\Scripts\Activate.ps1
```

#### 3) Install deps
```bash
pip install -r requirements.txt
```

---

## Run Examples

**A) `main.py`**
```bash
uvicorn main:app --reload
```

**Open:**
- App: http://127.0.0.1:8000/
- Docs: http://127.0.0.1:8000/docs
- ReDoc: http://127.0.0.1:8000/redoc

**B) `PathParameters.py`**
```bash
uvicorn PathParameters:app --reload
```

**Open:**
- App: http://127.0.0.1:8000/
- Docs: http://127.0.0.1:8000/docs

---

## What Each File Does
- [FILESTRUCTURE.md](FILESTRUCTURE.md) — File Structure To Know The Structure
- [.gitignore](.gitignore) — ignore caches/venv as needed.
- [main.py](main.py) — minimal FastAPI app with two routes: / and /about.

---
