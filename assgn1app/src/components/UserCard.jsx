import React from 'react';

function UserCard({ name, email, onViewProfile }) {
  return (
    <div className="bg-white rounded-xl shadow hover:shadow-xl transition-all duration-300 p-5 border border-gray-100 hover:border-indigo-300 cursor-pointer">
      <h2 className="text-lg font-semibold text-gray-800">{name}</h2>
      <p className="text-gray-500 text-sm mt-1">{email}</p>
      <button 
        onClick={onViewProfile}
        className="mt-4 bg-indigo-600 text-white py-1 px-3 rounded hover:bg-indigo-700 transition"
      >
        View Profile
      </button>
    </div>
  );
}

export default UserCard;
