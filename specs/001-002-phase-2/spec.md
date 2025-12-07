# Feature Specification: Phase II - Full-Stack Web Application + AI Features

**Feature Branch**: `001-002-phase-2`
**Created**: 2025-12-07
**Deadline**: 2025-12-12
**Points**: 150 + Bonus
**Status**: Draft
**Input**: "Full-stack web application with Next.js, FastAPI, SQLModel, Neon DB + Bonus AI features"

## User Scenarios & Testing

### User Story 1 - Basic Web Todo Management (Priority: P1)

As a user, I want to manage my tasks through a modern web interface with persistent database storage, so I can access my tasks from any browser and have them saved permanently.

**Why this priority**: Core functionality - must work before any advanced features. This is the MVP.

**Independent Test**: Can create, view, update, delete, and mark tasks complete through the web UI. Data persists after browser refresh or app restart.

**Acceptance Scenarios**:

1. **Given** I am on the web dashboard, **When** I create a new task with title "Buy groceries", **Then** it appears in my task list immediately
2. **Given** I have tasks in my list, **When** I refresh the browser, **Then** all my tasks are still visible (persisted in Neon DB)
3. **Given** I have a task, **When** I click the checkbox, **Then** the task is marked complete with visual feedback
4. **Given** I have a completed task, **When** I click edit and change the title, **Then** the task updates immediately in the database

---

### User Story 2 - Advanced Task Organization (Priority: P2)

As a user, I want to organize my tasks with priorities and tags, and quickly find tasks using search and filters, so I can manage complex task lists efficiently.

**Why this priority**: Enhances usability significantly, especially for users with many tasks. Required for Phase II completion.

**Independent Test**: Can assign priorities (high/medium/low) and tags to tasks. Can search by text, filter by status/priority/tags, and sort by different criteria.

**Acceptance Scenarios**:

1. **Given** I am creating a task, **When** I set priority to "High" and add tags "work, urgent", **Then** the task shows with a red priority badge and both tags
2. **Given** I have 20 tasks with different priorities, **When** I filter by "High priority", **Then** only high-priority tasks are displayed
3. **Given** I have tasks with various titles, **When** I type "meeting" in the search box, **Then** only tasks containing "meeting" are shown
4. **Given** I have tasks, **When** I sort by priority, **Then** tasks are ordered: High → Medium → Low

---

### User Story 3 - Multi-language Voice Commands (Priority: P3 - Bonus)

As a user, I want to add and manage tasks using voice commands in my native language (English, Urdu, Arabic, Spanish, French, or German), so I can quickly capture tasks hands-free regardless of my language preference.

**Why this priority**: Bonus feature for extra credit. Demonstrates Physical AI integration and comprehensive multi-language support with 6 languages.

**Independent Test**: Can speak commands in any of the 6 supported languages and the system understands and creates tasks. Language auto-detection works correctly.

**Acceptance Scenarios**:

1. **Given** I am on the dashboard, **When** I click the microphone icon and say "Add task call doctor" (English), **Then** a new task "call doctor" is created
2. **Given** I switch to Urdu, **When** I say "نیا کام شامل کریں خریداری" (Add task shopping), **Then** a task "shopping" is created
3. **Given** I switch to Arabic, **When** I say "أضف مهمة اجتماع" (Add task meeting), **Then** a task "meeting" is created
4. **Given** I switch to Spanish, **When** I say "Agregar tarea compras" (Add task shopping), **Then** the task is created
5. **Given** I switch to French, **When** I say "Ajouter tâche réunion" (Add task meeting), **Then** the task is created
6. **Given** I switch to German, **When** I say "Aufgabe hinzufügen Einkaufen" (Add task shopping), **Then** the task is created
7. **Given** voice recognition is active in any language, **When** I say "Complete task 5", **Then** task with ID 5 is marked complete

---

### User Story 4 - Multi-language AI Assistant with Claude Code (Priority: P3 - Bonus)

As a user, I want an AI chatbot assistant powered by Claude that can help me manage tasks conversationally in my preferred language, understand context, and provide intelligent suggestions.

**Why this priority**: Bonus feature demonstrating reusable intelligence via Claude Code Subagents and comprehensive multi-language AI support.

**Independent Test**: Can type natural language commands in any of the 6 supported languages and get intelligent responses in the same language.

**Acceptance Scenarios**:

