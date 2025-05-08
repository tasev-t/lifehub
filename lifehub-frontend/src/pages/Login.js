import React, { useState } from 'react';
import { Box, TextField, Button, Typography } from '@mui/material';
import { useNavigate } from 'react-router-dom';

export default function Login() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    // TODO: volání login API + uložení tokenů
    navigate('/');
  };

  return (
    <Box sx={{ width: 300, margin: 'auto', mt: 10 }} component="form" onSubmit={handleSubmit}>
      <Typography variant="h5" gutterBottom>Login</Typography>
      <TextField fullWidth label="Email" margin="normal" value={email} onChange={e => setEmail(e.target.value)} />
      <TextField fullWidth label="Password" type="password" margin="normal" value={password} onChange={e => setPassword(e.target.value)} />
      <Button type="submit" variant="contained" fullWidth sx={{ mt: 2 }}>Sign In</Button>
    </Box>
  );
}
