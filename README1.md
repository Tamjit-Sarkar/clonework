# 🚀 TaskFlow

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-green.svg)
![Status](https://img.shields.io/badge/Status-Live-success.svg)
![Deployment](https://img.shields.io/badge/Railway-Deployed-purple.svg)

TaskFlow is a modern ⚡ task management web application built with FastAPI. It includes authentication 🔐, a personal dashboard 📋, and full CRUD functionality for managing tasks. The application is deployed and accessible online 🌍.

---

## 🌐 Live Demo

👉 **[INSERT YOUR RAILWAY LINK HERE]**

---

## 🧠 Project Overview

TaskFlow demonstrates real-world backend development using FastAPI 🚀 including authentication, routing, and task management logic in a clean and scalable structure. A full visual explanation is available on the Miro board below which shows system architecture 🏗️, user authentication flow 🔐, task lifecycle (Create → Update → Complete → Delete) 🔄, backend routes 📡, and overall workflow design 🧩.

👉 **[INSERT YOUR MIRO BOARD LINK HERE]**

---

## ✨ Features

TaskFlow allows users to register and login 🔐, manage a personal task dashboard 👤, create ➕ edit ✏️ delete ❌ tasks, mark tasks as complete ✔️ or incomplete, and ensures secure user-based data isolation 🧑‍💻. It is built with FastAPI ⚡, is fully Railway-ready ☁️, and provides public live access 🌍.

---

## ⚙️ Local Setup

To run TaskFlow locally, first clone the repository using `git clone https://github.com/your-username/taskflow.git` and enter the project folder using `cd taskflow`. Then install all dependencies using `pip install -r requirements.txt`. After installation, start the server with `uvicorn main:app --reload` and open the app in your browser at `http://localhost:8000`.

---

## 🔐 Environment Variables

The application uses environment variables for configuration. Set your password or auth value using `APP_PASSWORD=your_secure_password`. This is used for authentication logic depending on your implementation.

---

## 🚀 Deployment (Railway)

To deploy using GitHub, push your project to GitHub, open Railway, create a new project, select "Deploy from GitHub Repo", allow Railway to auto-detect FastAPI, add environment variables in settings, and deploy to get your live URL 🎉.

Alternatively, you can deploy using Railway CLI by running `npm install -g @railway/cli`, then `railway login`, `railway init`, `railway up`, and finally setting variables with `railway variables set APP_PASSWORD=your_secure_password`.

---

## 🏗️ Project Structure

The project consists of `main.py` which contains the FastAPI application including routes, authentication, dashboard, and task logic. It also includes `requirements.txt` for dependencies, `Procfile` for Railway startup configuration, and `railway.toml` for deployment settings.

---

## 📡 API Routes

The application provides the following routes: `/` for landing page 🏠, `/login` for authentication 🔐, `/logout` for logging out 🚪, `/dashboard` for the task dashboard 📋, `/task/add` to create tasks ➕, `/task/complete/{id}` to toggle task completion ✔️, `/task/edit/{id}` to edit tasks ✏️, and `/task/delete/{id}` to delete tasks ❌.

---

## 📝 Notes

Tasks are stored in memory 🧠 and will reset on redeploy 🔄. Sessions may also reset depending on configuration. For production use, a database such as PostgreSQL on Railway is recommended 🗄️. This project is intended for learning, demonstration, and portfolio use 🎯.

---

## 📊 Why This Project

This project demonstrates FastAPI backend development ⚡, authentication systems 🔐, REST API design 📡, CRUD operations 🧩, cloud deployment ☁️, and real-world full-stack architecture 🏗️.

---

## ⭐ Showcase

The live application 🌍 shows full functionality, the Miro board 🗺️ explains system design visually, and the codebase 🧠 demonstrates clean backend architecture with production-ready structure 🚀.

---

## 💡 Author

Built as a backend portfolio project using FastAPI 🚀
