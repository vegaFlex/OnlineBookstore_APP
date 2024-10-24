/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    './templates/**/*.html',
    './**/*.html',
    './static/**/*.js',
  ],
  theme: {
    extend: {
      colors: {
        // Добавяне на персонализирани цветове
        'custom-blue': '#1E3A8A',
        'custom-gray': '#374151',
      },
      borderRadius: {
        // Персонализирани стойности за радиус на ъглите
        'lg': '0.5rem',
      },
      boxShadow: {
        // Персонализирана сянка за елементи
        'card': '0 4px 6px rgba(0, 0, 0, 0.1)',
      },
      height: {
        // Добавяне на персонализирана височина за изображенията
        '64': '16rem',
        'auto': 'auto',
      },
      width: {
        '64': '16rem',
        'full': '100%',
      },
    },
  },
  plugins: [],
}
