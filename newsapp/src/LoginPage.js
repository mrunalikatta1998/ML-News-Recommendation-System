import React, { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import axios from 'axios';
import Cookies from 'js-cookie'; // Import js-cookie
import './LoginPage.css';

function LoginPage() {
  const [username, setUsername] = useState('');
  const [password, setPassword] = useState('');
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();

    // Clear previous error message
    setErrorMessage('');

    // Validate username and password
    if (!username || !password) {
      setErrorMessage('Username and Password are required.');
      return;
    }

    try {
      // Make an API call to your authentication route
      const response = await axios.post('http://localhost:8000/login/', {
        username: username,
        password: password,
      });

      // Assuming the API returns a success message and token on correct credentials
      if (response.status === 201 || response.status === 200) {
        const { token, user } = response.data;

        // Store the token in cookies
        Cookies.set('authToken', token, { expires: 7 }); // Expires in 7 days (adjust as needed)

        // Redirect to the WelcomePage
        navigate('/welcome');
      } else {
        setErrorMessage('Invalid credentials');
      }
    } catch (error) {
      // Handle errors here, such as network issues, server down, etc.
      setErrorMessage('Login failed. Please try again later.');
    }
  };

  return (
    <div className="login-container">
      <h2>
        <u>News Recommendation</u>
      </h2>
      <h2>
        <center>Login</center>
      </h2>
      <form onSubmit={handleSubmit} className="login-form">
        <div className="form-group">
          <label htmlFor="username">Username:</label>
          <input
            type="text"
            id="username"
            value={username}
            onChange={(e) => setUsername(e.target.value)}
            placeholder="Enter your username"
            required
          />
        </div>

        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input
            type="password"
            id="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            placeholder="Enter your password"
            required
          />
        </div>

        {errorMessage && <div className="error-message">{errorMessage}</div>}

        <button type="submit" className="login-btn">
          Login
        </button>
      </form>
      <p className="signup-link">
        Don't have an account? <Link to="/SignupPage">Sign up</Link>
      </p>
    </div>
  );
}

export default LoginPage;
