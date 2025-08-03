import React, { useState, useEffect } from 'react';
import axios from 'axios';
import Cookies from 'js-cookie'; // For handling cookies
import { useNavigate } from 'react-router-dom'; // For navigation
import './WelcomePage.css';

function WelcomePage() {
  const [preferredNews, setPreferredNews] = useState({});
  const [otherNews, setOtherNews] = useState({});
  const [preferredCategories, setPreferredCategories] = useState([]);
  const [currentIndicesPreferred, setCurrentIndicesPreferred] = useState({});
  const [currentIndicesOther, setCurrentIndicesOther] = useState({});
  const [selectedModel, setSelectedModel] = useState('nb'); // Default model
  const [isLoading, setIsLoading] = useState(false); // Loader state
  const ITEMS_PER_PAGE = 4;

  const navigate = useNavigate(); // Initialize navigate function

  // Fetch news based on the selected model
  useEffect(() => {
    const fetchNews = async () => {
      setIsLoading(true); // Show loader
      try {
        const token = Cookies.get('authToken');
    
        if (!token) {
          console.error('No auth token found!');
          return;
        }
    
        const response = await axios.get(
          `http://127.0.0.1:8000/get_news/?model_name=${selectedModel}`,
          {
            headers: {
              Authorization: `Bearer ${token}`,
            },
          }
        );
    
        const news = response.data.recommended_news || [];
        const categories = response.data.preferedCategories || [];
        setPreferredCategories(categories);
    
        // Corrected category matching
        const preferred = [];
        for (const item of news) {
          for (const cat of categories) {
            const prediction = item.prediction?.trim().toLowerCase();
            const category = cat.trim().toLowerCase();
            if (prediction === category) {
              preferred.push(item);
              break; // Exit the inner loop once a match is found
            }
          }
        }
        
        const others = news.filter(
          (item) =>
            !categories.some((cat) =>
              item.prediction?.trim().toLowerCase() === cat.trim().toLowerCase()
            )
        );
    
        const groupByCategory = (articles) =>
          articles.reduce((acc, item) => {
            const category = item.prediction || 'Uncategorized';
            if (!acc[category]) acc[category] = [];
            acc[category].push(item);
            return acc;
          }, {});
    
        const preferredGrouped = groupByCategory(preferred);
        const otherGrouped = groupByCategory(others);
    
        const initIndices = (groupedNews) =>
          Object.keys(groupedNews).reduce((acc, key) => {
            acc[key] = 0;
            return acc;
          }, {});
    
        setPreferredNews(preferredGrouped);
        setOtherNews(otherGrouped);
        setCurrentIndicesPreferred(initIndices(preferredGrouped));
        setCurrentIndicesOther(initIndices(otherGrouped));
      } catch (error) {
        console.error('Error fetching news:', error);
      } finally {
        setIsLoading(false); // Hide loader
      }
    };    
    fetchNews();
  }, [selectedModel]);

  const handleNext = (category, section) => {
    const setIndices = section === 'preferred' ? setCurrentIndicesPreferred : setCurrentIndicesOther;
    const currentIndices = section === 'preferred' ? currentIndicesPreferred : currentIndicesOther;
    const groupedNews = section === 'preferred' ? preferredNews : otherNews;

    setIndices((prev) => ({
      ...prev,
      [category]: Math.min(
        prev[category] + ITEMS_PER_PAGE,
        groupedNews[category].length - ITEMS_PER_PAGE
      ),
    }));
  };

  const handlePrev = (category, section) => {
    const setIndices = section === 'preferred' ? setCurrentIndicesPreferred : setCurrentIndicesOther;

    setIndices((prev) => ({
      ...prev,
      [category]: Math.max(0, prev[category] - ITEMS_PER_PAGE),
    }));
  };

  const handleModelChange = (e) => {
    setSelectedModel(e.target.value); // Update the selected model
  };

  const handleLogout = () => {
    Cookies.remove('authToken'); // Clear the auth token
    navigate('/login'); // Redirect to login page
  };

  const renderNewsSection = (title, groupedNews, currentIndices, section) => (
    <div className="news-section">
      <h3 className="section-title">{title}</h3>
      {Object.entries(groupedNews).map(([category, news]) => (
        <div key={category} className="category-section">
          <h4 className="category-title">{category}</h4>
          <div className="carousel-container">
            <button
              className="nav-button prev"
              onClick={() => handlePrev(category, section)}
              disabled={currentIndices[category] === 0}
            >
              ←
            </button>
            <div className="news-list">
              {news
                .slice(
                  currentIndices[category],
                  currentIndices[category] + ITEMS_PER_PAGE
                )
                .map((item, index) => (
                  <div className="news-card" key={index}>
                    <img
                      src={item.url_to_image || 'https://via.placeholder.com/300x150'}
                      alt={item.title}
                      className="news-card-image"
                    />
                    <div className="news-card-text">
                      <h3>{item.title}</h3>
                      <p>{item.description}</p>
                    </div>
                    <div className="source-row">
                      <small className="source-text">
                        Source: {item.source_name || 'Unknown'}
                      </small>
                      <a
                        href={item.url}
                        target="_blank"
                        rel="noopener noreferrer"
                        className="read-more-btn"
                      >
                        Read More
                      </a>
                    </div>
                  </div>
                ))}
            </div>
            <button
              className="nav-button next"
              onClick={() => handleNext(category, section)}
              disabled={currentIndices[category] >= news.length - ITEMS_PER_PAGE}
            >
              →
            </button>
          </div>
        </div>
      ))}
    </div>
  );

  return (
    <div className="welcome-container">
      <div className="header">
        <button className="logout-button" onClick={handleLogout}>
          Logout
        </button>
        <h2>News Recommendations</h2>
        <select
          className="model-dropdown"
          value={selectedModel}
          onChange={handleModelChange}
        >
          <option value="nb">Naive Bayes</option>
          <option value="lr">Logistic Regression</option>
          <option value="svm">SVM</option>
          <option value="bert">BERT</option>
        </select>
      </div>

      {isLoading ? (
        <div className="loader">Loading...</div>
      ) : (
        <>
          {renderNewsSection(
            'Recommended Based on Your Choice',
            preferredNews,
            currentIndicesPreferred,
            'preferred'
          )}
          {renderNewsSection(
            'Other Items You Might Be Interested In',
            otherNews,
            currentIndicesOther,
            'other'
          )}
        </>
      )}
    </div>
  );
}

export default WelcomePage;
