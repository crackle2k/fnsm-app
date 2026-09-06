const API_BASE = import.meta.env.VITE_API_BASE ?? 'http://localhost:8000'

async function request(path, options) {
  const res = await fetch(`${API_BASE}${path}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options,
  })
  if (!res.ok) {
    const body = await res.json().catch(() => null)
    throw new Error(body?.detail ? JSON.stringify(body.detail) : `Request failed: ${res.status}`)
  }
  return res.json()
}

export const fetchCrimes = () => request('/api/crimes')

export const fetchNeighbourhoods = () => request('/api/neighbourhoods')

export const fetchCategories = () => request('/api/categories')

export const reportCrime = (payload) =>
  request('/api/crimes', { method: 'POST', body: JSON.stringify(payload) })
