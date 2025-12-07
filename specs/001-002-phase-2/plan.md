# Implementation Plan: Phase II - Full-Stack Web Application + Multi-language AI

**Branch**: `001-002-phase-2` | **Date**: 2025-12-07 | **Deadline**: 2025-12-12
**Spec**: [spec.md](./spec.md)

## Summary

Transform the Phase I console application into a full-stack web application with persistent PostgreSQL storage (Neon DB), modern React frontend (Next.js), RESTful API (FastAPI), and bonus features including multi-language support (6 languages), voice commands, and AI chatbot integration. This phase adds priorities, tags, search, filter, and sort capabilities while maintaining all Phase I CRUD operations.

**Key Additions:**
- Migrate from in-memory to Neon DB (PostgreSQL)
- Build Next.js frontend with TypeScript + Tailwind CSS
- Implement FastAPI REST API with SQLModel ORM
- Add priorities (high/medium/low) and tags
- Build search, filter, and sort functionality
- **BONUS**: Voice commands in 6 languages (EN, UR, AR, ES, FR, DE)
- **BONUS**: AI chatbot with Claude integration
- **BONUS**: Claude Code Skills for reusable intelligence

## Technical Context

**Language/Version**: Python 3.13+ (backend), TypeScript 5.3+ (frontend)
**Primary Dependencies**: FastAPI 0.104+, SQLModel 0.0.14, Next.js 14+, React 18+
**Storage**: Neon DB (Serverless PostgreSQL)
**Testing**: pytest (backend), Jest + React Testing Library (frontend)
**Target Platform**: Web browsers (Chrome, Firefox, Safari, Edge), Linux/Windows server
**Project Type**: Full-stack web application (backend + frontend)
**Performance Goals**: API response time <500ms (p95), Search results <200ms, UI updates <100ms
**Constraints**: Deadline Dec 12 (5 days), Must maintain Phase I compatibility, Multi-language support
**Scale/Scope**: 100+ concurrent users, 1000+ tasks, 6 languages, Voice + AI features

## Constitution Check

*GATE: Must pass before Phase 0 research. Re-check after Phase 1 design.*

### Phase II Requirements (from Constitution)

✅ **PASS** - Technology Stack Compliance:
- Backend: FastAPI 0.104+ ✓
- ORM: SQLModel ✓
- Database: Neon DB (PostgreSQL) ✓
- Frontend: Next.js 14+ ✓
- Language: TypeScript ✓

✅ **PASS** - Feature Scope Compliance:
- Implements all 5 Phase I features (Add, View, Update, Delete, Mark Complete) ✓
- Adds 5 Phase II features (Priorities, Tags, Search, Filter, Sort) ✓
- Does NOT implement Phase III features (Recurring, Due Dates, Reminders) ✓

✅ **PASS** - Architecture Evolution:
- Preserves Phase I code in `src/todo/` for reference ✓
- Creates new `backend/` and `frontend/` directories ✓
- Maintains backward compatibility with Phase I data model ✓

✅ **PASS** - Spec-Driven Development:
- Specification created via `/sp.specify` ✓
- Implementation plan via `/sp.plan` (this document) ✓
- Will generate tasks via `/sp.tasks` ✓
- Will implement via `/sp.implement` ✓

⚠️ **REVIEW** - Bonus Features (Not in Constitution Phase II):
- Multi-language support (6 languages) - BONUS ✓
- Voice commands - BONUS ✓
- AI chatbot - BONUS (designated for Phase III in constitution)
- **Justification**: Hackathon bonus requirements, does not conflict with Phase II core

### Post-Design Re-check
*To be completed after Phase 1 design artifacts*

## Project Structure

### Documentation (this feature)

```text
specs/001-002-phase-2/
├── spec.md              # Feature specification
├── plan.md              # This file (/sp.plan output)
├── research.md          # Phase 0: Technology research
├── data-model.md        # Phase 1: Database schema
├── quickstart.md        # Phase 1: Setup instructions
├── contracts/           # Phase 1: API contracts
│   ├── openapi.yaml     # OpenAPI 3.0 spec
│   └── api-examples.md  # Request/response examples
└── tasks.md             # Phase 2: Task breakdown (/sp.tasks)
```

