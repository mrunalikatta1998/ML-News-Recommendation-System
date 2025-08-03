import React from "react";
import { Routes, Route, Navigate } from "react-router-dom";
import LoginPage from "./LoginPage"; // Make sure this is the correct path
import WelcomePage from "./WelcomePage"; // Make sure this is the correct path
import HomePage from "./HomePage"; // You can add a home page if you need
import SignupPage from "./SignupPage";

function App() {
  return (
    <Routes>
      <Route path="/" element={<Navigate to="/login" replace />} />
      {/* Default route will show LoginPage */}
      <Route path="/login" element={<LoginPage />} /> {/* Login page route */}
      
      {/* These routes are for after successful login */}
      <Route path="/welcome" element={<WelcomePage />} /> {/* Welcome page route */}

      {/* These routes are for after successful login */}
      <Route path="/HomePage" element={<HomePage />} /> {/* Welcome page route */}

      {/* These routes are for after successful login */}
      <Route path="/SignupPage" element={<SignupPage />} /> {/* Welcome page route */}

    </Routes>
  );
}

export default App;
