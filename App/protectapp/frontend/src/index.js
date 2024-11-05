// src/index.js
import React from 'react';
<<<<<<< HEAD
import ReactDOM from 'react-dom/client'; // Importa desde 'react-dom/client'
=======
<<<<<<< HEAD
import ReactDOM from 'react-dom/client'; // Importa desde 'react-dom/client'
=======
import ReactDOM from 'react-dom';
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
import { BrowserRouter as Router } from 'react-router-dom';
import App from './App';
import './css/App.css';

<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
// Utiliza createRoot en lugar de ReactDOM.render
const root = ReactDOM.createRoot(document.getElementById('root'));

root.render(
  <React.StrictMode>
    <Router>
      <App />
    </Router>
  </React.StrictMode>
<<<<<<< HEAD
=======
=======
ReactDOM.render(
  <Router>
    <App />
  </Router>,
  document.getElementById('root')
>>>>>>> 93377ebfbcd26d14f6f4e8a0b8a9a9d138f8e145
>>>>>>> 2f5224bd1b0c95acdfcd897b3ce2d8a61d63705f
);
