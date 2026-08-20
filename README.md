# 🎓 AI Learning Content Studio

> **An AI-powered learning content workspace for creating structured course roadmaps, generating chapter content, editing learning material, and building a reusable personal content library.**

AI Learning Content Studio is a modular learning-content generation platform built with **Streamlit, Flask, LangChain, LangGraph, and multiple LLM providers**.

It provides an end-to-end workflow for turning a learning topic into a structured course:

**Topic → Roadmap → Chapters → AI-Generated Content → Editing → Storage → Review**

---

## ✨ Highlights

* 🤖 Generate structured learning roadmaps using AI
* 📚 Build beginner-to-advanced course structures
* 🧠 Generate detailed chapter content with LLMs
* 🔄 Support multiple AI providers
* ✏️ Edit generated content directly in the browser
* 📤 Upload existing roadmap JSON files
* 📄 Upload existing `.txt` chapter content
* 💾 Save roadmaps and chapters locally
* 🔍 Browse previously generated chapters
* ⬇️ Download roadmaps and learning content
* 🧩 LangGraph-based content generation workflow
* 🔌 Flask REST API backend
* 🎨 Streamlit interactive frontend
* 📁 Simple file-based local persistence
* ⚙️ Modular architecture for future database integration

---

## 🖥️ Application Workflow

```text
                    ┌──────────────────────┐
                    │       User           │
                    └──────────┬───────────┘
                               │
                               ▼
                    ┌──────────────────────┐
                    │  Streamlit Frontend  │
                    │                      │
                    │  • Login             │
                    │  • Roadmap Creator   │
                    │  • Content Creator   │
                    │  • Chapter Viewer   │
                    └──────────┬───────────┘
                               │
                         HTTP / REST
                               │
                               ▼
                    ┌──────────────────────┐
                    │    Flask Backend     │
                    └──────────┬───────────┘
                               │
             ┌─────────────────┼─────────────────┐
             │                 │                 │
             ▼                 ▼                 ▼
      Authentication      Roadmap Service   Content Service
             │                 │                 │
             │                 └────────┬────────┘
             │                          │
             │                          ▼
             │                   LLM Provider
             │              ┌──────────┼──────────┐
             │              │          │          │
             │           OpenAI     Gemini      Groq
             │
             ▼
       Local Storage
       ┌───────────────┐
       │ Roadmaps JSON │
       │ Chapters TXT  │
       └───────────────┘
```

---

# 🚀 Core Features

## 1. 🔐 Local Authentication

The application provides simple file-based authentication for local development.

Development users are stored in:

```text
backend/users.json
```

> ⚠️ This authentication system is intended for development only and should be replaced with secure authentication before production deployment.

---

## 2. 🗺️ AI Roadmap Generator

Enter a learning topic and generate a structured roadmap using an AI provider.

Example:

```text
Python Programming
```

The generated roadmap can contain:

* Course overview
* Learning objectives
* Chapter progression
* Beginner-to-advanced structure
* Practical topics
* Industry-oriented concepts
* Chapter subtopics

Example conceptual structure:

```text
Python Programming
│
├── Chapter 1: Python Fundamentals
│   ├── Variables
│   ├── Data Types
│   ├── Operators
│   └── Input / Output
│
├── Chapter 2: Control Flow
│   ├── Conditions
│   ├── Loops
│   └── Comprehensions
│
├── Chapter 3: Functions
│   ├── Function Design
│   ├── Arguments
│   └── Decorators
│
└── Chapter 4: Advanced Python
    ├── OOP
    ├── Generators
    ├── Async Programming
    └── Advanced Patterns
```

---

## 3. 🤖 Multiple AI Providers

The application supports multiple LLM providers.

| Provider      | Model                     |
| ------------- | ------------------------- |
| OpenAI        | `gpt-4o-mini`             |
| Google Gemini | `gemini-1.5-flash`        |
| Groq          | `llama-3.3-70b-versatile` |

The provider can be selected from the Streamlit interface before generating content.

