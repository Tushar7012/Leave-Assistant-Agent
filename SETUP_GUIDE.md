# Quick Setup Guide - Multi-Agent Leave Assistant

## ⚠️ PowerShell Execution Policy Issue

Your system's PowerShell execution policy is blocking npm/npx. **Solution: Use Command Prompt (CMD) instead!**

---

## 🚀 Complete Setup Instructions

### Step 1: Install Flask CORS Support

Open **Command Prompt** (not PowerShell!) and run:

```cmd
cd D:\Agentic_AI\RWS
pip install flask-cors
```

### Step 2: Install Frontend Dependencies

In Command Prompt, navigate to the frontend folder and install dependencies:

```cmd
cd D:\Agentic_AI\RWS\frontend
npm install
```

This will install:
- Next.js
- React
- TailwindCSS
- Framer Motion
- React Markdown
- TypeScript
- And all other dependencies

**Expected time:** 1-3 minutes depending on internet speed

### Step 3: Create Environment File

Create a new file: `D:\Agentic_AI\RWS\frontend\.env.local`

Add this single line:
```
NEXT_PUBLIC_API_URL=http://localhost:5000
```

You can create it using:
```cmd
cd D:\Agentic_AI\RWS\frontend
echo NEXT_PUBLIC_API_URL=http://localhost:5000 > .env.local
```

### Step 4: Start the Backend

Open **Command Prompt Window #1**:

```cmd
cd D:\Agentic_AI\RWS
python src\flask_app\app.py
```

You should see:
```
* Running on http://127.0.0.1:5000
* Debug mode: on
```

✅ Keep this window running!

### Step 5: Start the Frontend

Open **Command Prompt Window #2**:

```cmd
cd D:\Agentic_AI\RWS\frontend
npm run dev
```

You should see:
```
▲ Next.js 14.x.x
- Local: http://localhost:3000
✓ Ready in X.Xs
```

✅ Keep this window running too!

### Step 6: Open Your Browser

Navigate to: **http://localhost:3000**

You should see the beautiful new interface! 🎉

---

## 🔧 Alternative: Fix PowerShell (Optional)

If you prefer using PowerShell, run PowerShell **as Administrator** and execute:

```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

Then restart PowerShell and try the commands again.

---

## 📝 Quick Test Commands

### Test Frontend Only (without backend)
```cmd
cd D:\Agentic_AI\RWS\frontend
npm run dev
```

### Test Backend Only
```cmd
cd D:\Agentic_AI\RWS
python src\flask_app\app.py
```

### Run Console Tests
```cmd
cd D:\Agentic_AI\RWS
python tests\test_agent.py
```

---

## 🐛 Troubleshooting

### Error: "Port 3000 already in use"
Kill the process:
```cmd
taskkill /F /IM node.exe
```

Then try again.

### Error: "Port 5000 already in use"
Kill the process:
```cmd
FOR /F "tokens=5" %P IN ('netstat -ano ^| findstr :5000') DO taskkill /F /PID %P
```

### Error: "npm not found"
Install Node.js from https://nodejs.org/ (LTS version recommended)

### Error: "python not found"
Make sure Python is in your PATH or use the full path to python.exe

### CORS Errors in Browser Console
Make sure:
1. Flask backend is running on port 5000
2. `flask-cors` is installed (`pip install flask-cors`)
3. Both servers are running

---

## 📂 Project Structure

```
D:\Agentic_AI\RWS\
├── frontend\              # Next.js frontend
│   ├── app\              # Pages and layouts
│   ├── components\       # React components
│   ├── lib\             # API client
│   └── package.json     # Dependencies
├── src\
│   ├── flask_app\       # Flask backend
│   └── agents\          # Multi-agent system
├── tests\               # Test scripts
└── requirements.txt     # Python dependencies
```

---

## ✅ Verification Checklist

- [ ] `flask-cors` installed
- [ ] `npm install` completed successfully
- [ ] `.env.local` file created in frontend folder
- [ ] Backend running on http://localhost:5000
- [ ] Frontend running on http://localhost:3000
- [ ] Browser opened to http://localhost:3000
- [ ] Can send messages and get responses

---

## 🎯 What You Should See

### Backend Terminal:
```
* Serving Flask app 'app'
* Debug mode: on
* Running on http://127.0.0.1:5000
Press CTRL+C to quit
```

### Frontend Terminal:
```
▲ Next.js 14.2.0
- Local: http://localhost:3000

✓ Ready in 2.5s
```

### Browser at http://localhost:3000:
- Beautiful gradient background
- Chat interface with emoji (👋) and welcome message
- Three suggestion chips
- "Multi-Agent Leave Assistant" header
- Green "Online" indicator

---

## 💡 Tips

1. **Always use Command Prompt (CMD)** for npm commands to avoid PowerShell policy issues
2. **Keep both terminals running** - you need backend AND frontend
3. **Check both ports** - Backend on 5000, Frontend on 3000
4. **Clear browser cache** if you see old interface
5. **Use Ctrl+C** to stop servers when done

---

## 🎨 Sample Queries to Test

Once running, try these queries in the chat:

1. **Policy Query:**
   ```
   What is the sick leave policy?
   ```

2. **Employee Data:**
   ```
   My employee ID is EMP001. Check my leave balance.
   ```

3. **Email Draft:**
   ```
   Send an email to manager@company.com requesting leave.
   ```

---

## 🚀 You're All Set!

Your modern Multi-Agent Leave Assistant is ready to use!

**Questions?** Check the README.md files or the walkthrough document.

**Enjoy your new beautiful interface! 🎉**
