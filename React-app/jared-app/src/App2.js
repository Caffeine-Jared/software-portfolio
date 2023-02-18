import React, { useState } from 'react';
import './App2.css';

function App() {
  const [selectedColor, setSelectedColor] = useState('');

  const handleColorClick = (color) => {
    setSelectedColor(color);
  };

  return (
    <div className="App">
      <h1>Color Picker</h1>
      <div className="color-grid">
        <div className="color" style={{ backgroundColor: '#FF4136' }} onClick={() => handleColorClick('#FF4136')}></div>
        <div className="color" style={{ backgroundColor: '#0074D9' }} onClick={() => handleColorClick('#0074D9')}></div>
        <div className="color" style={{ backgroundColor: '#2ECC40' }} onClick={() => handleColorClick('#2ECC40')}></div>
        <div className="color" style={{ backgroundColor: '#FFDC00' }} onClick={() => handleColorClick('#FFDC00')}></div>
        <div className="color" style={{ backgroundColor: '#7FDBFF' }} onClick={() => handleColorClick('#7FDBFF')}></div>
        <div className="color" style={{ backgroundColor: '#B10DC9' }} onClick={() => handleColorClick('#B10DC9')}></div>
      </div>
      {selectedColor && (
        <div className="selected-color">
          Selected Color: <span className="color-value">{selectedColor}</span>
        </div>
      )}
    </div>
  );
}

export default App;

  

