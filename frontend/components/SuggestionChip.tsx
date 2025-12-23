'use client';

import { motion } from 'framer-motion';

interface SuggestionChipProps {
    text: string;
    onClick: () => void;
    delay?: number;
}

export default function SuggestionChip({ text, onClick, delay = 0 }: SuggestionChipProps) {
    return (
        <motion.button
            initial={{ opacity: 0, scale: 0.8 }}
            animate={{ opacity: 1, scale: 1 }}
            transition={{ delay, duration: 0.3 }}
            whileHover={{ scale: 1.05, y: -2 }}
            whileTap={{ scale: 0.95 }}
            onClick={onClick}
            className="px-4 py-2 bg-white text-primary-700 border-2 border-primary-200 rounded-full text-sm font-medium hover:bg-primary-50 hover:border-primary-300 transition-all shadow-sm hover:shadow-md"
        >
            {text}
        </motion.button>
    );
}
