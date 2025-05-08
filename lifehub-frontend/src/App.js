import React from 'react';
import { Routes, Route, Navigate } from 'react-router-dom';
import Layout from './components/Layout';
import Login from './pages/Login';
import Dashboard from './pages/Dashboard';

function App() {
  const isAuthenticated = false; // TODO: reálná kontrola JWT

  return (
    <Routes>
      <Route path="/login" element={<Login />} />
      <Route
        path="/"
        element={
          isAuthenticated
            ? <Layout><Dashboard /></Layout>
            : <Navigate to="/login" replace />
        }
      />
    </Routes>
  );
}

export default App;
