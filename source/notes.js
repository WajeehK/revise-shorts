// v11: build app/data/notes.json from src/notes/<topic-id>.md (one file per topic).
// Syntax: @spec / @intro, "# " section, "## " sub-heading, paragraphs, "- " bullets, "1. " steps, "$$...$$",
// "> " callout, "!fig name caption", "| a | b |" tables, and blocks ":::def|eq|ex|warn|tip|sum|prac [title]" ... ":::".
const fs=require('fs'),path=require('path'),katex=require('../tools/node_modules/katex');
const esc=s=>s.replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;');
const FIGS=JSON.parse(fs.readFileSync(path.join(__dirname,'../app/data/figs.json')));
let errs=0,nTex=0,nFig=0;const figUse={},out={},stats={};
function chk(t,d,where){nTex++;try{katex.renderToString(t,{throwOnError:true,displayMode:d,strict:'ignore'})}catch(e){errs++;console.log('TEX ERR',where,t,'::',e.message.slice(0,90))}}
function inline(s,where){return s.split(/(\$[^$]+\$)/).map(p=>{
  if(/^\$[^$]+\$$/.test(p)){const t=p.slice(1,-1);chk(t,false,where);return `<span class="tx">${esc(t)}</span>`}
  return esc(p).replace(/\*\*(.+?)\*\*/g,'<b>$1</b>').replace(/(^|[\s(])_(.+?)_(?=[\s.,;:)]|$)/g,'$1<i>$2</i>').replace(/`(.+?)`/g,'<code>$1</code>')}).join('')}
