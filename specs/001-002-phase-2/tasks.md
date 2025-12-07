# Implementation Tasks - Phase II

**Feature**: Phase II - Full-Stack Web Application + Multi-language AI
**Branch**: `001-002-phase-2`
**Generated**: 2025-12-07
**Deadline**: 2025-12-12 (5 days)

---

## Overview

This document contains **actionable implementation tasks** organized by user story priority. Each task follows the format:
```
- [ ] [TaskID] [P?] [Story?] Description with file path
```

- **[P]** = Parallelizable (can be done concurrently with other [P] tasks)
- **[Story]** = User story label (US1, US2, US3, US4)

**Total Tasks**: 85
**MVP Scope**: Phase 3 only (User Story 1 - 22 tasks)
**Parallel Opportunities**: 45 tasks marked [P]

---

## Task Summary by Phase

| Phase | Story | Tasks | Parallel | Description |
|-------|-------|-------|----------|-------------|
| 1 | Setup | 8 | 4 | Project initialization, dependencies |
| 2 | Foundation | 12 | 6 | Database, core models, shared services |
| 3 | US1 (P1) | 22 | 12 | Basic web todo CRUD (MVP) |
| 4 | US2 (P2) | 15 | 8 | Priorities, tags, search, filter, sort |
| 5 | US3 (P3) | 12 | 6 | Multi-language voice commands |
| 6 | US4 (P3) | 10 | 5 | AI chatbot with Claude |
| 7 | Polish | 6 | 4 | Testing, deployment, documentation |

---

## Phase 1: Setup & Project Initialization

**Goal**: Initialize project structure, install dependencies, configure environment

**Estimated Time**: 2-3 hours

### Tasks

- [ ] T001 Create backend project directory structure per plan.md at backend/
- [ ] T002 Create frontend project directory structure per plan.md at frontend/
- [ ] T003 [P] Create backend/requirements.txt with FastAPI, SQLModel, uvicorn, python-dotenv, psycopg2-binary, asyncpg, anthropic, pydantic, pytest
- [ ] T004 [P] Create frontend/package.json with next@14.0.4, react, typescript, tailwindcss, swr, i18next, react-i18next, next-i18next
- [ ] T005 [P] Create backend/.env.example with DATABASE_URL, ANTHROPIC_API_KEY, CORS_ORIGINS placeholders
- [ ] T006 [P] Create frontend/.env.local.example with NEXT_PUBLIC_API_URL, NEXT_PUBLIC_ANTHROPIC_API_KEY placeholders
- [ ] T007 Install backend dependencies by running: cd backend && python -m venv venv && source venv/bin/activate && pip install -r requirements.txt
- [ ] T008 Install frontend dependencies by running: cd frontend && npm install

**Validation**: ✅ Both backend/frontend directories exist with dependencies installed

---

## Phase 2: Foundational Infrastructure

**Goal**: Set up database, core models, shared utilities (blocking prerequisites for all user stories)

**Estimated Time**: 4-5 hours

### Tasks

- [ ] T009 Create Neon DB project and database at https://neon.tech, save connection string
- [ ] T010 Configure backend/.env with actual Neon DB connection string in postgresql+asyncpg:// format
- [ ] T011 Create backend/app/__init__.py with package initialization
- [ ] T012 Create backend/app/database.py with async SQLModel engine, session factory, init_db function per research.md
- [ ] T013 [P] Create backend/app/models.py with Task SQLModel class (id, title, description, completed, priority, tags, created_at, updated_at) per data-model.md
- [ ] T014 [P] Create backend/app/schemas.py with TaskCreate, TaskUpdate, TaskPatch, TaskRead, TaskListResponse Pydantic schemas per data-model.md
- [ ] T015 [P] Create frontend/lib/types.ts with Task, TaskCreate, TaskUpdate TypeScript interfaces matching backend schemas
- [ ] T016 [P] Create frontend/next-i18next.config.js with locales: en, ur, ar, es, fr, de per research.md
- [ ] T017 [P] Create frontend/public/locales/en/common.json with English translations (app.title, actions.add, priority.high/medium/low)
- [ ] T018 [P] Create frontend/tailwind.config.js with RTL support directives per research.md
- [ ] T019 Initialize database tables by running: python -c "from app.database import init_db; import asyncio; asyncio.run(init_db())"
- [ ] T020 Verify database connection and tables created in Neon DB console

