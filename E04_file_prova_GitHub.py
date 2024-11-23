Lezione 4: Uso di GitHub

VSC
Un Version Control System (VSC) è una piattaforma che permette di salvare versioni
di software e sviluppo software in modo collaborativo.

ATTIVAZIONE ACCOUNT
1. Recarsi online al sito "https://github.com/"
2. Da terminale "git clone https://github.com/nome_utente/home_repository.git"
3. Da terminale "git status" mostra la versione locale

CREAZIONE TOKEN (questioni di sicurezza)
Sul profilo personale di GitHub, andare su "Settings", "Develope settings"
e ancora "Personal access token". Cliccare "Tokens (classic)" e "Generate new token".
Attivato il "repo", prendere nota del codice del proprio token
    token "tolkien": ghp_V6\Bl\0JJxwoRvy1klGFmo8TmfB0NY22rRPQ
Completare la configurazione da terminale del token appena generato sul
proprio account scrivendo "git config credential.helper store", passare il codice
del token per avere accesso e poi "git config user.name "lf-iacob"".

CARICAMENTO DI UN FILE SU GITHUB DA TERMINALE
Creato un file emacs nome_file.py di tipo Python da caricare su GitHub, da terminale
digitare "git add new_file.py", "git commit new_file.py -m 'message'" e "git push".
Per aggiornare un file già esistente, si riproponga lo stesso procedimento solo non
usando il comando con "add". A prescindere, per non ricadere in ambiguità, sarebbe
preferibile modificare il file direttamente su git in caso di necessità.

NB: il caricamento avverà sulla brench "main"
