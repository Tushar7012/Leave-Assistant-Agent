'use client';

import { useState, useRef, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { sendMessage, ChatMessage } from '@/lib/api';
import MessageBubble from './MessageBubble';
import SuggestionChip from './SuggestionChip';
import LoadingIndicator from './LoadingIndicator';
import Header from './Header';

const SUGGESTIONS = [
    'What is the sick leave policy?',
    'My ID is EMP001. Check my leave balance.',
    'Send an email to manager@company.com requesting leave.',
];

export default function ChatInterface() {
    const [messages, setMessages] = useState<ChatMessage[]>([]);
    const [input, setInput] = useState('');
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState<string | null>(null);
    const messagesEndRef = useRef<HTMLDivElement>(null);
    const inputRef = useRef<HTMLInputElement>(null);

    const scrollToBottom = () => {
        messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    };

    useEffect(() => {
        scrollToBottom();
    }, [messages]);

    const handleSendMessage = async (messageText?: string) => {
        const textToSend = messageText || input.trim();

        if (!textToSend || isLoading) return;

        // Add user message
        const userMessage: ChatMessage = {
            role: 'user',
            content: textToSend,
        };

        setMessages((prev) => [...prev, userMessage]);
        setInput('');
        setIsLoading(true);
        setError(null);

        // Send to API
        try {
            const response = await sendMessage(textToSend);

            if (response.error) {
                setError(response.error);
                return;
            }

            const assistantMessage: ChatMessage = {
                role: 'assistant',
                content: response.response,
            };

            setMessages((prev) => [...prev, assistantMessage]);
        } catch (err) {
            setError('Failed to get response. Please try again.');
        } finally {
            setIsLoading(false);
            inputRef.current?.focus();
        }
    };

    const handleKeyPress = (e: React.KeyboardEvent) => {
        if (e.key === 'Enter' && !e.shiftKey) {
            e.preventDefault();
            handleSendMessage();
        }
    };

    const handleSuggestionClick = (suggestion: string) => {
        handleSendMessage(suggestion);
    };

    return (
        <div className="w-full max-w-4xl h-[85vh] flex flex-col glass rounded-2xl shadow-2xl overflow-hidden">
            <Header />

            {/* Messages Area */}
            <div className="flex-1 overflow-y-auto p-6 space-y-4">
                {messages.length === 0 ? (
                    <div className="flex flex-col items-center justify-center h-full text-center">
                        <motion.div
                            initial={{ scale: 0.8, opacity: 0 }}
                            animate={{ scale: 1, opacity: 1 }}
                            transition={{ duration: 0.5 }}
                            className="space-y-6"
                        >
                            <div className="text-6xl mb-4">👋</div>
                            <h2 className="text-3xl font-bold text-gray-800">
                                How can I help you today?
                            </h2>
                            <p className="text-gray-600 max-w-md">
                                I can check your leave balance, explain policies, or draft emails.
                            </p>

                            <div className="flex flex-wrap gap-3 justify-center mt-8">
                                {SUGGESTIONS.map((suggestion, index) => (
                                    <SuggestionChip
                                        key={index}
                                        text={suggestion}
                                        onClick={() => handleSuggestionClick(suggestion)}
                                        delay={index * 0.1}
                                    />
                                ))}
                            </div>
                        </motion.div>
                    </div>
                ) : (
                    <AnimatePresence>
                        {messages.map((message, index) => (
                            <MessageBubble
                                key={index}
                                message={message}
                                index={index}
                            />
                        ))}
                    </AnimatePresence>
                )}

                {isLoading && <LoadingIndicator />}

                {error && (
                    <motion.div
                        initial={{ opacity: 0, y: 10 }}
                        animate={{ opacity: 1, y: 0 }}
                        className="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded-lg"
                    >
                        <p className="text-sm">{error}</p>
                    </motion.div>
                )}

                <div ref={messagesEndRef} />
            </div>

            {/* Input Area */}
            <div className="border-t border-gray-200 p-4 bg-white/50 backdrop-blur-sm">
                <div className="flex gap-3">
                    <input
                        ref={inputRef}
                        type="text"
                        value={input}
                        onChange={(e) => setInput(e.target.value)}
                        onKeyPress={handleKeyPress}
                        placeholder="Type your message..."
                        disabled={isLoading}
                        className="flex-1 px-4 py-3 border border-gray-300 rounded-xl focus:outline-none focus:ring-2 focus:ring-primary-500 focus:border-transparent transition-all disabled:bg-gray-100 disabled:cursor-not-allowed"
                    />
                    <button
                        onClick={() => handleSendMessage()}
                        disabled={!input.trim() || isLoading}
                        className="px-6 py-3 bg-gradient-to-r from-primary-600 to-primary-700 text-white rounded-xl font-semibold hover:from-primary-700 hover:to-primary-800 disabled:opacity-50 disabled:cursor-not-allowed transition-all transform hover:scale-105 active:scale-95"
                    >
                        Send
                    </button>
                </div>
            </div>
        </div>
    );
}