1. **Given** I open the AI chat panel in English, **When** I type "What tasks do I have for today?", **Then** the AI lists all tasks in English and highlights high-priority ones
2. **Given** I have multiple high-priority tasks, **When** I ask "What should I focus on?" in any language, **Then** the AI suggests tasks based on priority and context in that language
3. **Given** I type "Add a task to prepare presentation" in English, **Then** the AI creates a task with title "Prepare presentation"
4. **Given** I ask in Urdu "میرے کام دکھائیں" (Show my tasks), **Then** the AI responds in Urdu with the task list
5. **Given** I ask in Arabic "ما هي المهام العاجلة؟" (What are the urgent tasks?), **Then** the AI responds in Arabic
6. **Given** I ask in Spanish "¿Cuáles son mis tareas?" (What are my tasks?), **Then** the AI responds in Spanish
7. **Given** I ask in French "Quelles sont mes tâches?" (What are my tasks?), **Then** the AI responds in French
8. **Given** I ask in German "Was sind meine Aufgaben?" (What are my tasks?), **Then** the AI responds in German

---

### Edge Cases

- What happens when no internet connection? → Show offline message, queue actions for when back online
- How does system handle very long task titles (>200 chars)? → Reject with validation error
- What if voice recognition fails or misunderstands? → Show transcription for user to confirm/edit before saving
- How to handle empty search results? → Show helpful empty state with suggestions
- What if database connection fails? → Show error message, retry logic with exponential backoff
- How does AI handle ambiguous commands? → Ask clarifying questions before acting
- What if user speaks mixed English/Urdu? → Detect language per phrase, handle gracefully

## Requirements

### Functional Requirements - Core (P1)

- **FR-001**: System MUST provide a web-based UI accessible from modern browsers (Chrome, Firefox, Safari, Edge)
- **FR-002**: System MUST persist all task data in Neon DB (PostgreSQL) with immediate consistency
- **FR-003**: System MUST provide RESTful API with endpoints for all CRUD operations
- **FR-004**: Users MUST be able to create tasks with title (required, 1-200 chars) and description (optional, max 2000 chars)
- **FR-005**: System MUST display all tasks in a responsive list view (mobile + desktop)
- **FR-006**: Users MUST be able to update task title and description
- **FR-007**: Users MUST be able to delete tasks with confirmation dialog
- **FR-008**: Users MUST be able to mark tasks complete/incomplete with visual feedback
- **FR-009**: System MUST assign unique sequential IDs to tasks
- **FR-010**: System MUST record created_at and updated_at timestamps in ISO 8601 format

### Functional Requirements - Enhanced (P2)

- **FR-011**: Users MUST be able to assign priority levels (high, medium, low) to tasks
- **FR-012**: Users MUST be able to add multiple tags to categorize tasks
- **FR-013**: System MUST provide real-time search across task titles and descriptions
- **FR-014**: System MUST allow filtering by completion status, priority, and tags
- **FR-015**: System MUST support sorting by: created_at, updated_at, priority, title
- **FR-016**: System MUST display visual priority indicators (colors/badges)
- **FR-017**: System MUST handle tag management (add, remove, autocomplete)

### Functional Requirements - Bonus Features (P3)

- **FR-018**: System MUST support voice input for task creation and commands
- **FR-019**: System MUST support voice commands in 6 languages (English, Urdu, Arabic, Spanish, French, German)
- **FR-020**: System MUST integrate Claude AI chatbot for conversational task management
- **FR-021**: AI chatbot MUST understand natural language commands in all 6 supported languages
- **FR-022**: AI chatbot MUST provide intelligent task suggestions based on context
- **FR-023**: System MUST implement Claude Code Subagents for reusable intelligence patterns
- **FR-024**: System MUST use Agent Skills for cloud-native blueprints

### Non-Functional Requirements

- **NFR-001**: API response time MUST be < 500ms for 95th percentile
- **NFR-002**: UI MUST be responsive and usable on mobile devices (320px+)
- **NFR-003**: System MUST handle at least 100 concurrent users without degradation
- **NFR-004**: System MUST validate all inputs with clear error messages
- **NFR-005**: Voice recognition accuracy MUST be > 80% for common commands
- **NFR-006**: AI responses MUST be returned within 3 seconds

### Key Entities

