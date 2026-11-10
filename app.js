'use strict';
const VERSION='v11';
const $=s=>document.querySelector(s);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const shuffle=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]]}return a};
const PAL=['purple','green','orange','blue'];
const SUBJ_COL={maths:'purple',physics:'blue',chemistry:'orange'};
let DB=null, TOPICS={};
const store={get(k,d){try{return JSON.parse(localStorage.getItem('rs.'+k))??d}catch(e){return d}},set(k,v){localStorage.setItem('rs.'+k,JSON.stringify(v))},del(k){localStorage.removeItem('rs.'+k)}};
// ---------- settings, theme, migrations
const DEF={deg:true,theme:'system',ts:1,shuffle:true,explain:'now',sound:false,haptics:true,goal:20,qn:10,autoCalc:true};
let settings=Object.assign({},DEF,store.get('settings',{}));
// Topic ids were kept stable in v11 (sections were re-grouped, ids unchanged). Any future id renames go in this map and are applied once.
const ID_MIGRATIONS={};
(function migrate(){const v=store.get('schema',1);if(v>=3)return;const p=store.get('progress',{}),np={};
 for(const k in p){const [id,n]=k.split(':');const nid=ID_MIGRATIONS[id]||id;np[n?nid+':'+n:nid]=p[k]}
 store.set('progress',np);store.set('schema',3)})();
const mq=window.matchMedia?matchMedia('(prefers-color-scheme: dark)'):{matches:false};
function isDark(){return settings.theme==='dark'||(settings.theme==='system'&&mq.matches)}
function applyTheme(){const r=document.documentElement;r.dataset.theme=isDark()?'dark':'light';r.style.setProperty('--ts',settings.ts);document.querySelectorAll('meta[name=theme-color]').forEach(m=>m.content=isDark()?'#000000':'#ffffff')}
if(mq.addEventListener)mq.addEventListener('change',()=>{applyTheme()});
applyTheme();
function saveSettings(){store.set('settings',settings);applyTheme();render()}
function setOpt(k,v){settings[k]=v;saveSettings()}
const prog=()=>store.get('progress',{});
// ---------- daily goal, streak, resume
const dkey=d=>d.getFullYear()+'-'+String(d.getMonth()+1).padStart(2,'0')+'-'+String(d.getDate()).padStart(2,'0');
const todayN=()=>store.get('days',{})[dkey(new Date())]||0;
function logAnswer(){const a=store.get('days',{});const k=dkey(new Date());a[k]=(a[k]||0)+1;store.set('days',a)}
function streak(){const a=store.get('days',{}),g=settings.goal;const d=new Date();if((a[dkey(d)]||0)<g)d.setDate(d.getDate()-1);let n=0;while((a[dkey(d)]||0)>=g){n++;d.setDate(d.getDate()-1)}return n}
function bestStreak(){const a=store.get('days',{}),g=settings.goal;const ks=Object.keys(a).filter(k=>a[k]>=g).sort();let best=0,run=0,prev=null;
 ks.forEach(k=>{const d=new Date(k+'T12:00:00');if(prev&&(d-prev)/864e5<1.5)run++;else run=1;best=Math.max(best,run);prev=d});return Math.max(best,streak())}
function saveResume(){if(Q&&Q.tid&&Q.i<Q.qs.length&&Q.ans.some(Boolean))store.set('resume',{Q,t:Date.now()});}
function clearResume(){store.del('resume')}
// ---------- feedback (sound / haptics)
let AC=null;
function beep(ok){if(settings.haptics&&navigator.vibrate)navigator.vibrate(ok?18:[30,50,30]);if(!settings.sound)return;
 try{AC=AC||new (window.AudioContext||window.webkitAudioContext)();const t=AC.currentTime;(ok?[660,880]:[300,220]).forEach((f,i)=>{const o=AC.createOscillator(),g=AC.createGain();o.frequency.value=f;o.type='sine';g.gain.setValueAtTime(.0001,t+i*.09);g.gain.exponentialRampToValueAtTime(.18,t+i*.09+.01);g.gain.exponentialRampToValueAtTime(.0001,t+i*.09+.16);o.connect(g).connect(AC.destination);o.start(t+i*.09);o.stop(t+i*.09+.18)})}catch(e){}}
function toast(msg){let t=$('#toast');if(!t){t=document.createElement('div');t.id='toast';document.body.appendChild(t)}t.textContent=msg;t.className='show';clearTimeout(t._h);t._h=setTimeout(()=>t.className='',2600)}
const ICON={
home:'<svg viewBox="0 0 24 24"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/></svg>',
play:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M10 8l6 4-6 4z" class="fillc"/></svg>',
trophy:'<svg viewBox="0 0 24 24"><path d="M8 4h8v5a4 4 0 0 1-8 0zM8 6H4a4 4 0 0 0 4 4M16 6h4a4 4 0 0 1-4 4M12 13v4M8 20h8M9 17h6"/></svg>',
gear:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>',
calc:'<svg viewBox="0 0 24 24"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h1M12 12h1M16 12h0M8 16h1M12 16h1M16 12v4"/></svg>',
book:'<svg viewBox="0 0 24 24"><path d="M4 5a2 2 0 0 1 2-2h13v16H6a2 2 0 0 0-2 2zM4 21V5M8 7h7M8 11h7"/></svg>',
back:'<svg viewBox="0 0 24 24"><path d="M15 5l-7 7 7 7"/></svg>',
up:'<svg viewBox="0 0 24 24"><path d="M6 14l6-6 6 6"/></svg>'};
function tabs(on){return ''}
// ---- v13 persistent liquid-glass dock (ported from news-reel: spring physics, stretch while moving, drag to scrub) ----
const DOCK_T=[['home','#/','Home'],['play','#/videos','Videos'],['trophy','#/scores','Scores'],['gear','#/settings','Settings']];
const RMQ=window.matchMedia?matchMedia('(prefers-reduced-motion: reduce)'):{matches:false};
const vib=n=>{if(navigator.vibrate&&navigator.userActivation&&navigator.userActivation.hasBeenActive)try{navigator.vibrate(n)}catch(_){}};
let dock=null,bub=null,jel=null,tbs=[],dockI=-1,bw=0,press=1,ddrag=null,moved=0;
function spring(o){const s={x:0,v:0,target:0,k:o.k,c:o.c,on:o.on,raf:0,set(t,instant){s.target=t;if(instant||RMQ.matches){if(s.raf){cancelAnimationFrame(s.raf);s.raf=0}s.x=t;s.v=0;s.on(s.x,0);return}
  if(!s.raf){let last=performance.now();const f=now=>{const dt=Math.min(.032,(now-last)/1000);last=now;const a=-s.k*(s.x-s.target)-s.c*s.v;s.v+=a*dt;s.x+=s.v*dt;s.on(s.x,s.v);
  if(Math.abs(s.v)<2&&Math.abs(s.x-s.target)<.3){s.x=s.target;s.v=0;s.on(s.x,0);s.raf=0;if(s.settle)s.settle();return}s.raf=requestAnimationFrame(f)};s.raf=requestAnimationFrame(f)}}};return s}
