// src/components/ChatBot.jsx
import React from 'react';

const ChatBot = () => {
  const questions = [
    'How much water should I drink today?',
    'What are signs of dehydration?',
    'Tips for staying hydrated in hot weather?',
    'How to prevent heat stroke?'
  ];

  return (
    <div>
      <div className="flex items-center mb-6">
        <svg
          className="w-8 h-8 text-blue-600 mr-3"
          fill="none"
          stroke="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path
            strokeLinecap="round"
            strokeLinejoin="round"
            strokeWidth="2"
            d="M9.663 17h4.673M12 3v13.5m0 0l-3.376-3.376M12 16.5l3.376-3.376M21 12c0 4.418-4.03 8-9 8a9 9 0 01-9-8c0-4.418 4.03-8 9-8s9 3.582 9 8z"
          ></path>
        </svg>
        <div>
          <h2 className="text-2xl font-bold text-gray-800">Health Guide</h2>
          <p className="text-gray-500">Your AI hydration assistant</p>
        </div>
      </div>
      <div className="flex flex-col items-center justify-center py-10 text-center">
        <svg
          className="w-24 h-24 text-blue-400 mb-6"
          fill="currentColor"
          viewBox="0 0 24 24"
          xmlns="http://www.w3.org/2000/svg"
        >
          <path d="M12 2C6.477 2 2 6.477 2 12c0 5.253 4.887 9.278 10 12 5.113-2.722 10-6.747 10-12 0-5.523-4.477-10-10-10zm0 18.062c-3.834-2.583-7-6.52-7-10.062C5 7.582 8.582 4 12 4s7 3.582 7 8c0 3.542-3.166 7.479-7 10.062zM12 6c-2.761 0-5 2.239-5 5v3c0 1.657 1.343 3 3 3h4c1.657 0 3-1.343 3-3v-3c0-2.761-2.239-5-5-5z"></path>
        </svg>
        <h3 className="text-2xl font-semibold text-gray-700 mb-3">Welcome to your Health Guide!</h3>
        <p className="text-gray-600 mb-8">
          Ask me anything about hydration, heat safety, or wellness tips.
        </p>
        <p className="text-gray-500 text-lg">Try asking:</p>
      </div>
      <div className="space-y-4">
        {questions.map((question, index) => (
          <div
            key={index}
            className="px-6 py-4 bg-gray-50 border border-gray-200 rounded-lg text-gray-700 cursor-pointer hover:bg-gray-100 transition duration-200"
          >
            {question}
          </div>
        ))}
      </div>
    </div>
  );
};

export default ChatBot;