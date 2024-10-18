import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

export default defineConfig({
  plugins: [vue()],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url)),
    },
  },
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000', // 目标服务器的地址
        changeOrigin: true, // 是否改变源地址
        rewrite: path => path.replace(/^\/api/, ''), // 重写路径
      },
    },
  },
})
