import './style.css'

document.querySelector('#app').innerHTML = `
  <main class="app-shell">
    <header class="top-bar" aria-label="FNSM app header">
      <span class="app-title">FNSM</span>
      <span class="city-label">NYC Feed</span>
    </header>

    <section class="hero-card" aria-label="Primary neighborhood alert">
      <p class="hero-kicker">Friendly Neighborhood Spider-Man</p>
      <h1>Local Activity Monitor</h1>
      <p class="hero-copy">Base layout prototype inspired by the in-game FNSM app.</p>
    </section>

    <section class="panel-grid" aria-label="App sections">
      <article class="panel">
        <h2>Requests</h2>
        <p>Citizen requests queue placeholder.</p>
      </article>
      <article class="panel">
        <h2>Crimes</h2>
        <p>Incidents and response status placeholder.</p>
      </article>
      <article class="panel">
        <h2>Districts</h2>
        <p>Borough map and activity heatmap placeholder.</p>
      </article>
      <article class="panel">
        <h2>Suit Intel</h2>
        <p>Upgrade and gadget summary placeholder.</p>
      </article>
    </section>
  </main>
`
