import React, { useEffect, useState } from 'react';

const ShotList = () => {
  const [shots, setShots] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState('');

  useEffect(() => {
    fetch('/api/shots')
      .then(res => {
        if (!res.ok) throw new Error('Network response was not ok');
        return res.json();
      })
      .then(data => {
        setShots(data);
        setLoading(false);
      })
      .catch(err => {
        setError(err.message);
        setLoading(false);
      });
  }, []);

  if (loading) return <p>Loading shots...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <section>
      <h2>Shot Recipes ({shots.length})</h2>
      <ul>
        {shots.map(shot => (
          <li key={shot.id}>
            <div>
              <h3>{shot.title}</h3>
              <p>Duration: {shot.duration}s</p>
              <p>Transition: {shot.transition}</p>
              <p>Theme: {shot.theme}</p>
            </div>
          </li>
        ))}
      </ul>
    </section>
  );
};

export default ShotList;
