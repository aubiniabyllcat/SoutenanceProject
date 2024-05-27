import { useState } from 'react';
import { useRouter } from 'next/router';

const ProfileImageUpload = ({ customerId, fetchCustomer }) => {

  const router = useRouter();
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  const handleUpload = async () => {
    const accessToken = localStorage.getItem('accessToken');

    if (!accessToken) {
      console.error('User not authenticated');
      return;
    }

    const formData = new FormData();
    formData.append('images', selectedFile);

    try {
      const response = await fetch(`http://127.0.0.1:8000/profile/images/{image_name}`, {
        method: 'POST',
        headers: {
          'Authorization': `Bearer ${accessToken}`, // Ajouter le token JWT dans l'en-tête
        },
        body: formData,
      });

      if (response.ok) {
        router.push('/login');
      } else {
        console.error('Failed to upload image');
      }
    } catch (error) {
      console.error('Upload error:', error.message);
    }
  };

  return (
    <div>
      <h2>Upload Profile Picture</h2>
      <input type="file" onChange={handleFileChange} />
      <button onClick={handleUpload} disabled={!selectedFile}>
        Upload
      </button>
    </div>
  );
};

export default ProfileImageUpload;
