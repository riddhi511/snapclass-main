# SnapClass - AI-Powered Attendance System

SnapClass is a full-stack attendance management platform that replaces manual roll-call with AI-driven face and voice recognition. Teachers can take attendance for an entire classroom from a single photo or a short audio recording, while students enroll in courses instantly via a shareable link or QR code.

#
**Live app:** https://snapclass-407929015471.us-central1.run.app
#
**Landing page:** https://snapclass-landingpage-psi.vercel.app
#

## Demo

https://github.com/user-attachments/assets/0a9c5284-5cfa-4fa0-86d2-57ce4bafe2a0

## Features

**For Teachers**
- Secure password-based authentication
- Create and manage subjects, each with an auto-generated join code
- Share a subject via a copyable link or QR code for instant student enrollment
- Take attendance from a single classroom photo — AI detects and matches every enrolled student's face in one pass
- Take attendance via sequential voice roll-call — students say "I am present" and the AI matches their voice against stored voiceprints
- Review, confirm, and save attendance records, with historical logs per subject

**For Students**
- Face-ID login — no password required
- One-time face (and optional voice) enrollment on first login
- Instant course enrollment via shared link, QR code, or manual join code
- Personal dashboard showing enrolled subjects and attendance history per subject

## Tech Stack

| Layer | Technology |
|---|---|
| Frontend / App | [Streamlit](https://streamlit.io) |
| Backend / Database | [Supabase](https://supabase.com) (PostgreSQL) |
| Face Recognition | `face_recognition`, `dlib` |
| Voice Recognition | `Resemblyzer`, `librosa` |
| Auth | `bcrypt` password hashing |
| Landing Page | HTML / CSS, deployed on Vercel |
| Deployment | Docker container on Google Cloud Run |
| Secrets Management | Google Secret Manager |

## Architecture

- The core app is a Streamlit application, containerized with Docker and deployed on **Google Cloud Run**.
- All application data (teachers, students, subjects, enrollments, attendance logs) is stored in **Supabase**.
- Face embeddings are generated with `face_recognition`/`dlib` and matched against enrolled students at attendance time.
- Voice embeddings are generated with `Resemblyzer` and matched using cosine similarity against stored student voiceprints.
- Credentials are managed via **Google Secret Manager** in production, with a local `.streamlit/secrets.toml` fallback for development.
- A separate static landing page (HTML/CSS) is deployed on **Vercel** and links out to the live app.

## Running Locally

**1. Clone the repository**
```bash
git clone https://github.com/riddhi511/snapclass-main.git
cd snapclass-main
```

**2. Create and activate a virtual environment**
```bash
python -m venv venv
venv\Scripts\Activate.ps1      # Windows
source venv/bin/activate       # macOS/Linux
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Configure secrets**

Create `.streamlit/secrets.toml` in the project root:
```toml
SUPABASE_URL = "your-supabase-project-url"
SUPABASE_KEY = "your-supabase-api-key"
```

**5. Run the app**
```bash
streamlit run app.py
```

## Deployment

The app is containerized and deployed on **Google Cloud Run**:

```bash
gcloud run deploy snapclass \
  --source . \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --set-secrets="SUPABASE_URL=SUPABASE_URL:latest,SUPABASE_KEY=SUPABASE_KEY:latest"
```

Supabase credentials are stored in **Google Secret Manager** rather than checked into source control.

## Project Structure

```
snapclass-main/
├── app.py                      # Entry point & routing
├── Dockerfile                  # Container definition for Cloud Run
├── requirements.txt
├── src/
│   ├── screens/                # Top-level pages (home, teacher, student)
│   ├── components/              # Dialogs & reusable UI components
│   ├── pipelines/               # Face & voice recognition pipelines
│   ├── database/                # Supabase client & queries
│   └── ui/                      # Shared styling
```

## Roadmap

- [ ] Automatic email/SMS notifications for low attendance
- [ ] Exportable attendance reports (CSV/PDF)
- [ ] Multi-teacher subject co-ownership
- [ ] Custom domain for the deployed app

---

Built by **Riddhi Soni**