- **Task**: Represents a todo item with title, description, completion status, priority (high/medium/low), tags (array), created_at, updated_at timestamps
- **Priority**: Enum (high, medium, low) with visual representations (colors, badges)
- **Tag**: String label for categorization, can be reused across tasks, supports autocomplete
- **VoiceCommand**: Represents transcribed voice input with detected language and intent
- **AIConversation**: Chat history between user and Claude assistant for context

## Success Criteria

### Measurable Outcomes - Core

- **SC-001**: Users can complete all 5 CRUD operations via web UI successfully
- **SC-002**: Data persists in Neon DB and survives app restarts (100% reliability)
- **SC-003**: All API endpoints respond within 500ms under normal load
- **SC-004**: UI is fully responsive on devices from 320px to 1920px width
- **SC-005**: System handles 100+ tasks without performance degradation

### Measurable Outcomes - Enhanced

- **SC-006**: Search returns results within 200ms as user types
- **SC-007**: Filters and sorts update UI within 100ms
- **SC-008**: Users can assign priorities and tags to tasks in < 5 seconds
- **SC-009**: Tag autocomplete suggests existing tags after typing 2 characters

### Measurable Outcomes - Bonus

- **SC-010**: Voice recognition successfully transcribes commands with >80% accuracy
- **SC-011**: AI chatbot responds to task queries within 3 seconds
- **SC-012**: All 6 languages (English, Urdu, Arabic, Spanish, French, German) correctly handle task creation and queries
- **SC-013**: Language auto-detection works with >90% accuracy
- **SC-014**: RTL languages (Arabic, Urdu) display correctly in UI
- **SC-015**: Claude Code Subagents demonstrate reusable intelligence patterns (at least 2 custom skills)

## Technical Architecture

### Technology Stack

#### Backend
- **Framework**: FastAPI (Python 3.13+)
- **ORM**: SQLModel (Pydantic + SQLAlchemy)
- **Database**: Neon DB (Serverless PostgreSQL)
- **AI Integration**: Anthropic Claude API
- **Speech-to-Text**: Web Speech API (browser) + OpenAI Whisper (fallback)
- **Server**: Uvicorn (ASGI)

#### Frontend
- **Framework**: Next.js 14+ (App Router)
- **Language**: TypeScript
- **Styling**: Tailwind CSS
- **UI Components**: shadcn/ui or custom
- **State**: React hooks + SWR/TanStack Query
- **Voice**: Web Speech API
- **AI Chat**: Custom chat UI + Claude API

#### Infrastructure
- **Database**: Neon DB (cloud PostgreSQL)
- **Deployment**: Vercel (frontend) + Railway/Render (backend)
- **Environment**: Docker containers (optional)

### Data Model

```typescript
interface Task {
  id: number;                    // Auto-increment primary key
  title: string;                 // Max 200 chars, required
  description: string;           // Max 2000 chars, optional
  completed: boolean;            // Default false
  priority: 'high' | 'medium' | 'low';  // Default 'medium'
  tags: string[];                // Array of tag strings
  created_at: string;            // ISO 8601 timestamp
  updated_at: string;            // ISO 8601 timestamp
}

interface VoiceCommand {
  id: number;
  transcript: string;            // What was said
  language: 'en' | 'ur' | 'ar' | 'es' | 'fr' | 'de';  // Detected language
  intent: string;                // Parsed intent (create_task, complete_task, etc.)
  confidence: number;            // 0-1 confidence score
  created_at: string;
}

interface ChatMessage {
  id: number;
  role: 'user' | 'assistant';
  content: string;
  language: 'en' | 'ur' | 'ar' | 'es' | 'fr' | 'de';  // Message language
  created_at: string;
}
```

### API Endpoints

```
Base URL: http://localhost:8000/api/v1

# Task Management
GET    /tasks              # List all tasks with query params
GET    /tasks/{id}         # Get single task
POST   /tasks              # Create new task
PUT    /tasks/{id}         # Update task (full)
PATCH  /tasks/{id}         # Partial update
DELETE /tasks/{id}         # Delete task

# Voice Features
POST   /voice/transcribe   # Transcribe voice to text
POST   /voice/command      # Execute voice command

# AI Chatbot
POST   /chat/message       # Send message to AI
GET    /chat/history       # Get chat history
DELETE /chat/history       # Clear chat history

Query Parameters for GET /tasks:
- search: string (search in title/description)
- completed: boolean
- priority: high|medium|low
- tags: comma-separated string
- sort: created_at|updated_at|priority|title
- order: asc|desc
- limit: number (pagination)
- offset: number (pagination)
```