const BOX={def:['Key definitions','def'],eq:['Key equations','eq'],ex:['Worked example','ex'],warn:['Common mistakes','warn'],tip:['Exam tips','tip'],sum:['Summary','sum'],prac:['Practical skills','prac'],note:['Note','note']};
const ids=[];const Q=JSON.parse(fs.readFileSync(path.join(__dirname,'../app/data/questions.json')));
Q.subjects.forEach(s=>s.sections.forEach(sec=>sec.topics.forEach(t=>ids.push(t.id))));
for(const id of ids){
  const p=path.join(__dirname,'notes',id+'.md');if(!fs.existsSync(p)){console.log('MISSING notes',id);errs++;continue}
  const L=fs.readFileSync(p,'utf8').split('\n');let html='',spec='',intro='',secs=[],nEx=0,words=0,list=null,table=null,box=null,boxBody='',exN=0;
  const emit=h=>{if(box)boxBody+=h;else html+=h};
  const closeList=()=>{if(list){emit(`</${list}>`);list=null}};
  const closeTable=()=>{if(table){emit('<div class="tbl"><table>'+table.map((r,i)=>'<tr>'+r.map(c=>i===0?`<th>${c}</th>`:`<td>${c}</td>`).join('')+'</tr>').join('')+'</table></div>');table=null}};
  const flush=()=>{closeList();closeTable()};
  let secOpen=false;
  L.forEach((raw,i)=>{const w=id+':'+(i+1);const ln=raw.replace(/\s+$/,'').replace(/^\s+(?=- )/,'');
    if(box&&ln===':::'){flush();const [lab,cls]=BOX[box.t];const title=box.t==='ex'?`Worked example ${exN}${box.title?': '+inline(box.title,w):''}`:(box.title?inline(box.title,w):lab);
      html+=`<div class="box ${cls}"><div class="bh">${title}</div>${boxBody}</div>`;box=null;boxBody='';return}
    const bm=ln.match(/^:::(\w+)\s*(.*)$/);
    if(bm){flush();if(!BOX[bm[1]]){errs++;console.log('BAD BOX',w,bm[1])}box={t:bm[1],title:bm[2]};boxBody='';if(bm[1]==='ex'){nEx++;exN++}return}
    if(!ln.trim()){flush();return}
    if(ln.startsWith('@spec ')){spec=ln.slice(6);return}
    if(ln.startsWith('@intro ')){intro=inline(ln.slice(7),w);words+=ln.split(/\s+/).length;return}
    words+=ln.replace(/\$[^$]*\$/g,'x').split(/\s+/).filter(Boolean).length;
    if(ln.startsWith('# ')){flush();if(box){errs++;console.log('UNCLOSED BOX',w)}if(secOpen)html+='</section>';secs.push(ln.slice(2));html+=`<section id="s${secs.length}"><h2><span class="sn">${secs.length}</span>${inline(ln.slice(2),w)}</h2>`;secOpen=true;return}
    if(ln.startsWith('## ')){flush();emit(`<h3>${inline(ln.slice(3),w)}</h3>`);return}
    const fm=ln.match(/^!fig\s+([\w-]+)\s*(.*)$/);
    if(fm){flush();const svg=FIGS[fm[1]];if(!svg){errs++;console.log('FIG MISSING',w,fm[1]);return}
      const alt=fm[2]||(svg.match(/aria-label="([^"]*)"/)||[])[1]||'';nFig++;figUse[fm[1]]=(figUse[fm[1]]||0)+1;
      emit(`<figure class="fig" data-fig="${fm[1]}"><figcaption>${inline(alt,w)}</figcaption></figure>`);return}
    const m=ln.match(/^\$\$(.+)\$\$$/);
    if(m){flush();const parts=[];let d=0,st=0;const t=m[1];for(let i=0;i<t.length;i++){const ch=t[i];if(ch==='{')d++;else if(ch==='}')d--;else if(d===0&&t.startsWith('\\qquad',i)){parts.push(t.slice(st,i));st=i+6;i+=5}}parts.push(t.slice(st));for(let q of parts){q=q.trim().replace(/^,|,$/g,'').trim();if(!q)continue;chk(q,true,w);emit(`<div class="tx d">${esc(q)}</div>`)}return}
    if(ln.startsWith('|')){closeList();const cells=[];let buf='',math=false;const row=ln.replace(/^\||\|$/g,'');
      for(const ch of row){if(ch==='$'){math=!math;buf+=ch}else if(ch==='|'&&!math){cells.push(buf.trim());buf=''}else buf+=ch}
      cells.push(buf.trim());if(cells.every(c=>/^:?-+:?$/.test(c)))return;table=table||[];table.push(cells.map(c=>inline(c,w)));return}
    closeTable();
    if(ln.startsWith('- ')){if(list!=='ul'){closeList();emit('<ul>');list='ul'}emit(`<li>${inline(ln.slice(2),w)}</li>`);return}
    const om=ln.match(/^\d+\.\s+(.*)$/);
    if(om){if(list!=='ol'){closeList();emit('<ol>');list='ol'}emit(`<li>${inline(om[1],w)}</li>`);return}
    closeList();
    if(ln.startsWith('> ')){emit(`<p class="call">${inline(ln.slice(2),w)}</p>`);return}
    if(box&&box.t==='ex'&&/^Q:\s*/.test(ln)){emit(`<p class="exq">${inline(ln.replace(/^Q:\s*/,''),w)}</p>`);return}
    if(box&&box.t==='ex'&&/^A:\s*/.test(ln)){emit(`<p class="exa"><b>Answer:</b> ${inline(ln.replace(/^A:\s*/,''),w)}</p>`);return}
    if(box&&box.t==='def'){const dm=ln.match(/^\*\*(.+?)\*\*:?\s*(.*)$/);if(dm){emit(`<p class="dt"><b>${inline(dm[1],w)}</b> ${inline(dm[2],w)}</p>`);return}}
    emit(`<p>${inline(ln,w)}</p>`)});
  flush();if(box){errs++;console.log('UNCLOSED BOX at end',id)}if(secOpen)html+='</section>';
  const mins=Math.max(1,Math.round(words/180));
  out[id]={h:html,spec,intro,secs,w:words,m:mins,x:nEx};stats[id]=words;
}
fs.writeFileSync(path.join(__dirname,'../app/data/notes.json'),JSON.stringify(out));
const ws=Object.values(stats);const thin=ids.filter(i=>stats[i]!==undefined&&stats[i]<600);
console.log('notes topics',Object.keys(out).length,'/',ids.length,'words total',ws.reduce((a,b)=>a+b,0),'min',Math.min(...ws),'tex',nTex,'figs placed',nFig,'distinct',Object.keys(figUse).length,'errors',errs);
if(thin.length)console.log('UNDER 600 words:',thin.length,thin.map(i=>i+':'+stats[i]).join(' '));
const noex=ids.filter(i=>out[i]&&out[i].x<2);if(noex.length)console.log('FEWER THAN 2 WORKED EXAMPLES:',noex.length);
process.exit(errs?1:0);
