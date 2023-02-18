import React, { useState , useEffect } from "react";
import { HexColorPicker } from "react-colorful";
import "./App.css";

function Calculator() {
  const [input, setInput] = useState("");
  const [result, setResult] = useState("");

  const handleClick = (event) => {
    const value = event.target.value;
    switch (value) {
      case "C":
        setInput("");
        setResult("");
        break;
      case "=":
        try {
          setResult(eval(input).toString());
        } catch (error) {
          setResult("Error");
        }
        break;
      default:
        setInput(input + value);
    }
  };

  return (
    <div className="calculator">
      <input type="text" value={input} onChange={(event) => setInput(event.target.value)} />
      <div className="calculator-button">
        <button value="1" onClick={handleClick}>1</button>
        <button value="2" onClick={handleClick}>2</button>
        <button value="3" onClick={handleClick}>3</button>
        <button value="4" onClick={handleClick}>4</button>
        <button value="5" onClick={handleClick}>5</button>
        <button value="6" onClick={handleClick}>6</button>
        <button value="7" onClick={handleClick}>7</button>
        <button value="8" onClick={handleClick}>8</button>
        <button value="9" onClick={handleClick}>9</button>
        <button value="0" onClick={handleClick}>0</button>
        <button value="." onClick={handleClick}>.</button>
        <button value="C" onClick={handleClick}>C</button>
        <button className="operator" value="/" onClick={handleClick}>/</button>
        <button className="operator" value="*" onClick={handleClick}>*</button>
        <button className="operator" value="-" onClick={handleClick}>-</button>
        <button className="operator" value="+" onClick={handleClick}>+</button>
        <button className="operator" value="=" onClick={handleClick}>=</button>
      </div>
      <input type="text" value={result} readOnly />
    </div>
  );
}

export default function App() {
  const [color, setColor] = useState("#b32aa9");
  const handleColorChange = (newColor) => {
    setColor(newColor);
    document.body.style.backgroundColor = newColor;
  };
  const rainbowColors = [
    "rgb(255, 0, 0)",
    "rgb(0, 255, 0)",
    "rgb(0, 0, 255)",
  ];
  
  let index = 0;

  const handleRainbowClick = () => {
    const delay = 2000;
    const nextIndex = (index + 1) % rainbowColors.length;
    const currentColor = rainbowColors[index];
    const nextColor = rainbowColors[nextIndex];
  
    const currentColorArray = currentColor.slice(4, -1).split(", ").map(Number);
    const nextColorArray = nextColor.slice(4, -1).split(", ").map(Number);
  
    const delta = nextColorArray.map((component, i) => {
      return (component - currentColorArray[i]) / (delay / 10);
    });
  
    let i = 0;
    const applyColor = () => {
      const newColorArray = currentColorArray.map((component, j) => {
        return Math.round(component + (i + 1) * delta[j]);
      });
      const newColor = `rgb(${newColorArray.join(", ")})`;
  
      setColor(newColor);
      document.body.style.backgroundColor = newColor;
  
      i++;
      if (i < delay / 10) {
        setTimeout(applyColor, 10);
      } else {
        index = nextIndex;
      }
    };
  
    applyColor();
  };
  

  const handleRainbowStop = () => {
    setIsRainbowActive(false);
    index = 0;
  };
  
  const [isRainbowActive, setIsRainbowActive] = useState(false);

  useEffect(() => {
    let intervalId;

    if (isRainbowActive) {
      intervalId = setInterval(() => {
        handleRainbowClick();
      }, 1000);
    }

    return () => clearInterval(intervalId);
  }, [isRainbowActive]);

  return (
    <div className="App">
      <Calculator />
      <HexColorPicker color={color} onChange={handleColorChange} />
      <div className="value" style={{ borderLeftColor: color }}>
        Current color is {color}
      </div>
      <div className="colorpicker-button">
        <button onClick={() => handleColorChange("#c6ad23")}>Choose gold</button>
        <button onClick={() => handleColorChange("#556b2f")}>Choose green</button>
        <button onClick={() => handleColorChange("#207bd7")}>Choose blue</button>
        <button onClick={() => handleColorChange("#ff6347")}>Choose coral</button>
        <button onClick={() => handleColorChange("#9c27b0")}>Choose purple</button>
        <button onClick={() => handleColorChange("#ff9800")}>Choose orange</button>
        <button onClick={() => handleColorChange("#03a9f4")}>Choose light blue</button>
        <button onClick={() => handleColorChange("#8bc34a")}>Choose lime</button>
        <button onClick={() => setIsRainbowActive(true)}>Rainbow (seizure warning)</button>
        <button onClick={handleRainbowStop}>Stop</button>
      </div>
    </div>
  );
}