### Project Structure

```
physical-ai-todo/
├── backend/
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py              # FastAPI app + CORS
│   │   ├── database.py          # Neon DB connection
│   │   ├── models.py            # SQLModel models
│   │   ├── schemas.py           # Pydantic schemas
│   │   ├── crud.py              # Database operations
│   │   ├── routes/
│   │   │   ├── tasks.py         # Task CRUD endpoints
│   │   │   ├── voice.py         # Voice command endpoints
│   │   │   └── chat.py          # AI chatbot endpoints
│   │   ├── services/
│   │   │   ├── voice_service.py # Speech processing
│   │   │   └── ai_service.py    # Claude integration
│   │   └── skills/              # Claude Code Skills
│   │       ├── task_analyzer.py
│   │       └── urdu_translator.py
│   ├── requirements.txt
│   ├── .env
│   └── Dockerfile
│
├── frontend/
│   ├── app/
│   │   ├── page.tsx             # Main dashboard
│   │   ├── layout.tsx
│   │   └── globals.css
│   ├── components/
│   │   ├── TaskList.tsx
│   │   ├── TaskForm.tsx
│   │   ├── TaskItem.tsx
│   │   ├── FilterBar.tsx
│   │   ├── PriorityBadge.tsx
│   │   ├── VoiceInput.tsx       # Voice command button
│   │   ├── ChatBot.tsx          # AI chat panel
│   │   └── LanguageToggle.tsx   # English/Urdu switch
│   ├── lib/
│   │   ├── api.ts               # API client
│   │   ├── types.ts             # TypeScript types
│   │   └── voice.ts             # Voice utilities
│   ├── package.json
│   ├── tailwind.config.js
│   └── .env.local
│
├── src/todo/                     # Phase I code (reference)
├── specs/
│   └── 001-002-phase-2/
│       ├── spec.md              # This file
│       ├── plan.md              # Implementation plan
│       └── tasks.md             # Task breakdown
├── .claude/
│   └── skills/                  # Claude Code Skills
│       ├── task-analyzer.md
│       └── urdu-support.md
└── README.md
```

## Implementation Timeline (5 Days + Bonus)

### Day 1 (Dec 7): Planning & Backend Setup ✓
- [x] Create Phase II specification
- [ ] Create implementation plan
- [ ] Set up Neon DB account and database
- [ ] Initialize FastAPI project structure
- [ ] Create SQLModel models with priority and tags
- [ ] Set up database connection and test
- [ ] Implement basic CRUD endpoints

### Day 2 (Dec 8): Complete Backend API
- [ ] Add search, filter, sort logic to GET /tasks
- [ ] Implement validation for all endpoints
- [ ] Enable CORS for frontend
- [ ] Test all API endpoints with Postman
- [ ] Add error handling and logging
- [ ] Document API with OpenAPI/Swagger

### Day 3 (Dec 9): Frontend Core
- [ ] Initialize Next.js 14 project with TypeScript
- [ ] Set up Tailwind CSS and component library
- [ ] Create layout and basic routing
- [ ] Build API client functions
- [ ] Implement TaskList and TaskItem components
- [ ] Build TaskForm (create/edit) with priority and tags
- [ ] Connect to backend API and test

### Day 4 (Dec 10): Frontend Enhanced + Voice
- [ ] Implement search, filter, sort UI
- [ ] Add loading states and error handling
- [ ] Make responsive for mobile
- [ ] Polish UI with proper styling
- [ ] Implement voice input button
- [ ] Integrate Web Speech API for voice recognition
- [ ] Test voice commands (English)

### Day 5 (Dec 11): AI Features + Urdu Support
- [ ] Integrate Claude API for chatbot
- [ ] Build chat UI component
- [ ] Implement natural language command parsing
- [ ] Add Urdu language support
- [ ] Create Claude Code Skills for task analysis
- [ ] Test AI chatbot with various queries
- [ ] Add language toggle (English/Urdu)

### Day 6 (Dec 12): Final Polish & Submission
- [ ] End-to-end testing of all features
- [ ] Fix bugs and edge cases
- [ ] Update README with full setup instructions
- [ ] Create demo video showing all features
- [ ] Prepare hackathon submission
- [ ] Deploy to Vercel + Railway (optional)
- [ ] Submit before deadline ⏰

