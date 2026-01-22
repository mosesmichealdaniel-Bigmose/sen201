
# SEN ASSIGNMENT – Software Engineering (Python)

## Project Title
Study Group Matchmaker (Non-Social Media)

## Project Overview
The **Study Group Matchmaker** is a Python-based academic system that intelligently matches students into study groups
based on academic parameters rather than social interaction.

Unlike social media platforms, this system has:
- ❌ No posts
- ❌ No likes
- ❌ No followers  
✔️ Only academic-based matching

The goal is to improve exam preparation and collaborative learning.

---

## 1. Requirement Analysis

### Functional Requirements
- Register a student
- Capture student academic details:
  - Course
  - Skill level (Beginner / Intermediate / Confident)
  - Availability (Morning / Afternoon / Evening)
  - Exam timeline (Weeks to exam)
- Match students into compatible study groups
- View matched study groups

### Non‑Functional Requirements
- Simple Command Line Interface (CLI)
- Easy to maintain and extend
- Written in Python 3
- No internet or social interaction features

---

## 2. Feasibility Study

### Technical Feasibility
Python supports file handling, condition matching, and modular programming.

### Economic Feasibility
Uses free and open‑source tools.

### Operational Feasibility
Easy for students to use without training.

---

## 3. System Design

### Architecture
Modular, file‑based system.

### Modules
- `main.py` – Application entry point
- `student.py` – Student model
- `matcher.py` – Matching logic
- `storage.py` – Data persistence

### Data Storage
Students are stored in `students.txt`.

---

## 4. Implementation

Matching is done when students share:
- Same course
- Same skill level
- Same availability
- Similar exam timeline (±1 week)

All names and logic used in design exactly match the implementation.

---

## 5. Testing

| Feature | Status |
|-------|-------|
| Register student | Pass |
| Match students | Pass |
| View groups | Pass |
| File storage | Pass |

---

## 6. Deployment

Run the application using:
```bash
python main.py
```

---

## 7. Maintenance

Future improvements:
- GUI interface
- Database storage
- Automated group chat creation (e.g., WhatsApp, Telegram)

---

## Author
Ewenla Issachar Teninla  
Department of Computer Science