**Validation**: ✅ Database connected, Task table exists, schemas defined

---

## Phase 3: User Story 1 - Basic Web Todo Management (P1 - MVP)

**Story**: As a user, I want to manage my tasks through a modern web interface with persistent database storage.

**Independent Test**: Can create, view, update, delete, and mark tasks complete through the web UI. Data persists after browser refresh.

**Estimated Time**: 8-10 hours

### Backend API Tasks

- [ ] T021 [US1] Create backend/app/crud.py with async create_task(task_data, session) function using SQLModel
- [ ] T022 [US1] Add async list_tasks(session, limit, offset) function to crud.py returning tuple[list[Task], int]
- [ ] T023 [US1] Add async get_task(task_id, session) function to crud.py
- [ ] T024 [US1] Add async update_task(task_id, task_data, session) function to crud.py
- [ ] T025 [US1] Add async delete_task(task_id, session) function to crud.py
- [ ] T026 [US1] Add async toggle_complete(task_id, session) function to crud.py
- [ ] T027 [US1] Create backend/app/routes/__init__.py
- [ ] T028 [US1] Create backend/app/routes/tasks.py with FastAPI router and GET /api/v1/tasks endpoint using crud.list_tasks
- [ ] T029 [US1] Add POST /api/v1/tasks endpoint to routes/tasks.py with TaskCreate schema validation
- [ ] T030 [US1] Add GET /api/v1/tasks/{id} endpoint to routes/tasks.py
- [ ] T031 [US1] Add PUT /api/v1/tasks/{id} endpoint to routes/tasks.py with TaskUpdate schema
- [ ] T032 [US1] Add PATCH /api/v1/tasks/{id} endpoint to routes/tasks.py with TaskPatch schema
- [ ] T033 [US1] Add DELETE /api/v1/tasks/{id} endpoint to routes/tasks.py
- [ ] T034 [US1] Create backend/app/main.py with FastAPI app, CORS middleware (origins from .env), routes registration, health endpoint

### Frontend UI Tasks

- [ ] T035 [P] [US1] Create frontend/app/layout.tsx with RootLayout, html lang/dir attributes, global CSS import
- [ ] T036 [P] [US1] Create frontend/app/globals.css with Tailwind directives (@tailwind base/components/utilities)
- [ ] T037 [P] [US1] Create frontend/lib/api.ts with fetchTasks(), createTask(), updateTask(), deleteTask(), toggleComplete() functions using fetch API
- [ ] T038 [P] [US1] Create frontend/hooks/useTasks.ts with SWR hook for fetching and mutating tasks
- [ ] T039 [P] [US1] Create frontend/components/TaskItem.tsx with task display, checkbox, edit/delete buttons
- [ ] T040 [P] [US1] Create frontend/components/TaskList.tsx rendering TaskItem[] with empty state message
- [ ] T041 [P] [US1] Create frontend/components/TaskForm.tsx with title input, description textarea, save/cancel buttons, form validation
- [ ] T042 [US1] Create frontend/app/page.tsx integrating TaskList, TaskForm, useTasks hook, add task button

**Validation**: ✅ All CRUD operations work via web UI, data persists in Neon DB, browser refresh retains tasks

---

## Phase 4: User Story 2 - Advanced Task Organization (P2)

**Story**: As a user, I want to organize my tasks with priorities and tags, and quickly find tasks using search and filters.

**Independent Test**: Can assign priorities/tags, search tasks, filter by status/priority/tags, sort by criteria.

**Estimated Time**: 6-8 hours

### Backend Enhancements

- [ ] T043 [US2] Update crud.list_tasks() to accept search, completed, priority, tags, sort, order parameters
- [ ] T044 [US2] Implement search logic in crud.list_tasks() using SQL LIKE on title/description fields
- [ ] T045 [US2] Implement filter logic in crud.list_tasks() for completed (bool), priority (enum), tags (JSON contains)
- [ ] T046 [US2] Implement sort logic in crud.list_tasks() with ORDER BY created_at/updated_at/priority/title
- [ ] T047 [US2] Update GET /api/v1/tasks endpoint to accept query parameters: search, completed, priority, tags, sort, order per openapi.yaml

### Frontend Enhancements

