module.exports = {
  async redirects() {
    return [
      {
        source: '/',
        destination: '/article/helloworld',
        permanent: true,
      },
    ]
  },
  distDir: 'build',
  target: 'serverless',
}