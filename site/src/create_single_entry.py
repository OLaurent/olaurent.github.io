from app import app, db
from models import Exercice
import uuid

# Créez la base de données et les tables
with app.app_context():

    # Données à ajouter
    exercices_data = [
        {
            "id": str(uuid.uuid4()),
            "level": "Première",
            "theme": "Applications de la dérivation",
            "selected" : False, 
            "content": r"""
            <p>Soit $h$ la fonction définie sur $[2;+\infty[$ par $h(x)=x^3+3x^2-9x-1$.</p>
            <ol>
              <li>Dresser le tableau de variations de la fonction $h$.</li>
              <li>En déduire que pour tout $x\geqslant 2$, $x^3\geqslant -3x^2+9x+2$.</li>
            </ol>
            """,
            "latex_code": r"""
                    Soit $h$ la fonction définie sur $[2;+\infty[$ par $h(x)=x^3+3x^2-9x-1$.
  
  \begin{enumerate}
    \item Dresser le tableau de variations de la fonction $h$.
    \item En déduire que pour tout $x\geqslant 2$, $x^3\geqslant -3x^2+9x+2$.
  \end{enumerate}
            """,
            "correction": r"""
            <ol>
  <li>
    <p>Pour dresser le tableau de variations de la fonction $h$, on commence par calculer la dérivée de $h$.</p>
    
    <p>Pour tout $x\in[2;+\infty[$, on a:</p>
    $$h'(x)=3x^2+6x-9$$

    <p>On cherche les valeurs de $x$ pour lesquelles $h'(x)=0$.</p>

    <p>On calcule le discriminant de $h'$: $\Delta = 6^2-4\times 3\times (-9)=36+108=144$. $\Delta$ est strictement positif, donc l'équation $h'(x)=0$ admet deux solutions réelles distinctes:</p>
    $$x_1=\dfrac{-6-\sqrt{144}}{2\times 3}=-3 \quad \text{et} \quad x_2=\dfrac{-6+\sqrt{144}}{2\times 3}=1$$

    <p>Ces deux racines ne sont pas dans l'intervalle $[2;+\infty[$, donc $h'(x)$ ne s'annule pas sur cet intervalle et est positive sur cet intervalle.</p>

    <p>On en déduit le tableau de variations suivant:</p>
   
    
      <div class="text-center">

      <svg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='170.480485pt' height='85.437585pt' viewBox='-72.000035 -72.000035 170.480485 85.437585'>
<defs>
<font id='cmsy10' horiz-adv-x='0'>
<font-face font-family='cmsy10' units-per-em='1000' ascent='775' descent='960'/>
<glyph unicode='∞' horiz-adv-x='1000' vert-adv-y='1000' glyph-name='infinity' d='M508 271C454 339 442 354 411 379C355 424 299 442 248 442C131 442 55 332 55 215C55 100 129-11 244-11S442 80 491 160C545 92 557 77 588 52C644 7 700-11 751-11C868-11 944 99 944 216C944 331 870 442 755 442S557 351 508 271ZM534 237C575 309 649 410 762 410C868 410 922 306 922 216C922 118 855 37 767 37C709 37 664 79 643 100C618 127 595 158 534 237ZM465 194C424 122 350 21 237 21C131 21 77 125 77 215C77 313 144 394 232 394C290 394 335 352 356 331C381 304 404 273 465 194Z'/>
</font>
<font id='cmr10' horiz-adv-x='0'>
<font-face font-family='cmr10' units-per-em='1000' ascent='750' descent='250'/>
<glyph unicode='(' horiz-adv-x='388' vert-adv-y='388' glyph-name='parenleft' d='M331-240C331-237 331-235 314-218C189-92 157 97 157 250C157 424 195 598 318 723C331 735 331 737 331 740C331 747 327 750 321 750C311 750 221 682 162 555C111 445 99 334 99 250C99 172 110 51 165-62C225-185 311-250 321-250C327-250 331-247 331-240Z'/>
<glyph unicode=')' horiz-adv-x='388' vert-adv-y='388' glyph-name='parenright' d='M289 250C289 328 278 449 223 562C163 685 77 750 67 750C61 750 57 746 57 740C57 737 57 735 76 717C174 618 231 459 231 250C231 79 194-97 70-223C57-235 57-237 57-240C57-246 61-250 67-250C77-250 167-182 226-55C277 55 289 166 289 250Z'/>
<glyph unicode='+' horiz-adv-x='777' vert-adv-y='777' glyph-name='plus' d='M409 230H688C702 230 721 230 721 250S702 270 688 270H409V550C409 564 409 583 389 583S369 564 369 550V270H89C75 270 56 270 56 250S75 230 89 230H369V-50C369-64 369-83 389-83S409-64 409-50V230Z'/>
<glyph unicode='1' horiz-adv-x='500' vert-adv-y='500' glyph-name='one' d='M294 640C294 664 294 666 271 666C209 602 121 602 89 602V571C109 571 168 571 220 597V79C220 43 217 31 127 31H95V0C130 3 217 3 257 3S384 3 419 0V31H387C297 31 294 42 294 79V640Z'/>
<glyph unicode='2' horiz-adv-x='500' vert-adv-y='500' glyph-name='two' d='M127 77L233 180C389 318 449 372 449 472C449 586 359 666 237 666C124 666 50 574 50 485C50 429 100 429 103 429C120 429 155 441 155 482C155 508 137 534 102 534C94 534 92 534 89 533C112 598 166 635 224 635C315 635 358 554 358 472C358 392 308 313 253 251L61 37C50 26 50 24 50 0H421L449 174H424C419 144 412 100 402 85C395 77 329 77 307 77H127Z'/>
</font>
<font id='cmsy7' horiz-adv-x='0'>
<font-face font-family='cmsy7' units-per-em='1000' ascent='782' descent='951'/>
<glyph unicode='' horiz-adv-x='329' vert-adv-y='329' glyph-name='prime' d='M290 472C298 489 299 497 299 504C299 535 271 559 240 559C202 559 190 528 185 512L53 79C52 77 48 64 48 63C48 51 79 41 87 41C94 41 95 43 102 58L290 472Z'/>
</font>
<font id='cmmi10' horiz-adv-x='0'>
<font-face font-family='cmmi10' units-per-em='1000' ascent='750' descent='250'/>
<glyph unicode='h' horiz-adv-x='576' vert-adv-y='576' glyph-name='h' d='M287 683C287 684 287 694 274 694C251 694 178 686 152 684C144 683 133 682 133 664C133 652 142 652 157 652C205 652 207 645 207 635L204 615L59 39C55 25 55 23 55 17C55-6 75-11 84-11C100-11 116 1 121 15L140 91L162 181C168 203 174 225 179 248C181 254 189 287 190 293C193 302 224 358 258 385C280 401 311 420 354 420S408 386 408 350C408 296 370 187 346 126C338 103 333 91 333 71C333 24 368-11 415-11C509-11 546 135 546 143C546 153 537 153 534 153C524 153 524 150 519 135C504 82 472 11 417 11C400 11 393 21 393 44C393 69 402 93 411 115C427 158 472 277 472 335C472 400 432 442 357 442C294 442 246 411 209 365L287 683Z'/>
<glyph unicode='x' horiz-adv-x='571' vert-adv-y='571' glyph-name='x' d='M334 302C340 328 363 420 433 420C438 420 462 420 483 407C455 402 435 377 435 353C435 337 446 318 473 318C495 318 527 336 527 376C527 428 468 442 434 442C376 442 341 389 329 366C304 432 250 442 221 442C117 442 60 313 60 288C60 278 70 278 72 278C80 278 83 280 85 289C119 395 185 420 219 420C238 420 273 411 273 353C273 322 256 255 219 115C203 53 168 11 124 11C118 11 95 11 74 24C99 29 121 50 121 78C121 105 99 113 84 113C54 113 29 87 29 55C29 9 79-11 123-11C189-11 225 59 228 65C240 28 276-11 336-11C439-11 496 118 496 143C496 153 487 153 484 153C475 153 473 149 471 142C438 35 370 11 338 11C299 11 283 43 283 77C283 99 289 121 300 165L334 302Z'/>
</font>
</defs>
<style type='text/css'>
<![CDATA[text.f0 {font-family:cmsy10;font-size:9.96264px}
text.f1 {font-family:cmsy7;font-size:6.973848px}
text.f2 {font-family:cmmi10;font-size:9.96264px}
text.f3 {font-family:cmr10;font-size:9.96264px}
]]>
</style>
<g id='page1'>
<text class='f2' x='-51.970455' y='-71.800754' transform='matrix(1 0 0 1 5.6693 16.3182)'>x</text>
<text class='f2' x='-60.112393' y='-71.800754' transform='matrix(1 0 0 1 5.6693 45.0198)'>h</text>
<text class='f1' x='-54.372323' y='-75.416118' transform='matrix(1 0 0 1 5.6693 45.0198)'></text>
<text class='f3' x='-51.577248' y='-71.800754' transform='matrix(1 0 0 1 5.6693 45.0198)'>(</text>
<text class='f2' x='-47.702874' y='-71.800754' transform='matrix(1 0 0 1 5.6693 45.0198)'>x</text>
<text class='f3' x='-42.008942' y='-71.800754' transform='matrix(1 0 0 1 5.6693 45.0198)'>)</text>
<text class='f2' x='-58.714863' y='-71.800754' transform='matrix(1 0 0 1 5.6693 73.3577)'>h</text>
<text class='f3' x='-52.974793' y='-71.800754' transform='matrix(1 0 0 1 5.6693 73.3577)'>(</text>
<text class='f2' x='-49.100419' y='-71.800754' transform='matrix(1 0 0 1 5.6693 73.3577)'>x</text>
<text class='f3' x='-43.406487' y='-71.800754' transform='matrix(1 0 0 1 5.6693 73.3577)'>)</text>
<path d='M-71.800785-43.4531H98.2812' stroke='#000' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
<path d='M-71.800785-15.1055H98.2812' stroke='#000' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
<path d='M-71.800785 13.2383H98.2812' stroke='#000' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
<path d='M-71.800785-71.800785V13.2383H98.2812V-71.800785Z' stroke='#000' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
<path d='M-15.1055-71.800785V13.2383' stroke='#000' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
<text class='f3' x='-71.800754' y='-71.800754' transform='matrix(1 0 0 1 68.37633 17.3836)'>2</text>
<text class='f3' x='-71.800754' y='-71.800754' transform='matrix(1 0 0 1 147.0517 16.6641)'>+</text>
<text class='f0' x='-64.052007' y='-71.800754' transform='matrix(1 0 0 1 147.0517 16.6641)'>∞</text>
<text class='f3' x='-71.800754' y='-71.800754' transform='matrix(1 0 0 1 109.5128 45.0109)'>+</text>
<path d='M-5.418 9.2539H3.5508V-1.1523H-5.418Z' fill='#fff'/>
<text class='f3' x='-71.800754' y='-71.800754' transform='matrix(1 0 0 1 68.37632 79.06276)'>1</text>
<path d='M-5.418 9.2539H3.5508V-1.1523H-5.418Z' fill='#fff'/>
<text class='f3' x='-71.800754' y='-71.800754' transform='matrix(1 0 0 1 68.37632 79.06276)'>1</text>
<path d='M80.4532-7.1367H87.7582V-11.1211H80.4532Z' fill='#fff'/>
<path d='M80.4532-7.1367H87.7582V-11.1211H80.4532Z' fill='#fff'/>
<path d='M7.5117 2.7422L74.1292-7.5859' stroke='#000' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
<path d='M76.492187-7.949219C75.47656-7.996094 73.644538-8.113281 72.324225-8.816405C73.476569-7.88672 73.601567-7.097657 72.781247-5.863278C73.828132-6.933595 75.53907-7.601564 76.492187-7.949219Z'/>
</g>
</svg>
    </div>


  </li>

  <li>
    <p>D'après la question précédente, pour tout $x\in[2;+\infty[$, $h(x)\geqslant 1$.</p>
    
    \begin{align}
     & h(x) \geqslant 1 \\
     \iff & x^3+3x^2-9x-1 \geqslant 1 \\
      \iff & x^3 \geqslant -3x^2+9x+1 +1  \\
      \iff & x^3 \geqslant -3x^2+9x+2
    \end{align}

    <p>On a donc pour tout $x\in[2;+\infty[$, $x^3\geqslant -3x^2+9x+2$.</p>
  </li>
</ol>
            """,
            "latex_correction": r"""
  \begin{enumerate}
    \item Pour dresser le tableau de variations de la fonction $h$, on commence par calculer la dérivée de $h$.
    
    Pour tout $x\in[2;+\infty[$, on a:
    $$h'(x)=3x^2+6x-9$$

    On cherche les valeurs de $x$ pour lesquelles $h'(x)=0$. 

    On calcule le discriminant de $h'$:  $\Delta = 6^2-4\times 3\times (-9)=36+108=144$.  $\Delta$ est strictement positif, donc l'équation $h'(x)=0$ admet deux solutions réelles distinctes:
    $$x_1=\dfrac{-6-\sqrt{144}}{2\times 3}=-3 \quad \text{et} \quad x_2=\dfrac{-6+\sqrt{144}}{2\times 3}=1$$

    Ces deux racines ne sont pas dans l'intervalle $[2;+\infty[$, donc $h'(x)$ ne s'annule pas sur cet intervalle et est positive sur cet intervalle.

    On en déduit le tableau de variations suivant:
    \begin{center}
      \begin{tikzpicture}
        \tkzTabInit{$x$ / 1 , $h'(x)$ / 1, $h(x)$ / 1}{$2$, $+\infty$}
        \tkzTabLine{, +,}
        \tkzTabVar{-/$1$, +/$~$}
      \end{tikzpicture}
    \end{center}


    \item D'après la question précédente, pour tout $x\in[2;+\infty[$, $h(x)\geqslant 1$.
    
    \begin{flalign*}
     & h(x) \geqslant 1 \\
     \iff & x^3+3x^2-9x-1 \geqslant 1 \\
      \iff & x^3 \geqslant -3x^2+9x+1 +1  \\
      \iff & x^3 \geqslant -3x^2+9x+2
    \end{flalign*}

    On a donc pour tout $x\in[2;+\infty[$, $x^3\geqslant -3x^2+9x+2$.


  \end{enumerate}
            """
        }
    ]

    # Ajouter les données à la base de données
    for exercice_data in exercices_data:
        exercice = Exercice(**exercice_data)
        db.session.add(exercice)

    # Valider les changements
    db.session.commit()

    print("Entrée ajoutée !")