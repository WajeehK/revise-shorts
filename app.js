'use strict';
const $=s=>document.querySelector(s);
const esc=s=>String(s).replace(/[&<>"]/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]));
const shuffle=a=>{a=a.slice();for(let i=a.length-1;i>0;i--){const j=Math.random()*(i+1)|0;[a[i],a[j]]=[a[j],a[i]]}return a};
const PAL=['purple','green','orange','blue'];
const SUBJ_COL={maths:'purple',physics:'blue',chemistry:'orange'};
let DB=null, TOPICS={};
const store={get(k,d){try{return JSON.parse(localStorage.getItem('rs.'+k))??d}catch(e){return d}},set(k,v){localStorage.setItem('rs.'+k,JSON.stringify(v))}};
let settings=store.get('settings',{deg:true});
const prog=()=>store.get('progress',{});
const ICON={
home:'<svg viewBox="0 0 24 24"><path d="M3 11l9-7 9 7v9a1 1 0 0 1-1 1h-5v-6h-6v6H4a1 1 0 0 1-1-1z"/></svg>',
play:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9"/><path d="M10 8l6 4-6 4z" fill="#222"/></svg>',
trophy:'<svg viewBox="0 0 24 24"><path d="M8 4h8v5a4 4 0 0 1-8 0zM8 6H4a4 4 0 0 0 4 4M16 6h4a4 4 0 0 1-4 4M12 13v4M8 20h8M9 17h6"/></svg>',
gear:'<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="3"/><path d="M19.4 15a1.7 1.7 0 0 0 .3 1.8l.1.1a2 2 0 1 1-2.8 2.8l-.1-.1a1.7 1.7 0 0 0-1.8-.3 1.7 1.7 0 0 0-1 1.5V21a2 2 0 1 1-4 0v-.1a1.7 1.7 0 0 0-1.1-1.5 1.7 1.7 0 0 0-1.8.3l-.1.1a2 2 0 1 1-2.8-2.8l.1-.1a1.7 1.7 0 0 0 .3-1.8 1.7 1.7 0 0 0-1.5-1H3a2 2 0 1 1 0-4h.1a1.7 1.7 0 0 0 1.5-1.1 1.7 1.7 0 0 0-.3-1.8l-.1-.1a2 2 0 1 1 2.8-2.8l.1.1a1.7 1.7 0 0 0 1.8.3H9a1.7 1.7 0 0 0 1-1.5V3a2 2 0 1 1 4 0v.1a1.7 1.7 0 0 0 1 1.5 1.7 1.7 0 0 0 1.8-.3l.1-.1a2 2 0 1 1 2.8 2.8l-.1.1a1.7 1.7 0 0 0-.3 1.8V9a1.7 1.7 0 0 0 1.5 1H21a2 2 0 1 1 0 4h-.1a1.7 1.7 0 0 0-1.5 1z"/></svg>',
calc:'<svg viewBox="0 0 24 24"><rect x="5" y="3" width="14" height="18" rx="2"/><path d="M8 7h8M8 12h1M12 12h1M16 12h0M8 16h1M12 16h1M16 12v4"/></svg>'};
function tabs(on){const t=[['home','#/','Home'],['play','#/videos','Videos'],['trophy','#/scores','Scores'],['gear','#/settings','Settings']];
 return '<nav class="tabs">'+t.map(([i,h,l])=>`<button class="${on===i?'on':''}" onclick="location.hash='${h}'" aria-label="${l}">${ICON[i]}<span>${l}</span></button>`).join('')+'</nav>'}
function subjStats(s){const p=prog();let n=0,done=0,sum=0;s.sections.forEach(sec=>sec.topics.forEach(t=>{n++;if(p[t.id]){done++;sum+=p[t.id].best}}));return{n,done,avg:done?Math.round(sum/done):0,cover:Math.round(done/n*100)}}
// ---------- screens
function home(){const name=store.get('name','A-Level');
 return `<div class="screen"><div class="hello"><span>Hey, ${esc(name)} Hero!</span><span class="avatar"></span></div><div class="scroll">
 <h1 class="title">Your A Levels</h1><div class="sub">Choose a subject to test your knowledge:</div>
 <button class="bar b-green" onclick="startMix('all')"><span>Quick-fire mix: all subjects</span><span class="arrow">➜</span></button>
 ${DB.subjects.map(s=>{const st=subjStats(s);const c=SUBJ_COL[s.id];return `<button class="subjcard c-${c}" onclick="location.hash='#/s/${s.id}'"><div class="nm">${esc(s.name)}</div><div class="bd">${esc(s.board)}</div>
 <div class="prog"><i style="width:${st.cover}%"></i></div><div class="row"><span>${st.done}/${st.n} topics tried${st.done?` · avg best ${st.avg}%`:''}</span><span class="arrow">➜</span></div></button>`}).join('')}
 </div>${tabs('home')}</div>`}
function subject(id){const s=DB.subjects.find(x=>x.id===id);if(!s)return home();const p=prog();const c=SUBJ_COL[s.id];
 const boardName=s.board.replace(/ \(.*\)/,'');
 return `<div class="screen"><div class="hello"><button onclick="location.hash='#/'" aria-label="Back">← Subjects</button><span class="avatar"></span></div><div class="scroll">
 <h1 class="title">${esc(boardName.replace(' A level',''))} A Level ${esc(s.name)}</h1><div class="sub">Choose a quiz to test your knowledge:</div>
 <button class="bar b-${c}" onclick="startMix('${s.id}')"><span>Mixed ${esc(s.name)} quiz (10 questions)</span><span class="arrow">➜</span></button>
 ${s.sections.map((sec,i)=>{const col=PAL[(PAL.indexOf(c)+1+i)%4];return `<div class="card c-${col}"><h2>${esc(sec.name)}</h2>${sec.topics.map(t=>`<button class="topic" onclick="location.hash='#/q/${t.id}'"><span>${esc(t.title)}</span><span class="r">${p[t.id]?`<span class="pill">best ${p[t.id].best}%</span>`:''}<span class="arrow">➜</span></span></button>`).join('')}</div>`}).join('')}
 </div>${tabs('home')}</div>`}
function scores(){const p=prog();
 return `<div class="screen"><div class="hello"><span>Your scores</span><span class="avatar"></span></div><div class="scroll"><h1 class="title">Personal bests</h1><div class="sub">Beat your best score on every topic!</div>
 ${DB.subjects.map(s=>{const st=subjStats(s);const rows=[];s.sections.forEach(sec=>sec.topics.forEach(t=>{if(p[t.id])rows.push(`<div class="li"><span>${esc(t.title)}</span><span>${p[t.id].best}% <small style="font-weight:400">(last ${p[t.id].last}%, ×${p[t.id].n})</small></span></div>`)}));
 const mx=p['mix-'+s.id];if(mx)rows.unshift(`<div class="li"><span>Mixed quiz</span><span>${mx.best}% <small style="font-weight:400">(×${mx.n})</small></span></div>`);
 return `<div class="card c-${SUBJ_COL[s.id]}"><h2>${esc(s.name)} · ${st.done}/${st.n} topics · avg ${st.avg}%</h2><div class="list">${rows.join('')||'<div class="li"><span>No quizzes yet – go try one!</span></div>'}</div></div>`}).join('')}
 </div>${tabs('trophy')}</div>`}
const YT='https://www.youtube.com/';
function videos(){
 return `<div class="screen"><div class="hello"><span>Videos</span><span class="avatar"></span></div><div class="scroll"><h1 class="title">Watch &amp; revise</h1><div class="sub">Videos open in YouTube.</div>
 <a class="vid b-green" href="${YT}@ScienceShorts" target="_blank" rel="noopener"><span class="play"></span><span>Science Shorts channel<small>All videos by Science Shorts on YouTube</small></span></a>
 ${DB.subjects.map(s=>{const c=SUBJ_COL[s.id];const top=s.playlist?`<a class="vid b-${c}" href="${YT}playlist?list=${s.playlist}" target="_blank" rel="noopener"><span class="play"></span><span>Science Shorts: ${s.id==='physics'?'OCR AS/A-level Physics':'AQA A-level Chemistry'}<small>Full playlist</small></span></a>`:`<div class="note">Science Shorts doesn't make A level Maths videos, so these open a YouTube search for each Edexcel topic.</div>`;
 const q=t=>s.playlist?`${YT}@ScienceShorts/search?query=${encodeURIComponent(t.title.replace(/^[\d.:]+\s*/,''))}`:`${YT}results?search_query=${encodeURIComponent('Edexcel A level maths '+t.title.replace(/^[\d.:]+\s*/,''))}`;
 return `<div class="card c-${c}"><h2>${esc(s.name)} · ${esc(s.board)}</h2>${top}${s.sections.map(sec=>sec.topics.map(t=>`<a class="topic" href="${q(t)}" target="_blank" rel="noopener"><span>▶ ${esc(t.title)}</span><span class="arrow">➜</span></a>`).join('')).join('')}</div>`}).join('')}
 </div>${tabs('play')}</div>`}
function settingsScr(){const name=store.get('name','A-Level');
 return `<div class="screen"><div class="hello"><span>Settings</span><span class="avatar"></span></div><div class="scroll"><h1 class="title">Settings</h1>
 <div class="toggle"><span>Your name</span><input class="inp" style="width:55%;font-size:14px;padding:6px" value="${esc(name)}" onchange="store.set('name',this.value||'A-Level')"></div>
 <div class="toggle"><span>Calculator angle mode</span><button class="btn w" style="border:1px solid #ccc" onclick="settings.deg=!settings.deg;store.set('settings',settings);render()">${settings.deg?'Degrees':'Radians'}</button></div>
 <div class="toggle"><span>Reset all scores</span><button class="btn d" onclick="if(confirm('Delete all saved scores?')){store.set('progress',{});render()}">Reset</button></div>
 <p class="note">Revise Shorts: original exam-style questions written for Edexcel A level Maths (9MA0), OCR A Physics (H556) and AQA Chemistry (7405). Not affiliated with any exam board or with Science Shorts. Works offline. To install, use your browser's “Add to Home screen”.</p>
 <p class="note">${countQ()} questions · v1</p></div>${tabs('gear')}</div>`}
function countQ(){let n=0;Object.values(TOPICS).forEach(t=>n+=t.questions.length);return n}
// ---------- quiz
let Q=null;
function startTopic(id){const t=TOPICS[id];if(!t)return false;Q={key:id,title:t.title,color:t.color,qs:shuffle(t.questions).map(q=>prep(q,t)),i:0,ans:[]};return true}
function startMix(sid){let pool=[];Object.values(TOPICS).forEach(t=>{if(sid==='all'||t.subj===sid)t.questions.forEach(q=>pool.push([q,t]))});
 const n=sid==='all'?15:10;Q={key:'mix-'+sid,title:sid==='all'?'Quick-fire mix':'Mixed '+DB.subjects.find(s=>s.id===sid).name,color:sid==='all'?'green':SUBJ_COL[sid],qs:shuffle(pool).slice(0,n).map(([q,t])=>prep(q,t)),i:0,ans:[]};location.hash='#/quiz'}
function prep(q,t){q=Object.assign({},q,{topic:t.title});if(q.t==='mc')q.opts=shuffle([q.a,...q.w]);if(q.t==='order')q.shuf=shuffle(q.items.map((x,i)=>i));if(q.t==='match')q.right=shuffle(q.pairs.map((x,i)=>i));return q}
let cur={};
function quiz(){if(!Q)return home();if(Q.i>=Q.qs.length)return results();
 const q=Q.qs[Q.i],a=Q.ans[Q.i],col=Q.color;cur=a?a.resp:(Q.draft&&Q.draft.i===Q.i?Q.draft.v:{});
 const pct=Math.round(Q.ans.filter(Boolean).length/Q.qs.length*100);
 let body=`<div class="qtext">${esc(q.q)}</div>`;
 if(q.t==='mc'){body+='<div class="hint">Choose the correct answer:</div>'+q.opts.map((o,k)=>{let c='';if(a){if(o===q.a)c='ok';else if(cur.v===o)c='bad'}return `<button class="opt ${c}" data-k="${k}" ${a?'disabled':''} onclick="pickMC(${k})">${esc(o)}</button>`}).join('')}
 if(q.t==='num'){body+=`<div class="hint">Use the calculator, then enter your answer:</div><input id="ans" class="inp" inputmode="decimal" autocomplete="off" placeholder="Your answer" value="${esc(cur.v||'')}" ${a?'disabled':''} oninput="cur.v=this.value;upd()">${q.u?`<div class="unit">Unit: ${esc(q.u)}</div>`:''}`}
 if(q.t==='text'){body+=`<textarea id="ans" class="inp" placeholder="Enter your answer here..." ${a?'disabled':''} oninput="cur.v=this.value;upd()">${esc(cur.v||'')}</textarea>`}
 if(q.t==='order'){cur.seq=cur.seq||[];body+='<div class="hint">Tap the cards in the correct order:</div>'+q.items.map((x,k)=>{const v=cur.seq[k];let c=v!==undefined?'filled':'';if(a)c+=v===k?' ok':' bad';return `<button class="slot ${c}" ${a?'disabled':''} onclick="unOrder(${k})"><b>${k+1}.</b><span>${v!==undefined?esc(q.items[v]):''}</span></button>`}).join('')+
  (a?'':`<div class="tiles" style="margin-top:12px">${q.shuf.filter(k=>!cur.seq.includes(k)).map(k=>`<button class="tile" onclick="addOrder(${k})">${esc(q.items[k])}</button>`).join('')}</div>`)}
 if(q.t==='match'){cur.m=cur.m||{};body+='<div class="hint">Tap left, then right, to match the pairs:</div><div class="match">'+q.pairs.map((p,k)=>{const rk=q.right[k];const lp=cur.m[k];const rIdx=Object.keys(cur.m).find(l=>cur.m[l]===rk);
  const lc=a?(lp===k?'ok':'bad'):(cur.sel===k?'act':'');const rc=a?(rIdx!==undefined&&+rIdx===rk?'ok':'bad'):'';
  return `<button class="mi l ${lc}" ${lp!==undefined?`data-p="${k+1}"`:''} ${a?'disabled':''} onclick="mL(${k})">${esc(p[0])}</button><button class="mi ${rc}" ${rIdx!==undefined?`data-p="${+rIdx+1}"`:''} ${a?'disabled':''} onclick="mR(${rk})">${esc(q.pairs[rk][1])}</button>`}).join('')+'</div>'}
 if(a)body+=feedback(q,a);
 return `<div class="screen"><div class="qhead b-${col}"><button class="ib" onclick="quitQuiz()" aria-label="Close">✕</button><span class="t">${esc(Q.title)}</span><button class="ib" onclick="toggleCalc()" aria-label="Calculator">${ICON.calc}</button></div>
 <div class="qprog"><i class="b-${col}" style="width:${pct}%;filter:saturate(2) brightness(.85)"></i></div>
 <div class="qbody">${body}</div><div id="calcwrap"></div>
 <div class="qfoot b-${col}"><div class="n">${Q.i>0?'<button class="ib" onclick="Q.i--;render()" aria-label="Previous">←</button>':''}<span>${Q.i+1}/${Q.qs.length}</span></div>
 ${a?'':'<button class="btn w" onclick="skip()">Skip</button>'}<button id="done" class="btn d" onclick="done()" ${a?'':'disabled'}>${a?(Q.i+1<Q.qs.length?'Next':'Finish'):'Done'}</button></div></div>`}
function feedback(q,a){let corr='';
 if(q.t==='mc')corr=`Answer: ${esc(q.a)}`;
 if(q.t==='num')corr=`Answer: ${q.a}${q.u?' '+esc(q.u):''}`;
 if(q.t==='text')corr=`Model answer: ${esc(q.e)}`;
 if(q.t==='order')corr='Correct order: '+q.items.map((x,i)=>`${i+1}. ${esc(x)}`).join(' → ');
 if(q.t==='match')corr='Pairs: '+q.pairs.map(p=>`${esc(p[0])} → ${esc(p[1])}`).join('; ');
 return `<div class="fb ${a.ok?'ok':'bad'}"><div class="h">${a.ok?'✓ Correct!':'✗ Not quite'}</div>${a.ok&&q.t!=='text'?'':corr+'<br>'}${q.t==='text'?'':esc(q.e)}</div>`}
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
const norm=s=>String(s).toLowerCase().replace(/[₀-₉]/g,c=>'0123456789'['₀₁₂₃₄₅₆₇₈₉'.indexOf(c)]).replace(/[⁰¹²³⁴-⁹]/g,c=>({'⁰':0,'¹':1,'²':2,'³':3,'⁴':4,'⁵':5,'⁶':6,'⁷':7,'⁸':8,'⁹':9}[c])).replace(/[⁺]/g,'+').replace(/[−–]/g,'-').replace(/\s+/g,'').replace(/ise/g,'ize').replace(/[×*]/g,'x');
function parseNum(s){s=String(s).trim().replace(/[−–]/g,'-').replace(/,/g,'').replace(/\s/g,'').replace(/[x×]10\^?\(?(-?\d+)\)?/i,'e$1');const v=parseFloat(s);return /^[-+]?(\d+\.?\d*|\.\d+)(e[-+]?\d+)?/i.test(s)?v:NaN}
function mark(q,r){
 if(q.t==='mc')return r.v===q.a;
 if(q.t==='num'){const v=parseNum(r.v);if(isNaN(v))return false;const tol=Math.max(q.tol,0.1)/100*Math.abs(q.a)+1e-9;return Math.abs(v-q.a)<=tol}
 if(q.t==='text'){const n=norm(r.v);return q.k.every(g=>g.some(k=>n.includes(norm(k))))}
 if(q.t==='order')return r.seq.every((v,i)=>v===i);
 if(q.t==='match')return q.pairs.every((p,k)=>r.m[k]===k)}
function done(){if(Q.ans[Q.i]){Q.i++;render();return}const q=Q.qs[Q.i];Q.ans[Q.i]={ok:mark(q,cur),resp:cur};Q.draft=null;render();const fb=$('.fb');if(fb)fb.scrollIntoView({behavior:'smooth',block:'nearest'})}
function skip(){Q.draft=null;const q=Q.qs.splice(Q.i,1)[0];Q.qs.push(q);cur={};render()}
function quitQuiz(){if(Q.ans.filter(Boolean).length&&!confirm('Quit this quiz? Your score won\'t be saved.'))return;const s=TOPICS[Q.key]?TOPICS[Q.key].subj:null;Q=null;location.hash=s?'#/s/'+s:'#/'}
function results(){const n=Q.qs.length,c=Q.ans.filter(a=>a&&a.ok).length,pc=Math.round(c/n*100);
 if(!Q.saved){const p=prog(),o=p[Q.key]||{best:0,n:0};Q.prevBest=o.n?o.best:null;p[Q.key]={best:Math.max(o.best,pc),last:pc,n:o.n+1,d:Date.now()};store.set('progress',p);Q.saved=true}
 const pb=Q.prevBest===null||pc>Q.prevBest;const back=TOPICS[Q.key]?TOPICS[Q.key].subj:null;
 return `<div class="screen"><div class="qhead b-${Q.color}"><button class="ib" onclick="Q=null;location.hash='${back?'#/s/'+back:'#/'}'">✕</button><span class="t">${esc(Q.title)}</span><span class="ib"></span></div><div class="scroll" style="padding-top:20px">
 <div class="big-score">${pc}%</div><div class="center">${c} out of ${n} correct</div>
 <div class="fb ${pb?'ok':'bad'} center"><div class="h">${pb?(Q.prevBest===null?'First score saved!':'🏆 New personal best!'):'Personal best: '+Q.prevBest+'%'}</div>${pb?'Come back later and try to beat it.':'Have another go to beat it!'}</div>
 <button class="btn d big" onclick="retry()">Try again</button><button class="btn big b-${Q.color}" onclick="Q=null;location.hash='${back?'#/s/'+back:'#/'}'">Back to topics</button>
 ${TOPICS[Q.key]?`<a class="vid b-green" target="_blank" rel="noopener" href="${TOPICS[Q.key].subj==='maths'?YT+'results?search_query='+encodeURIComponent('Edexcel A level maths '+Q.title.replace(/^[\d.:]+\s*/,'')):YT+'@ScienceShorts/search?query='+encodeURIComponent(Q.title.replace(/^[\d.:]+\s*/,''))}"><span class="play"></span><span>Watch a video on this topic<small>Opens YouTube</small></span></a>`:''}
 </div></div>`}
function retry(){const k=Q.key;if(k.startsWith('mix-')){startMix(k.slice(4));render()}else{startTopic(k);render()}}
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
// ---------- router
function render(){const h=location.hash||'#/';let html;
 if(h==='#/videos')html=videos();else if(h==='#/scores')html=scores();else if(h==='#/settings')html=settingsScr();
 else if(h.startsWith('#/s/'))html=subject(h.slice(4));
 else if(h.startsWith('#/q/')){const id=h.slice(4);if(!Q||Q.key!==id||Q.saved&&Q.i>=Q.qs.length&&false){if(!Q||Q.key!==id)startTopic(id)}html=quiz()}
 else if(h==='#/quiz')html=quiz();else html=home();
 $('#app').innerHTML=html;
 if(!h.startsWith('#/q/')&&h!=='#/quiz')window.scrollTo(0,0);
 const q=Q&&Q.qs[Q.i];if((h.startsWith('#/q/')||h==='#/quiz')&&q&&q.t==='num'&&!Q.ans[Q.i]&&!$('.calc')&&!Q._noAuto)openCalc();}
window.addEventListener('hashchange',()=>{if(!(location.hash.startsWith('#/q/')||location.hash==='#/quiz'))Q=null;render()});
fetch('data/questions.json').then(r=>r.json()).then(d=>{DB=d;d.subjects.forEach(s=>s.sections.forEach(sec=>sec.topics.forEach(t=>{t.subj=s.id;t.color=SUBJ_COL[s.id];TOPICS[t.id]=t})));render()});
if('serviceWorker' in navigator)window.addEventListener('load',()=>navigator.serviceWorker.register('sw.js').catch(()=>{}));
