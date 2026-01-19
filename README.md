# Memory Card Game (Django)

This project is a "Memory Card Game" built using the Django framework.
Users can sign up, test their memory by matching pairs of cards, and save their scores.

## Features
- 🔐 **Auth System**: User Registration and Login.
- 🃏 **Card Model**: Image-based cards fetched from the database.
- 🧩 **Gameplay**: Timer and scoring system.
- 📊 **Dashboard**: User statistics and Leaderboard.
- 🎨 **Design**: Modern "Glassmorphism" UI (Vanilla CSS).

## Installation and Setup

1. **Requirements**: Python must be installed.
2. **Install Dependencies**:
   ```bash
   pip install django pillow
   ```
3. **Migrations (Create Database)**:
   ```bash
   python3 manage.py migrate
   ```
4. **Load Initial Data** (Admin and Cards):
   ```bash
   python3 init_game_data.py
   ```
5. **Run the Project**:
   ```bash
   python3 manage.py runserver
   ```

## Usage

- Open `http://127.0.0.1:8000/` in your browser.
- **Login**: 
  - Username: `admin`
  - Password: `1`
  - Or create a new account ("Register").
- **Admin Panel**: `http://127.0.0.1:8000/admin/` (To add new cards).

## Technologies
- **Backend**: Django (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite
