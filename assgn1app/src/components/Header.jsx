import React from 'react';

function Header({ title }) {
  return (
    <header className="bg-indigo-600 text-white shadow-lg">
      <div className="container mx-auto py-4 px-6 text-center">
        <h1 className="text-3xl font-bold tracking-wide">{title}</h1>
        <p className="text-sm text-indigo-200 mt-1">
          Browse and explore the user list
        </p>
      </div>
    </header>
  );
}

export default Header;