const slotX=i=>tbs[i]?tbs[i].offsetLeft:0;
function dpaint(x,v){const st=RMQ.matches?0:Math.min(.34,Math.abs(v)/2400);moved=Math.max(moved,Math.abs(v));
 bub.style.transform=`translate3d(${x.toFixed(2)}px,0,0) scale(${((1+st)*press).toFixed(3)},${((1-st*.42)*press).toFixed(3)})`;
 const c=x+bw/2;tbs.forEach(b=>b.classList.toggle('on',dockI>=0&&c>=b.offsetLeft&&c<b.offsetLeft+b.offsetWidth))}
const bs=spring({k:380,c:26,on:(x,v)=>dpaint(x,v)});
bs.settle=()=>{if(moved>600&&!RMQ.matches&&!ddrag){jel.classList.remove('jelly');void jel.offsetWidth;jel.classList.add('jelly')}moved=0};
function sizeBubble(){if(!dock)return;bw=tbs[0].offsetWidth;bub.style.width=bw+'px';bs.set(slotX(Math.max(0,dockI)),true)}
const rubber=x=>{const a=slotX(0),b=slotX(tbs.length-1);return x<a?a-Math.pow(a-x,.7):x>b?b+Math.pow(x-b,.7):x};
const nearest=x=>{let best=0,d=1e9;tbs.forEach((b,i)=>{const dd=Math.abs(b.offsetLeft-x);if(dd<d){d=dd;best=i}});return best};
function hashTab(h){if(h==='#/videos')return 1;if(h==='#/scores')return 2;if(h==='#/settings')return 3;if(h==='#/'||h===''||h.startsWith('#/s/')||h.startsWith('#/t/'))return 0;return -1}
function dockGo(i){const prev=dockI;dockI=i;dock.classList.toggle('off',i<0);
 tbs.forEach((b,k)=>{if(k===i)b.setAttribute('aria-current','page');else b.removeAttribute('aria-current')});
 if(i<0){dpaint(bs.x,0);return}
 if(prev<0||!bw){if(!bw)sizeBubble();bs.set(slotX(i),prev<0&&bs.x===0?true:false)}else bs.set(slotX(i))}
function mountDock(){if(dock)return;dock=document.createElement('nav');dock.className='tabs off';dock.id='dock';dock.setAttribute('aria-label','Tabs');
 dock.innerHTML='<span class="dpill" aria-hidden="true"><i></i></span>'+DOCK_T.map(([ic,h,l],k)=>`<button type="button" data-k="${k}" aria-label="${l}">${ICON[ic]}<span>${l}</span></button>`).join('');
 document.body.appendChild(dock);bub=dock.querySelector('.dpill');jel=bub.querySelector('i');tbs=[...dock.querySelectorAll('button')];
 dock.addEventListener('pointerdown',e=>{if(e.button>0)return;try{dock.setPointerCapture(e.pointerId)}catch(_){}const r=dock.getBoundingClientRect();ddrag={left:r.left};press=1.08;dock.classList.add('drag');bs.set(rubber(e.clientX-r.left-bw/2))});
 dock.addEventListener('pointermove',e=>{if(ddrag)bs.set(rubber(e.clientX-ddrag.left-bw/2))});
 const end=e=>{if(!ddrag)return;const i=nearest(bs.target);ddrag=null;press=1;dock.classList.remove('drag');
  if(e.type==='pointercancel'){bs.set(slotX(dockI));return}
  const h=DOCK_T[i][1];if(i!==dockI)vib(6);if((location.hash||'#/')!==h){dockGo(i);location.hash=h}else{bs.set(slotX(i));if(i===dockI)window.scrollTo({top:0,behavior:RMQ.matches?'auto':'smooth'})}};
 dock.addEventListener('pointerup',end);dock.addEventListener('pointercancel',end);
 dock.addEventListener('keydown',e=>{if(e.key==='Enter'||e.key===' '){const b=e.target.closest('button');if(b){e.preventDefault();location.hash=DOCK_T[+b.dataset.k][1]}}});
 addEventListener('resize',()=>{bw=0;sizeBubble()});if(document.fonts&&document.fonts.ready)document.fonts.ready.then(()=>{bw=0;sizeBubble()});
 window.__dock={go:dockGo,bs}}
function subjStats(s){const p=prog();let n=0,done=0,sum=0;s.sections.forEach(sec=>sec.topics.forEach(t=>{n++;const b=[1,2,3].map(k=>p[t.id+':'+k]).filter(Boolean);if(b.length){done++;sum+=Math.max(...b.map(x=>x.best))}}));return{n,done,avg:done?Math.round(sum/done):0,cover:Math.round(done/n*100)}}
// ---------- screens
function resumeBar(){const r=store.get('resume',null);if(r&&r.Q&&TOPICS[r.Q.tid]){const q=r.Q;return `<button class="bar b-yellow cont" onclick="resumeQuiz()"><span><small>Continue where you left off</small>${esc(q.title)} · question ${Math.min(q.i+1,q.qs.length)} of ${q.qs.length}</span><span class="arrow">➜</span></button>`}
 const n=store.get('lastNotes',null);if(n&&TOPICS[n.id]){return `<button class="bar b-yellow cont" onclick="location.hash='#/n/${n.id}'"><span><small>Continue where you left off</small>Revision notes: ${esc(TOPICS[n.id].title)} · ${Math.round((n.f||0)*100)}% read</span><span class="arrow">➜</span></button>`}
 const l=store.get('lastTopic',null);if(l&&TOPICS[l]){return `<button class="bar b-yellow cont" onclick="location.hash='#/t/${l}'"><span><small>Continue where you left off</small>${esc(TOPICS[l].title)}</span><span class="arrow">➜</span></button>`}return ''}
function goalCard(){const n=todayN(),g=settings.goal,s=streak();const pc=Math.min(100,Math.round(n/g*100));
 return `<div class="goal"><div class="gs"><span class="fire">${s?'🔥':'✨'}</span><span><b>${s}</b>-day streak</span></div><div class="gp"><div class="gl"><span>Today</span><span>${n}/${g} questions${n>=g?' ✓':''}</span></div><div class="prog"><i style="width:${pc}%"></i></div></div></div>`}
function home(){const name=store.get('name','A-Level');
 return `<div class="screen"><div class="hello"><span class="brand"><span class="avatar"></span><span>Hey, ${esc(name)} Hero!</span></span><span class="appname">Revise Shorts</span></div><div class="scroll">
 <h1 class="title">Your A Levels</h1><div class="sub">Choose a subject to test your knowledge:</div>
 ${resumeBar()}${goalCard()}
 <button class="bar b-green" onclick="startMix('all')"><span>Quick-fire mix: all subjects</span><span class="arrow">➜</span></button>
 ${DB.subjects.map(s=>{const st=subjStats(s);const c=SUBJ_COL[s.id];return `<button class="subjcard c-${c}" onclick="location.hash='#/s/${s.id}'"><div class="nm">${esc(s.name)}</div><div class="bd">${esc(s.board)}</div>
 <div class="prog"><i style="width:${st.cover}%"></i></div><div class="row"><span>${st.done}/${st.n} topics tried${st.done?` · avg best ${st.avg}%`:''}</span><span class="arrow">➜</span></div></button>`}).join('')}
 </div>${tabs('home')}</div>`}