This architecture also makes it easier to add additional providers later.

---

## 4. 📚 Chapter Content Generator

After creating a roadmap, select an individual chapter and generate detailed learning content.

The content generation process uses:

```text
Selected Topic
      ↓
Selected Chapter
      ↓
Chapter Subtopics
      ↓
AI Prompt
      ↓
LLM
      ↓
Generated Learning Content
      ↓
LangGraph Workflow
      ↓
Final Chapter
```

The generated content can then be edited directly from the Streamlit interface.

---

## 5. ✏️ Content Editing

Generated chapter content is not treated as final.

Users can:

* Edit generated content
* Correct explanations
* Add examples
* Modify code
* Add notes
* Improve formatting
* Save the updated version

This makes the application useful as a **learning-content authoring workspace**, not just an AI generator.

---

## 6. 📤 Upload Existing Content

The application supports importing existing learning material.

### Roadmaps

Upload:

```text
.json
```

### Chapter Content

Upload:

```text
.txt
```

This allows users to continue working with content created outside the application.

---

## 7. 💾 Local Content Library

Generated material is stored locally.

### Roadmaps

```text
backend/storage/roadmaps/
```

Example:

```text
backend/storage/roadmaps/python_programming.json
```

### Chapters

```text
backend/storage/chapters/
```

Example:

```text
backend/storage/chapters/
└── python_programming/
    ├── chapter_01.txt
    ├── chapter_02.txt
    ├── chapter_03.txt
    └── chapter_04.txt
```

Topic and chapter names are converted into filesystem-safe filenames before saving.

---

# 🏗️ Technology Stack

| Layer                  | Technology                  |
| ---------------------- | --------------------------- |
| Frontend               | Streamlit                   |
| Backend                | Flask                       |
| AI Framework           | LangChain                   |
| Workflow Orchestration | LangGraph                   |
| LLM Providers          | OpenAI, Google Gemini, Groq |
| Persistence            | JSON / TXT                  |
| Configuration          | python-dotenv               |
| Language               | Python 3.11+                |
| API Communication      | HTTP / REST                 |

---

# 📁 Project Structure

```text
AILearningContentStudio/
│
├── backend/
│   │
│   ├── app.py
│   │
│   ├── routes/
│   │   ├── auth_routes.py
│   │   ├── roadmap_routes.py
│   │   └── content_routes.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── roadmap_service.py
│   │   ├── content_service.py
│   │   └── llm_service.py
│   │
│   ├── langgraph_flow/
│   │   └── content_graph.py
│   │
│   ├── storage/
│   │   ├── roadmaps/
│   │   └── chapters/
│   │
│   ├── utils/
│   │   ├── file_utils.py
│   │   └── validators.py
│   │
│   ├── users.json
│   └── requirements.txt
│
├── frontend/
│   │
│   ├── login_fe.py
│   ├── ui_theme.py
│   │
│   ├── pages/
│   │   ├── dashboard_fe.py
│   │   ├── roadmap_page.py
│   │   ├── content_page.py
│   │   └── chapter_viewer.py
│   │
│   └── requirements.txt
│
├── .env
├── .gitignore
├── README.md
├── project_flow.txt
└── project_structure.txt
```

---

# 🔄 Content Generation Architecture

The application separates responsibilities between the frontend, API layer, services, AI layer, and storage.

```text
┌───────────────────────────────┐
│       Streamlit Frontend      │
└───────────────┬───────────────┘
                │
                │ HTTP Request
                ▼
┌───────────────────────────────┐
│         Flask REST API        │
├───────────────────────────────┤
│ Authentication Routes         │
│ Roadmap Routes                │
│ Content Routes                │
└───────────────┬───────────────┘
                │
        ┌───────┴────────┐
        ▼                ▼
┌───────────────┐ ┌───────────────┐
│ Roadmap       │ │ Content       │
│ Service       │ │ Service       │
└───────┬───────┘ └───────┬───────┘
        │                 │
        └────────┬────────┘
                 ▼
        ┌──────────────────┐
        │   LLM Service    │
        └────────┬─────────┘
                 │
       ┌─────────┼─────────┐
       ▼         ▼         ▼
    OpenAI    Gemini      Groq

                 │
                 ▼
        ┌──────────────────┐
        │    LangGraph     │
        │ Content Workflow │
        └────────┬─────────┘
                 │
                 ▼
        ┌──────────────────┐
        │  Local Storage   │
        │                  │
        │ JSON + TXT Files │
        └──────────────────┘
```

