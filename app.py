from flask import Flask, render_template, redirect, request
import uuid

app = Flask(__name__)
app.debug = True


exercices = [
    {
        "id": str(uuid.uuid4()),
        "level": "Première",
        "theme": "Suites numériques",
        "selected" : False, 
        "content": r"""
        <p>Soit $(u_n)$ la suite définie pour $n \in \mathbb{N}$ par $u_n=-8 \times 0,9^n + 15$.</p>
        <ol>
            <li>Montrer que la suite $(u_n)$ est croissante.</li>
            <li>À l'aide de la calculatrice, déterminer le rang $n$ à partir duquel $u_n>14,5$.</li>
        </ol>
        """,
        "latexCode": r"""
                Soit $(u_n)$ la suite définie pour $n \in \N$ par $u_n=-8\times0,9^n+15$.
        \begin{enumerate}
        \item Montrer que la suite $(u_n)$ est croissante.
        \item \`A l'aide de la calculatrice, déterminer le rang $n$ à partir duquel $u_n>14,5$.
        \end{enumerate}"
        """,
        "correction": r"""
        <p>Correction de l'exercice 1</p>
        """,
        "latexCorrection": r"""
        Correction de l'exercice 1
        """
    },
    {
        "id": str(uuid.uuid4()),
        "level": "Première",
        "theme": "Suites numériques",
        "selected" : True, 
        "content": r"""
        <p>Soit $(v_n)$ la suite définie pour $n \in \mathbb{N}$ par $v_n=n^2-11n+10$.</p>
        <ol>
            <li>Montrer que $v_{n+1}-v_n=2n-10$.</li>
            <li>Résoudre l'inéquation $2n-10\geqslant 0$ et en déduire que la suite $(v_n)$ est monotone à partir d'un certain rang que l'on précisera.</li>
        </ol>
        """,
        "latexCode": r"""
        Soit $(v_n)$ la suite définie pour $n \in \N$ par $v_n=n^2-11n+10$.
        \begin{enumerate}
            \item Montrer que $v_{n+1}-v_n=2n-10$.
            \item Résoudre l'inéquation $2n-10\geqslant 0$ et en déduire que la suite $(v_n)$ est monotone à partir d'un certain rang que l'on précisera.
        \end{enumerate}
        """,
        "correction": r"""
        <p>Correction de l'exercice 2</p>
        """,
        "latexCorrection": r"""
        Correction de l'exercice 2
        """
    },
    {
        "id": str(uuid.uuid4()),
        "level": "Première",
        "theme": "Dérivation",
        "selected" : False, 
        "content": r"""
        <p>Un exercice bidon de dérivation.</p>
        <svg version='1.1' xmlns='http://www.w3.org/2000/svg' xmlns:xlink='http://www.w3.org/1999/xlink' width='9.674436pt' height='5.783849pt' viewBox='-63.593206 -37.972954 9.674436 5.783849'>
<defs>
<font id='cmr7' horiz-adv-x='0'>
<font-face font-family='cmr7' units-per-em='1000' ascent='750' descent='250'/>
<glyph unicode='1' horiz-adv-x='569' vert-adv-y='569' glyph-name='one' d='M335 636C335 663 333 664 305 664C241 601 150 600 109 600V564C133 564 199 564 254 592V82C254 49 254 36 154 36H116V0C134 1 257 4 294 4C325 4 451 1 473 0V36H435C335 36 335 49 335 82V636Z'/>
<glyph unicode='2' horiz-adv-x='569' vert-adv-y='569' glyph-name='two' d='M505 182H471C468 160 458 101 445 91C437 85 360 85 346 85H162C267 178 302 206 362 253C436 312 505 374 505 469C505 590 399 664 271 664C147 664 63 577 63 485C63 434 106 429 116 429C140 429 169 446 169 482C169 500 162 535 110 535C141 606 209 628 256 628C356 628 408 550 408 469C408 382 346 313 314 277L73 39C63 30 63 28 63 0H475L505 182Z'/>
<glyph unicode='3' horiz-adv-x='569' vert-adv-y='569' glyph-name='three' d='M273 334C351 334 407 280 407 173C407 49 335 12 277 12C237 12 149 23 107 82C154 84 165 117 165 138C165 170 141 193 110 193C82 193 54 176 54 135C54 41 158-20 279-20C418-20 514 73 514 173C514 251 450 329 340 352C445 390 483 465 483 526C483 605 392 664 281 664S85 610 85 530C85 496 107 477 137 477C168 477 188 500 188 528C188 557 168 578 137 580C172 624 241 635 278 635C323 635 386 613 386 526C386 484 372 438 346 407C313 369 285 367 235 364C210 362 208 362 203 361C201 361 193 359 193 348C193 334 202 334 219 334H273Z'/>
<glyph unicode='4' horiz-adv-x='569' vert-adv-y='569' glyph-name='four' d='M529 164V200H418V646C418 667 418 674 396 674C384 674 380 674 370 660L39 200V164H333V82C333 48 333 36 252 36H225V0C275 2 339 4 375 4C412 4 476 2 526 0V36H499C418 36 418 48 418 82V164H529ZM340 566V200H76L340 566Z'/>
</font>
<font id='cmmi10' horiz-adv-x='0'>
<font-face font-family='cmmi10' units-per-em='1000' ascent='750' descent='250'/>
<glyph unicode='u' horiz-adv-x='572' vert-adv-y='572' glyph-name='u' d='M350 56C361 15 396-11 439-11C474-11 497 12 513 44C530 80 543 141 543 143C543 153 534 153 531 153C521 153 520 149 517 135C503 79 484 11 442 11C421 11 411 24 411 57C411 79 423 126 431 161L459 269C462 284 472 322 476 337C481 360 491 398 491 404C491 422 477 431 462 431C457 431 431 430 423 396C404 323 360 148 348 95C347 91 307 11 234 11C182 11 172 56 172 93C172 149 200 228 226 297C238 327 243 341 243 360C243 405 211 442 161 442C66 442 29 297 29 288C29 278 39 278 41 278C51 278 52 280 57 296C82 383 120 420 158 420C167 420 183 419 183 387C183 363 172 334 166 319C129 220 108 158 108 109C108 14 177-11 231-11C297-11 333 34 350 56Z'/>
</font>
</defs>
<style type='text/css'>
<![CDATA[text.f0 {font-family:cmmi10;font-size:9.96264px}
text.f1 {font-family:cmr7;font-size:6.973848px}
]]>
</style>
<g id='page1'>
<text class='f0' x='-63.593206' y='-33.683486'>u</text>
<text class='f1' x='-57.89001' y='-32.189105'>1</text>
<text class='f0' x='-63.593206' y='-33.683486'>u</text>
<text class='f1' x='-57.89001' y='-32.189105'>2</text>
<text class='f0' x='-63.593206' y='-33.683486'>u</text>
<text class='f1' x='-57.89001' y='-32.189105'>3</text>
<text class='f0' x='-63.593206' y='-33.683486'>u</text>
<text class='f1' x='-57.89001' y='-32.189105'>4</text>
</g>
</svg>


        """,
        "latexCode": r"""
        Un exercice bidon de dérivation.
        """,
        "correction": r"""
        Une correction bidon""",
        "latexCorrection": r"""
        Une correction bidon
        """ 
    }
]




@app.route('/')
def home():
    return render_template('index.html', exercices=exercices)

@app.route('/filter_exercices', methods=['GET'])
def filter_exercices():
    level = request.args.get('level')
    if level == 'all':
        return render_template('index.html', todos=todos, exercices=exercices)
    filtered_exercices = [exercice for exercice in exercices if exercice['level'] == level]
    return render_template('index.html', exercices=filtered_exercices)

if __name__ == '__main__':
    app.run(debug=True)