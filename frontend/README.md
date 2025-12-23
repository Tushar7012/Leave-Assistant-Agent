# Multi-Agent Leave Assistant - Next.js Frontend

Modern, interactive frontend for the Multi-Agent Leave Assistant built with Next.js, TypeScript, and TailwindCSS.

## Features

✨ **Modern UI/UX**
- Beautiful gradient backgrounds with glassmorphism effects
- Smooth animations using Framer Motion
- Responsive design that works on all devices

🎨 **Rich Content Rendering**
- Markdown support for AI responses
- Syntax highlighting for code blocks
- Copy-to-clipboard functionality

⚡ **Real-time Interactions**
- Typing indicators
- Auto-scroll to latest messages
- Keyboard shortcuts (Enter to send)
- Quick suggestion chips

## Setup Instructions

### 1. Install Dependencies

Make sure you have Node.js (v18 or higher) installed, then run:

```bash
cd frontend
npm install
```

### 2. Create Environment File

Create a `.env.local` file in the `frontend` directory:

```bash
NEXT_PUBLIC_API_URL=http://localhost:5000
```

### 3. Install Python Dependencies (if not already done)

From the root directory:

```bash
pip install flask-cors
```

### 4. Start the Backend

From the root directory:

```bash
python src/flask_app/app.py
```

The Flask backend will run on http://localhost:5000

### 5. Start the Frontend

In a new terminal, from the `frontend` directory:

```bash
npm run dev
```

The Next.js app will run on http://localhost:3000

## Project Structure

```
frontend/
├── app/
│   ├── layout.tsx         # Root layout with metadata
│   ├── page.tsx           # Home page
│   └── globals.css        # Global styles
├── components/
│   ├── ChatInterface.tsx  # Main chat component
│   ├── MessageBubble.tsx  # Message display with markdown
│   ├── SuggestionChip.tsx # Quick action buttons
│   ├── LoadingIndicator.tsx # Typing indicator
│   └── Header.tsx         # App header
├── lib/
│   └── api.ts             # API client for Flask backend
├── package.json           # Dependencies
├── tsconfig.json          # TypeScript config
├── tailwind.config.ts     # TailwindCSS config
└── next.config.mjs        # Next.js config with API proxy
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm start` - Start production server
- `npm run lint` - Run ESLint

## Technology Stack

- **Next.js 14** - React framework with App Router
- **TypeScript** - Type-safe JavaScript
- **TailwindCSS** - Utility-first CSS framework
- **Framer Motion** - Animation library
- **React Markdown** - Markdown rendering
- **React Syntax Highlighter** - Code syntax highlighting

## API Integration

The frontend communicates with the Flask backend through the `/chat` endpoint:

```typescript
POST /chat
{
  "message": "What is the sick leave policy?"
}

Response:
{
  "response": "Based on the company's policy..."
}
```

The Next.js config includes an API proxy that forwards requests from `/api/*` to `http://localhost:5000/*`.

## Customization

### Colors

Edit `tailwind.config.ts` to customize the color scheme:

```typescript
colors: {
  primary: {
    500: '#6366f1', // Main brand color
    ...
  },
}
```

### Animations

Customize animations in `tailwind.config.ts` under the `animation` and `keyframes` sections.

### Suggestions

Edit the `SUGGESTIONS` array in `components/ChatInterface.tsx` to change default suggestions.

## Troubleshooting

**Port already in use:**
```bash
# Kill process on port 3000
npx kill-port 3000
```

**CORS errors:**
- Ensure Flask backend has `flask-cors` installed
- Verify CORS is configured in `src/flask_app/app.py`

**Dependencies not found:**
```bash
# Clear cache and reinstall
rm -rf node_modules package-lock.json
npm install
```

## Production Deployment

1. Build the production bundle:
```bash
npm run build
```

2. Start the production server:
```bash
npm start
```

The optimized build will be created in the `.next` folder.

---

Built with ❤️ using Next.js and Flask
