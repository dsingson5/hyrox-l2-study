/* Coach Eye service worker — the app shell loads with no network.
   Clips are NOT cached here: they live in IndexedDB (imported on-device or
   pulled from the user's Drive), so /clips/ and range requests pass straight
   through. manifest.json is also never cached — boot() must see the server's
   real answer (or a clean failure that routes to the IndexedDB fallback);
   a cached copy would fake "server mode" after the local server stops.
   Cross-origin calls (gist sync, Drive, Anthropic) pass through untouched
   and simply fail offline, which the page handles.
   BUMP VERSION whenever any shell file changes, together with the BUILD
   stamp in index.html (and keep the knowledge.js ?v= pin below in step with
   the <script> tag there). */
var VERSION = 'coach-eye-v9';
var SHELL_CRITICAL = [
  './',
  'index.html',
  'knowledge.js?v=3',
  'app.webmanifest'
];
var SHELL_EXTRA = [
  'icon-192.png',
  'icon-512.png',
  'icon-180.png'
];

self.addEventListener('install', function (ev) {
  ev.waitUntil(
    caches.open(VERSION).then(function (c) {
      /* cache:'no-cache' revalidates against the server — without it a
         VERSION bump can precache a stale shell straight out of the HTTP
         cache (GitHub Pages serves max-age=600) */
      var fresh = function (u) { return new Request(u, { cache: 'no-cache' }); };
      return c.addAll(SHELL_CRITICAL.map(fresh)).then(function () {
        /* icons are cosmetic: a missing one must not kill offline support */
        return Promise.all(SHELL_EXTRA.map(function (u) {
          return c.add(fresh(u)).catch(function (e) {
            console.warn('[coach-eye sw] optional shell file skipped:', u, e);
          });
        }));
      });
    }).catch(function (e) {
      console.error('[coach-eye sw] install failed:', e);
      throw e;
    }).then(function () { return self.skipWaiting(); })
  );
});

self.addEventListener('activate', function (ev) {
  ev.waitUntil(
    caches.keys().then(function (keys) {
      return Promise.all(keys.map(function (k) {
        return k === VERSION ? null : caches.delete(k);
      }));
    }).then(function () { return self.clients.claim(); })
  );
});

self.addEventListener('fetch', function (ev) {
  var req = ev.request;
  if (req.method !== 'GET') return;
  var url = new URL(req.url);
  if (url.origin !== self.location.origin) return;
  if (url.pathname.indexOf('/clips/') !== -1) return;
  if (url.pathname.split('/').pop() === 'manifest.json') return;
  if (req.headers.get('range')) return;
  ev.respondWith(
    /* network first keeps the app fresh when online; every good response is
       recached so it is there the next time the network is not */
    fetch(req).then(function (res) {
      if (res && res.ok && res.type === 'basic') {
        var copy = res.clone();
        caches.open(VERSION).then(function (c) { c.put(req, copy); });
      }
      return res;
    }).catch(function () {
      return caches.match(req).then(function (hit) {
        if (hit) return hit;
        /* a version-bumped query (knowledge.js?v=4) still gets the last
           cached copy rather than nothing */
        var base = url.pathname.split('/').pop() || './';
        return caches.match(base, { ignoreSearch: true }).then(function (loose) {
          if (loose) return loose;
          if (req.mode === 'navigate') return caches.match('index.html');
          return Response.error();
        });
      });
    })
  );
});
