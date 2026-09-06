import './style.css'
import { fetchCrimes, fetchNeighbourhoods, fetchCategories, reportCrime } from './api.js'

const app = document.querySelector('#app')

app.innerHTML = `
  <main class="app-shell">
    <header class="top-bar" aria-label="FNSM app header">
      <span class="app-title">FNSM</span>
      <span class="city-label">Toronto Feed</span>
    </header>

    <section class="hero-card" aria-label="Primary neighbourhood alert">
      <p class="hero-kicker">Friendly Neighbourhood Spider-Man</p>
      <h1>Toronto Activity Monitor</h1>
      <p class="hero-copy">Crowd-sourced crime reports across the city, straight from your neighbours.</p>
    </section>

    <section class="panel-grid" aria-label="App sections">
      <article class="panel" id="report-panel">
        <h2>Report a Crime</h2>
        <form id="report-form" class="report-form">
          <input name="title" placeholder="Short title" required minlength="3" maxlength="120" />
          <textarea name="description" placeholder="What happened?" required minlength="10" maxlength="2000" rows="3"></textarea>
          <select name="category" required>
            <option value="" disabled selected>Category</option>
          </select>
          <select name="neighbourhood" required>
            <option value="" disabled selected>Neighbourhood</option>
          </select>
          <input name="reporter_name" placeholder="Your name (optional)" maxlength="80" />
          <button type="submit">Submit report</button>
          <p class="form-status" id="form-status" role="status"></p>
        </form>
      </article>

      <article class="panel" id="crimes-panel">
        <h2>Crimes</h2>
        <ul class="crime-list" id="crime-list">
          <li class="crime-empty">Loading incidents…</li>
        </ul>
      </article>

      <article class="panel" id="districts-panel">
        <h2>Districts</h2>
        <ul class="district-list" id="district-list">
          <li class="crime-empty">Loading neighbourhoods…</li>
        </ul>
      </article>

      <article class="panel">
        <h2>Suit Intel</h2>
        <p>Upgrade and gadget summary placeholder.</p>
      </article>
    </section>
  </main>
`

const crimeListEl = document.querySelector('#crime-list')
const districtListEl = document.querySelector('#district-list')
const formEl = document.querySelector('#report-form')
const statusEl = document.querySelector('#form-status')
const categorySelect = formEl.querySelector('select[name="category"]')
const neighbourhoodSelect = formEl.querySelector('select[name="neighbourhood"]')

function formatCategory(category) {
  return category.replaceAll('_', ' ')
}

function formatTimestamp(isoString) {
  return new Date(isoString).toLocaleString('en-CA', {
    dateStyle: 'medium',
    timeStyle: 'short',
  })
}

function renderCrimes(crimes) {
  if (!crimes.length) {
    crimeListEl.innerHTML = '<li class="crime-empty">No incidents reported yet.</li>'
    return
  }
  crimeListEl.innerHTML = crimes
    .map(
      (crime) => `
        <li class="crime-item">
          <div class="crime-item-head">
            <span class="crime-category">${formatCategory(crime.category)}</span>
            <span class="crime-status">${crime.status.replaceAll('_', ' ')}</span>
          </div>
          <p class="crime-title">${crime.title}</p>
          <p class="crime-meta">${crime.neighbourhood} · ${formatTimestamp(crime.created_at)}</p>
        </li>
      `
    )
    .join('')
}

function renderDistricts(neighbourhoods) {
  districtListEl.innerHTML = neighbourhoods
    .map((name) => `<li class="district-item">${name}</li>`)
    .join('')
}

async function loadCrimes() {
  try {
    const crimes = await fetchCrimes()
    renderCrimes(crimes)
  } catch (err) {
    crimeListEl.innerHTML = `<li class="crime-empty">Couldn't reach the FNSM API. Is the backend running?</li>`
  }
}

async function loadFilters() {
  try {
    const [categories, neighbourhoods] = await Promise.all([
      fetchCategories(),
      fetchNeighbourhoods(),
    ])
    categorySelect.insertAdjacentHTML(
      'beforeend',
      categories.map((c) => `<option value="${c}">${formatCategory(c)}</option>`).join('')
    )
    neighbourhoodSelect.insertAdjacentHTML(
      'beforeend',
      neighbourhoods.map((n) => `<option value="${n}">${n}</option>`).join('')
    )
    renderDistricts(neighbourhoods)
  } catch (err) {
    districtListEl.innerHTML = `<li class="crime-empty">Couldn't reach the FNSM API. Is the backend running?</li>`
  }
}

formEl.addEventListener('submit', async (event) => {
  event.preventDefault()
  const data = Object.fromEntries(new FormData(formEl).entries())
  if (!data.reporter_name) delete data.reporter_name

  statusEl.textContent = 'Submitting…'
  try {
    await reportCrime(data)
    statusEl.textContent = 'Report submitted. Thanks for keeping the neighbourhood safe.'
    formEl.reset()
    await loadCrimes()
  } catch (err) {
    statusEl.textContent = `Couldn't submit report: ${err.message}`
  }
})

loadFilters()
loadCrimes()
