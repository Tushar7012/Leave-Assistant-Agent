'use client';

import { motion } from 'framer-motion';
import ReactMarkdown from 'react-markdown';
import { Prism as SyntaxHighlighter } from 'react-syntax-highlighter';
import { tomorrow } from 'react-syntax-highlighter/dist/esm/styles/prism';
import { ChatMessage } from '@/lib/api';
import { useState } from 'react';

interface MessageBubbleProps {
    message: ChatMessage;
    index: number;
}

export default function MessageBubble({ message, index }: MessageBubbleProps) {
    const [copied, setCopied] = useState(false);
    const isUser = message.role === 'user';

    const copyToClipboard = () => {
        navigator.clipboard.writeText(message.content);
        setCopied(true);
        setTimeout(() => setCopied(false), 2000);
    };

    return (
        <motion.div
            initial={{ opacity: 0, y: 20 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0, y: -20 }}
            transition={{ duration: 0.3, delay: index * 0.05 }}
            className={`flex ${isUser ? 'justify-end' : 'justify-start'} group`}
        >
            <div
                className={`max-w-[80%] rounded-2xl px-5 py-3 ${isUser
                    ? 'bg-gradient-to-r from-primary-600 to-primary-700 text-white rounded-br-sm'
                    : 'bg-white text-gray-800 shadow-md rounded-bl-sm'
                    }`}
            >
                {isUser ? (
                    <p className="whitespace-pre-wrap break-words">{message.content}</p>
                ) : (
                    <div className="prose prose-sm max-w-none">
                        <ReactMarkdown
                            components={{
                                code(props: any) {
                                    const { node, className, children, ...rest } = props;
                                    const match = /language-(\w+)/.exec(className || '');
                                    const isInline = props.inline;
                                    return !isInline && match ? (
                                        <SyntaxHighlighter
                                            {...rest}
                                            style={tomorrow as any}
                                            language={match[1]}
                                            PreTag="div"
                                        >
                                            {String(children).replace(/\n$/, '')}
                                        </SyntaxHighlighter>
                                    ) : (
                                        <code className={className} {...rest}>
                                            {children}
                                        </code>
                                    );
                                },
                            }}
                        >
                            {message.content}
                        </ReactMarkdown>
                    </div>
                )}

                {!isUser && (
                    <button
                        onClick={copyToClipboard}
                        className="mt-2 text-xs text-gray-500 hover:text-primary-600 opacity-0 group-hover:opacity-100 transition-opacity"
                    >
                        {copied ? '✓ Copied!' : '📋 Copy'}
                    </button>
                )}
            </div>
        </motion.div>
    );
}
