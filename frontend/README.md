# File Hub Frontend

React-based frontend for the File Hub application, built with TypeScript and modern web technologies.

## 🚀 Technology Stack

- React 18.x
- TypeScript 4.x
- React Router 6.x
- Axios for API communication
- Docker for containerization

## 📋 Prerequisites

- Node.js 18.x or higher
- npm 8.x or higher
- Docker (if using containerized setup)

## 🛠️ Installation & Setup

### Local Development

1. **Install Dependencies**
   ```bash
   npm install
   ```

2. **Start Development Server**
   ```bash
   npm start
   ```
   Access the application at http://localhost:3000

### Docker Setup

```bash
# Build the image
docker build -t file-hub-frontend .

# Run the container
docker run -p 3000:3000 file-hub-frontend
```

## 📁 Project Structure

```
src/
├── components/     # React components
├── hooks/         # Custom React hooks
├── services/      # API services
├── types/         # TypeScript types
└── utils/         # Utility functions
```

## 🔧 Available Scripts

- `npm start`: Start development server
- `npm run build`: Build for production
- `npm run test`: Run tests
- `npm run eject`: Eject from Create React App

## 🌐 API Integration

The frontend communicates with the backend API at `http://localhost:8000/api`. Key endpoints:

- `GET /api/files/`: List all files
- `POST /api/files/`: Upload new file
- `GET /api/files/<id>/`: Get file details
- `DELETE /api/files/<id>/`: Delete file

## 🔒 Environment Variables

```env
REACT_APP_API_URL=http://localhost:8000/api
```

## 🐛 Troubleshooting

1. **Build Issues**
   - Clear npm cache: `npm cache clean --force`
   - Delete node_modules: `rm -rf node_modules && npm install`

2. **API Connection Issues**
   - Verify API URL in environment variables
   - Check CORS settings
   - Ensure backend is running

## 📚 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request
