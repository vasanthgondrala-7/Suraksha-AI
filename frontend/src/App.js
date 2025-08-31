import React, { useEffect, useState } from "react";

function App() {
  const [alerts, setAlerts] = useState([]);

  useEffect(() => {
    fetch("http://127.0.0.1:8000/alerts")
      .then((res) => res.json())
      .then((data) => setAlerts(data))
      .catch((err) => console.error("Error fetching alerts:", err));
  }, []);

  return (
    <div style={{ padding: "20px" }}>
      <h1>Suraksha AI</h1>
      <h2>Live Alerts</h2>
      <ul>
        {alerts.map((alert) => (
          <li key={alert.id}>
            <strong>{alert.type}:</strong> {alert.message}
          </li>
        ))}
      </ul>
    </div>
  );
}

export default App;
