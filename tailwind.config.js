/** @type {import('tailwindcss').Config} */
module.exports = {
  purge: ['./index.html', './src/**/*.{vue,js,ts,jsx,tsx}'],
  darkMode: false, // or 'media' or 'class'
  theme: {
    extend: {
      colors: {
        primary: {
          100: '#000',
        }
      }
    },
    container: {
      center: true,
      padding: '2rem',
    }
  },
  variants: {
    extend: {},
  },
  plugins: [],
}