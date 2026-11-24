"""Diaporama autonome avec images locales et commandes accessibles."""
from base64 import b64encode
from pathlib import Path
from html import escape
import streamlit as st
import streamlit.components.v1 as components

@st.cache_data
def _image(nom):
    return "data:image/png;base64," + b64encode((Path(__file__).parent / "assets" / nom).read_bytes()).decode()

def afficher_campagne():
    scenes = [
        ("plantation-cacao.png", "AU CŒUR DES TERROIRS IVOIRIENS", "Chaque récolte<br>porte un avenir.", "Préparez votre campagne cacao avec une vision claire de votre protection.", "Cacaoyers et producteur dans une plantation ivoirienne"),
        ("recolte-cacao.png", "DE LA PLANTATION À LA COOPÉRATIVE", "Une campagne se prépare.<br>Un revenu se protège.", "Quantités livrées, surfaces cultivées : vos données donnent du sens à votre estimation.", "Cabosses et fèves de cacao au moment de la récolte"),
    ]
    slides = ""
    for i, (nom, kicker, titre, texte, alt) in enumerate(scenes):
        actif = 'active' if i == 0 else ''
        hidden = 'false' if i == 0 else 'true'
        slides += f'<section class="slide {actif}" aria-hidden="{hidden}"><img src="{_image(nom)}" alt="{escape(alt)}"><div class="shade"></div><div class="copy"><div class="eyebrow">{kicker}</div><h1>{titre}</h1><p>{texte}</p></div></section>'
    components.html("""<!doctype html><html lang="fr"><head><meta name="viewport" content="width=device-width, initial-scale=1"><style>
    *{box-sizing:border-box}body{margin:0;font-family:'Segoe UI',Arial,sans-serif;background:transparent}
    .campaign{height:435px;position:relative;overflow:hidden;border-radius:20px;background:#102c20;color:white}
    .slide{position:absolute;inset:0;opacity:0;transition:opacity 1s ease;pointer-events:none}.slide.active{opacity:1}
    img{width:100%;height:100%;object-fit:cover;object-position:center}.shade{position:absolute;inset:0;background:linear-gradient(90deg,rgba(5,25,15,.88),rgba(5,25,15,.35) 65%,rgba(5,25,15,.07))}
    .copy{position:absolute;left:5%;right:6%;top:18%;max-width:640px}.eyebrow{font-size:11px;font-weight:700;letter-spacing:.16em;color:#f5c68b}
    h1{font-family:Georgia,serif;font-size:clamp(30px,4.8vw,56px);font-weight:500;line-height:1.08;letter-spacing:-.025em;margin:20px 0 18px}
    p{font-size:15px;line-height:1.7;max-width:450px;color:#f0f2ec;margin:0}.controls{position:absolute;bottom:23px;left:5%;right:5%;display:flex;align-items:center;gap:9px}
    button{border:1px solid #ffffff80;border-radius:50%;width:35px;height:35px;background:#102c2055;color:white;cursor:pointer;font-size:16px}
    button:hover,button:focus-visible{background:#bb5200;outline:2px solid white;outline-offset:2px}.counter{font-size:11px;letter-spacing:.1em;margin:0 8px}.pause{margin-left:auto;width:auto;border-radius:18px;padding:0 15px;font-size:12px}
    .credit{position:absolute;right:5%;top:20px;font-size:9px;letter-spacing:.08em;color:#ffffffb3}
    @media(max-width:600px){.campaign{border-radius:14px}.copy{top:21%;left:7%}h1{font-size:34px}p{font-size:13px;max-width:290px}.eyebrow{font-size:9px}.shade{background:linear-gradient(90deg,#05190fe0,#05190f55)}}
    @media(prefers-reduced-motion:reduce){.slide{transition:none}}
    </style></head><body><div class="campaign" role="region" aria-roledescription="carrousel" aria-label="La campagne cacao">
    """ + slides + """<span class="credit">VISUELS DE CAMPAGNE · IA</span><div class="controls"><button id="prev" aria-label="Image précédente">‹</button><span class="counter" id="counter" aria-live="polite">01 / 02</span><button id="next" aria-label="Image suivante">›</button><button class="pause" id="pause" aria-label="Mettre le défilement en pause">Pause ❚❚</button></div></div>
    <script>
    const slides=Array.from(document.querySelectorAll('.slide'));let index=0,timer=null;
    const reduced=window.matchMedia('(prefers-reduced-motion: reduce)').matches;let paused=reduced;
    const button=document.getElementById('pause');
    function show(n){index=(n+slides.length)%slides.length;slides.forEach((s,i)=>{s.classList.toggle('active',i===index);s.setAttribute('aria-hidden',i!==index)});document.getElementById('counter').textContent=String(index+1).padStart(2,'0')+' / 02'}
    function schedule(){clearInterval(timer);if(!paused)timer=setInterval(()=>show(index+1),6500);button.textContent=paused?'Lecture ▶':'Pause ❚❚';button.setAttribute('aria-label',paused?'Reprendre le défilement':'Mettre le défilement en pause')}
    document.getElementById('prev').onclick=()=>{show(index-1);schedule()};document.getElementById('next').onclick=()=>{show(index+1);schedule()};button.onclick=()=>{paused=!paused;schedule()};schedule();
    document.addEventListener('visibilitychange',()=>{if(document.hidden)clearInterval(timer);else schedule()});
    </script></body></html>""", height=445, scrolling=False)
