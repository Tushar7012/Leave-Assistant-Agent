'use client';

import { motion } from 'framer-motion';

export default function LoadingIndicator() {
    return (
        <motion.div
            initial={{ opacity: 0, y: 10 }}
            animate={{ opacity: 1, y: 0 }}
            exit={{ opacity: 0 }}
            className="flex justify-start"
        >
            <div className="bg-white rounded-2xl rounded-bl-sm px-5 py-4 shadow-md">
                <div className="flex space-x-2">
                    <motion.div
                        animate={{ scale: [1, 1.2, 1] }}
                        transition={{ duration: 0.6, repeat: Infinity, delay: 0 }}
                        className="w-2 h-2 bg-primary-400 rounded-full"
                    />
                    <motion.div
                        animate={{ scale: [1, 1.2, 1] }}
                        transition={{ duration: 0.6, repeat: Infinity, delay: 0.2 }}
                        className="w-2 h-2 bg-primary-400 rounded-full"
                    />
                    <motion.div
                        animate={{ scale: [1, 1.2, 1] }}
                        transition={{ duration: 0.6, repeat: Infinity, delay: 0.4 }}
                        className="w-2 h-2 bg-primary-400 rounded-full"
                    />
                </div>
            </div>
        </motion.div>
    );
}
