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
<p>Soit $f$ la fonction définie sur $[0;+\infty[$ par $f(x)=\dfrac{2x}{x^2+9}$.</p>
<ol>
  <li>Montrer que pour tout $x\geqslant 0$, $f'(x)=\dfrac{2(3+x)(3-x)}{(x^2+9)^2}$.</li>
  <li>En déduire le tableau de variation de la fonction $f$.</li>
</ol>
            """,
            "latex_code": r"""
                         Soit $f$ la fonction définie sur $[0;+\infty[$ par $f(x)=\dfrac{2x}{x^2+9}$.
      \begin{enumerate}
        \item Montrer que pour tout $x\geqslant 0$, $f'(x)=\dfrac{2(3+x)(3-x)}{(x^2+9)^2}$.
        \item En déduire le tableau de variation de la fonction $f$.
      \end{enumerate}
            """,
            "correction": r"""
    <ol>
        <li>
          <p>$f(x)$ est de la forme $\dfrac{u(x)}{v(x)}$ avec $u(x)=2x$ et $v(x)=x^2+9$</p>
      
          <p>On a pour tout $x\in [0;+\infty[$:</p>
          $$f'(x)=\dfrac{u'(x)v(x)-u(x)v'(x)}{v(x)^2}= \dfrac{2(x^2+9)-2x.2x}{(x^2+9)^2}=\dfrac{2x^2+18-4x^2}{(x^2+9)^2}=\dfrac{-2x^2+18}{(x^2+9)^2}$$
      
          <p>Or $2(3+x)(3-x)=2(9-x^2)=18-2x^2$ donc:</p>
          
          <p>pour tout $x\in [0;+\infty[$, $f'(x)=\dfrac{2(3+x)(3-x)}{(x^2+9)^2}$.</p>
        </li>
      
        <li>
          <p>Les racines de $18-2x^2$ sont $3$ et $-3$. On en déduit le tableau de variation de $f$:</p>
          
          <div class="has-text-centered" style="display: block; margin: 0 auto;">
            <svg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='255.519942pt' height='577.83437pt' viewBox='76.710908 52.800748 255.519942 577.83437'>
                <defs>
                <font id='cmsy10' horiz-adv-x='0'>
                <font-face font-family='cmsy10' units-per-em='1000' ascent='775' descent='960'/>
                <glyph unicode='−' horiz-adv-x='777' vert-adv-y='777' glyph-name='minus' d='M659 230C676 230 694 230 694 250S676 270 659 270H118C101 270 83 270 83 250S101 230 118 230H659Z'/>
                <glyph unicode='∞' horiz-adv-x='1000' vert-adv-y='1000' glyph-name='infinity' d='M508 271C454 339 442 354 411 379C355 424 299 442 248 442C131 442 55 332 55 215C55 100 129-11 244-11S442 80 491 160C545 92 557 77 588 52C644 7 700-11 751-11C868-11 944 99 944 216C944 331 870 442 755 442S557 351 508 271ZM534 237C575 309 649 410 762 410C868 410 922 306 922 216C922 118 855 37 767 37C709 37 664 79 643 100C618 127 595 158 534 237ZM465 194C424 122 350 21 237 21C131 21 77 125 77 215C77 313 144 394 232 394C290 394 335 352 356 331C381 304 404 273 465 194Z'/>
                </font>
                <font id='cmr10' horiz-adv-x='0'>
                <font-face font-family='cmr10' units-per-em='1000' ascent='750' descent='250'/>
                <glyph unicode='(' horiz-adv-x='388' vert-adv-y='388' glyph-name='parenleft' d='M331-240C331-237 331-235 314-218C189-92 157 97 157 250C157 424 195 598 318 723C331 735 331 737 331 740C331 747 327 750 321 750C311 750 221 682 162 555C111 445 99 334 99 250C99 172 110 51 165-62C225-185 311-250 321-250C327-250 331-247 331-240Z'/>
                <glyph unicode=')' horiz-adv-x='388' vert-adv-y='388' glyph-name='parenright' d='M289 250C289 328 278 449 223 562C163 685 77 750 67 750C61 750 57 746 57 740C57 737 57 735 76 717C174 618 231 459 231 250C231 79 194-97 70-223C57-235 57-237 57-240C57-246 61-250 67-250C77-250 167-182 226-55C277 55 289 166 289 250Z'/>
                <glyph unicode='+' horiz-adv-x='777' vert-adv-y='777' glyph-name='plus' d='M409 230H688C702 230 721 230 721 250S702 270 688 270H409V550C409 564 409 583 389 583S369 564 369 550V270H89C75 270 56 270 56 250S75 230 89 230H369V-50C369-64 369-83 389-83S409-64 409-50V230Z'/>
                <glyph unicode='0' horiz-adv-x='500' vert-adv-y='500' glyph-name='zero' d='M460 320C460 400 455 480 420 554C374 650 292 666 250 666C190 666 117 640 76 547C44 478 39 400 39 320C39 245 43 155 84 79C127-2 200-22 249-22C303-22 379-1 423 94C455 163 460 241 460 320ZM249 0C210 0 151 25 133 121C122 181 122 273 122 332C122 396 122 462 130 516C149 635 224 644 249 644C282 644 348 626 367 527C377 471 377 395 377 332C377 257 377 189 366 125C351 30 294 0 249 0Z'/>
                <glyph unicode='1' horiz-adv-x='500' vert-adv-y='500' glyph-name='one' d='M294 640C294 664 294 666 271 666C209 602 121 602 89 602V571C109 571 168 571 220 597V79C220 43 217 31 127 31H95V0C130 3 217 3 257 3S384 3 419 0V31H387C297 31 294 42 294 79V640Z'/>
                <glyph unicode='3' horiz-adv-x='500' vert-adv-y='500' glyph-name='three' d='M290 352C372 379 430 449 430 528C430 610 342 666 246 666C145 666 69 606 69 530C69 497 91 478 120 478C151 478 171 500 171 529C171 579 124 579 109 579C140 628 206 641 242 641C283 641 338 619 338 529C338 517 336 459 310 415C280 367 246 364 221 363C213 362 189 360 182 360C174 359 167 358 167 348C167 337 174 337 191 337H235C317 337 354 269 354 171C354 35 285 6 241 6C198 6 123 23 88 82C123 77 154 99 154 137C154 173 127 193 98 193C74 193 42 179 42 135C42 44 135-22 244-22C366-22 457 69 457 171C457 253 394 331 290 352Z'/>
                </font>
                <font id='cmsy7' horiz-adv-x='0'>
                <font-face font-family='cmsy7' units-per-em='1000' ascent='782' descent='951'/>
                <glyph unicode='' horiz-adv-x='329' vert-adv-y='329' glyph-name='prime' d='M290 472C298 489 299 497 299 504C299 535 271 559 240 559C202 559 190 528 185 512L53 79C52 77 48 64 48 63C48 51 79 41 87 41C94 41 95 43 102 58L290 472Z'/>
                </font>
                <font id='cmmi10' horiz-adv-x='0'>
                <font-face font-family='cmmi10' units-per-em='1000' ascent='750' descent='250'/>
                <glyph unicode='f' horiz-adv-x='489' vert-adv-y='489' glyph-name='f' d='M367 400H453C473 400 483 400 483 420C483 431 473 431 456 431H373L394 545C398 566 412 637 418 649C427 668 444 683 465 683C469 683 495 683 514 665C470 661 460 626 460 611C460 588 478 576 497 576C523 576 552 598 552 636C552 682 506 705 465 705C431 705 368 687 338 588C332 567 329 557 305 431H236C217 431 206 431 206 412C206 400 215 400 234 400H300L225 5C207-92 190-183 138-183C134-183 109-183 90-165C136-162 145-126 145-111C145-88 127-76 108-76C82-76 53-98 53-136C53-181 97-205 138-205C193-205 233-146 251-108C283-45 306 76 307 83L367 400Z'/>
                <glyph unicode='x' horiz-adv-x='571' vert-adv-y='571' glyph-name='x' d='M334 302C340 328 363 420 433 420C438 420 462 420 483 407C455 402 435 377 435 353C435 337 446 318 473 318C495 318 527 336 527 376C527 428 468 442 434 442C376 442 341 389 329 366C304 432 250 442 221 442C117 442 60 313 60 288C60 278 70 278 72 278C80 278 83 280 85 289C119 395 185 420 219 420C238 420 273 411 273 353C273 322 256 255 219 115C203 53 168 11 124 11C118 11 95 11 74 24C99 29 121 50 121 78C121 105 99 113 84 113C54 113 29 87 29 55C29 9 79-11 123-11C189-11 225 59 228 65C240 28 276-11 336-11C439-11 496 118 496 143C496 153 487 153 484 153C475 153 473 149 471 142C438 35 370 11 338 11C299 11 283 43 283 77C283 99 289 121 300 165L334 302Z'/>
                </font>
                </defs>
                <style type='text/css'>
                <![CDATA[text.f0 {font-family:cmsy10;font-size:9.96264px}
                text.f1 {fill:#3e8ed0;font-family:cmsy7;font-size:6.973848px}
                text.f2 {fill:#3e8ed0;font-family:cmmi10;font-size:9.96264px}
                text.f3 {fill:#3e8ed0;font-family:cmr10;font-size:9.96264px}
                ]]>
                </style>
                <g id='page1'>
                <text class='f2' x='96.741878' y='53.001242' transform='matrix(1 0 0 1 5.6693 16.3182)'>x</text>
                <text class='f2' x='88.494987' y='53.001242' transform='matrix(1 0 0 1 5.6693 45.0198)'>f</text>
                <text class='f1' x='94.444934' y='49.385878' transform='matrix(1 0 0 1 5.6693 45.0198)'></text>
                <text class='f3' x='97.24001' y='53.001242' transform='matrix(1 0 0 1 5.6693 45.0198)'>(</text>
                <text class='f2' x='101.114384' y='53.001242' transform='matrix(1 0 0 1 5.6693 45.0198)'>x</text>
                <text class='f3' x='106.808316' y='53.001242' transform='matrix(1 0 0 1 5.6693 45.0198)'>)</text>
                <text class='f2' x='89.892533' y='53.001242' transform='matrix(1 0 0 1 5.6693 73.3578)'>f</text>
                <text class='f3' x='95.84248' y='53.001242' transform='matrix(1 0 0 1 5.6693 73.3578)'>(</text>
                <text class='f2' x='99.716854' y='53.001242' transform='matrix(1 0 0 1 5.6693 73.3578)'>x</text>
                <text class='f3' x='105.410786' y='53.001242' transform='matrix(1 0 0 1 5.6693 73.3578)'>)</text>
                <path d='M76.910158 81.3477H332.0316' stroke='#3e8ed0' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
                <path d='M76.910158 109.6953H332.0316' stroke='#3e8ed0' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
                <path d='M76.910158 138.043H332.0316' stroke='#3e8ed0' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
                <path d='M76.910158 52.999998V138.043H332.0316V52.999998Z' stroke='#3e8ed0' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
                <path d='M133.6055 52.999998V138.043' stroke='#3e8ed0' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
                <text class='f3' x='76.911579' y='53.001242' transform='matrix(1 0 0 1 68.3764 17.3836)'>0</text>
                <text class='f3' x='76.911579' y='53.001242' transform='matrix(1 0 0 1 153.4164 17.3836)'>3</text>
                <text class='f3' x='76.911579' y='53.001242' transform='matrix(1 0 0 1 232.0924 16.6641)'>+</text>
                <text class='f0' x='84.660326' y='53.001242' transform='matrix(1 0 0 1 232.0924 16.6641)'>∞</text>
                <text class='f3' x='76.911579' y='53.001242' transform='matrix(1 0 0 1 109.5124 45.0109)'>+</text>
                <path d='M232.8206 81.3477V109.6953' stroke='#3e8ed0' fill='none' stroke-width='.3985' stroke-miterlimit='10' stroke-dasharray='.3985 1.99255'/>
                <text class='f3' x='76.911579' y='53.001242' transform='matrix(1 0 0 1 153.4164 45.7304)'>0</text>
                <text class='f0' x='76.911579' y='53.001242' transform='matrix(1 0 0 1 194.5534 45.0109)'>−</text>
                <text class='f2' x='76.911579' y='53.001242' transform='matrix(1 0 0 1 146.5674 76.5718)'>f</text>
                <text class='f3' x='82.861526' y='53.001242' transform='matrix(1 0 0 1 146.5674 76.5718)'>(3)</text>
                <text class='f2' x='76.911579' y='53.001242' transform='matrix(1 0 0 1 146.5674 76.5718)'>f</text>
                <text class='f3' x='82.861526' y='53.001242' transform='matrix(1 0 0 1 146.5674 76.5718)'>(3)</text>
                <path d='M155.3984 116.6953L215.1486 124.7148' stroke='#3e8ed0' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
                <path d='M217.51912 125.031694C216.55819 124.703572 214.831622 124.066854 213.769127 123.019968C214.608968 124.238727 214.503499 125.027785 213.37068 125.984818C214.675367 125.254347 216.503489 125.098098 217.51912 125.031694Z'/>
                <path d='M248.1176 125.0312L307.8716 117.0117' stroke='#3e8ed0' fill='none' stroke-width='.3985' stroke-miterlimit='10'/>
                <path d='M310.238772 116.695166C309.227066 116.628758 307.39503 116.47251 306.090353 115.742046C307.223163 116.695163 307.332527 117.48814 306.488769 118.70689C307.555197 117.656103 309.277834 117.023297 310.238772 116.695166Z'/>
                <text class='f3' x='231.13325' y='630.635118'>1</text>
                </g>
                </svg>
          </div>
        </li>
      </ol>

            """,
            "latex_correction": r"""

      \begin{enumerate}
        \item $f(x)$ est de la forme $\dfrac{u(x)}{v(x)}$ avec $\begin{dcases}
          u(x)=2x\\
          v(x)=x^2+9
        \end{dcases}$

        On a pour tout $x\in [0;+\infty[$:
        $$f'(x)=\dfrac{u'(x)v(x)-u(x)v'(x)}{v(x)^2}= \dfrac{2(x^2+9)-2x.2x}{(x^2+9)^2}=\dfrac{2x^2+18-4x^2}{(x^2+9)^2}=\dfrac{-2x^2+18}{(x^2+9)^2}$$

        Or $2(3+x)(3-x)=2(9-x^2)=18-2x^2$ donc:
        
        pour tout $x\in [0;+\infty[$, $f'(x)=\dfrac{2(3+x)(3-x)}{(x^2+9)^2}$.

        \item Les racines de $18-2x^2$ sont $3$ et $-3$. On en déduit le tableau de variation de $f$:
        
        \begin{center}
          \begin{tikzpicture}
            \tkzTabInit{$x$ / 1 , $f'(x)$ / 1, $f(x)$ / 1}{$0$, $3$, $+\infty$}
            \tkzTabLine{, +, z, -,}
            \tkzTabVar{+/$~$, -/$f(3)$, +/$~$}
          \end{tikzpicture}
        \end{center}
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