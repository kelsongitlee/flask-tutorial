# Git Cheat Sheet - Flask Tutorial Project

## 🚀 Initial Setup (First Time)

### 1. Initialize Repository
```bash
# Navigate to your project directory
cd "D:\Desktop Backup\GitHub Project\microblog-2018"

# Initialize Git repository
git init

# Set up your Git identity (only needed once)
git config --global user.name "kelsongitlee"
git config --global user.email "gimsheng.lee@gmail.com"
```

### 2. Create .gitignore File
```bash
# Create .gitignore to exclude virtual environment
# (Already created in your project)
```

### 3. First Commit
```bash
# Add all files to staging
git add .

# Make initial commit
git commit -m "Initial commit: Complete Flask Microblog tutorial project"

# Rename branch to main
git branch -M main
```

### 4. Connect to GitHub
```bash
# Add GitHub remote
git remote add origin https://github.com/kelsongitlee/flask-tutorial.git

# Push to GitHub
git push -u origin main
```

---

## 📚 Chapter Workflow (Creating New Chapters)

### Create New Chapter Branch
```bash
# 1. Switch to main branch
git checkout main

# 2. Create new chapter branch
git checkout -b "chapter-X-chapter-name"

# 3. Add all changes
git add .

# 4. Commit changes
git commit -m "Chapter X: Chapter Name"

# 5. Push new branch to GitHub
git push -u origin chapter-X-chapter-name
```

### Replace Existing Chapter Branch
```bash
# 1. Commit current changes to main first
git add .
git commit -m "Update main with latest changes"

# 2. Switch to chapter branch
git checkout chapter-X-chapter-name

# 3. Reset branch to match main (replaces everything)
git reset --hard main

# 4. Force push to replace remote branch
git push origin chapter-X-chapter-name --force
```

---

## 🔄 Common Daily Commands

### Check Status
```bash
# See current status
git status

# See current branch
git branch

# See all branches (local and remote)
git branch -a
```

### Switch Between Branches
```bash
# Switch to main branch
git checkout main

# Switch to specific chapter
git checkout chapter-2-templates

# Create and switch to new branch
git checkout -b "new-branch-name"
```

### Make Changes and Commit
```bash
# Add specific files
git add filename.py

# Add all changes
git add .

# Commit with message
git commit -m "Your commit message here"

# Push to current branch
git push
```

### Update Main Branch
```bash
# Switch to main
git checkout main

# Pull latest changes from GitHub
git pull origin main

# Add your changes
git add .
git commit -m "Update main branch"

# Push to GitHub
git push origin main
```

---

## 🎯 Your Specific Chapter Names

### Chapter Branches Created:
- `main` - Complete project
- `chapter-1-hello-world` - Hello, World! checkpoint
- `chapter-2-templates` - Templates checkpoint
- `chapter-3-web-forms` - Web Forms checkpoint

### Future Chapter Names (Examples):
- `chapter-4-database` - Database chapter
- `chapter-5-user-logins` - User authentication
- `chapter-6-profile-pages` - User profiles
- `chapter-7-error-handling` - Error handling
- `chapter-8-followers` - Following system
- `chapter-9-pagination` - Pagination
- `chapter-10-email-support` - Email features
- `chapter-11-facelift` - UI improvements
- `chapter-12-dates-times` - Date/time handling
- `chapter-13-i18n-l10n` - Internationalization
- `chapter-14-ajax` - AJAX features
- `chapter-15-api` - REST API
- `chapter-16-testing` - Testing
- `chapter-17-deployment` - Deployment

---

## 🛠️ Troubleshooting Commands

### Fix Common Issues
```bash
# Undo last commit (keep changes)
git reset --soft HEAD~1

# Undo last commit (lose changes)
git reset --hard HEAD~1

# Delete local branch
git branch -D branch-name

# Delete remote branch
git push origin --delete branch-name

# Force push (use carefully)
git push origin branch-name --force

# Pull and merge
git pull origin main

# See commit history
git log --oneline

# See file changes
git diff
```

### Recover Lost Files
```bash
# See what files were deleted
git status

# Restore deleted file
git checkout HEAD -- filename.py

# Restore all deleted files
git checkout HEAD -- .
```

---

## 📋 Quick Reference

### Your Repository URL:
`https://github.com/kelsongitlee/flask-tutorial.git`

### Current Working Directory:
`D:\Desktop Backup\GitHub Project\microblog-2018`

### Virtual Environment Activation:
```bash
cd "D:\Desktop Backup\GitHub Project\microblog-2018\microblog"
& ".\venv\Scripts\Activate.ps1"
```

### Flask Run Command:
```bash
flask run
```

---

## 🎯 Quick Workflow Summary

### For New Chapter:
1. `git checkout main`
2. `git checkout -b "chapter-X-name"`
3. `git add .`
4. `git commit -m "Chapter X: Name"`
5. `git push -u origin chapter-X-name`

### For Daily Work:
1. `git add .`
2. `git commit -m "Description of changes"`
3. `git push`

### To Replace Chapter:
1. `git add . && git commit -m "Update main"`
2. `git checkout chapter-X-name`
3. `git reset --hard main`
4. `git push origin chapter-X-name --force`

---

*This cheat sheet covers all the Git commands you'll need for your Flask tutorial project! 🚀*