function subject(id){const s=DB.subjects.find(x=>x.id===id);if(!s)return home();const p=prog();const c=SUBJ_COL[s.id];
 const boardName=s.board.replace(/ \(.*\)/,'');
 return `<div class="screen"><div class="hello"><button onclick="location.hash='#/'" aria-label="Back">← Subjects</button><span class="avatar"></span></div><div class="scroll">
 <h1 class="title">${esc(boardName.replace(' A level',''))} A Level ${esc(s.name)}</h1><div class="sub">Choose a topic to revise:</div>
 <button class="bar b-${c}" onclick="startMix('${s.id}')"><span>Mixed ${esc(s.name)} quiz (10 questions)</span><span class="arrow">➜</span></button>
 ${s.sections.map((sec,i)=>{const col=PAL[(PAL.indexOf(c)+1+i)%4];return `<div class="card c-${col}"><h2>${esc(sec.name)}${sec.note?`<small>${esc(sec.note)}</small>`:''}</h2>${sec.topics.map(t=>{const d=[1,2,3].filter(n=>p[t.id+':'+n]).length;return `<button class="topic" onclick="location.hash='#/t/${t.id}'"><span>${esc(t.title)}</span><span class="r">${d?`<span class="pill">${'★'.repeat(d)}${'☆'.repeat(3-d)}</span>`:''}<span class="arrow">➜</span></span></button>`}).join('')}</div>`}).join('')}
 </div>${tabs('home')}</div>`}
function scores(){const p=prog();
 return `<div class="screen"><div class="hello"><span>Your scores</span><span class="avatar"></span></div><div class="scroll"><h1 class="title">Personal bests</h1><div class="sub">Beat your best score on every topic!</div>
 ${goalCard()}
 ${DB.subjects.map(s=>{const st=subjStats(s);const rows=[];s.sections.forEach(sec=>sec.topics.forEach(t=>{const b=[1,2,3].map(k=>p[t.id+':'+k]);if(b.some(Boolean))rows.push(`<div class="li"><span>${esc(t.title)}</span><span>${b.map((x,i)=>`Q${i+1} ${x?x.best+'%':'–'}`).join(' · ')}</span></div>`)}));
 const mx=p['mix-'+s.id];if(mx)rows.unshift(`<div class="li"><span>Mixed quiz</span><span>${mx.best}% <small style="font-weight:400">(×${mx.n})</small></span></div>`);
 return `<div class="card c-${SUBJ_COL[s.id]}"><h2>${esc(s.name)} · ${st.done}/${st.n} topics · avg ${st.avg}%</h2><div class="list">${rows.join('')||'<div class="li"><span>No quizzes yet – go try one!</span></div>'}</div></div>`}).join('')}
 </div>${tabs('trophy')}</div>`}