---

# ⚙️ Prerequisites

Before installing the project, make sure you have:

* Python **3.11 or later**
* Git
* Internet connection
* An API key for at least one supported AI provider
* PowerShell, Command Prompt, or another terminal

---

# 📦 Installation

## 1. Clone the Repository

```powershell
git clone <your-repository-url>

cd AILearningContentStudio
```

---

## 2. Create a Virtual Environment

```powershell
python -m venv .venv
```

Activate it:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks script execution, you can use Command Prompt:

```cmd
.venv\Scripts\activate
```

---

## 3. Install Backend Dependencies

```powershell
python -m pip install -r backend\requirements.txt
```

---

## 4. Install Frontend Dependencies

```powershell
python -m pip install -r frontend\requirements.txt
```

---

# 🔑 Environment Configuration

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
GOOGLE_API_KEY=your_google_api_key
GROQ_API_KEY=your_groq_api_key
```

You only need to configure the provider(s) you intend to use.

### 🔒 Important

Never commit real API keys to GitHub.

Add this to `.gitignore`:

```gitignore
.env
.venv/
__pycache__/
*.pyc
```

---

# ▶️ Running the Application

The application consists of two separate processes:

```text
Flask Backend
     +
Streamlit Frontend
```

Both must be running.

---

## 1. Start Flask Backend

Open Terminal 1:

```powershell
cd AILearningContentStudio

cd backend

python app.py
```

The backend will run at:

```text
http://127.0.0.1:5000
```

> Start Flask from the `backend` directory because the current authentication and storage implementation uses relative paths.

---

## 2. Start Streamlit Frontend

Open Terminal 2:

```powershell
cd AILearningContentStudio

cd frontend

streamlit run login_fe.py
```

Streamlit normally starts at:

```text
http://localhost:8501
```

Open the displayed URL in your browser.

---

# 🔐 Development Login

The current development environment includes:

| Username | Password   |
| -------- | ---------- |
| `admin`  | `admin123` |
| `niki`   | `niki123`  |

These credentials are for **local development only**.

For production, replace this implementation with:

* Password hashing
* Database-backed users
* Authentication tokens
* Session management
* Password reset
* Account management

---

# 🌐 REST API

The Flask backend exposes the following endpoints:

| Method | Endpoint            | Description                 |
| ------ | ------------------- | --------------------------- |
| `POST` | `/login`            | Authenticate a user         |
| `POST` | `/generate-roadmap` | Generate a learning roadmap |
| `POST` | `/save-roadmap`     | Save a roadmap              |
| `POST` | `/generate-chapter` | Generate chapter content    |
| `POST` | `/save-chapter`     | Save chapter content        |
| `POST` | `/load-chapter`     | Load saved chapter          |
| `POST` | `/saved-chapters`   | List saved chapters         |

---

# 🧪 API Example

Generate a roadmap for Python Programming:

```powershell
Invoke-RestMethod `
  -Uri http://127.0.0.1:5000/generate-roadmap `
  -Method Post `
  -ContentType "application/json" `
  -Body '{"topic":"Python Programming","model":"openai"}'
```

Example JSON request:

```json
{
  "topic": "Python Programming",
  "model": "openai"
}
```

---

# 🧑‍💻 Typical User Workflow

```text
1. Login
   ↓
2. Open Roadmap Creator
   ↓
3. Enter learning topic
   ↓
4. Select AI provider
   ↓
5. Generate roadmap
   ↓
