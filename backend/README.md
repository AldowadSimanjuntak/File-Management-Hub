# File Hub Backend

Django-based backend for the File Hub application, providing a robust API for file management.

## 🚀 Technology Stack

- Python 3.9+
- Django 4.x
- Django REST Framework
- SQLite (Development database)
- Docker
- WhiteNoise for static file serving

## 📋 Prerequisites

- Python 3.9 or higher
- pip
- Docker (if using containerized setup)
- virtualenv or venv (recommended)

## 🛠️ Installation & Setup

### Local Development

1. **Create and activate virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Environment Setup**
   Create a `.env` file in the backend directory:
   ```env
   DEBUG=True
   SECRET_KEY=your-secret-key
   ALLOWED_HOSTS=localhost,127.0.0.1
   ```

4. **Database Setup**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser
   ```
   Note: SQLite database will be automatically created at `db.sqlite3`

5. **Run Development Server**
   ```bash
   python manage.py runserver
   ```
   Access the API at http://localhost:8000/api

### Docker Setup

```bash
# Build the image
docker build -t file-hub-backend .

# Run the container
docker run -p 8000:8000 file-hub-backend
```

## 📁 Project Structure

```
backend/
├── core/           # Project settings and main URLs
├── files/          # File management app
│   ├── models.py   # Data models
│   ├── views.py    # API views
│   ├── urls.py     # URL routing
│   └── tests.py    # Unit tests
├── db.sqlite3      # SQLite database
└── manage.py       # Django management script
```

## 🔌 API Endpoints

### Files API (`/api/files/`)

- `GET /api/files/`: List all files
  - Query Parameters:
    - `search`: Search files by name
    - `sort`: Sort by created_at, name, or size

- `POST /api/files/`: Upload new file
  - Request: Multipart form data
  - Fields:
    - `file`: File to upload
    - `description`: Optional file description

- `GET /api/files/<uuid>/`: Get file details
- `DELETE /api/files/<uuid>/`: Delete file

## 🔒 Security Features

- UUID-based file identification
- WhiteNoise for secure static file serving
- CORS configuration for frontend integration
- Django's built-in security features:
  - CSRF protection
  - XSS prevention
  - SQL injection protection

## 🧪 Testing

```bash
# Run all tests
python manage.py test

# Run specific test file
python manage.py test files.tests
```

## 🐛 Troubleshooting

1. **Database Issues**
   ```bash
   # Reset database
   rm db.sqlite3
   python manage.py migrate
   ```

2. **Static Files**
   ```bash
   python manage.py collectstatic
   ```

3. **Permission Issues**
   - Check file permissions in media directory
   - Ensure write permissions for SQLite database directory

## 📚 Contributing

1. Fork the repository
2. Create your feature branch
3. Write and run tests
4. Commit your changes
5. Push to the branch
6. Create a Pull Request

## 📖 Documentation

- API documentation available at `/api/docs/`
- Admin interface at `/admin/`
- Detailed API schema at `/api/schema/` 