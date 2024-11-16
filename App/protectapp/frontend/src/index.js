// src/index.js
import React from 'react';
import ReactDOM from 'react-dom/client'; // Importa desde 'react-dom/client'
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';
import './css/App.css';

// Utiliza createRoot en lugar de ReactDOM.render
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>
);
