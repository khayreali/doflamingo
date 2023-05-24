import React, { useState } from 'react';

const App = () => {
  const [smiles, setSmiles] = useState('');
  const [imgSrc, setImgSrc] = useState('');

  const onSubmit = async (event) => {
    event.preventDefault();

    const res = await fetch('http://localhost:5000/generate_pdf', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ smiles })
    });
    const blob = await res.blob();
    setImgSrc(URL.createObjectURL(blob));
  };

  return (
    <div>
      <h1>SMILES Viewer</h1>
      <form onSubmit={onSubmit}>
        <label>Enter a SMILES string: </label> 
        <input value={smiles} onChange={e => setSmiles(e.target.value)} />
        <button type="submit">View Structure</button>
      </form>
      {imgSrc && <img src={imgSrc} alt="Structure" />}
    </div>
  );
};

export default App;