const YT='https://www.youtube.com/';
function videos(){
 return `<div class="screen"><div class="hello"><span>Videos</span><span class="avatar"></span></div><div class="scroll"><h1 class="title">Watch &amp; revise</h1><div class="sub">Videos open in YouTube.</div>
 <a class="vid b-green" href="${YT}@ScienceShorts" target="_blank" rel="noopener"><span class="play"></span><span>Science Shorts channel<small>All videos by Science Shorts on YouTube</small></span></a>
 ${DB.subjects.map(s=>{const c=SUBJ_COL[s.id];const top=s.playlist?`<a class="vid b-${c}" href="${YT}playlist?list=${s.playlist}" target="_blank" rel="noopener"><span class="play"></span><span>Science Shorts: ${s.id==='physics'?'OCR AS/A-level Physics':'AQA A-level Chemistry'}<small>Full playlist</small></span></a>`:`<div class="note">Science Shorts doesn't make A level Maths videos, so these open a YouTube search for each Edexcel topic.</div>`;
 const q=t=>s.playlist?`${YT}@ScienceShorts/search?query=${encodeURIComponent(t.title.replace(/^[\d.:–]+\s*/,''))}`:`${YT}results?search_query=${encodeURIComponent('Edexcel A level maths '+t.title.replace(/^[\d.:]+\s*/,''))}`;
 return `<div class="card c-${c}"><h2>${esc(s.name)} · ${esc(s.board)}</h2>${top}${s.sections.map(sec=>sec.topics.map(t=>`<a class="topic" href="${q(t)}" target="_blank" rel="noopener"><span>▶ ${esc(t.title)}</span><span class="arrow">➜</span></a>`).join('')).join('')}</div>`}).join('')}
 </div>${tabs('play')}</div>`}
// ---------- settings
let confirmReset=false,pendingImport=null;
const seg=(k,opts)=>`<div class="seg">${opts.map(([v,l])=>`<button class="${settings[k]===v?'on':''}" onclick="setOpt('${k}',${JSON.stringify(v).replace(/"/g,"'")})">${l}</button>`).join('')}</div>`;
const sw=(k,label,sub)=>`<div class="srow"><span>${label}${sub?`<small>${sub}</small>`:''}</span><button class="switch ${settings[k]?'on':''}" role="switch" aria-checked="${!!settings[k]}" aria-label="${label}" onclick="setOpt('${k}',${!settings[k]})"><i></i></button></div>`;
function settingsScr(){const name=store.get('name','A-Level');const nq=DB.count||countQ();
 return `<div class="screen"><div class="hello"><span>Settings</span><span class="avatar"></span></div><div class="scroll"><h1 class="title">Settings</h1>
 <div class="sgroup"><div class="sh">Appearance</div>
  <div class="srow col"><span>Theme</span>${seg('theme',[['system','System'],['light','Light'],['dark','Dark']])}</div>
  <div class="srow col"><span>Text size<small>Notes, questions and answers</small></span>${seg('ts',[[0.9,'Small'],[1,'Normal'],[1.15,'Large'],[1.3,'Extra large']])}</div>
 </div>
 <div class="sgroup"><div class="sh">Quizzes</div>
  ${sw('shuffle','Shuffle questions','Off: questions appear in the order they are written')}
  <div class="srow col"><span>Show explanations</span>${seg('explain',[['now','After each question'],['end','At the end']])}</div>
  <div class="srow col"><span>Questions per topic quiz</span>${seg('qn',[[10,'10'],[0,'All in the quiz']])}</div>
  ${sw('autoCalc','Open calculator automatically','On numeric questions')}
  <div class="srow"><span>Calculator angle mode</span><button class="btn w bd1" onclick="setOpt('deg',${!settings.deg})">${settings.deg?'Degrees':'Radians'}</button></div>
  ${sw('sound','Sound effects','Short tones for right and wrong answers')}
  ${sw('haptics','Vibration','On phones that support it')}
 </div>
 <div class="sgroup"><div class="sh">Daily goal and streak</div>
  <div class="srow col"><span>Daily goal<small>Questions answered per day. Your streak counts the days in a row you hit it.</small></span>${seg('goal',[[10,'10'],[20,'20'],[30,'30'],[50,'50']])}</div>
  <div class="srow"><span>Today</span><b>${todayN()} / ${settings.goal}</b></div>
  <div class="srow"><span>Current streak</span><b>${streak()} day${streak()===1?'':'s'}</b></div>
  <div class="srow"><span>Best streak</span><b>${bestStreak()} day${bestStreak()===1?'':'s'}</b></div>
 </div>
 <div class="sgroup"><div class="sh">You</div>
  <div class="srow"><span>Your name</span><input class="inp sm" value="${esc(name)}" onchange="store.set('name',this.value||'A-Level')"></div>
 </div>
 <div class="sgroup"><div class="sh">Your data</div>
  <div class="srow"><span>Export progress<small>Saves scores, streak and settings as a JSON file</small></span><button class="btn w bd1" onclick="exportData()">Export</button></div>
  <div class="srow"><span>Import progress<small>Replaces what is on this device</small></span><label class="btn w bd1">Import<input type="file" accept="application/json,.json" hidden onchange="importData(this)"></label></div>
  ${pendingImport?`<div class="confirm"><b>Replace your progress with the imported file?</b><br>${pendingImport.n} saved items from ${esc(pendingImport.date)}.<div class="cb"><button class="btn w bd1" onclick="pendingImport=null;render()">Cancel</button><button class="btn danger" onclick="applyImport()">Replace</button></div></div>`:''}
  <div class="srow"><span>Reset progress<small>Deletes all scores, streaks and reading progress</small></span><button class="btn danger" onclick="confirmReset=true;render()">Reset</button></div>
  ${confirmReset?`<div class="confirm"><b>Delete all progress?</b><br>This cannot be undone. Export first if you want a backup.<div class="cb"><button class="btn w bd1" onclick="confirmReset=false;render()">Cancel</button><button class="btn danger" onclick="doReset()">Yes, delete everything</button></div></div>`:''}
 </div>
 <div class="sgroup"><div class="sh">About and offline</div>
  <div class="srow"><span>Version</span><b>${VERSION}${DB.built?` · ${esc(DB.built)}`:''}</b></div>
  <div class="srow"><span>Content</span><b>${nq} questions · ${Object.keys(NOTES).length} notes · ${Object.keys(FIGS).length} diagrams</b></div>
  <div class="srow"><span>Offline</span><b id="offl">Checking…</b></div>
  <div class="srow"><span>Storage used</span><b id="stor">–</b></div>
  <p class="note">Revise Shorts: original exam-style questions and notes written for Edexcel A level Maths (9MA0), OCR A Physics (H556) and AQA Chemistry (7405). Not affiliated with any exam board or with Science Shorts. Progress is stored only on this device. Once loaded, the app works offline; to install it, use your browser's “Add to Home screen”.</p>
 </div></div>${tabs('gear')}</div>`}
function settingsInfo(){if('caches' in window)caches.has('rs-'+VERSION).then(h=>{const e=$('#offl');if(e)e.textContent=h?'Ready: works without internet':'Not cached yet (open once online)'}).catch(()=>{});else{const e=$('#offl');if(e)e.textContent='Not supported in this browser'}
 if(navigator.storage&&navigator.storage.estimate)navigator.storage.estimate().then(s=>{const e=$('#stor');if(e)e.textContent=(s.usage/1048576).toFixed(1)+' MB'}).catch(()=>{})}
function allData(){const o={};for(let i=0;i<localStorage.length;i++){const k=localStorage.key(i);if(k.startsWith('rs.'))o[k.slice(3)]=localStorage.getItem(k)}return o}
function exportData(){const blob=new Blob([JSON.stringify({app:'revise-shorts',version:VERSION,exported:new Date().toISOString(),data:allData()},null,1)],{type:'application/json'});
 const a=document.createElement('a');a.href=URL.createObjectURL(blob);a.download='revise-shorts-progress-'+dkey(new Date())+'.json';document.body.appendChild(a);a.click();setTimeout(()=>{URL.revokeObjectURL(a.href);a.remove()},500);toast('Progress exported')}
function importData(inp){const f=inp.files&&inp.files[0];if(!f)return;const r=new FileReader();r.onload=()=>{try{const j=JSON.parse(r.result);if(j.app!=='revise-shorts'||typeof j.data!=='object')throw 0;
 pendingImport={data:j.data,n:Object.keys(j.data).length,date:(j.exported||'').slice(0,10)||'unknown date'};render()}catch(e){toast('That file is not a Revise Shorts export')}};r.readAsText(f)}
function applyImport(){const d=pendingImport.data;Object.keys(allData()).forEach(k=>store.del(k));for(const k in d)if(typeof d[k]==='string')localStorage.setItem('rs.'+k,d[k]);pendingImport=null;settings=Object.assign({},DEF,store.get('settings',{}));applyTheme();render();toast('Progress imported')}
function doReset(){['progress','days','resume','lastNotes','lastTopic','notesRead'].forEach(k=>store.del(k));confirmReset=false;render();toast('Progress reset')}
function countQ(){let n=0;Object.values(TOPICS).forEach(t=>t.quizzes.forEach(z=>n+=z.length));return n}
// ---------- quiz
let Q=null;
function startTopic(id,n){const t=TOPICS[id];if(!t||!t.quizzes[n-1]||!t.quizzes[n-1].length)return false;const pool=settings.shuffle?shuffle(t.quizzes[n-1]):t.quizzes[n-1].slice();
 Q={key:id+':'+n,tid:id,qn:n,title:t.title+' · Quiz '+n,color:t.color,qs:(settings.qn?pool.slice(0,settings.qn):pool).map(q=>prep(q,t)),i:0,ans:[]};clearResume();store.set('lastTopic',id);return true}
function resumeQuiz(){const r=store.get('resume',null);if(!r)return;Q=r.Q;Q.draft=null;location.hash='#/quiz';render()}
function startMix(sid){let pool=[];Object.values(TOPICS).forEach(t=>{if(sid==='all'||t.subj===sid)t.quizzes.forEach(z=>z.forEach(q=>pool.push([q,t])))});
 const n=sid==='all'?15:10;Q={key:'mix-'+sid,title:sid==='all'?'Quick-fire mix':'Mixed '+DB.subjects.find(s=>s.id===sid).name,color:sid==='all'?'green':SUBJ_COL[sid],qs:shuffle(pool).slice(0,n).map(([q,t])=>prep(q,t)),i:0,ans:[]};location.hash='#/quiz'}
function prep(q,t){q=Object.assign({},q,{topic:t.title});if(q.t==='mc')q.opts=shuffle([q.a,...q.w]);if(q.t==='order')q.shuf=shuffle(q.items.map((x,i)=>i));if(q.t==='match')q.right=shuffle(q.pairs.map((x,i)=>i));return q}
let cur={};
function quiz(){if(!Q)return home();if(Q.i>=Q.qs.length)return results();
 const q=Q.qs[Q.i],a=Q.ans[Q.i],col=Q.color;cur=a?a.resp:(Q.draft&&Q.draft.i===Q.i?Q.draft.v:{});
 const show=a&&settings.explain==='now';
 const pct=Math.round(Q.ans.filter(Boolean).length/Q.qs.length*100);
 let body=`<div class="qtext">${esc(q.q)}</div>`+(q.fig&&FIGS[q.fig]?`<figure class="fig q">${FIGS[q.fig]}</figure>`:'');
 if(q.t==='mc'){body+='<div class="hint">Choose the correct answer:</div>'+q.opts.map((o,k)=>{let c='';if(show){if(o===q.a)c='ok';else if(cur.v===o)c='bad'}else if(a&&cur.v===o)c='sel';return `<button class="opt ${c}" data-k="${k}" ${a?'disabled':''} onclick="pickMC(${k})">${esc(o)}</button>`}).join('')}
 if(q.t==='num'){body+=`<div class="hint">Use the calculator, then enter your answer:</div><input id="ans" class="inp" inputmode="decimal" autocomplete="off" placeholder="Your answer" value="${esc(cur.v||'')}" ${a?'disabled':''} oninput="cur.v=this.value;upd()">${q.u?`<div class="unit">Unit: ${esc(q.u)}</div>`:''}`}
 if(q.t==='text'){body+=`<textarea id="ans" class="inp" placeholder="Enter your answer here..." ${a?'disabled':''} oninput="cur.v=this.value;upd()">${esc(cur.v||'')}</textarea>`}
 if(q.t==='order'){cur.seq=cur.seq||[];body+='<div class="hint">Tap the cards in the correct order:</div>'+q.items.map((x,k)=>{const v=cur.seq[k];let c=v!==undefined?'filled':'';if(show)c+=v===k?' ok':' bad';return `<button class="slot ${c}" ${a?'disabled':''} onclick="unOrder(${k})"><b>${k+1}.</b><span>${v!==undefined?esc(q.items[v]):''}</span></button>`}).join('')+
  (a?'':`<div class="tiles" style="margin-top:12px">${q.shuf.filter(k=>!cur.seq.includes(k)).map(k=>`<button class="tile" onclick="addOrder(${k})">${esc(q.items[k])}</button>`).join('')}</div>`)}
 if(q.t==='match'){cur.m=cur.m||{};body+='<div class="hint">Tap left, then right, to match the pairs:</div><div class="match">'+q.pairs.map((p,k)=>{const rk=q.right[k];const lp=cur.m[k];const rIdx=Object.keys(cur.m).find(l=>cur.m[l]===rk);
  const lc=show?(lp===k?'ok':'bad'):(cur.sel===k?'act':'');const rc=show?(rIdx!==undefined&&+rIdx===rk?'ok':'bad'):'';
  return `<button class="mi l ${lc}" ${lp!==undefined?`data-p="${k+1}"`:''} ${a?'disabled':''} onclick="mL(${k})">${esc(p[0])}</button><button class="mi ${rc}" ${rIdx!==undefined?`data-p="${+rIdx+1}"`:''} ${a?'disabled':''} onclick="mR(${rk})">${esc(q.pairs[rk][1])}</button>`}).join('')+'</div>'}
 if(show)body+=feedback(q,a,Q.i);else if(a)body+='<div class="fb neutral"><div class="h">Answer saved</div>You will see the answers and explanations at the end.</div>';
 return `<div class="screen"><div class="qhead b-${col}"><button class="ib" onclick="quitQuiz()" aria-label="Close">✕</button><span class="t">${esc(Q.title)}</span><button class="ib" onclick="toggleCalc()" aria-label="Calculator">${ICON.calc}</button></div>
 <div class="qprog"><i class="b-${col}" style="width:${pct}%"></i></div>
 <div class="qbody">${body}</div><div id="calcwrap"></div>
 <div class="qfoot b-${col}"><div class="n">${Q.i>0?'<button class="ib" onclick="Q.i--;render()" aria-label="Previous">←</button>':''}<span>${Q.i+1}/${Q.qs.length}</span></div>
 ${a?'':'<button class="btn w" onclick="skip()">Skip</button>'}<button id="done" class="btn d" onclick="done()" ${a?'':'disabled'}>${a?(Q.i+1<Q.qs.length?'Next':'Finish'):'Done'}</button></div></div>`}
function corrText(q){if(q.t==='mc')return `Answer: ${esc(q.a)}`;if(q.t==='num')return `Answer: ${q.a}${q.u?' '+esc(q.u):''}`;if(q.t==='text')return `Model answer: ${esc(q.e)}`;
 if(q.t==='order')return 'Correct order: '+q.items.map((x,i)=>`${i+1}. ${esc(x)}`).join(' → ');if(q.t==='match')return 'Pairs: '+q.pairs.map(p=>`${esc(p[0])} → ${esc(p[1])}`).join('; ');return ''}
function feedback(q,a,i){const corr=corrText(q);
 return `<div class="fb ${a.ok?'ok':'bad'}"><div class="h">${a.ok?'✓ Correct!':'✗ Not quite'}</div>${a.ok&&q.t!=='text'?'':corr+'<br>'}${q.t==='text'?'':esc(q.e)}${q.t==='text'&&!a.ok?`<br><small>Looking for: ${q.k.map(g=>esc(g[0])).join(', ')}</small><br><button class="btn w bd1" style="margin-top:8px" onclick="selfMark(${i})">My answer was right – count it</button>`:''}</div>`}
function selfMark(i){const a=Q.ans[i];a.ok=true;a.resp.self=true;if(Q.saved){Q.saved=false}render()}
function respText(q,a){if(!a)return 'Skipped';const r=a.resp||{};if(q.t==='mc'||q.t==='num'||q.t==='text')return esc(r.v||'');if(q.t==='order')return (r.seq||[]).map(k=>esc(q.items[k])).join(' → ');if(q.t==='match')return q.pairs.map((p,k)=>esc(p[0])+' → '+(r.m&&r.m[k]!==undefined?esc(q.pairs[r.m[k]][1]):'?')).join('; ');return ''}
function upd(){const q=Q.qs[Q.i];let ready=false;
 if(q.t==='mc')ready=cur.v!==undefined;if(q.t==='num'||q.t==='text')ready=!!(cur.v&&cur.v.trim());
 if(q.t==='order')ready=cur.seq.length===q.items.length;if(q.t==='match')ready=Object.keys(cur.m).length===q.pairs.length;
 const d=$('#done');if(d)d.disabled=!ready}
function pickMC(k){const q=Q.qs[Q.i];cur.v=q.opts[k];document.querySelectorAll('.opt').forEach(b=>b.classList.toggle('sel',+b.dataset.k===k));upd()}
function addOrder(k){cur.seq.push(k);rerenderQ()}
function unOrder(k){if(cur.seq[k]!==undefined){cur.seq.splice(k,1);rerenderQ()}}
function mL(k){if(cur.m[k]!==undefined){delete cur.m[k]}cur.sel=k;rerenderQ()}
function mR(rk){if(cur.sel===undefined)return;for(const l in cur.m)if(cur.m[l]===rk)delete cur.m[l];cur.m[cur.sel]=rk;delete cur.sel;rerenderQ()}
function rerenderQ(){const calcOpen=!!$('.calc');Q.draft={i:Q.i,v:cur};Q._noAuto=true;render();Q._noAuto=false;if(calcOpen)openCalc();upd()}
const norm=s=>String(s).toLowerCase().replace(/[‘’]/g,"'").replace(/won't/g,'will not').replace(/can't/g,'cannot').replace(/n't/g,' not').replace(/[₀-₉]/g,c=>'0123456789'['₀₁₂₃₄₅₆₇₈₉'.indexOf(c)]).replace(/[⁰¹²³⁴-⁹]/g,c=>({'⁰':0,'¹':1,'²':2,'³':3,'⁴':4,'⁵':5,'⁶':6,'⁷':7,'⁸':8,'⁹':9}[c])).replace(/[⁺]/g,'+').replace(/[−–]/g,'-').replace(/\s+/g,'').replace(/ise/g,'ize').replace(/[×*]/g,'x');
function parseNum(s){s=String(s).trim().replace(/[−–]/g,'-').replace(/,/g,'').replace(/\s/g,'').replace(/[x×]10\^?\(?(-?\d+)\)?/i,'e$1');const v=parseFloat(s);return /^[-+]?(\d+\.?\d*|\.\d+)(e[-+]?\d+)?/i.test(s)?v:NaN}
function mark(q,r){
 if(q.t==='mc')return r.v===q.a;
 if(q.t==='num'){const v=parseNum(r.v);if(isNaN(v))return false;const tol=Math.max(q.tol,0.1)/100*Math.abs(q.a)+1e-9;return Math.abs(v-q.a)<=tol}
 if(q.t==='text'){if(r.self)return true;const hit=textHits(q,r.v);return hit>=Math.ceil(q.k.length*0.6)}
 if(q.t==='order')return r.seq.every((v,i)=>v===i);
 if(q.t==='match')return q.pairs.every((p,k)=>r.m[k]===k)}
function done(){if(Q.ans[Q.i]){Q.i++;render();return}const q=Q.qs[Q.i];const ok=mark(q,cur);Q.ans[Q.i]={ok,resp:cur};Q.draft=null;logAnswer();beep(ok);saveResume();
 if(settings.explain==='end'){Q.i++;cur={};render();return}
 render();const fb=$('.fb');if(fb)fb.scrollIntoView({behavior:'smooth',block:'nearest'})}
function skip(){Q.draft=null;const q=Q.qs.splice(Q.i,1)[0];Q.qs.push(q);cur={};render()}
function quitQuiz(){if(Q.ans.filter(Boolean).length&&!confirm('Quit this quiz? Your score won\'t be saved, but you can carry on later from the home screen.'))return;const t=Q.tid;Q=null;location.hash=t?'#/t/'+t:'#/'}
function results(){const n=Q.qs.length,c=Q.ans.filter(a=>a&&a.ok).length,pc=Math.round(c/n*100);
 if(!Q.saved){const p=prog(),o=p[Q.key]||{best:0,n:0};if(Q.prevBest===undefined)Q.prevBest=o.n?o.best:null;p[Q.key]={best:Math.max(o.best,pc),last:pc,n:o.n+(Q.counted?0:1),d:Date.now()};store.set('progress',p);Q.saved=true;Q.counted=true;clearResume()}
 const pb=Q.prevBest===null||pc>Q.prevBest;const back=Q.tid||null;
 const rev=Q.qs.map((q,i)=>{const a=Q.ans[i];return `<details class="rv ${a&&a.ok?'ok':'bad'}" ${settings.explain==='end'&&!(a&&a.ok)?'open':''}><summary><span class="rk">${a&&a.ok?'✓':'✗'}</span><span>${i+1}. ${esc(q.q)}</span></summary><div class="rb">
  ${q.fig&&FIGS[q.fig]?`<figure class="fig q">${FIGS[q.fig]}</figure>`:''}<div><b>Your answer:</b> ${respText(q,a)||'–'}</div><div>${corrText(q)}</div>${q.t==='text'?'':`<div class="ex">${esc(q.e)}</div>`}
  ${q.t==='text'&&a&&!a.ok?`<button class="btn w bd1" style="margin-top:8px" onclick="selfMark(${i})">My answer was right – count it</button>`:''}</div></details>`}).join('');
 return `<div class="screen"><div class="qhead b-${Q.color}"><button class="ib" onclick="Q=null;location.hash='${back?'#/t/'+back:'#/'}'">✕</button><span class="t">${esc(Q.title)}</span><span class="ib"></span></div><div class="scroll" style="padding-top:20px">
 <div class="big-score">${pc}%</div><div class="center">${c} out of ${n} correct</div>
 <div class="fb ${pb?'ok':'bad'} center"><div class="h">${pb?(Q.prevBest===null?'First score saved!':'🏆 New personal best!'):'Personal best: '+Q.prevBest+'%'}</div>${pb?'Come back later and try to beat it.':'Have another go to beat it!'}</div>
 <h2 class="rvh">Review your answers</h2>${rev}
 <button class="btn d big" onclick="retry()">Try again</button><button class="btn big b-${Q.color}" onclick="Q=null;location.hash='${back?'#/t/'+back:'#/'}'">Back to quizzes</button>
 ${Q.tid?`<button class="btn big b-yellow" onclick="Q=null;location.hash='#/n/${back}'">Read the revision notes</button><a class="vid b-green" target="_blank" rel="noopener" href="${vidURL(TOPICS[Q.tid])}"><span class="play"></span><span>Watch a video on this topic<small>Opens YouTube</small></span></a>`:''}
 </div></div>`}
function retry(){const k=Q.key;if(k.startsWith('mix-')){startMix(k.slice(4));render()}else{startTopic(Q.tid,Q.qn);render()}}
// ---------- calculator
const K=[['SHIFT','sh'],['x²','sq'],['√','rt'],['π','pi'],['SF','sf'],['(','('],[')',')'],['sin','sin'],['cos','cos'],['tan','tan'],['7'],['8'],['9'],['DEL','del'],['AC','ac'],['4'],['5'],['6'],['×','*'],['÷','/'],['1'],['2'],['3'],['+','+'],['−','-'],['0'],['.'],['×10ˣ','e10'],['ANS','ans'],['=','=']];
const KS={sq:'xʸ',rt:'ln',pi:'e',sf:'log',sin:'sin⁻¹',cos:'cos⁻¹',tan:'tan⁻¹'};
const C={toks:[],pos:0,shift:false,ans:0,res:'0',sfMode:false};
function calcHTML(){return `<div class="calc"><button class="calcclose" onclick="toggleCalc()" aria-label="Close calculator">✕</button><div class="top"><button class="mv" onclick="cMove(-1)">←</button><button class="mv" onclick="cMove(1)">→</button>
 <div class="disp"><span class="mode" onclick="settings.deg=!settings.deg;store.set('settings',settings);drawCalc()">${settings.deg?'DEG':'RAD'}</span>${C.shift?'<span class="shiftOn">SHIFT</span>':''}<div class="expr">${C.toks.slice(0,C.pos).map(t=>esc(t.d)).join('')}<span class="cur"></span>${C.toks.slice(C.pos).map(t=>esc(t.d)).join('')}</div><div class="res">${esc(C.res)}</div></div></div>
 <div class="keys">${K.map(([l,c])=>{c=c||l;const lab=C.shift&&KS[c]?KS[c]:l;return `<button class="${c==='='?'eq':''} ${c==='sh'?'sh'+(C.shift?' on':''):''}" onclick="cKey('${c}')">${lab}</button>`}).join('')}</div></div>`}
function openCalc(){const w=$('#calcwrap');if(w){w.innerHTML=calcHTML();const qb=$('.qbody');if(qb)qb.style.paddingBottom='420px'}}
function drawCalc(){if($('.calc'))openCalc()}
function toggleCalc(){if($('.calc')){$('#calcwrap').innerHTML='';const qb=$('.qbody');if(qb)qb.style.paddingBottom=''}else openCalc()}
function cMove(d){C.pos=Math.max(0,Math.min(C.toks.length,C.pos+d));drawCalc()}
function ins(d,j,ty){C.toks.splice(C.pos,0,{d,j,ty});C.pos++}
function cKey(c){const sh=C.shift;C.shift=false;
 if(c==='sh'){C.shift=!sh}
 else if(c==='ac'){C.toks=[];C.pos=0;C.res='0'}
 else if(c==='del'){if(C.pos>0){C.toks.splice(C.pos-1,1);C.pos--}}
 else if(/^[0-9.]$/.test(c))ins(c,c,'d');
 else if(c==='+'||c==='-')ins(c==='-'?'−':'+',c,'o');
 else if(c==='*'||c==='/')ins(c==='*'?'×':'÷',c,'o');
 else if(c==='('||c===')')ins(c,c,c==='('?'f':'c');
 else if(c==='sq')sh?ins('^','**','o'):ins('²','**2','p');
 else if(c==='rt')sh?ins('ln(','LN(','f'):ins('√(','SQ(','f');
 else if(c==='pi')sh?ins('e','Math.E','k'):ins('π','Math.PI','k');
 else if(c==='sf'){if(sh)ins('log(','LG(','f');else{C.sfMode=!C.sfMode;fmtRes()}}
 else if(['sin','cos','tan'].includes(c))sh?ins(c+'⁻¹(','A'+c.toUpperCase()+'(','f'):ins(c+'(',c.toUpperCase()+'(','f');
 else if(c==='e10')ins('×10^(','*10**(','o');
 else if(c==='ans')ins('Ans','ANS','k');
 else if(c==='='){evalCalc()}
 drawCalc()}
function evalCalc(){let js='',prev=null,open=0;
 for(const t of C.toks){if(prev&&(['d','k','c','p'].includes(prev.ty))&&(['f','k'].includes(t.ty)||(t.ty==='d'&&prev.ty!=='d')))js+='*';js+=t.j;open+=(t.j.match(/\(/g)||[]).length-(t.j.match(/\)/g)||[]).length;prev=t}
 js+=')'.repeat(Math.max(0,open));
 const r=settings.deg?Math.PI/180:1;
 try{const v=Function('SIN','COS','TAN','ASIN','ACOS','ATAN','LN','LG','SQ','ANS','"use strict";return ('+(js||'0')+')')(x=>Math.sin(x*r),x=>Math.cos(x*r),x=>Math.tan(x*r),x=>Math.asin(x)/r,x=>Math.acos(x)/r,x=>Math.atan(x)/r,Math.log,Math.log10,Math.sqrt,C.ans);
  if(typeof v!=='number'||!isFinite(v))throw 0;C.ans=v;C.val=v;fmtRes();
  const q=Q&&Q.qs[Q.i];if(q&&q.t==='num'&&!Q.ans[Q.i]){const inp=$('#ans');cur.v=fmtNum(v,false);if(inp)inp.value=cur.v;upd()}}
 catch(e){C.res='Math ERROR'}}
function fmtNum(v,sf){if(sf)return v.toExponential(3).replace('e',' ×10^').replace('+','');return String(+v.toPrecision(10))}
function fmtRes(){if(C.val!==undefined)C.res=fmtNum(C.val,C.sfMode)}
// ---------- notes
function notesSummary(id){const n=NOTES[id];if(!n)return 'Loading…';return `${n.m} min read · ${n.secs.length} sections · ${n.x} worked example${n.x===1?'':'s'}`}
function tocText(s){return esc(s).replace(/\$([^$]+)\$/g,'<span class="tx">$1</span>').replace(/\*\*(.+?)\*\*/g,'$1')}
function notesScr(id){const t=TOPICS[id];if(!t)return home();const n=NOTES[id];const col=t.color;
 const head=`<div class="nhead b-yellow"><button class="ib" onclick="location.hash='#/t/${id}'" aria-label="Back to topic">${ICON.back}</button><span class="t">Revision notes</span><button class="ib" onclick="window.scrollTo({top:0,behavior:'smooth'})" aria-label="Back to top">${ICON.up}</button><div class="rp"><i id="rprog"></i></div></div>`;
 if(!n)return `<div class="screen">${head}<div class="scroll"><p class="note center" style="margin-top:40px">Loading notes…</p></div></div>`;
 const html=n.h.replace(/<figure class="fig" data-fig="([\w-]+)">/g,(m,f)=>m+(FIGS[f]||''));
 return `<div class="screen notes-screen">${head}<div class="scroll npage">
 <header class="nhero c-${col}"><div class="kicker">${esc(t.sec)}</div><h1>${esc(t.title)}</h1><div class="meta">${notesSummary(id)}</div>${n.spec?`<div class="spec">Specification: ${esc(n.spec)}</div>`:''}</header>
 ${n.intro?`<p class="lead">${n.intro}</p>`:''}
 <nav class="toc"><div class="th">In this topic</div><ol>${n.secs.map((s,i)=>`<li><button onclick="jumpSec(${i+1})">${tocText(s)}</button></li>`).join('')}</ol></nav>
 <article class="nt">${html}</article>
 <div class="nend"><div class="th">Test yourself</div>${t.quizzes.map((z,i)=>z.length?`<button class="bar b-${['green','orange','purple'].map(c=>c===col?'blue':c)[i]}" onclick="location.hash='#/q/${id}/${i+1}'"><span>${QN[i]}</span><span class="arrow">➜</span></button>`:'').join('')}
 <button class="btn big b-yellow" onclick="location.hash='#/t/${id}'">Back to the topic</button></div>
 </div></div>`}
function jumpSec(i){const e=document.getElementById('s'+i);if(e)e.scrollIntoView({behavior:'smooth',block:'start'})}
let _np=0;
function onScroll(){const h=location.hash;if(!h.startsWith('#/n/'))return;const d=document.documentElement;const max=d.scrollHeight-innerHeight;const f=max>0?Math.min(1,scrollY/max):1;
 const b=$('#rprog');if(b)b.style.width=(f*100)+'%';const now=Date.now();if(now-_np>800){_np=now;const id=h.slice(4);const r=store.get('notesRead',{});r[id]=Math.max(r[id]||0,f);store.set('notesRead',r);store.set('lastNotes',{id,f,y:scrollY,t:now})}}
window.addEventListener('scroll',onScroll,{passive:true});
const QN=['Quiz 1 · Warm-up','Quiz 2 · Exam practice','Quiz 3 · Exam-style multi-step'];
const QD=['Core facts and one-step questions','Applying ideas: two-step questions','Harder exam-style problems'];
function vidURL(t){const n=t.title.replace(/^[\d.:–]+\s*/,'');return t.subj==='maths'?YT+'results?search_query='+encodeURIComponent('Edexcel A level maths '+n):YT+'@ScienceShorts/search?query='+encodeURIComponent(n)}
function topicScr(id){const t=TOPICS[id];if(!t)return home();store.set('lastTopic',id);const p=prog();const col=t.color;const pal=['green','orange','purple'].map(c=>c===col?'blue':c);
 const rd=Math.round((store.get('notesRead',{})[id]||0)*100);
 return `<div class="screen"><div class="hello"><button onclick="location.hash='#/s/${t.subj}'" aria-label="Back">← Topics</button><span class="avatar"></span></div><div class="scroll">
 <h1 class="title">${esc(t.title)}</h1><div class="sub">${esc(t.sec)}</div>
 <button class="subjcard c-yellow" onclick="location.hash='#/n/${id}'"><div class="nm">📖 Revision notes</div><div class="bd">${notesSummary(id)}</div>
 <div class="prog"><i style="width:${rd}%"></i></div><div class="row"><span>${rd?(rd>=95?'Read ✓':`${rd}% read`):'Not read yet'}</span><span class="arrow">➜</span></div></button>
 ${t.quizzes.map((z,i)=>{const r=p[id+':'+(i+1)];const n=settings.qn?Math.min(settings.qn,z.length):z.length;return `<button class="subjcard c-${pal[i]}" ${n?`onclick="location.hash='#/q/${id}/${i+1}'"`:'disabled style="opacity:.5"'}><div class="nm">${QN[i]}</div><div class="bd">${QD[i]} · ${n?n+' questions':'coming soon'}</div>
 <div class="prog"><i style="width:${r?r.best:0}%"></i></div><div class="row"><span>${r?`Best ${r.best}% · last ${r.last}% · played ×${r.n}`:'Not tried yet'}</span><span class="arrow">➜</span></div></button>`}).join('')}
 <a class="vid b-${col}" href="${vidURL(t)}" target="_blank" rel="noopener"><span class="play"></span><span>Watch a video on this topic<small>Opens YouTube</small></span></a>
 </div>${tabs('home')}</div>`}
// ---------- router
let lastHash='';
function render(){if(!DB)return;const h=location.hash||'#/';let html;mountDock();dockGo(hashTab(h));
 if(h==='#/videos')html=videos();else if(h==='#/scores')html=scores();else if(h==='#/settings')html=settingsScr();
 else if(h.startsWith('#/s/'))html=subject(h.slice(4));
 else if(h.startsWith('#/t/'))html=topicScr(h.slice(4));
 else if(h.startsWith('#/n/'))html=notesScr(h.slice(4));
 else if(h.startsWith('#/q/')){const [id,n]=h.slice(4).split('/');const key=id+':'+(n||1);if(!Q||Q.key!==key)startTopic(id,+(n||1));html=quiz()}
 else if(h==='#/quiz')html=quiz();else html=home();
 $('#app').innerHTML=html;texAll();
 const changed=h!==lastHash;lastHash=h;
 if(h==='#/settings')settingsInfo();
 if(h.startsWith('#/n/')&&changed){const ln=store.get('lastNotes',null);const id=h.slice(4);if(ln&&ln.id===id&&ln.y>200&&ln.f<0.98)requestAnimationFrame(()=>window.scrollTo(0,ln.y));else window.scrollTo(0,0)}
 else if(changed&&!h.startsWith('#/q/')&&h!=='#/quiz')window.scrollTo(0,0);
 const q=Q&&Q.qs[Q.i];if((h.startsWith('#/q/')||h==='#/quiz')&&q&&q.t==='num'&&!Q.ans[Q.i]&&!$('.calc')&&!Q._noAuto&&settings.autoCalc)openCalc();}
window.addEventListener('hashchange',()=>{if(!(location.hash.startsWith('#/q/')||location.hash==='#/quiz'))Q=null;render()});
let NOTES={},FIGS={};fetch('data/figs.json').then(r=>r.json()).then(f=>{FIGS=f;render()}).catch(()=>{});
fetch('data/notes.json').then(r=>r.json()).then(n=>{NOTES=n;const h=location.hash||'';if(h.startsWith('#/t/')||h.startsWith('#/n/')||h==='#/settings'){lastHash='';render()}}).catch(()=>{});
function texAll(){if(!window.katex)return;document.querySelectorAll('.tx:not([data-r])').forEach(e=>{try{katex.render(e.textContent,e,{displayMode:e.classList.contains('d'),throwOnError:false})}catch(_){}e.dataset.r=1});if(document.querySelector('.npage')){requestAnimationFrame(fitTx);setTimeout(fitTx,350);document.fonts&&document.fonts.ready.then(fitTx)}}
function fitTx(){document.querySelectorAll('.npage .tx.d').forEach(e=>{const k=e.querySelector('.katex-display>.katex')||e.firstElementChild;if(!k)return;k.style.fontSize='';let f=1.21;for(let n=0;n<4;n++){const w=e.clientWidth,sw=e.scrollWidth;if(!w||sw<=w+1)break;f=Math.max(.6,f*(w-2)/sw);k.style.fontSize=f+'em';if(f<=.6)break}})}
addEventListener('resize',()=>fitTx())
fetch('data/questions.json').then(r=>r.json()).then(d=>{DB=d;d.subjects.forEach(s=>s.sections.forEach(sec=>sec.topics.forEach(t=>{t.subj=s.id;t.sec=sec.name;t.color=SUBJ_COL[s.id];TOPICS[t.id]=t})));render()});
if('serviceWorker' in navigator){let _had=!!navigator.serviceWorker.controller,_rl=false;navigator.serviceWorker.addEventListener('controllerchange',()=>{if(_had&&!_rl){_rl=true;location.reload();}});window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js',{updateViaCache:'none'}).then(r=>{r.update();document.addEventListener('visibilitychange',()=>{if(document.visibilityState==='visible')r.update();});}).catch(()=>{}));}
function stem(w){return w.replace(/(ations|ation|ings|ing|ions|ion|ies|es|ed|ly|s)$/,'')}
function lev(a,b){if(Math.abs(a.length-b.length)>2)return 9;const d=[...Array(b.length+1).keys()];for(let i=1;i<=a.length;i++){let p=d[0];d[0]=i;for(let j=1;j<=b.length;j++){const t=d[j];d[j]=Math.min(d[j]+1,d[j-1]+1,p+(a[i-1]===b[j-1]?0:1));p=t}}return d[b.length]}
function kwHit(ans,words,k){const nk=norm(k);if(nk.length<4&&!/\s/.test(k)&&/^[a-z0-9]+$/.test(nk))return words.includes(nk);if(ans.includes(nk))return true;if(/\s/.test(k.trim())||nk.length<4)return false;const sk=stem(nk);return words.some(w=>{const sw=stem(w);return sw===sk||(sk.length>=4&&(sw.startsWith(sk)||sk.startsWith(sw)&&sw.length>=4))||lev(sw,sk)<=(sk.length>=8?2:1)})}
function textHits(q,v){const ans=norm(v);const words=String(v).toLowerCase().replace(/[₀-₉]/g,c=>'0123456789'['₀₁₂₃₄₅₆₇₈₉'.indexOf(c)]).split(/[^a-z0-9+²³⁻]+/).filter(w=>w.length>1);return q.k.filter(g=>g.some(k=>kwHit(ans,words,k))).length}