## Out of Scope

- ❌ User authentication / multi-user (save for Phase III)
- ❌ Due dates and reminders (Phase III)
- ❌ Recurring tasks (Phase III)
- ❌ Real-time collaboration
- ❌ File attachments
- ❌ Email notifications
- ❌ Mobile native apps
- ❌ Offline-first PWA
- ❌ Advanced AI features (calendar integration, smart suggestions)

## Dependencies

### Backend (`requirements.txt`)
```
fastapi==0.104.1
sqlmodel==0.0.14
uvicorn[standard]==0.24.0
python-dotenv==1.0.0
psycopg2-binary==2.9.9
anthropic==0.7.8
pydantic==2.5.0
```

### Frontend (`package.json`)
```json
{
  "dependencies": {
    "next": "14.0.4",
    "react": "^18.2.0",
    "react-dom": "^18.2.0",
    "typescript": "^5.3.3",
    "tailwindcss": "^3.4.0",
    "@anthropic-ai/sdk": "^0.9.1",
    "swr": "^2.2.4",
    "i18next": "^23.7.0",
    "react-i18next": "^13.5.0",
    "next-i18next": "^15.2.0"
  }
}
```

## Environment Variables

### Backend (`.env`)
```bash
DATABASE_URL=postgresql://user:password@neon-host/dbname
ANTHROPIC_API_KEY=sk-ant-xxxxx
CORS_ORIGINS=http://localhost:3000,https://your-domain.vercel.app
```

### Frontend (`.env.local`)
```bash
NEXT_PUBLIC_API_URL=http://localhost:8000
NEXT_PUBLIC_ANTHROPIC_API_KEY=sk-ant-xxxxx
```

## Bonus Features Overview

### 1. Reusable Intelligence via Claude Code Subagents
- Create custom Agent Skills for task analysis
- Skill 1: Task priority recommender (analyzes title/description to suggest priority)
- Skill 2: Tag suggester (analyzes content to recommend tags)
- Skill 3: Multi-language translator for seamless language switching

### 2. Cloud-Native Blueprints via Agent Skills
- Create blueprint skill for deploying to Vercel + Railway
- Automated setup skill for Neon DB + FastAPI boilerplate
- Infrastructure-as-code templates for easy replication

### 3. Multi-language Support (6 Languages)
- **Supported Languages**: English, Urdu, Arabic, Spanish, French, German
- UI text translation with RTL support (Arabic, Urdu)
- Voice commands in all 6 languages
- AI chatbot responds in user's selected language
- Language auto-detection from voice/text input
- Language switcher in UI with flag icons

### 4. Voice Commands
- Voice-to-text transcription using Web Speech API
- Intelligent command parsing and execution
- Supports actions: add, complete, delete, search, list, filter
- Works across all 6 supported languages
- Confidence scoring for transcription accuracy

## Success Metrics

- ✅ All Phase I features working in web UI
- ✅ All Phase II enhanced features (priority, tags, search, filter, sort)
- ✅ Data persists in Neon DB
- ✅ Responsive design (mobile + desktop)
- ✅ Voice commands working in 6 languages (English, Urdu, Arabic, Spanish, French, German)
- ✅ AI chatbot functional with context awareness
- ✅ At least 2 Claude Code Skills implemented
- ✅ Clean, documented codebase
- ✅ Demo video showcasing all features
- ✅ Deployed and accessible online

## Risk Mitigation

1. **Tight Timeline**: Focus on P1 features first (core CRUD), then P2 (enhancements), then bonus features (voice, AI, multi-language)
2. **Voice API Limitations**: Use Web Speech API (free, browser-based) with potential Whisper API fallback for unsupported languages
3. **Claude API Costs**: Implement caching, limit context size, add rate limiting, use smaller models for simple queries
4. **Multi-language Complexity**:
   - Phase implementation: Start with English, add one language at a time
   - Use i18next or similar library for translations
   - RTL support (Arabic, Urdu): Test early with CSS direction changes
   - Voice recognition: Web Speech API may have varying support across languages
5. **Database Issues**: Test Neon DB connection early on Day 1, have local PostgreSQL backup for development
6. **Deployment Issues**: Test deployment early on Day 4, don't wait until Day 6
7. **Translation Quality**: Use Claude API for dynamic translations, pre-translate UI strings manually for accuracy
