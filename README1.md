# 🚀 TaskFlow

TaskFlow is a FastAPI-based task management web application with user authentication 🔐 and full CRUD functionality 📋.

---

## 🌐 Live App
👉 https://YOUR-RAILWAY-LINK-HERE

---

## 🚀 Deployment (Railway)

GitHub Deploy (Recommended):
1. Push project to GitHub
2. Go to https://railway.app
3. Click New Project → Deploy from GitHub Repo
4. Select repository
5. Railway auto-detects FastAPI ⚡
6. Add environment variables (if needed)
7. Deploy 🚀
8. Copy your live URL 🌐

Railway CLI Deploy:
npm install -g @railway/cli
railway login
railway init
railway up
railway variables set APP_PASSWORD=your_secure_password

---

## 💻 Run Locally

pip install -r requirements.txt
uvicorn main:app --reload

Open in browser:
http://localhost:8000

---

## ⚙️ Environment Variables

APP_PASSWORD=your_secure_password

---

## 🧠 Project Overview

TaskFlow lets users:
🔐 Register & login  
👤 Access personal dashboard  
➕ Create tasks  
✏️ Edit tasks  
✔️ Complete tasks  
❌ Delete tasks  

Full system design (Miro):
👉 https://YOUR-MIRO-LINK-HERE

---

## ✨ Features

🔐 Authentication system  
👤 User-specific dashboards  
➕ Create tasks  
✏️ Edit tasks  
✔️ Complete tasks  
❌ Delete tasks  
📊 Progress tracking  

---

## 🛠️ Tech Stack

Python 🐍  
FastAPI ⚡  
HTML / CSS 🎨  
Session authentication 🔐  
In-memory storage 🧠  

---

## 📝 Notes

⚠️ Data resets on restart  
🔄 Sessions may reset depending on setup  
🚀 Built for learning + portfolio showcase  
