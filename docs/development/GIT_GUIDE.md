# Git Workflow

## Create Branch

git checkout main

git pull

git checkout -b feature/module-name

---

## Commit

git add .

git commit -m "Implement module"

---

## Push

git push origin feature/module-name

---

## Merge

git checkout main

git merge feature/module-name

git push origin main

---

## Rules

Satu branch

↓

Satu modul

↓

Satu commit besar

↓

Merge

↓

Lanjut modul berikutnya