import sys,asyncio,importlib
sys.path.insert(0,'src/figs')
mods=sys.argv[1].split(','); per=int(sys.argv[2]) if len(sys.argv)>2 else 6
F={}
for m in mods: F.update(importlib.import_module(m).F)
names=[n for n in F if len(sys.argv)<4 or n in sys.argv[3].split(',')]
from playwright.async_api import async_playwright
async def main():
  async with async_playwright() as p:
    br=await p.chromium.launch(executable_path='/usr/bin/google-chrome'); pg=await br.new_page(viewport={'width':740,'height':400})
    for i in range(0,len(names),per):
      ch=names[i:i+per]
      html='<body style="margin:0;background:#c9ecfd;display:flex;flex-wrap:wrap;gap:6px;padding:6px;width:728px">'+''.join(f'<div style="width:358px;font:11px sans-serif">{n}{F[n]}</div>' for n in ch)+'</body>'
      await pg.set_content(html); await pg.screenshot(path=f'/tmp/sheet_{mods[0]}_{i//per}_{len(sys.argv)}{abs(hash(str(sys.argv)))%9999}.png',full_page=True)
    await br.close()
asyncio.run(main()); print(len(names))
