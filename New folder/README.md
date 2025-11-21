# Cloud-Native Auto-Scaling ML API (Free deploy on Render)

This repository contains a minimal, GitHub-ready project to deploy a simple ML inference API
using FastAPI. It's intended for zero-cost deployment on Render (free tier) as explained in the accompanying materials.

## Files
- `train.py` - trains a RandomForest on the Iris dataset and saves `model.joblib`
- `model.joblib` - (created after running `train.py`) the saved model artifact
- `app.py` - FastAPI app that loads `model.joblib` and exposes `/predict`
- `requirements.txt` - Python dependencies
- `Dockerfile` - optional Dockerfile for containerized deployment
- `One_Page_Proposal.pdf` - one page project proposal for submission
- `Step_By_Step_Instructions.pdf` - detailed beginner-friendly guide
- `Architecture.png` - simple architecture diagram
- `Final_Report.docx` - a short report draft
- `deploy_render.md` - quick Render deployment steps (zero-cost)

## Quick local test
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Train model and create `model.joblib`:
   ```bash
   python train.py
   ```
3. Run the app:
   ```bash
   uvicorn app:app --reload --host 0.0.0.0 --port 8000
   ```
4. Test prediction:
   ```bash
   curl -X POST "http://127.0.0.1:8000/predict" -H "Content-Type: application/json" -d '{"values":[5.1,3.5,1.4,0.2]}'
   ```
