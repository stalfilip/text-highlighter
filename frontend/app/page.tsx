"use client";
import { useState } from 'react';
import axios from 'axios';

export default function Page() {
  const [text, setText] = useState('');
  const [isLoading, setIsLoading] = useState(false);

  const handleTextChange = (event: React.ChangeEvent<HTMLTextAreaElement>) => {
    setText(event.target.value);
  };

  const highlightText = async () => {
    setIsLoading(true);
    try {
      console.log('Highlighting text:', text);  // Add this line
      const response = await axios.post('http://localhost:5000/ingest', { text });
      console.log(response.data);  // Add this line
      setText(response.data.text); 
    } catch (error) {
      console.error('Error highlighting text:', error);
    }
    setIsLoading(false);
  };

  return (
    <div>
      <textarea
        value={text}
        onChange={handleTextChange}
        style={{ width: '100%', height: '300px' }}
      />
      <button onClick={highlightText} disabled={isLoading}>
        {isLoading ? 'Highlighting...' : 'Highlight'}
      </button>
    </div>
  );
}

