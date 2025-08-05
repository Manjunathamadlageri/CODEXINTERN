import React, { useState } from 'react';
import Header from './components/Header.jsx';
import UserList from './components/UserList.jsx';
import UserDetails from './components/UserDetails.jsx';
import Footer from './components/Footer.jsx';

function App() {
  const [selectedUser, setSelectedUser] = useState(null);

  const users = [
    { name: 'Manjunath Madlageri', email: 'madlagerimanju8141@gmail.com', bio: 'AI & Data Science Enthusiast' },
    { name: 'John Doe', email: 'john@example.com', bio: 'Full Stack Developer' },
    { name: 'Jane Smith', email: 'jane@example.com', bio: 'UX/UI Designer' }
  ];

  return (
    <div className="min-h-screen flex flex-col bg-gradient-to-b from-gray-50 to-gray-200">
      <Header title="User Directory" />
      <main className="flex-grow container mx-auto px-4 py-6">
        {selectedUser ? (
          <UserDetails user={selectedUser} goBack={() => setSelectedUser(null)} />
        ) : (
          <UserList users={users} onUserSelect={setSelectedUser} />
        )}
      </main>
      <Footer footerText="© 2025 User Directory. All rights reserved." />
    </div>
  );
}

export default App;