### Source Code (repository root)

```text
physical-ai-todo/
├── backend/                    # FastAPI application
│   ├── app/
│   │   ├── __init__.py
│   │   ├── main.py            # FastAPI app + CORS + middleware
│   │   ├── database.py        # Neon DB connection + engine
│   │   ├── models.py          # SQLModel table definitions
│   │   ├── schemas.py         # Pydantic request/response schemas
│   │   ├── crud.py            # Database CRUD operations
│   │   ├── routes/
│   │   │   ├── __init__.py
│   │   │   ├── tasks.py       # Task CRUD endpoints
│   │   │   ├── voice.py       # Voice command endpoints
│   │   │   └── chat.py        # AI chatbot endpoints
│   │   ├── services/
│   │   │   ├── voice_service.py # Voice processing logic
│   │   │   ├── ai_service.py    # Claude API integration
│   │   │   └── translation.py   # Multi-language support
│   │   └── skills/            # Claude Code Skills
│   │       ├── task_analyzer.py
│   │       ├── priority_recommender.py
│   │       └── tag_suggester.py
│   ├── tests/
│   │   ├── conftest.py        # pytest fixtures
│   │   ├── test_crud.py       # Unit tests for CRUD
│   │   ├── test_api.py        # Integration tests for API
│   │   ├── test_voice.py      # Voice service tests
│   │   └── test_chat.py       # AI chatbot tests
│   ├── requirements.txt
│   ├── .env.example
│   └── Dockerfile
│
├── frontend/                   # Next.js application
│   ├── app/
│   │   ├── page.tsx           # Main dashboard
│   │   ├── layout.tsx         # Root layout
│   │   ├── globals.css        # Global Tailwind styles
│   │   └── api/               # API route handlers (if needed)
│   ├── components/
│   │   ├── ui/                # shadcn/ui components
│   │   ├── TaskList.tsx
│   │   ├── TaskItem.tsx
│   │   ├── TaskForm.tsx       # Create/edit form
│   │   ├── FilterBar.tsx      # Search/filter controls
│   │   ├── SortControls.tsx   # Sort dropdown
│   │   ├── PriorityBadge.tsx  # Priority indicator
│   │   ├── TagInput.tsx       # Tag management
│   │   ├── VoiceInput.tsx     # Voice command button
│   │   ├── ChatBot.tsx        # AI chat panel
│   │   └── LanguageSelector.tsx # Language switcher
│   ├── lib/
│   │   ├── api.ts             # API client functions
│   │   ├── types.ts           # TypeScript interfaces
│   │   ├── voice.ts           # Voice utilities
│   │   └── utils.ts           # Helper functions
│   ├── hooks/
│   │   ├── useTasks.ts        # SWR hook for tasks
│   │   ├── useVoice.ts        # Voice recognition hook
│   │   └── useChat.ts         # Chat state hook
│   ├── public/
│   │   ├── locales/           # Translation files
│   │   │   ├── en.json
│   │   │   ├── ur.json
│   │   │   ├── ar.json
│   │   │   ├── es.json
│   │   │   ├── fr.json
│   │   │   └── de.json
│   │   └── flags/             # Flag icons for languages
│   ├── tests/
│   │   ├── components/        # Component tests
│   │   └── integration/       # E2E tests
│   ├── package.json
│   ├── tsconfig.json
│   ├── tailwind.config.js
│   ├── next.config.js
│   ├── .env.local.example
│   └── Dockerfile
│
├── src/todo/                   # Phase I code (preserved)
│   └── (existing Phase I files - DO NOT MODIFY)
│
├── .claude/
│   └── skills/                # Claude Code Skills
│       ├── task-analyzer.md
│       ├── priority-recommender.md
│       ├── tag-suggester.md
│       └── deployment-blueprint.md
│
├── specs/                     # All feature specs
├── history/                   # PHRs and ADRs
├── docker-compose.yml         # Local dev environment
└── README.md                  # Updated with Phase II instructions
```

**Structure Decision**: Web application structure (Option 2) selected based on frontend + backend requirements. Backend uses FastAPI with layered architecture (routes → services → CRUD → models). Frontend uses Next.js App Router with component-based UI. Phase I code preserved in `src/todo/` for reference.

