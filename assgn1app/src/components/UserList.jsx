import React from 'react';
import UserCard from './UserCard.jsx';

function UserList({ users, onUserSelect }) {
  return (
    <div className="grid gap-6 grid-cols-1 sm:grid-cols-2 lg:grid-cols-3">
      {users.map((user, index) => (
        <UserCard 
          key={index} 
          name={user.name} 
          email={user.email} 
          onViewProfile={() => onUserSelect(user)} 
        />
      ))}
    </div>
  );
}

export default UserList;
