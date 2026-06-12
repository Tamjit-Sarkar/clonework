# 🚀 TaskFlow

> A clean, fast, SaaS-style task management system built with FastAPI ⚡  
> Designed for simplicity, scalability, and real-world backend engineering.

---

## 🌐 Live App

👉 https://clonework-production.up.railway.app/

---

## ✨ Overview

TaskFlow is a modern task management web application where users can securely create an account, log in, and manage personal tasks in an isolated workspace 👤.

It is built with a focus on:
- Clean architecture 🧠  
- Secure authentication 🔐  
- Fast performance ⚡  


---

## 🧭 User Flow

Sign Up / Login → Dashboard → Create Tasks → Manage Tasks → Track Progress

---

## ⚙️ Features

🔐 Authentication  
- Secure sign up & login  
- Session-based access control  
- Protected routes  

📋 Task Management  
- Create tasks ➕  
- Edit tasks ✏️  
- Complete tasks ✔️  
- Delete tasks ❌  

👤 User Experience  
- Personal dashboard per user  
- Isolated task storage  
- Clean and minimal UI  

---

## 🧠 System Architecture

TaskFlow is built using a simple but scalable backend design:

FastAPI ⚡ handles routing and server logic  
Session authentication 🔐 manages user access  
In-memory storage 🧠 stores users and tasks  
HTML/CSS 🎨 provides frontend rendering  

Full architecture breakdown:
👉 https://miro.com/app/live-embed/uXjVHHWsE2o=/?embedMode=view_only_without_ui&moveToViewport=-1646%2C-1809%2C5887%2C2690&embedId=741063422540

---

## 🚀 Deployment (Railway)

GitHub Deploy (Recommended):
1. Push project to GitHub  
2. Go to https://railway.app  
3. Create New Project → Deploy from GitHub Repo  
4. Select repository  
5. Railway auto-detects FastAPI ⚡  
6. Add environment variables if needed  
7. Deploy 🚀  
8. Copy live URL 🌐  

CLI Deploy:
npm install -g @railway/cli  
railway login  
railway init  
railway up  
railway variables set APP_PASSWORD=your_secure_password  

---

## 💻 Local Setup

pip install -r requirements.txt  
uvicorn main:app --reload  

Open in browser:
http://localhost:8000

---

## 🔐 Environment Variables

APP_PASSWORD=your_secure_password

---

## 🏗️ Tech Stack

Python 🐍  
FastAPI ⚡  
HTML / CSS 🎨  
Session Authentication 🔐  
In-Memory Storage 🧠  
Railway Deployment ☁️  

---

## 📊 Highlights

⚡ Fast and lightweight backend  
🔐 Secure authentication system  
👤 User-isolated task management  
📦 Easy Railway deployment  
🧠 Simple but scalable architecture  


