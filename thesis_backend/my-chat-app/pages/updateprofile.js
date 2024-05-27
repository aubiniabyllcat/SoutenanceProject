import React, { useState, useEffect } from 'react';
import axios from 'axios';

const UserProfileForm = () => {
  // États pour stocker les données de l'utilisateur et les données modifiées
  const [userData, setUserData] = useState({
    bio: ''
  });
  const [updatedData, setUpdatedData] = useState({
    bio: ''
  });

  // Fonction pour charger les données de l'utilisateur depuis l'API
  const fetchUserData = async () => {
    try {
      const accessToken = localStorage.getItem('accessToken');
      if (!accessToken) {
        console.error('User not authenticated');
        return;
      }

      const response = await axios.get('http://127.0.0.1:8000/profile/', {
        headers: {
          'Authorization': `Bearer ${accessToken}`
        }
      });
      const userDataFromAPI = response.data;
      console.log(userDataFromAPI);
      setUserData(userDataFromAPI);
    } catch (error) {
      console.error('Failed to fetch user data:', error);
    }
  };

  // Effet pour charger les données de l'utilisateur lors du chargement initial du composant
  useEffect(() => {
    fetchUserData();
  }, []);

  // Fonction pour gérer les changements dans le formulaire
  const handleChange = (e) => {
    const { name, value } = e.target;
    setUpdatedData(prevData => ({
      ...prevData,
      [name]: value
    }));
  };

  // Fonction pour soumettre les données modifiées
  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // Envoyer les données modifiées à l'API pour mise à jour
      const accessToken = localStorage.getItem('accessToken');
      if (!accessToken) {
        console.error('User not authenticated');
        return;
      }

      await axios.patch('http://127.0.0.1:8000/profile/', updatedData, {
        headers: {
          'Authorization': `Bearer ${accessToken}`
        }
      });
      // Rafraîchir les données de l'utilisateur après la mise à jour
      fetchUserData();
      // Réinitialiser les données modifiées
      setUpdatedData({
        bio: ''
      });
    } catch (error) {
      console.error('Failed to update user data:', error);
    }
  };

  // Rendu du composant
  return (
    <div>
      <h2>Modifier le profil utilisateur</h2>
      <form onSubmit={handleSubmit}>
        <div>
          <label htmlFor="bio">Biographie :</label>
          <input type="text" id="bio" name="bio" value={updatedData.bio || userData.bio} onChange={handleChange} />
        </div>
        
        <button type="submit">Enregistrer les modifications</button>
      </form>
    </div>
  );
};

export default UserProfileForm;