6. Review roadmap
   ↓
7. Save / download roadmap
   ↓
8. Select a chapter
   ↓
9. Generate chapter content
   ↓
10. Edit content
   ↓
11. Save chapter
   ↓
12. Open Chapter Viewer
   ↓
13. Review previously created content
```

---

# 📚 Example Use Case

Suppose the user wants to create a course on:

```text
Generative AI with Python
```

The application can create a roadmap such as:

```text
Generative AI with Python
│
├── 1. Python for AI
├── 2. Introduction to Machine Learning
├── 3. Neural Networks
├── 4. Large Language Models
├── 5. Prompt Engineering
├── 6. Embeddings
├── 7. Vector Databases
├── 8. RAG Applications
├── 9. LangChain
├── 10. LangGraph
└── 11. Production AI Applications
```

The user can then generate each chapter individually instead of generating the entire course at once.

---

# 🧩 LangGraph Workflow

Chapter generation is organized using LangGraph.

Conceptually:

```text
              ┌───────────────┐
              │ Chapter Input │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Build Prompt  │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │   Generate    │
              │    Content    │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Validate /    │
              │ Finalize      │
              └───────┬───────┘
                      │
                      ▼
              ┌───────────────┐
              │ Final Chapter │
              └───────────────┘
```

This separation allows the workflow to be extended later with additional nodes such as:

* Content validation
* Fact checking
* Summarization
* Quiz generation
* Code validation
* Difficulty evaluation
* Learning objectives
* Exercises
* Assessment generation

---

# 📂 Local Storage

The current application uses a lightweight file-based persistence system.

```text
backend/storage/
│
├── roadmaps/
│   ├── python_programming.json
│   ├── generative_ai.json
│   └── data_science.json
│
└── chapters/
    │
    ├── python_programming/
    │   ├── chapter_01.txt
    │   ├── chapter_02.txt
    │   └── chapter_03.txt
    │
    └── generative_ai/
        ├── chapter_01.txt
        └── chapter_02.txt
```

This approach is intentionally simple for local development.

---

# 🛡️ Current Limitations

The current version is primarily designed for:

* Learning
* Prototyping
* Local development
* Personal content creation
* Small-scale usage

Current limitations include:

### Authentication

* JSON-based user storage
* No password hashing
* No authentication tokens
* No production session management

### Storage

* Local filesystem persistence
* No relational database
* No object storage
* Limited support for concurrent users

### API

* Flask debug mode may be enabled
* No rate limiting
* No centralized production error handling
* No production CORS configuration

### AI Output

* Roadmap generation depends on valid structured model output
* LLM responses can occasionally be malformed
* Generated content should be reviewed before publishing

---

# 🚀 Production Roadmap

The architecture is intentionally modular so the application can evolve beyond a local prototype.

## Phase 1 — Security

* [ ] Password hashing
* [ ] Secure authentication
* [ ] Session/token authentication
* [ ] User registration
* [ ] Password reset
* [ ] Role-based access

## Phase 2 — Database

* [ ] Replace JSON authentication with database users
* [ ] Store roadmaps in a database
* [ ] Store chapters in a database
* [ ] Add user-specific content
* [ ] Add content versioning

## Phase 3 — AI Improvements

* [ ] Structured output validation
* [ ] Automatic JSON repair
* [ ] Content quality evaluation
* [ ] AI-generated quizzes
* [ ] Exercises and assignments
* [ ] Learning objectives
* [ ] Chapter summaries
* [ ] Code examples
* [ ] Difficulty levels

## Phase 4 — Advanced RAG

* [ ] Document upload
* [ ] PDF ingestion
* [ ] Embeddings
* [ ] Vector database
* [ ] Retrieval-Augmented Generation
* [ ] Source citations
* [ ] Personal knowledge base

## Phase 5 — Platform Features

* [ ] Course management
* [ ] User dashboards
* [ ] Course publishing
* [ ] Progress tracking
* [ ] Learning analytics
* [ ] Search
* [ ] Favorites
* [ ] Content sharing

## Phase 6 — Production Deployment

* [ ] Docker
* [ ] Production WSGI server
* [ ] HTTPS
* [ ] Cloud deployment
* [ ] Managed database
* [ ] Secret management
* [ ] Logging
* [ ] Monitoring
* [ ] Automated tests
* [ ] CI/CD

---

# 🧪 Testing

Before making the application public, automated tests should be added for:

```text
tests/
│
├── test_auth.py
├── test_roadmap.py
├── test_content.py
├── test_storage.py
├── test_validators.py
└── test_api.py
```

Recommended testing layers:

```text
Unit Tests
    ↓
