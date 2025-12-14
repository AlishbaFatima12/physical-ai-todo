import { redirect } from 'next/navigation'

export default function HomePage() {
  // Always redirect to landing page
  // Users will be redirected to dashboard after login
  redirect('/landing')
}
