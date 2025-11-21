# Quick Render.com Deployment (Free)
1. Push repository to GitHub.
2. Sign up at https://render.com and connect GitHub.
3. New -> Web Service -> Connect your repo.
4. Build Command: `pip install -r requirements.txt`
5. Start Command: `uvicorn app:app --host 0.0.0.0 --port 10000`
6. Choose Free instance and deploy.
7. Use provided URL to test the API.
