# GitHub for beginners (explained like you're 10)

Think of GitHub as an online **locker** for your project folder. Git is the **notebook** that remembers every change you ever made, so you can look back or undo.

## Words you need
| Word | Simple meaning |
|---|---|
| Repository (repo) | A project folder kept in the locker |
| Commit | A saved snapshot with a note, like a page in the notebook |
| Push | Send your snapshots from your computer up to the locker |
| Pull | Bring the latest snapshots down from the locker |
| Branch | A copy of the project to try ideas safely |
| Private | Only you (and people you invite) can see it |

## Step 1: Create an account
1. Go to github.com and sign up.
2. Confirm your email.

## Step 2: Make a repository (you already did this)
1. Click **+** (top right) → **New repository**.
2. Name it, pick **Private**, and click **Create repository**.

## Step 3: Put files in it (web upload, no commands)
1. Open your repo and click **Add file → Upload files**.
2. Drag your files in (for example `README.md`).
3. Scroll down, type a short note like "first upload", and click **Commit changes**.

## Step 4: Use the command line (the "real" way)
You need Git installed on your computer (git-scm.com).

```
git clone https://github.com/YOUR-NAME/YOUR-REPO.git   # copy the locker to your computer
cd YOUR-REPO                                            # go inside the folder
git status                                              # what changed?
git add .                                               # pick all changes for the next snapshot
git commit -m "describe what you did"                   # take the snapshot
git push                                                # send it to GitHub
git pull                                                # get the latest from GitHub
```

## Step 5: Logging in from the command line
GitHub no longer accepts your account password for command-line pushes. Use one of:
- **GitHub CLI:** install `gh`, then run `gh auth login` and follow the prompts.
- **A personal access token:** GitHub → Settings → Developer settings → Personal access tokens. Store it safely; never paste it into chat or a file you share.

## Safety rules for beginners
- Never put passwords, bank details, broker logins, or API keys in a repo, even a private one.
- Keep trading-related repos **private**.
- Check `git status` before every commit so you don't upload the wrong files.
