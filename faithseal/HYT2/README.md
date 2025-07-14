# Project HYT2: A Faith-Aware AI Development Platform

## 1. Vision & Mission

**Core Mission:** To architect and build a modular, AI-driven platform that embodies the principles of "Sacred Futurism." This project will serve as a foundational framework for creating faith-aligned digital tools, content platforms, and developer utilities. Our work must adhere to the **Imago Dei Honor Code** and the **Tinned Fruit Test**, ensuring every component is built righteously, written responsibly, and architected with awe.

**Guiding Metaphor (C.S. Lewis):** We are not creating a new sun, but a lamp. The lamp does not generate its own light but is a vessel for the electricity that powers it. Similarly, our AI is a tool—a vessel—for channeling and shaping content in a way that illuminates truth, but it is not the source of truth itself.

## 2. High-Level Architecture

We will build a modular, API-first system using a Python backend (FastAPI) hosted on a serverless platform (like Google Cloud Functions or Vercel) and integrated with Firebase for data persistence and user management. The system will be designed with two primary modes of operation:

1.  **Strategic Developer Partner Mode:** Provide API endpoints and services that assist developers in building clean, ethical applications.
2.  **Faith-Tech Ethics Sentinel Mode:** Provide tools for auditing, analyzing, and flagging content against our core faith-based principles.

## 3. File Structure

```
faithseal/HYT2/
├── .github/
│   └── workflows/
│       └── python-app.yml      # Basic CI/CD workflow for tests
├── api/
│   ├── src/
│   │   ├── __init__.py
│   │   ├── main.py             # FastAPI app instantiation and middleware
│   │   ├── core/
│   │   │   ├── __init__.py
│   │   │   └── config.py       # Pydantic settings for env vars (API keys, etc.)
│   │   ├── models/
│   │   │   ├── __init__.py
│   │   │   └── audit.py        # Pydantic models for API requests/responses
│   │   ├── routers/
│   │   │   ├── __init__.py
│   │   │   └── audit.py        # FastAPI router for /audit endpoints
│   │   └── services/
│   │       ├── __init__.py
│   │       ├── ai_cross_ref.py # Logic for calling external AIs
│   │       ├── ethics_sentinel.py # Core text analysis logic
│   │       └── firebase_client.py # Firebase Admin SDK logic
│   ├── tests/                  # Pytest directory
│   │   ├── __init__.py
│   │   ├── test_audit_endpoint.py
│   │   └── conftest.py
│   ├── .env.example            # Example environment variables
│   ├── Dockerfile              # To containerize the FastAPI app
│   └── requirements.txt        # Python dependencies
├── chrome-extension/
│   ├── icons/
│   │   ├── icon16.png
│   │   └── icon48.png
│   ├── background.js           # Handles context menu creation, API calls
│   ├── content_script.js       # Injected into pages (if needed for UI)
│   ├── manifest.json           # Extension configuration
│   └── popup/
│       ├── popup.html
│       └── popup.js
└── README.md
```

## 4. Development Setup

1.  **Clone the repository:**
    ```bash
    git clone <repository_url>
    cd faithseal/HYT2/api
    ```
2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```
3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Set up environment variables:**
    -   Copy the `.env.example` file to `.env`.
    -   Add your API keys and Firebase configuration to the `.env` file.
5.  **Run the FastAPI application:**
    ```bash
    uvicorn src.main:app --reload
    ```
The application will be available at `http://127.0.0.1:8000`.
