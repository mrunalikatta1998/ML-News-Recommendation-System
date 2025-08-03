import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import './SignupPage.css'

function SignupPage() {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [name, setName] = useState('');
  const [phoneNumber, setPhoneNumber] = useState('');
  const [preferredNewsCategories, setPreferredNewsCategories] = useState([]);
  const [errorMessage, setErrorMessage] = useState('');
  const navigate = useNavigate();

  const handlePreferenceChange = (event) => {
    const value = event.target.value;
    if (event.target.checked) {
      setPreferredNewsCategories([...preferredNewsCategories, value]);
    } else {
      setPreferredNewsCategories(preferredNewsCategories.filter(item => item !== value));
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setErrorMessage(''); // Clear previous error message

    if (!username || !email || !password || !name || !phoneNumber || preferredNewsCategories.length === 0) {
      setErrorMessage('All fields are required.');
      return;
    }

    const preferencesString = preferredNewsCategories.join(', '); // Convert array to comma-separated string

    try {
      const response = await axios.post('http://localhost:8000/signup/', {
        username,
        email,
        password,
        name,
        phone_number: phoneNumber,
        preferred_news_categories: preferencesString
      });

      if (response.status === 201 || response.status === 200) {
        navigate('/login');
      } else {
        setErrorMessage(response.data.message || 'Failed to sign up');
      }
    } catch (error) {
      setErrorMessage('An error occurred. Please try again later.');
    }
  };

  return (
    <div className="signup-container">
      <h2>Sign Up</h2>
      <form onSubmit={handleSubmit} className="signup-form">
        <div className="form-group">
          <label htmlFor="username">Username:</label>
          <input type="text" id="username" value={username}
            onChange={(e) => setUsername(e.target.value)} placeholder="Enter your username" required />
        </div>

        <div className="form-group">
          <label htmlFor="email">Email:</label>
          <input type="email" id="email" value={email}
            onChange={(e) => setEmail(e.target.value)} placeholder="Enter your email" required />
        </div>

        <div className="form-group">
          <label htmlFor="password">Password:</label>
          <input type="password" id="password" value={password}
            onChange={(e) => setPassword(e.target.value)} placeholder="Enter your password" required />
        </div>

        <div className="form-group">
          <label htmlFor="name">Name:</label>
          <input type="text" id="name" value={name}
            onChange={(e) => setName(e.target.value)} placeholder="Enter your full name" required />
        </div>

        <div className="form-group">
          <label htmlFor="phoneNumber">Phone Number:</label>
          <input type="text" id="phoneNumber" value={phoneNumber}
            onChange={(e) => setPhoneNumber(e.target.value)} placeholder="Enter your phone number" required />
        </div>

        <div className="form-group preferences">
          <label>Preferred News Categories:</label>
          <div className="checkbox-group">
            {["arts, culture, entertainment and media", "conflict, war and peace", "crime, law and justice", "disaster, accident and emergency incident", "economy, business and finance", "education", "environment", "health" , "human interest", "labour" , "lifestyle and leisure", "politics", "religion and belief", "science and technology", "society", "sport", "weather"
].map(category => (
              <div key={category}>
                <input type="checkbox" id={category} value={category}
                  checked={preferredNewsCategories.includes(category)}
                  onChange={handlePreferenceChange} />
                <label htmlFor={category}>{category}</label>
              </div>
            ))}
          </div>
        </div>

        {errorMessage && <div className="error-message">{errorMessage}</div>}

        <button type="submit" className="signup-btn">Sign Up</button>
      </form>
      <p className="login-link">
        Already have an account? <Link to="/">Login</Link>
      </p>
    </div>
  );
}

export default SignupPage;
