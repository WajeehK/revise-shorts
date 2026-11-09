const C='rs-v3';
const FILES=['./','index.html','style.css','app.js','data/questions.json','manifest.webmanifest','fonts/cn-400.woff2','fonts/cn-700.woff2','icons/icon-192.png','icons/icon-512.png','icons/maskable-192.png','icons/maskable-512.png','icons/apple-touch-icon.png','icons/favicon-32.png','favicon.svg'];
self.addEventListener('install',e=>{e.waitUntil(caches.open(C).then(c=>c.addAll(FILES)));self.skipWaiting();});
self.addEventListener('activate',e=>{e.waitUntil(caches.keys().then(ks=>Promise.all(ks.filter(k=>k!==C).map(k=>caches.delete(k)))));self.clients.claim();});
self.addEventListener('fetch',e=>{if(e.request.method!=='GET')return;e.respondWith(caches.match(e.request,{ignoreSearch:true}).then(r=>r||fetch(e.request).then(res=>{if(res.ok&&new URL(e.request.url).origin===location.origin){const cl=res.clone();caches.open(C).then(c=>c.put(e.request,cl));}return res;}).catch(()=>caches.match('index.html'))));});
