
# CST8919 Lab 1 - Flask App with Auth0 Integration

This project is a simple Flask web application that uses Auth0 for authentication. After login, users are redirected to a protected dashboard page that displays their profile information.

---

## 1. How to Set Up the App

### Auth0 Configuration

1. Sign up at https://auth0.com/ and create a new "Regular Web Application".
2. Go to the application settings and configure the following fields:

- **Allowed Callback URLs**: `http://localhost:5000/callback`
- **Allowed Logout URLs**: `http://localhost:5000`
- **Allowed Web Origins**: `http://localhost:5000`

3. Copy your **Client ID**, **Client Secret**, and **Domain** for use in the `.env` file.

---

## 2. Install Dependencies and Run the App

```bash
# Create and activate a virtual environment
python -m venv venv
venv\Scripts\activate   # On Windows

# Install Python dependencies
pip install -r requirements.txt

# Start the Flask app
python app.py
```

---

## 3. Environment Variables

Create a `.env` file in the root of your project with the following:

```env
AUTH0_CLIENT_ID=your-client-id
AUTH0_CLIENT_SECRET=your-client-secret
AUTH0_DOMAIN=your-auth0-domain
AUTH0_CALLBACK_URL=http://localhost:5000/callback
AUTH0_AUDIENCE=https://your-auth0-domain/userinfo
```

---

## 4. Demo Video


---

## 5. What I Learned

- How to integrate OAuth2 login using Auth0
- How to protect Flask routes using session
- How to securely use environment variables
- How to create a simple web login flow

---

## 6. Project Files

```
.
├── app.py
├── requirements.txt
├── .gitignore
├── templates/
│   ├── home.html
│   └── dashboard.html
└── README.md
```

---

## 7. GitHub Repository

This project is pushed to a public GitHub repository with multiple commits documenting progress.  
The demo video link is included above in this README.

---

## Author

Zhe Zhang  
Algonquin College – CST8919  
