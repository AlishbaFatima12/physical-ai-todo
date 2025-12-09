'use client'
import { useEffect, useState } from 'react'
import { useRouter, useSearchParams } from 'next/navigation'
import { useAuth } from '@/contexts/AuthContext'

export default function GitHubCallbackPage() {
  const router = useRouter()
  const searchParams = useSearchParams()
  const { refreshUser } = useAuth()
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    const handleCallback = async () => {
      const code = searchParams.get('code')
      const error = searchParams.get('error')

      if (error) {
        setError(`GitHub authorization failed: ${error}`)
        setTimeout(() => router.push('/auth/signin'), 3000)
        return
      }

      if (!code) {
        setError('No authorization code received')
        setTimeout(() => router.push('/auth/signin'), 3000)
        return
      }

      try {
        // Send code to backend
        const response = await fetch('http://localhost:8000/api/v1/auth/github/callback', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          credentials: 'include',
          body: JSON.stringify({ code })
        })

        if (!response.ok) {
          const errorData = await response.json()
          throw new Error(errorData.detail || 'GitHub authentication failed')
        }

        // Refresh user data
        await refreshUser()

        // Redirect to dashboard
        router.push('/dashboard')
      } catch (err) {
        setError(err instanceof Error ? err.message : 'Authentication failed')
        setTimeout(() => router.push('/auth/signin'), 3000)
      }
    }

    handleCallback()
  }, [searchParams, router, refreshUser])

  if (error) {
    return (
      <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-900 via-purple-900 to-violet-900">
        <div className="glass-morphism p-8 rounded-2xl max-w-md">
          <div className="text-center">
            <div className="text-6xl mb-4">❌</div>
            <h1 className="text-2xl font-bold text-white mb-2">Authentication Failed</h1>
            <p className="text-gray-300 mb-4">{error}</p>
            <p className="text-sm text-gray-400">Redirecting to sign in...</p>
          </div>
        </div>
      </div>
    )
  }

  return (
    <div className="min-h-screen flex items-center justify-center bg-gradient-to-br from-gray-900 via-purple-900 to-violet-900">
      <div className="glass-morphism p-8 rounded-2xl">
        <div className="text-center">
          <div className="animate-spin text-6xl mb-4">⚙️</div>
          <h1 className="text-2xl font-bold text-white mb-2">Completing GitHub Sign In...</h1>
          <p className="text-gray-300">Please wait while we authenticate you.</p>
        </div>
      </div>
    </div>
  )
}
