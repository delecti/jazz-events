# Jazz Events

A simple event tracking app. It lets me track recurring IRL events over time. As a simple example, it will let me answer questions like "when's the last time I bought shampoo" or "how often do I buy shampoo," and easily track when I do 

The main motivations for this are to teach myself how to code with AI assistance, Django (and to a lesser extent get better at Python), and to a lesser extent GitHub.

## Setup

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env  # then fill in values
python manage.py migrate
python manage.py runserver
```

## Environment Variables

| Variable | Description |
|---|---|
| `SECRET_KEY` | Django secret key |
| `DEBUG` | `True` or `False` |
| `DATABASE_URL` | Database connection string (defaults to SQLite) |

## API

| Method | URL | Description |
|---|---|---|
| `GET` | `/events/` | List all event names with counts |
| `GET` | `/events/{name}/` | Get count and timestamps for a specific event |
| `PUT` | `/events/{name}/` | Create a new event (409 if already exists) |
| `POST` | `/events/{name}/` | Add an occurrence to an existing event |
| `DELETE` | `/events/{name}/` | Delete all occurrences of an event |

## Running on a local network

```bash
python manage.py runserver 0.0.0.0:8000
```

Then access from other devices at `http://<your-ip>:8000`.