- [ ] T048 [P] [US2] Create frontend/components/PriorityBadge.tsx with color coding (red=high, yellow=medium, blue=low)
- [ ] T049 [P] [US2] Create frontend/components/TagInput.tsx with tag addition/removal, autocomplete from existing tags
- [ ] T050 [P] [US2] Create frontend/components/FilterBar.tsx with search input, priority dropdown, tag filter, completed checkbox
- [ ] T051 [P] [US2] Create frontend/components/SortControls.tsx with dropdown for sort field and order (asc/desc)
- [ ] T052 [US2] Update TaskForm.tsx to include priority select dropdown and TagInput component
- [ ] T053 [US2] Update TaskItem.tsx to display PriorityBadge and tags
- [ ] T054 [US2] Update page.tsx to integrate FilterBar and SortControls, pass filters to useTasks hook
- [ ] T055 [US2] Update lib/api.ts fetchTasks() to accept and pass query parameters for search/filter/sort
- [ ] T056 [US2] Update hooks/useTasks.ts to accept filter/sort params and construct query string
- [ ] T057 [US2] Add responsive styling to all components using Tailwind for mobile (320px+) and desktop

**Validation**: ✅ Can set priorities/tags, search returns correct results <200ms, filters work, sorting orders correctly

---

## Phase 5: User Story 3 - Multi-language Voice Commands (P3 - Bonus)

**Story**: As a user, I want to add and manage tasks using voice commands in my native language (6 languages).

**Independent Test**: Can speak commands in EN/UR/AR/ES/FR/DE, tasks created correctly, language auto-detection works.

**Estimated Time**: 5-6 hours

### Backend Voice Integration

- [ ] T058 [P] [US3] Create backend/app/models.py VoiceCommand SQLModel class (id, transcript, language, intent, confidence, created_at) per data-model.md
- [ ] T059 [P] [US3] Create backend/app/services/voice_service.py with parse_voice_command(transcript, language) function returning intent and parameters
- [ ] T060 [US3] Create backend/app/routes/voice.py with POST /api/v1/voice/command endpoint accepting transcript and language, calling voice_service
- [ ] T061 [US3] Implement command parsing in voice_service.py for intents: create_task, complete_task, delete_task, list_tasks
- [ ] T062 [US3] Update main.py to register voice router

### Frontend Voice UI

- [ ] T063 [P] [US3] Create frontend/hooks/useVoice.ts with Web Speech API integration per research.md, supporting language codes: en-US, ur-PK, ar-SA, es-ES, fr-FR, de-DE
- [ ] T064 [P] [US3] Create frontend/components/VoiceInput.tsx with microphone button, recording animation, transcript display
- [ ] T065 [P] [US3] Create frontend/components/LanguageSelector.tsx with dropdown for 6 languages, flag icons
- [ ] T066 [US3] Update page.tsx to integrate VoiceInput and LanguageSelector components
- [ ] T067 [US3] Implement voice command execution in page.tsx: call /api/v1/voice/command on transcript, refresh task list
- [ ] T068 [US3] Add browser compatibility check in useVoice.ts, show "unsupported browser" message for Firefox
- [ ] T069 [US3] Create translation files: frontend/public/locales/{ur,ar,es,fr,de}/common.json with UI text per language

**Validation**: ✅ Voice commands work in Chrome/Edge for all 6 languages, tasks created correctly, transcription shown for confirmation

---

## Phase 6: User Story 4 - Multi-language AI Assistant (P3 - Bonus)

**Story**: As a user, I want an AI chatbot assistant that helps me manage tasks conversationally in my preferred language.

**Independent Test**: Can type natural language queries in 6 languages, receive intelligent responses in same language.

**Estimated Time**: 4-5 hours

### Backend AI Integration

- [ ] T070 [P] [US4] Create backend/app/models.py ChatMessage SQLModel class (id, role, content, language, created_at) per data-model.md
- [ ] T071 [P] [US4] Create backend/app/services/ai_service.py with async chat_with_claude(message, language, context) streaming generator per research.md
- [ ] T072 [P] [US4] Implement get_system_prompt(language) in ai_service.py returning multi-language prompts for EN/UR/AR/ES/FR/DE
- [ ] T073 [US4] Create backend/app/routes/chat.py with POST /api/v1/chat/message endpoint returning StreamingResponse
- [ ] T074 [US4] Add GET /api/v1/chat/history and DELETE /api/v1/chat/history endpoints to chat.py
- [ ] T075 [US4] Update main.py to register chat router

### Frontend Chat UI

- [ ] T076 [P] [US4] Create frontend/components/ChatBot.tsx with message list, input box, send button, streaming response handling
- [ ] T077 [P] [US4] Create frontend/hooks/useChat.ts with SWR for chat history, sendMessage function with streaming
- [ ] T078 [US4] Implement Server-Sent Events (SSE) parsing in ChatBot.tsx for streaming AI responses per research.md
- [ ] T079 [US4] Update page.tsx to add ChatBot component in collapsible panel or modal

**Validation**: ✅ Can chat in all 6 languages, AI responds within 3 seconds, streaming works, responses contextually relevant

---

## Phase 7: Polish, Testing & Deployment

**Goal**: Final testing, documentation, deployment

**Estimated Time**: 3-4 hours

### Testing

- [ ] T080 [P] Create backend/tests/test_crud.py with pytest cases for all CRUD functions (create, read, update, delete, list with filters)
- [ ] T081 [P] Create backend/tests/test_api.py with httpx async tests for all API endpoints, including error cases (404, 422)
- [ ] T082 [P] Run pytest in backend/ directory, ensure >80% coverage, fix failing tests

### Deployment

- [ ] T083 [P] Create Dockerfile in backend/ with Python 3.13, uvicorn CMD per quickstart.md
- [ ] T084 Update README.md with Phase II setup instructions, link to quickstart.md, demo screenshots
- [ ] T085 Deploy backend to Railway and frontend to Vercel per research.md deployment strategy

**Validation**: ✅ All tests pass, backend deployed, frontend deployed, demo accessible, README updated

---

## Dependencies & Execution Order

### User Story Dependencies

```
Phase 1 (Setup) → Phase 2 (Foundation) → Independent Stories ↓

Phase 3 (US1 - P1) ─┐
                     ├→ Phase 4 (US2 - P2)
                     ├→ Phase 5 (US3 - P3) [Parallel]
                     └→ Phase 6 (US4 - P3) [Parallel]
                               ↓
                        Phase 7 (Polish)
```

**Blocking Dependencies**:
- Phase 3 (US1) MUST complete before Phase 4 (US2) - search/filter depend on core CRUD
- Phase 5 (US3) and Phase 6 (US4) can run in parallel after Phase 3

**Independent Phases**:
- US1, US2, US3, US4 are each independently testable
- US3 (voice) and US4 (AI) do NOT depend on US2 (search/filter)

### Parallel Execution Examples

**Within Phase 3 (US1)**:
```
Parallel Group 1:
- T035 [P] [US1] layout.tsx
- T036 [P] [US1] globals.css
- T037 [P] [US1] api.ts
- T038 [P] [US1] useTasks.ts

Sequential: T021-T034 (backend CRUD + routes)

Parallel Group 2:
- T039 [P] [US1] TaskItem.tsx
- T040 [P] [US1] TaskList.tsx
- T041 [P] [US1] TaskForm.tsx

Sequential: T042 [US1] page.tsx (integrates all)
```

**Between Phases 5 & 6 (Bonus Features)**:
```
Phase 5 (Voice) Tasks and Phase 6 (AI) Tasks can run in parallel:
- One developer on T058-T069 (voice)
- Another developer on T070-T079 (AI)
```

---

## Implementation Strategy

### MVP First (Phase 3 Only)

**Scope**: User Story 1 - Basic Web Todo Management
**Tasks**: T001-T042 (42 tasks total)
**Outcome**: Fully functional web todo app with persistent storage
**Demo**: Create, read, update, delete, mark complete via browser

### Incremental Delivery

1. **Milestone 1** (Day 1-2): Setup + Foundation + US1 Backend
   - Tasks: T001-T034
   - Deliverable: Working API with all CRUD endpoints

2. **Milestone 2** (Day 3): US1 Frontend
   - Tasks: T035-T042
   - Deliverable: Web UI connected to API, MVP complete

3. **Milestone 3** (Day 4): US2 Advanced Features
   - Tasks: T043-T057
   - Deliverable: Search, filter, sort, priorities, tags

4. **Milestone 4** (Day 5): Bonus Features
   - Tasks: T058-T079
   - Deliverable: Voice commands + AI chatbot

5. **Milestone 5** (Day 6): Polish & Deploy
   - Tasks: T080-T085
   - Deliverable: Tests pass, deployed, documented

---

## Testing Approach

### No TDD Required

