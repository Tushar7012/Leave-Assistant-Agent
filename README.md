# Leave Assistant Agent

Multi-Agent Leave Management System powered by LangGraph and Next.js

## 🚀 Features

- **Multi-Agent Architecture**: Three specialized AI agents (Data, Policy, Email)
- **Real-time Chat Interface**: Modern Next.js 14 frontend with streaming support
- **LangGraph Orchestration**: Intelligent routing between agents
- **Beautiful UI**: Glassmorphism design with smooth animations

## 🏗️ Tech Stack

### Backend
- Flask
- LangGraph
- LangChain
- Groq LLM API

### Frontend
- Next.js 14
- TypeScript
- Tailwind CSS
- Framer Motion

## 📦 Installation

### Prerequisites
- Python 3.10+
- Node.js 18+
- Groq API Key

### Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/Tushar7012/Leave-Assistant-Agent.git
   cd Leave-Assistant-Agent
   ```

2. **Setup (Windows)**
   ```bash
   setup.bat
   ```

3. **Configure Environment**
   - Copy `.env.example` to `.env`
   - Add your Groq API key

4. **Run the application**
   
   Backend:
   ```bash
   start_backend.bat
   ```
   
   Frontend (in new terminal):
   ```bash
   start_frontend.bat
   ```

5. **Open browser**
   - Navigate to http://localhost:3000

## 📖 Documentation

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for detailed installation instructions.

See [STATUS.md](STATUS.md) for current application status and troubleshooting.

## 🤖 Agents

- **Data Agent**: Handles employee data queries and leave balance lookups
- **Policy Agent**: Provides leave policy information and guidelines
- **Email Agent**: Composes professional leave request emails

## 🎯 Example Queries

- "What is the sick leave policy?"
- "My ID is EMP001. Check my leave balance."
- "Send an email to manager@company.com requesting leave."

## 📝 License

MIT

## 👤 Author

Tushar - [GitHub](https://github.com/Tushar7012)