## Complexity Tracking

> **No constitution violations requiring justification**

Bonus features (voice, AI, multi-language) are additive and do not conflict with Phase II core requirements.

## Phase 0: Research & Technical Decisions

### Research Tasks

#### 1. Neon DB Setup & Connection
**Question**: How to set up Neon DB and connect from FastAPI?
**Task**: Research Neon DB provisioning, connection string format, SQLModel integration

#### 2. Multi-language Implementation
**Question**: Best approach for 6-language support in Next.js + FastAPI?
**Task**: Research i18next, next-i18next, RTL support, language detection

#### 3. Voice Recognition
**Question**: Web Speech API support across browsers and languages?
**Task**: Research browser compatibility, language support, fallback strategies

#### 4. Claude AI Integration
**Question**: How to integrate Claude API for chatbot in FastAPI?
**Task**: Research Anthropic SDK, streaming responses, rate limiting

#### 5. Deployment Strategy
**Question**: Best way to deploy Next.js + FastAPI + Neon DB?
**Task**: Research Vercel (frontend), Railway/Render (backend), environment variables

### Research Outputs (to be generated in research.md)

For each research task, document:
- **Decision**: Selected approach
- **Rationale**: Why this choice
- **Alternatives**: Other options considered
- **Implementation**: Key code patterns
- **Risks**: Potential issues

## Phase 1: Design & Contracts

### Data Model (to be generated in data-model.md)

#### Core Entities

**Task** (SQLModel table)
- Fields: id, title, description, completed, priority, tags, created_at, updated_at
- Indexes: id (PK), title, completed, priority
- Validation: title 1-200 chars, description max 2000 chars
- Relationships: None (single-user Phase II)

**VoiceCommand** (SQLModel table - optional, for logging)
- Fields: id, transcript, language, intent, confidence, created_at
- Purpose: Track voice command usage and accuracy

**ChatMessage** (SQLModel table - optional, for history)
- Fields: id, role, content, language, created_at
- Purpose: Persist chat history

### API Contracts (to be generated in contracts/openapi.yaml)

#### REST Endpoints

**Base URL**: `http://localhost:8000/api/v1`

**Tasks**
- `GET /tasks` - List all tasks (with query params)
  - Query: search, completed, priority, tags, sort, order, limit, offset
  - Response: `{ tasks: Task[], total: number }`
- `GET /tasks/{id}` - Get single task
  - Response: `Task`
- `POST /tasks` - Create task
  - Body: `{ title, description?, priority?, tags? }`
  - Response: `Task`
- `PUT /tasks/{id}` - Update task (full)
  - Body: `{ title, description, priority, tags, completed }`
  - Response: `Task`
- `PATCH /tasks/{id}` - Partial update
  - Body: `{ title?, description?, priority?, tags?, completed? }`
  - Response: `Task`
- `DELETE /tasks/{id}` - Delete task
  - Response: `{ message: string }`

**Voice**
- `POST /voice/transcribe` - Transcribe audio to text
  - Body: `{ audio: base64, language?: string }`
  - Response: `{ transcript: string, language: string, confidence: number }`
- `POST /voice/command` - Execute voice command
  - Body: `{ transcript: string, language: string }`
  - Response: `{ action: string, result: any }`

**Chat**
- `POST /chat/message` - Send message to AI
  - Body: `{ content: string, language: string }`
  - Response: `{ response: string, language: string }`
- `GET /chat/history` - Get chat history
  - Response: `{ messages: ChatMessage[] }`
- `DELETE /chat/history` - Clear history
  - Response: `{ message: string }`

### Quickstart Guide (to be generated in quickstart.md)

Sections:
1. Prerequisites (Python 3.13+, Node.js 18+, Neon DB account)
2. Environment setup (.env files)
3. Backend setup (install dependencies, run migrations, start server)
4. Frontend setup (install dependencies, configure API URL, start dev server)
5. Testing instructions
6. Deployment guide

### Agent Context Update

After generating design artifacts, run:
```bash
.specify/scripts/bash/update-agent-context.sh claude
```

This will update `CLAUDE.md` with Phase II technology stack.

