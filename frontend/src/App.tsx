import { useState, useEffect } from 'react'
import './App.css'

function App() {
  const [, setData] = useState([])

  useEffect(() => {
    const apiUrl = import.meta.env.VITE_API_URL;
    const fetchData = async () => {
      try {
        const response = await fetch(`${apiUrl}`);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const result = await response.json();
        setData(result);
      } catch (error) {
        console.error('Error fetching data:', error);
      }
    };

    fetchData();
  }, [])

  return (
    <>
      hello world
    </>
  )
}

export default App
