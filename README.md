# Demo App: Frontend & Backend

This repository contains a simple two-component web application:

- 🖥️ **Frontend**: Static site served by Nginx
- 🔧 **Backend**: Flask API returning current timestamp and server IP

Each component is built and published as a separate Docker image to **GitHub Container Registry (GHCR)**.

---

## 📁 Directory Structure

```

.
├── frontend/          # Nginx static site (Dockerfile + HTML)
├── backend/           # Flask API (Dockerfile + Python app)
└── .github/
└── workflows/
└── docker-publish.yml

```

---

## 🚀 Container Images

Images are published to [GHCR](https://ghcr.io/) under your GitHub account:

- `ghcr.io/<your-user>/demo-frontend:latest`
- `ghcr.io/<your-user>/demo-backend:latest`

> Replace `<your-user>` with your GitHub username or organization name.

---

## 🔄 CI/CD: GitHub Actions

This repository includes an automated workflow to:

- Build both `frontend` and `backend` images
- Push them to `ghcr.io`
- Trigger on:
  - Push to `main`
  - Manual trigger via GitHub UI (Actions → Run workflow)

### Trigger manually:

1. Go to the **Actions** tab
2. Select **Build & Push Frontend + Backend**
3. Click **"Run workflow"**

---

## 🧪 Local Development

### Build frontend locally

```bash
docker build -t demo-frontend:local ./frontend
docker run -p 8080:80 demo-frontend:local
```

### Build backend locally

```bash
docker build -t demo-backend:local ./backend
docker run -p 5000:5000 demo-backend:local
```

---

## 📦 Used By

This repo is used in conjunction with a GitOps-based infrastructure repository (e.g. `demo-k8s-iaac`) that deploys these images into a Kubernetes cluster via ArgoCD.

---

## 🛠️ TODO

- [ ] Add automated version tags
- [ ] Add health checks
- [ ] Add unit tests for backend

---

## 📄 License

MIT – see [`LICENSE`](LICENSE) file.
