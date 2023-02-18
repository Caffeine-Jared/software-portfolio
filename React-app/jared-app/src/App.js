import React, { useState } from "react";
import "./App.css";

function App() {
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
    <div className="App">
      <div className="calculator">
        <input type="text" value={input} onChange={(event) => setInput(event.target.value)} />
        <div className="buttons">
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
    </div>
  );
}

export default App;