Service Tests
    ↓
API Tests
    ↓
Integration Tests
    ↓
End-to-End Tests
```

---

# 📸 Screenshots

Add application screenshots here once the UI is finalized.

Recommended screenshots:

### Login

```text
docs/images/login.png
```

### Dashboard

```text
docs/images/dashboard.png
```

### Roadmap Creator

```text
docs/images/roadmap_creator.png
```

### Chapter Content Creator

```text
docs/images/content_creator.png
```

### Chapter Viewer

```text
docs/images/chapter_viewer.png
```

Example Markdown:

```markdown
![Dashboard](docs/images/dashboard.png)
```

---

# 🔐 Security Notice

This project is currently designed as a **local development and learning project**.

Before deploying publicly:

* Never expose API keys
* Never commit `.env`
* Hash passwords
* Replace JSON authentication
* Disable Flask debug mode
* Validate all API requests
* Add authentication tokens
* Add rate limiting
* Configure CORS properly
* Add centralized error handling
* Use HTTPS
* Use secure secret management
* Add audit logging where appropriate

---

# 📌 Design Philosophy

AI Learning Content Studio follows a few core principles:

### Modular

Frontend, backend, AI services, workflows, and storage are separated.

### Provider Independent

The application can work with multiple LLM providers rather than being tightly coupled to one provider.

### Human-in-the-Loop

AI generates the initial content, while the user remains responsible for reviewing and editing it.

### Incremental Generation

Content is generated chapter by chapter rather than forcing the entire course into a single AI request.

### Extensible

The current file-based architecture can later be replaced with a database and cloud storage without completely redesigning the application.

---

# 🗺️ Future Vision

The long-term goal is to evolve AI Learning Content Studio from a simple local content generator into a complete **AI-assisted learning content development platform**.

The future platform could support:

```text
                    AI Learning Content Studio
                              │
          ┌───────────────────┼───────────────────┐
          │                   │                   │
          ▼                   ▼                   ▼
       Courses             Content             Knowledge
          │                   │                   │
          ▼                   ▼                   ▼
      Roadmaps            Chapters              RAG
      Modules             Lessons               PDFs
      Topics              Quizzes               Documents
          │                   │                   │
          └───────────────────┼───────────────────┘
                              │
                              ▼
                       Learning Platform
                              │
                ┌─────────────┼─────────────┐
                ▼             ▼             ▼
             Students      Instructors    Admins
```

---

# 🤝 Contributing

Contributions and improvements are welcome.

A typical contribution workflow:

```powershell
git checkout -b feature/new-feature

git add .

git commit -m "Add new feature"

git push origin feature/new-feature
```

Then open a Pull Request.

---

# 📄 License

No license has been selected yet.

If this project will be publicly distributed, choose an appropriate open-source license such as:

* MIT
* Apache 2.0
* GPL-3.0

Add the selected license to a `LICENSE` file in the repository.

---

# 👨‍💻 Project

**AI Learning Content Studio**

Built as a practical project combining:

**Python + Flask + Streamlit + LangChain + LangGraph + LLMs**

> **Learn → Generate → Edit → Save → Reuse**

---

## ⭐ If You Find This Project Useful

Consider giving the repository a ⭐ on GitHub and sharing improvements with the community.

**AI Learning Content Studio — turning learning ideas into structured, reusable learning content.**
