import React from 'react';

function Footer({ footerText }) {
  return (
    <footer className="bg-gray-900 text-gray-300 text-center py-4 mt-6">
      <p className="text-sm">{footerText}</p>
    </footer>
  );
}

export default Footer;
