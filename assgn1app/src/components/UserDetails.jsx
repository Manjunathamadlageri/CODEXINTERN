import React from 'react';

function UserDetails({ user, goBack }) {
  return (
    <div className="bg-white shadow-lg rounded-xl p-6 border border-gray-200">
      <h2 className="text-2xl font-bold text-gray-800 mb-2">{user.name}</h2>
      <p className="text-gray-600 mb-4">{user.email}</p>
      <p className="text-gray-500">{user.bio}</p>
      <button 
        onClick={goBack} 
        className="mt-6 bg-gray-600 text-white py-1 px-4 rounded hover:bg-gray-700"
      >
        Back to List
      </button>
    </div>
  );
}

export default UserDetails;
