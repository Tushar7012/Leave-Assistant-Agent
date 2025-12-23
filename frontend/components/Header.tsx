'use client';

import { motion } from 'framer-motion';

export default function Header() {
    return (
        <div className="border-b border-gray-200 bg-white/50 backdrop-blur-sm px-6 py-4">
            <div className="flex items-center justify-between">
                <motion.div
                    initial={{ x: -20, opacity: 0 }}
                    animate={{ x: 0, opacity: 1 }}
                    transition={{ duration: 0.5 }}
                    className="flex items-center space-x-3"
                >
                    <div className="w-10 h-10 bg-gradient-to-br from-primary-500 to-primary-700 rounded-full flex items-center justify-center">
                        <span className="text-white text-xl">🤖</span>
                    </div>
                    <div>
                        <h1 className="text-xl font-bold text-gray-800">
                            Multi-Agent Leave Assistant
                        </h1>
                        <p className="text-xs text-gray-500">Powered by AI</p>
                    </div>
                </motion.div>

                <motion.div
                    initial={{ scale: 0 }}
                    animate={{ scale: 1 }}
                    transition={{ delay: 0.3, type: 'spring', stiffness: 200 }}
                    className="flex items-center space-x-2"
                >
                    <span className="relative flex h-3 w-3">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-green-400 opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-3 w-3 bg-green-500"></span>
                    </span>
                    <span className="text-sm text-gray-600 font-medium">Online</span>
                </motion.div>
            </div>
        </div>
    );
}
