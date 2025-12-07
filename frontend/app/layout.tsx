import type { Metadata } from 'next'
import './globals.css'

export const metadata: Metadata = {
  title: 'Physical AI Todo - Task Management',
  description: 'Modern task management with AI-powered features and multi-language support',
}

export default function RootLayout({
  children,
}: {
  children: React.ReactNode
}) {
  return (
    <html lang="en">
      <head>
        <link rel="icon" href="/favicon.ico" />
      </head>
      <body>{children}</body>
    </html>
  )
}
