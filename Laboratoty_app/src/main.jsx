import React from 'react'
import ReactDOM from 'react-dom/client'
import App from './App.jsx'
import './index.css'
import Try from './try.jsx'
import MyApi from './api.jsx'


ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <App />
    <Try />
    <MyApi/>
  </React.StrictMode>,
)
