# 🚀 TaskFlow

TaskFlow is a **FastAPI-based web task management system** that allows users to securely register, log in, and manage personal tasks through a modern web dashboard 📋.

Each user has their own account and isolated task list 👤. After signing in, users can create ➕, edit ✏️, complete ✔️, and delete ❌ tasks while tracking their progress 📊.

---

# 📋 TASKFLOW - SYSTEM ARCHITECTURE

## 🧠 SYSTEM OVERVIEW

TaskFlow is a FastAPI web application designed for secure, user-based task management with session authentication 🔐.

**Tech Stack:**
- Python 🐍
- FastAPI ⚡
- HTML / CSS 🎨
- Session-based Authentication 🔐
- In-memory Python Dictionaries 🧠

---

## 🔄 USER FLOW

User Registration / Login → Authentication → Dashboard → Task Management (CRUD)

---

## 🧩 SYSTEM COMPONENTS

### ⚡ FASTAPI APPLICATION
Handles routing and backend logic.

**Responsibilities:**
- 🏠 Landing Page
- 🧾 User Registration
- 🔐 Login / Logout
- 📋 Dashboard
- 🧩 Task CRUD Operations

---

### 🔐 AUTHENTICATION SYSTEM
Manages users and sessions.

**Stored Data:**
- Users 👤
- Session Tokens 🔑
- Cookies 🍪

**Functions:**
- Register Account
- Login User
- Logout User
- Validate Sessions
- Verify Credentials

---

### 📌 TASK MANAGEMENT SYSTEM
Each user has a private task list stored in memory 🧠.

**Task Structure:**
- 🆔 ID
- 📝 Title
- 🏷️ Category
- ⚡ Priority
- 📂 Task Type
- 📅 Due Date
- ✔️ Completion Status

**Operations:**
- ➕ Add Task
- ✏️ Edit Task
- ✔️ Complete Task
- ❌ Delete Task
- 📊 Display Tasks

---

## 🔁 SYSTEM FLOW

### 🔐 Authentication Flow
Register → Login → Session Created → Dashboard Access

### 📋 Task Flow
Create Task → Store in User Data → Display → Update / Complete / Delete

---

## 💾 DATA STORAGE

TaskFlow uses in-memory Python dictionaries 🧠.

⚠️ Data resets when server restarts.

Stored:
- Users 👤
- Sessions 🔑
- Tasks per user 📋

---

## ⚙️ CORE FUNCTIONS

### 🔐 AUTHENTICATION
- Register User
- Login User
- Logout User
- Validate Credentials
- Create Session

### 📋 DASHBOARD
- Display Tasks
- Show Progress 📊
- Calculate Statistics

### 🧩 TASK MANAGEMENT
- Add Task ➕
- Edit Task ✏️
- Complete Task ✔️
- Delete Task ❌

---

## ✨ KEY FEATURES

✔️ User Registration  
✔️ Secure Login System 🔐  
✔️ Session Authentication 🍪  
✔️ Personal Dashboard 📋  
✔️ Add / Edit / Delete Tasks  
✔️ Mark Tasks as Complete ✔️  
✔️ Progress Tracking 📊  
✔️ Due Date Monitoring 📅  
✔️ User-based Data Isolation 👤  
✔️ Clean Web Interface 🎨  

---

## 🚀 LIVE DEMO

🌐 https://YOUR-RAILWAY-LINK-HERE

---

## 🗺️ SYSTEM DESIGN (MIRO)

📊 https://YOUR-MIRO-LINK-HERE

Includes:
- System architecture 🏗️
- Authentication flow 🔐
- Task lifecycle 🔄
- Backend routing 📡

---

## 🧾 FINAL NOTE

TaskFlow is a clean, scalable backend project demonstrating FastAPI ⚡, authentication 🔐, CRUD operations 🧩, and real-world deployment ☁️.

Built for learning, portfolio showcase, and production-style backend practice 🚀