Tests are included in Phase 7 for final validation, but NOT required before implementation. Focus on:
1. Manual testing during development
2. Browser console verification
3. API testing with Swagger UI (http://localhost:8000/docs)
4. Final pytest suite before submission

### Manual Test Checklist (per User Story)

**US1 (P1)**:
- [ ] Create task via web UI → appears in list
- [ ] Refresh browser → task still visible
- [ ] Mark task complete → checkbox updates
- [ ] Edit task → changes persist
- [ ] Delete task → removed from list

**US2 (P2)**:
- [ ] Set task priority to High → red badge appears
- [ ] Add tags "work, urgent" → tags display
- [ ] Search "meeting" → only matching tasks shown
- [ ] Filter by High priority → only high-priority tasks
- [ ] Sort by created_at desc → newest first

**US3 (P3)**:
- [ ] Click microphone → permission requested
- [ ] Say "Add task buy milk" → task created
- [ ] Switch to Spanish, say "Agregar tarea compras" → works
- [ ] Test all 6 languages → transcription accurate >80%

**US4 (P3)**:
- [ ] Open chat → panel appears
- [ ] Type "What tasks do I have?" → AI lists tasks
- [ ] Ask in Urdu → AI responds in Urdu
- [ ] Test all 6 languages → responses in correct language

---

## File Checklist

Ensure these files are created per plan.md:

### Backend
- [x] backend/requirements.txt
- [x] backend/.env
- [ ] backend/app/__init__.py
- [ ] backend/app/main.py
- [ ] backend/app/database.py
- [ ] backend/app/models.py
- [ ] backend/app/schemas.py
- [ ] backend/app/crud.py
- [ ] backend/app/routes/__init__.py
- [ ] backend/app/routes/tasks.py
- [ ] backend/app/routes/voice.py
- [ ] backend/app/routes/chat.py
- [ ] backend/app/services/voice_service.py
- [ ] backend/app/services/ai_service.py
- [ ] backend/tests/test_crud.py
- [ ] backend/tests/test_api.py
- [ ] backend/Dockerfile

### Frontend
- [x] frontend/package.json
- [x] frontend/.env.local
- [ ] frontend/app/layout.tsx
- [ ] frontend/app/page.tsx
- [ ] frontend/app/globals.css
- [ ] frontend/lib/api.ts
- [ ] frontend/lib/types.ts
- [ ] frontend/hooks/useTasks.ts
- [ ] frontend/hooks/useVoice.ts
- [ ] frontend/hooks/useChat.ts
- [ ] frontend/components/TaskList.tsx
- [ ] frontend/components/TaskItem.tsx
- [ ] frontend/components/TaskForm.tsx
- [ ] frontend/components/PriorityBadge.tsx
- [ ] frontend/components/TagInput.tsx
- [ ] frontend/components/FilterBar.tsx
- [ ] frontend/components/SortControls.tsx
- [ ] frontend/components/VoiceInput.tsx
- [ ] frontend/components/LanguageSelector.tsx
- [ ] frontend/components/ChatBot.tsx
- [ ] frontend/public/locales/en/common.json
- [ ] frontend/public/locales/{ur,ar,es,fr,de}/common.json
- [ ] frontend/next-i18next.config.js
- [ ] frontend/tailwind.config.js

---

## Success Metrics

- [ ] All 4 user stories implemented and independently testable
- [ ] MVP (US1) delivers value as standalone feature
- [ ] US2-US4 can be demonstrated independently
- [ ] Search returns results <200ms
- [ ] API responses <500ms (p95)
- [ ] Voice recognition >80% accuracy
- [ ] AI chatbot responds <3 seconds
- [ ] All 6 languages functional
- [ ] Mobile responsive (320px+)
- [ ] Deployed and accessible online

---

## Next Steps

1. **Review this task breakdown** - Ensure understanding of all tasks
2. **Start with MVP scope** - Focus on Phase 1-3 first (T001-T042)
3. **Run `/sp.implement`** - Begin implementation with tasks file
4. **Daily progress tracking** - Mark tasks complete as you go
5. **Incremental testing** - Validate each user story independently
6. **Deploy early** - Test deployment on Day 4, not Day 6

---

**Tasks File Status**: ✅ Complete
**Total Tasks**: 85
**Estimated Total Time**: 35-40 hours (5 days @ 8 hours/day)
**MVP Scope**: 42 tasks (Phases 1-3)
**Ready for Implementation**: Yes - Run `/sp.implement` to begin