## Phase 2: Implementation Tasks

*To be generated via `/sp.tasks` command*

High-level task categories:

### Day 1: Backend Setup & Database (Dec 7)
- Set up Neon DB instance
- Initialize FastAPI project structure
- Create SQLModel models with migrations
- Implement basic CRUD operations
- Test database connectivity

### Day 2: Backend API & Features (Dec 8)
- Implement all REST endpoints
- Add search, filter, sort logic
- Input validation with Pydantic
- Enable CORS for frontend
- API testing with pytest

### Day 3: Frontend Core (Dec 9)
- Initialize Next.js project with TypeScript
- Set up Tailwind CSS + shadcn/ui
- Build TaskList, TaskItem, TaskForm components
- Implement API client functions
- Connect frontend to backend

### Day 4: Frontend Enhanced + Voice (Dec 10)
- Build search, filter, sort UI
- Add loading states and error handling
- Implement responsive design
- Integrate Web Speech API
- Test voice commands

### Day 5: AI & Multi-language (Dec 11)
- Integrate Claude API for chatbot
- Build chat UI component
- Add i18next for translations
- Implement language switcher
- Create Claude Code Skills

### Day 6: Testing & Deployment (Dec 12)
- End-to-end testing
- Fix bugs and edge cases
- Update documentation
- Deploy to Vercel + Railway
- Create demo video

## Implementation Strategy

### Priority Order (P1 → P2 → P3)

**P1 (Must Have - Core Phase II)**
1. Backend API with all endpoints
2. Neon DB integration
3. Next.js frontend with CRUD
4. Priorities and tags
5. Search, filter, sort

**P2 (Should Have - Enhanced UX)**
6. Responsive design
7. Loading states and error handling
8. API documentation (Swagger)
9. Comprehensive testing

**P3 (Nice to Have - Bonus)**
10. Voice commands (6 languages)
11. AI chatbot
12. Multi-language UI
13. Claude Code Skills
14. Deployment

### Risk Mitigation

1. **Tight Timeline**: Focus P1 first, P2 second, P3 if time permits
2. **Database Issues**: Test Neon DB early, have local PostgreSQL fallback
3. **API Complexity**: Start with simple CRUD, add filters/search incrementally
4. **Voice API Limitations**: Use Web Speech API (free), accept limited browser support
5. **Multi-language**: Start with English + 1 language, add more incrementally
6. **Claude API**: Implement basic chat first, add context awareness later

### Testing Strategy

**Backend**
- Unit tests: CRUD operations, business logic
- Integration tests: API endpoints
- Test coverage: >80%

**Frontend**
- Component tests: React Testing Library
- Integration tests: User flows
- E2E tests: Playwright (optional)

**Manual Testing**
- All features in all 6 languages
- Voice commands in each language
- AI chatbot conversations
- Mobile responsive design

## Success Criteria

### Technical
- ✅ All API endpoints functional and tested
- ✅ Neon DB connected and persisting data
- ✅ Next.js frontend deployed and responsive
- ✅ Search returns results <200ms
- ✅ API responses <500ms (p95)
- ✅ Test coverage >80%

### Functional
- ✅ All 5 Phase I features working in web UI
- ✅ All 5 Phase II features (priorities, tags, search, filter, sort)
- ✅ Voice commands working in English (minimum)
- ✅ AI chatbot responds to basic queries
- ✅ At least 2 languages fully supported

### Documentation
- ✅ README updated with setup instructions
- ✅ API documented with OpenAPI/Swagger
- ✅ All specs, plans, tasks in `specs/001-002-phase-2/`
- ✅ Demo video or screenshots

## Next Steps

1. **Approve this plan**
2. **Run `/sp.tasks`** to generate detailed task breakdown
3. **Create PHR** for this planning session
4. **Begin implementation** via `/sp.implement`
5. **Daily standups** to track progress against timeline
6. **Continuous testing** as features are implemented
7. **Submit by Dec 12** before deadline

---

**Plan Status**: ✅ Ready for Phase 0 Research
**Next Command**: `/sp.tasks` (after research.md is generated)
**Estimated Effort**: 5 days (40+ hours)
**Risk Level**: Medium (tight timeline, multiple new technologies)
