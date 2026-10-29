from pathlib import Path
import json,shutil,argparse
R=Path(__file__).resolve().parent;C=R/'content';D=R/'dist';cfg=json.loads((C/'site.json').read_text(encoding='utf-8'))
p=argparse.ArgumentParser();p.add_argument('--release',action='store_true');args=p.parse_args()
if args.release and not cfg['publication_approved']:raise SystemExit('Public release has not been approved.')
D.mkdir(exist_ok=True);shutil.copytree(C/'assets',D/'assets',dirs_exist_ok=True)
for name in ['style.css','blocks.css','video-player.js']:shutil.copy2(R/name,D/name)
shutil.copytree(R/'fonts',D/'fonts',dirs_exist_ok=True)
def page(title,body,active=''):
 nav=''.join('<a href="'+url+'"'+(' aria-current="page"' if active==label else '')+'>'+label+'</a>' for label,url in [('首页','index.html'),('摄影','photography.html'),('文字','writing.html')])
 return '<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'+('' if args.release else '<meta name="robots" content="noindex,nofollow">')+'<meta name="description" content="Pscbo1 的照片与文字。"><title>'+title+' · Pscbo1</title><link rel="stylesheet" href="fonts/original-google-fonts.css"><link rel="stylesheet" href="blocks.css"><link rel="stylesheet" href="style.css"></head><body><a class="skip" href="#main">跳到内容</a><header class="masthead"><a class="wordmark" href="index.html">PSCBO1</a><nav class="site-nav" aria-label="主导航">'+nav+'</nav></header><main class="layout" id="main">'+body+'</main><footer class="footer"><span>Pscbo1</span></footer><script src="video-player.js" defer></script></body></html>'
def save(name,title,body,active=''):(D/name).write_text(page(title,body,active),encoding='utf-8')
save('index.html','首页','<div class="photo-stream home-stream">'+(C/'home.html').read_text(encoding='utf-8')+'</div><div class="collection-note"><a href="photography.html">更多摄影 →</a></div>','首页')
film='<section class="film" id="film"><h2>风筝节</h2><video controls playsinline preload="none" poster="'+cfg['kite_poster']+'" src="'+cfg['kite_video']+'">你的浏览器不支持视频播放。<a href="'+cfg['kite_video']+'">打开视频</a></video></section>'
film += '<section class="film" id="new-year-2024"><h2>深山拜年</h2><p>2024</p><div class="embedded-video"><button class="video-poster" type="button" aria-label="播放2024深山拜年视频"><img src="assets/new-year-2024-poster.jpg" alt="深山拜年视频中的山林"><span class="play-icon" aria-hidden="true">▶</span></button></div><div class="video-options"><a href="https://www.bilibili.com/video/BV1JD421E7t3/" target="_blank" rel="noopener noreferrer">在 Bilibili 观看 ↗</a><a href="https://www.youtube.com/watch?v=IiDuY4scFeY" target="_blank" rel="noopener noreferrer">在 YouTube 观看 ↗</a></div></section>'
save('photography.html','摄影','<h1 class="section-title">PHOTOGRAPHY</h1><div class="photo-stream">'+(C/'photography.html').read_text(encoding='utf-8')+'</div>'+film,'摄影')
save('writing.html','文字','<h1 class="section-title">文字</h1><div class="writing-list"><article><span class="meta">随笔 · 2020</span><h2><a href="village.html">小村记述</a></h2><p>是这样的一个小村。是众多小村里的一个。</p></article><article><span class="meta">译文 · 2023</span><h2><a href="translation.html">Patriarchy · 译文</a></h2><p class="source-line">原文来源：National Geographic</p></article></div>','文字')
for slug,title in [('village','小村记述'),('translation','Patriarchy · 译文')]:save(slug+'.html',title,'<article class="reading"><a class="back" href="writing.html">← 全部文字</a><h1>'+title+'</h1>'+(C/(slug+'.html')).read_text(encoding='utf-8')+'</article>','文字')
(D/'.nojekyll').write_text('',encoding='utf-8');(D/'robots.txt').write_text('User-agent: *\n'+('Allow: /\n' if args.release else 'Disallow: /\n'),encoding='utf-8')
print('Built 5 pages. Deployment is a separate step.')
