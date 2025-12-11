# FlowTask - Physical AI Todo Application

**Phase II: Full-Stack Web Application** 🚀

A modern, feature-rich task management application built with FastAPI, Next.js, and PostgreSQL. Features professional authentication, multi-language support (6 languages with RTL), and advanced task organization.

![Phase](https://img.shields.io/badge/Phase-II-blue)
![Status](https://img.shields.io/badge/Status-85%25%20Complete-green)
![Frontend](https://img.shields.io/badge/Frontend-Next.js%2014-black)
![Backend](https://img.shields.io/badge/Backend-FastAPI-009688)
![Database](https://img.shields.io/badge/Database-Neon%20Postgres-316192)

---

## 🌟 Features

### ✅ **Implemented (30 features - 85% complete)**

#### **Core Task Management**
- ✓ Create, read, update, delete tasks
- ✓ Mark tasks as complete/incomplete
- ✓ Priority levels (High, Medium, Low) with visual indicators
- ✓ Multi-tag support with colored badges
- ✓ Real-time search across title and description
- ✓ Advanced filtering (by status, priority, tags)
- ✓ Multi-criteria sorting (date, priority, title)

#### **Advanced Organization**
- ✓ **Subtasks** - Break down tasks with parent-child relationships
- ✓ **Task Notes** - Rich text notes attached to tasks
- ✓ **File Attachments** - Upload and manage files per task
- ✓ **Bulk Operations** - Select multiple tasks for batch actions

#### **Professional UI/UX**
- ✓ **Landing Page** - Marketing page with features showcase
- ✓ **Dark Mode** - Elegant dark/light theme toggle
- ✓ **Responsive Design** - Mobile, tablet, desktop layouts
- ✓ **Glassmorphism UI** - Modern backdrop blur effects
- ✓ **Smooth Animations** - 60fps transitions with framer-motion

#### **Authentication System**
- ✓ **Email/Password Auth** - Secure registration and login
- ✓ **Email Verification** - Token-based verification flow
- ✓ **GitHub OAuth** - Social login integration
- ✓ **JWT Sessions** - Secure httpOnly cookie-based authentication
- ✓ **Password Security** - bcrypt hashing

#### **Multi-Language Support (BONUS)**
- ✓ **6 Languages** - English, Urdu (اردو), Arabic (العربية), Spanish (Español), French (Français), German (Deutsch)
- ✓ **RTL Support** - Right-to-left layout for Arabic and Urdu
- ✓ **Dynamic Switching** - Change language without reload
- ✓ **Auto-Detection** - Browser language detection
- ✓ **Persistence** - Language preference saved in cookies

### ⏳ **Coming Soon (5 features - 15% remaining)**
- ⏳ Keyboard Shortcuts (Ctrl+N, /, Escape, j/k navigation)
- ⏳ Undo/Redo System (Ctrl+Z, Ctrl+Y)
- ⏳ Export/Import (CSV, JSON formats)
- ⏳ Task Templates (Reusable task patterns)
- ⏳ Analytics Dashboard (Task trends, productivity metrics)

---

## 🚀 Quick Start

### Prerequisites

- **Node.js** 18+ and npm
- **Python** 3.13+
- **PostgreSQL** (Neon DB account) or local Postgres

### 1. Clone Repository

```bash
git clone https://github.com/AlishbaFatima12/physical-ai-todo.git
cd physical-ai-todo
```

### 2. Backend Setup

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Configure environment variables
cp .env.example .env
# Edit .env with your database URL and API keys
```

**Required Environment Variables** (`.env`):
```env
# Database (Neon Postgres)
DATABASE_URL=postgresql+psycopg://your-connection-string

# JWT Secret (generate with: openssl rand -hex 32)
JWT_SECRET_KEY=your-secret-key-here

# Email Service (Resend API)
RESEND_API_KEY=re_your_resend_api_key

# GitHub OAuth (optional)
GITHUB_CLIENT_ID=your_github_client_id
GITHUB_CLIENT_SECRET=your_github_client_secret

# CORS
CORS_ORIGINS=http://localhost:3000
```

```bash
# Run backend server
python -m uvicorn app.main:app --reload
```

Backend will run at: **http://localhost:8000**

API Documentation: **http://localhost:8000/docs**

### 3. Frontend Setup

Open a new terminal:

```bash
cd frontend

# Install dependencies
npm install

# Run development server
npm run dev
```

Frontend will run at: **http://localhost:3000**

---

## 📖 Usage Guide

### **First Time Setup**

1. **Visit Landing Page**: http://localhost:3000
2. **Sign Up**: Click "Get Started" → Create account with email/password
3. **Verify Email**: Check console logs for verification link (if RESEND_API_KEY not configured)
4. **Or Use GitHub**: Sign up with GitHub OAuth (instant verification)

### **Using the App**

#### **Create Tasks**
1. Click **"Create New Task"** button
2. Enter title, description, priority, tags
3. Optionally add subtasks, notes, or attachments
4. Click **"Save"**

#### **Organize Tasks**
- **Search**: Type in search bar (filters title & description)
- **Filter**: Click filter dropdowns (status, priority, tags)
- **Sort**: Choose sort criteria (date, priority, title)
- **Bulk Actions**: Select multiple tasks → Delete or Complete

#### **Change Language**
- Click language dropdown (top right)
- Select from 6 languages
- UI automatically adjusts (including RTL for Arabic/Urdu)

#### **Toggle Theme**
- Click theme toggle switch (top right)
- Switch between light and dark modes

---

## 🏗️ Architecture

### **Tech Stack**

#### **Backend**
- **Framework**: FastAPI 0.100+
- **ORM**: SQLModel (Pydantic + SQLAlchemy)
- **Database**: Neon Postgres (serverless)
- **Authentication**: python-jose (JWT), passlib (bcrypt)
- **Email**: Resend API
- **Testing**: pytest

#### **Frontend**
- **Framework**: Next.js 14 (App Router)
- **Language**: TypeScript (strict mode)
- **Styling**: Tailwind CSS
- **Animations**: framer-motion
- **State**: React Query (TanStack Query)
- **i18n**: Custom React Context

### **Project Structure**

```
physical-ai-todo/
├── backend/                    # FastAPI Backend
│   ├── app/
│   │   ├── main.py            # FastAPI app with CORS
│   │   ├── models.py          # SQLModel schemas
│   │   ├── crud.py            # Database operations
│   │   ├── database.py        # DB connection
│   │   ├── auth/              # Authentication module
│   │   │   ├── routes.py      # Auth endpoints
│   │   │   ├── jwt.py         # JWT utilities
│   │   │   ├── password.py    # Password hashing
│   │   │   └── email_service.py # Email sending
│   │   └── routes/
│   │       └── tasks.py       # Task CRUD API
│   ├── tests/                 # Backend tests
│   └── requirements.txt
│
├── frontend/                   # Next.js Frontend
│   ├── app/
│   │   ├── page.tsx           # Auth redirect
│   │   ├── landing/           # Landing page
│   │   ├── auth/              # Sign up/in pages
│   │   └── dashboard/         # Main app
│   ├── components/            # React components
│   │   ├── TaskList.tsx
│   │   ├── TaskForm.tsx
│   │   ├── FilterBar.tsx
│   │   ├── ThemeToggle.tsx
│   │   ├── LanguageSwitcher.tsx
│   │   └── ...
│   ├── contexts/              # State management
│   │   ├── AuthContext.tsx
│   │   ├── ThemeContext.tsx
│   │   └── I18nContext.tsx
│   ├── lib/                   # Utilities
│   └── public/locales/        # Translation files
│       ├── en/common.json
│       ├── ur/common.json
│       ├── ar/common.json
│       ├── es/common.json
│       ├── fr/common.json
│       └── de/common.json
│
├── src/                        # Phase I (Console app)
├── specs/                      # Specifications
├── history/                    # PHRs and ADRs
├── .specify/                   # SpecKit Plus
└── README.md                   # This file
```

---

## 🗃️ Database Schema

### **User Table**
```sql
CREATE TABLE user (
    id SERIAL PRIMARY KEY,
    email VARCHAR UNIQUE NOT NULL,
    hashed_password VARCHAR NOT NULL,
    full_name VARCHAR,
    is_active BOOLEAN DEFAULT TRUE,
    is_verified BOOLEAN DEFAULT FALSE,
    verification_token VARCHAR,
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

### **Task Table**
```sql
CREATE TABLE task (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES user(id),
    title VARCHAR(200) NOT NULL,
    description TEXT,
    completed BOOLEAN DEFAULT FALSE,
    priority VARCHAR DEFAULT 'medium',
    tags TEXT DEFAULT '[]',
    parent_task_id INTEGER REFERENCES task(id),
    notes TEXT,
    attachments TEXT DEFAULT '[]',
    created_at TIMESTAMP,
    updated_at TIMESTAMP
);
```

---

## 🔐 Authentication Flow

### **Email/Password Registration**
1. User submits email, password, full name
2. Backend creates user with `is_verified=False`
3. Verification token generated
4. Email sent with verification link
5. User clicks link → `is_verified=True`
6. User can now log in

### **GitHub OAuth**
1. User clicks "Continue with GitHub"
2. Redirected to GitHub authorization
3. User approves
4. GitHub redirects back with code
5. Backend exchanges code for access token
6. Fetches user email from GitHub
7. Creates/logs in user (auto-verified)
8. JWT token set in httpOnly cookie

---

## 🌍 Multi-Language Implementation

### **Supported Languages**
1. **English** (en) - Default
2. **Urdu** (ur) - RTL ✓
3. **Arabic** (ar) - RTL ✓
4. **Spanish** (es)
5. **French** (fr)
6. **German** (de)

### **Translation Keys**
All UI strings use translation keys:
```typescript
t('app.title')           // "FlowTask"
t('actions.add')         // "Add Task"
t('task.completed')      // "Completed"
```

Translation files: `frontend/public/locales/{lang}/common.json`

---

## 🧪 Testing

### **Backend Tests**
```bash
cd backend
pytest
pytest --cov=app --cov-report=html
```

### **Frontend Tests**
```bash
cd frontend
npm test
npm run test:e2e
```

---

## 📊 API Endpoints

Base URL: `http://localhost:8000`

### **Authentication**
- `POST /api/v1/auth/register` - Register new user
- `POST /api/v1/auth/login` - Login with email/password
- `POST /api/v1/auth/logout` - Logout (clear cookie)
- `GET /api/v1/auth/me` - Get current user
- `POST /api/v1/auth/verify-email` - Verify email with token
- `GET /api/v1/auth/github/authorize` - GitHub OAuth start
- `POST /api/v1/auth/github/callback` - GitHub OAuth callback

### **Tasks**
- `GET /api/v1/tasks` - List tasks (with filters)
- `POST /api/v1/tasks` - Create task
- `GET /api/v1/tasks/{id}` - Get task by ID
- `PUT /api/v1/tasks/{id}` - Update task
- `DELETE /api/v1/tasks/{id}` - Delete task

**API Documentation**: http://localhost:8000/docs

---

## 🎨 Theme System

### **Dark Mode (Default)**
- Deep gradient backgrounds
- High contrast for readability
- Glassmorphism effects

### **Light Mode**
- Clean white backgrounds
- Soft shadows
- Professional aesthetic

Toggle between modes with the switch in the top right corner.

---

## 🚧 Development Roadmap

### **Phase I** ✅ Complete
- Console-based Python app
- In-memory storage
- 5 basic CRUD operations

### **Phase II** 🔄 85% Complete (Current)
- Full-stack web application
- Database persistence
- Authentication system
- Multi-language support
- Advanced features (subtasks, notes, attachments)

### **Phase III** ⏳ Planned
- AI-powered chatbot
- Natural language task creation
- Voice commands
- Recurring tasks
- Due dates & reminders

### **Phase IV** ⏳ Planned
- Kubernetes deployment
- Docker containerization
- Helm charts

### **Phase V** ⏳ Planned
- Cloud deployment (DigitalOcean)
- Event-driven architecture (Kafka)
- Microservices with Dapr

---

## 👥 Contributing

This is a portfolio project following **Spec-Driven Development** principles with Claude Code.

**Constitution**: See `.specify/memory/constitution.md` for development principles.

---

## 📝 License

MIT License - Feel free to use for learning purposes.

---

## 👨‍💻 Author

**Syeda Alishba Fatima**

Built with ❤️ using FastAPI, Next.js, and Claude Code

---

## 🆘 Troubleshooting

### **Frontend not loading**
- Hard refresh: `Ctrl + Shift + R`
- Visit directly: http://localhost:3000/landing
- Clear browser cache

### **Backend errors**
- Check `.env` configuration
- Verify database connection
- Check port 8000 is available

### **Email verification not working**
- Check console logs for verification link (if RESEND_API_KEY not set)
- Use GitHub OAuth for instant verification

### **Database connection issues**
- Verify Neon Postgres connection string
- Check network connectivity
- Ensure database exists

---

## 📞 Support

For issues or questions:
- GitHub Issues: [Create an issue](https://github.com/AlishbaFatima12/physical-ai-todo/issues)
- Email: your-email@example.com

---

**Last Updated**: December 9, 2025
**Version**: Phase II (v1.1.0 - 85% Complete)
