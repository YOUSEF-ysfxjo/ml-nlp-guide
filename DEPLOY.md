# Deploy ML/NLP Guide — Auto-update on every change

This project is a **static site** (`ml-nlp-guide.html` + `css/` + `js/`). To deploy it and have the live page update whenever you change the files, use **Git + a host that deploys on push** (Netlify or Vercel). No build step required.

---

## One-time setup

### 1. Turn the project into a Git repo (if not already)

In the project root (`New_ara`):

```bash
git init
git add ml-nlp-guide.html css/ js/ netlify.toml vercel.json .gitignore
git add GOAL_AND_APPROACH.md ML_NLP_Comprehensive_Summary.md ML_NLP_Paper_Reading_Guide.md
# Add any other files you want on the site or in the repo
git commit -m "Initial commit: ML/NLP guide static site"
```

*(Adjust the `git add` list if you want more/fewer files. Don’t add the whole `word2vec/` tree if you don’t need it deployed.)*

### 2. Create a GitHub repo and push

- On [github.com](https://github.com) → **New repository** (e.g. `ml-nlp-guide`).
- Do **not** add a README or .gitignore (you already have files).
- Then in your project folder:

```bash
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
git branch -M main
git push -u origin main
```

---

## Deploy with Netlify (recommended)

1. Go to [netlify.com](https://www.netlify.com) and sign in (e.g. with GitHub).
2. **Add new site** → **Import an existing project** → **GitHub**.
3. Choose the repo you just pushed. Netlify will use:
   - **Build command:** (leave empty)
   - **Publish directory:** `.` (root)
4. Click **Deploy site**.

Your site will be at `https://something.netlify.app`. The root URL `/` will show `ml-nlp-guide.html` (via the redirect in `netlify.toml`).

**From now on:** every time you run `git push`, Netlify will automatically rebuild and update the live page.

---

## Deploy with Vercel (alternative)

1. Go to [vercel.com](https://vercel.com) and sign in (e.g. with GitHub).
2. **Add New** → **Project** → import your GitHub repo.
3. Leave **Framework Preset** as “Other” and **Root Directory** as `.`. Deploy.
4. Your site will be at `https://your-project.vercel.app`. The root `/` will serve `ml-nlp-guide.html` (via `vercel.json`).

**From now on:** every `git push` triggers a new deployment and updates the live page.

---

## Updating the live site

Whenever you edit `ml-nlp-guide.html`, `css/styles.css`, or `js/app.js` (or any file you committed):

```bash
git add .
git commit -m "Update guide: ..."
git push
```

The host (Netlify or Vercel) will detect the push and deploy the new version. The page will update after the deploy finishes (usually within a minute).

---

## Optional: custom domain

- **Netlify:** Site settings → **Domain management** → Add custom domain.
- **Vercel:** Project → **Settings** → **Domains** → Add.

Both provide free HTTPS.
