/** @type {import('next').NextConfig} */
const nextConfig = {
  reactStrictMode: true,
  swcMinify: true,

  // Standalone output for optimized Docker images
  output: 'standalone',

  images: {
    domains: ['localhost'],
  },

  // Optimize for production
  compress: true,
  poweredByHeader: false,

  // Production-ready settings
  productionBrowserSourceMaps: false,

  // Disable type checking and linting during build (we'll do this in CI separately)
  typescript: {
    ignoreBuildErrors: true,
  },
  eslint: {
    ignoreDuringBuilds: true,
  },
}

module.exports = nextConfig
