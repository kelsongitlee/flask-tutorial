


Before you start coding, always follow these steps to "turn on" the project's isolated environment. 
This makes sure you're using the right tools for this specific project.

python -m venv venv (creates a new folder named venv in your current directory containing a self-contained Python environment specifically for this project)

**1. Navigate to your project directory:**
```powershell
cd "D:\Desktop Backup\GitHub Project\microblog-2018\microblog"
```

**2. Activate the virtual environment (use this command):**
[Why this is critical]: This command tells your terminal: 
"Stop using the main, shared Python on this computer. 
From now on, only use the Python and packages stored inside this project's venv folder."

You will know it worked when you see (venv) appear at the beginning of your command prompt line.

```powershell
& ".\venv\Scripts\Activate.ps1"
```

**3. Verify it's working:**
```powershell
python -c "import sys; print(sys.executable)"
```