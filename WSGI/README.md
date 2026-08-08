# WSGI Example

A minimal Flask WSGI example demonstrating how to create an app, define routes, and run it with the built-in development server.

Files
- app.py — the example Flask application (entry point).

Routes
- GET /        — "This is my home page."
- GET /second/ — "This is my second page"
- GET /debugger — Demonstrates a message about running with debug=True

How to run
1. (Optional) Create and activate a virtual environment and install Flask:
   pip install Flask
2. Run the app directly:
   python WSGI/app.py


Development notes
- app.py currently calls `app.run(debug=True)` when executed as `__main__` so changes may be hot-reloaded while developing.
- For production, use a proper WSGI server (gunicorn, uWSGI) and remove `debug=True`.
