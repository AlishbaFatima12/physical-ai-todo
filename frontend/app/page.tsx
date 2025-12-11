'use client'
import { useEffect } from 'react'
import { useRouter } from 'next/navigation'
import { useAuth } from '@/contexts/AuthContext'
import { motion } from 'framer-motion'

export default function HomePage() {
  const router = useRouter()
  const { user, isLoading } = useAuth()

  useEffect(() => {
    if (!isLoading) {
      if (user) {
        // User is authenticated, go to dashboard
        router.push('/dashboard')
      } else {
        // User is not authenticated, go to landing
        router.push('/landing')
      }
    }
  }, [user, isLoading, router])

  // Show loading spinner while checking auth
  return (
    <div className="min-h-screen bg-gradient-to-br from-gray-900 via-blue-900 to-purple-900 flex items-center justify-center">
      <motion.div
        initial={{ opacity: 0, scale: 0.9 }}
        animate={{ opacity: 1, scale: 1 }}
        className="text-center"
      >
        <div className="text-8xl mb-8">✓</div>
        <h1 className="text-4xl font-bold text-white mb-4">FlowTask</h1>
        <div className="inline-block w-8 h-8 border-4 border-white border-opacity-20 border-t-white rounded-full animate-spin" />
      </motion.div>
    </div>
  )
}
