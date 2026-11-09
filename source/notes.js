// Build app/data/notes.json from src/notes/*.md ; validates every TeX expression with KaTeX.
const fs=require('fs'),path=require('path'),katex=require('../tools/node_modules/katex');
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
let errs=0,out={},words={},nTex=0,nFig=0;const FIGS=JSON.parse(fs.readFileSync(path.join(__dirname,'../app/data/figs.json')));const figUse={};
function inline(s,where){
  // split on $...$ (no $ inside)
  return s.split(/(\$[^$]+\$)/).map(p=>{
    if(/^\$[^$]+\$$/.test(p)){const t=p.slice(1,-1);chk(t,false,where);return `<span class="tx">${esc(t)}</span>`}
    return esc(p).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>').replace(/`(.+?)`/g,'<code>$1</code>');
  }).join('')}
function chk(t,d,where){nTex++;try{katex.renderToString(t,{throwOnError:true,displayMode:d,strict:'ignore'})}catch(e){errs++;console.log('TEX ERR',where,t,'::',e.message.slice(0,90))}}
for(const f of ['maths','physics','chemistry']){
  const p=path.join(__dirname,'notes',f+'.md');if(!fs.existsSync(p))continue;
  const L=fs.readFileSync(p,'utf8').split('\n');let id=null,html='',sec=null,list=false,body='';
  const closeList=()=>{if(list){body+='</ul>';list=false}};
  const closeSec=()=>{closeList();if(sec!==null){html+=`<details class="nsec"${html?'':' open'}><summary>${inline(sec,id)}</summary><div class="nb">${body}</div></details>`;}sec=null;body=''};
  const closeTopic=()=>{closeSec();if(id){out[id]=html}html=''};
  L.forEach((ln,i)=>{const w=f+':'+(i+1);
    if(ln.startsWith('## ')){closeTopic();id=ln.slice(3).trim();words[id]=0;return}
    if(!id)return;
    if(ln.startsWith('### ')){closeSec();sec=ln.slice(4).trim();return}
    if(!ln.trim()){closeList();return}
    if(sec===null)sec='Overview';
    words[id]+=ln.split(/\s+/).length;
    const fm=ln.match(/^!fig\s+([\w-]+)\s*(.*)$/);
    if(fm){closeList();const svg=FIGS[fm[1]];if(!svg){errs++;console.log('FIG MISSING',w,fm[1]);return}
      const alt=fm[2]||(svg.match(/aria-label="([^"]*)"/)||[])[1]||'';nFig++;figUse[fm[1]]=(figUse[fm[1]]||0)+1;
      body+=`<figure class="fig" data-fig="${fm[1]}"><figcaption>${inline(alt,w)}</figcaption></figure>`;return}
    const m=ln.match(/^\$\$(.+)\$\$$/);
    if(m){closeList();chk(m[1],true,w);body+=`<div class="tx d">${esc(m[1])}</div>`;return}
    if(ln.startsWith('- ')){if(!list){body+='<ul>';list=true}body+=`<li>${inline(ln.slice(2),w)}</li>`;return}
    if(ln.startsWith('> ')){closeList();body+=`<p class="tip">${inline(ln.slice(2),w)}</p>`;return}
    closeList();body+=`<p>${inline(ln,w)}</p>`});
  closeTopic();
}
const Q=JSON.parse(fs.readFileSync(path.join(__dirname,'../app/data/questions.json')));
const ids=[];Q.subjects.forEach(s=>s.sections.forEach(sec=>sec.topics.forEach(t=>ids.push(t.id))));
const miss=ids.filter(i=>!out[i]);const thin=ids.filter(i=>out[i]&&words[i]<90);
fs.writeFileSync(path.join(__dirname,'../app/data/notes.json'),JSON.stringify(out));
console.log('notes topics',Object.keys(out).length,'/',ids.length,'tex',nTex,'figs placed',nFig,'distinct',Object.keys(figUse).length,'errors',errs);
if(miss.length)console.log('MISSING',miss.join(' '));
if(thin.length)console.log('THIN(<90 words)',thin.map(i=>i+':'+words[i]).join(' '));
const extra=Object.keys(out).filter(i=>!ids.includes(i));if(extra.length)console.log('UNKNOWN IDS',extra.join(' '));
process.exit(errs?1:0);
