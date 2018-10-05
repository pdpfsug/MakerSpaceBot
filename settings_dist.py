# Your Token for Telegram Bot, get it on Bot Father
TOKEN = "TOKEN"

# Start message
start_msg = "Benvenuto nel Bot relativo allo stand del MakerSpace di Fabriano! Digita il comando /info per ottenere "\
            "maggiori informazioni riguardanti questa realtà o digita il comando /timeline per visualizzare un'ampia raccolta "\
            "di date che hanno caratterizzato la storia dell'evoluzione dei ChatterBot!"

# Help message
help_msg = "I don't need help"

#Info message
info_msg = {}

info_msg[0] = "Il progetto Makerspace in Library a Fabriano è un progetto innovativo a livello internazionale. In America il primo MakerSpace in una biblioteca " \
              "nacque nel 2011 presso la biblioteca di Fayetteville (FFL) dello Stato di New York. In Europa, invece, è ancora poco diffuso. In Italia le biblioteche " \
              "che offrono spazi simili, benché con caratteristiche diverse, si trovano a Pistoia, a Cinisello Balsamo e a Settimo Torinese. \n" \
              "Molto frequentato e liberamente accessibile nel cuore della città di Fabriano, come è la nuova Biblioteca Multimediale Pubblica, rende " \
              "possibile l’incontro e la sperimentazione di diverse realtà, dalle associazioni agli studenti delle scuole di ogni ordine e grado." \

info_msg[1] = "Il Maker Space si inserisce nel movimento culturale dei makers, degli _artigiani digitali_, del software e dell'hardware libero." \
              "La creazione di uno spazio fisico, la sperimentazione di diverse realtà, dalle associazioni agli studenti delle scuole di ogni ordine e grado. " \
              "Questa iniziativa è autogestita dagli utenti stessi, giovani e meno giovani, di qualsiasi cultura, etnia, genere ed estrazione economica e sociale. " \
              "In maniera gratuita e volontaria, il gruppo propone, organizza e realizza le attività che si svolgono in modo continuativo: workshop per " \
              "la realizzazione di piccoli circuiti elettrici ed elettronici, progetti di open hardware (Arduino, Makey Makey, Raspberry Pi, Little Bits), " \
              "proposte per l’introduzione alla programmazione e alla robotica, in collaborazione con associazioni di altre aree geografiche." \

info_msg[2] = "Ad oggi tutto il materiale di cui è dotato il Maker Space, dalle schede elettroniche, ai materiali di consumo, ai libri di making, è stato ottenuto " \
              "tramite partecipazioni ad attività educative sponsorizzate da Google, Make e da alcune aziende locali. Fabriano è nella rete delle città " \
              "creative dell’Unesco per l'artigianato, le arti e le tradizioni popolari (in Italia solo Bologna, Torino e Fabriano hanno questo riconoscimento) " \
              "ed è famosa in tutto il mondo per la qualità della carta, vantando una tradizione cartaria dal 1264.\n\n" \
              "Se vuoi saperne di più puoi visitare il seguente [sito](https://goo.gl/9BhA7B)!\n\n"

#Timeline message
timeline_msg = "Seleziona una data dalla seguente lista per ottenere maggiori informazioni!"

#Events timeline
msg_style = {}

msg_style['1950'] = "Nel 1950 Alan Turing pubblicò un articolo dal titolo Computing Machinery and Intelligence, " \
                 "in cui propose un criterio - oggi definito Test di Turing - in grado di determinare se una " \
                 "macchina è in grado di pensare o meno. Per soddisfare questo criterio un software deve fingere di " \
                 "essere umano in una conversazione in tempo reale in modo che l'interlocutore non sia in grado di " \
                 "distinguere, basandosi solo sul contenuto della conversazione, se stia conversando con un programma " \
                 "o con un essere umano."

msg_style['1966'] = """ELIZA è un Chatterbot scritto nel 1966 da Joseph Weizenbaum. ELIZA si contraddistinse quale la parodia di un terapeuta Rogersiano, """ \
                 """in buona parte rispondendo al paziente con domande ottenute dalla riformulazione delle affermazioni del paziente stesso. """ \
                 """Così, per esempio, alla frase "Mi fa male la testa" il programma può ribattere con "Perché dici che ti fa male la testa?" """ \
                 """oppure la risposta a "Mia madre mi odia" potrebbe essere "Chi altro nella tua famiglia ti odia?"."""

msg_style['1972'] = "Lo psichiatra americano Kenneth Colby introdusse nel 1972 il bot Parry, ideato in modo da possedere i" \
                 " tratti tipici di un paziente affetto da schizofrenia. Il bot dimostrò di essere più avanzato del suo" \
                 " predecessore, tanto da venir definito “ELIZA con una mentalità”. "

msg_style['1988'] = "Scritto da Rollo Carpenter nel 1988, Jabberwacky era capace di tenere conversazioni che fossero diver" \
                "tenti e umoristiche. Fu uno dei primi tentativi di creazione di un’Intelligenza Artificiale attravers" \
                "o le interazioni umane. Il suo diretto successore fu Cleverbot, ideato dallo stesso Carpenter e acces" \
                "sibile online ancora oggi."

msg_style['1992 - Parte 1'] = "Nel 1992 Creative Labs rilasciò per la piattaforma MS-Dos Dr. Sbaitso. La conversazione con Sbaitso a" \
                   "veva la tipica impostazione di una seduta dallo psicologo con la possibilità per gli utenti di avere " \
                   "un’interazione ancora più viva con il programma grazie alla sintesi vocale delle sue risposte."

msg_style['1992 - Parte 2'] = "Nello stesso anno il giornalista e ricercatore Francesco Lentini pubblicò un articolo sulla Stampa in" \
                   " cui descriveva la possibilità di dialogare con una macchina. Prendendo spunto dalla prima edizione d" \
                   "el Premio Loebner, svoltasi al Computer Museum di Boston, Francesco Lentini creò ELOISA, invitando es" \
                   "perti di informatica, ricercatori di tutte le discipline e semplici curiosi a dialogarci."

msg_style['2000'] = "Nel 2000 Robert Hoffer e Timothy Kay fondarono la società ActiveBuddy allo scopo di creare agenti int" \
                 "elligenti, basati sulla conversazione, in grado di comunicare attraverso piattaforme di messaggistica" \
                 " istantanea. Hoffer ebbe l'idea di creare agenti interattivi per aggiungere funzionalità ai sempre pi" \
                 "ù popolari servizi di messaggistica. L'implementazione originale fu in un gioco di avventura, ma pres" \
                 "to furono aggiunte una vasta gamma di applicazioni basate sui database quali l'accesso alle notizie, " \
                 "al meteo, a informazioni di borsa oltre che svariati altri strumenti (calcolatrici, traduttori, ecc.)" \
                 ". Le applicazioni furono inserite in un unico pacchetto e lanciate, nel 2001, sotto il nome di Smarte" \
                 "rChild, una vetrina per il rapido accesso alle informazioni che offriva la possibilità di divertirsi " \
                 "anche attraverso la conversazione. Il successo del progetto - si raggiunsero oltre 13 milioni di uten" \
                 "ti - portò alla realizzazione di prodotti promozionali in ambito musicale, cinematografico e televisi" \
                 "vo - Radiohead, Austin Powers, The Sporting News sono solo alcuni dei brand coinvolti."

msg_style['2002'] = "Jargon, Web Agency Milanese, ottenne nel 2002 l'esclusiva per l'Italia della piattaforma tedesca per " \
                 "la creazione di chatbots LingoBot. Grazie all’operato di Jargon arrivò la versione in lingua italiana" \
                 """ di LingoBot, a partire dalla quale si sviluppò "Alfa, Il Robot" con applicazioni personalizzate come""" \
                 " l'invio di cartoline virtuali."

msg_style['2005'] = "Dreams and Co realizza Giorgia e, successivamente, AvClick una piattaforma per creare assistenti virt" \
                 "uali"

msg_style['2006'] = "Società come INPS, Gruppo BPM, IKEA e Bettini fanno uso di assistenti virtuali"

msg_style['2007'] = "Microsoft lancia Doretta, un assistente virtuale in grado di effettuare ricerche su internet attraver" \
                 "so MSN"

msg_style['2015'] = "Telegram lancia la possibilità inserire Agenti Virtuali in grado di rispondere a comandi, programmabi" \
                 "li sia in maniera visuale che utilizzando librerie proprietarie"

msg_style['2016 - Parte 1'] = "Facebook decide di aprire l'accesso ai bot sulla sua piattaforma di messaggistica istantanea Messenger "

msg_style['2016 - Parte 2'] = "Viene presentato GETrid, uno tra i primi Chatterbot con risvolti pratici nella vita comune: un assist" \
                   "ente virtuale in grado di consigliare il corretto modus operandi nella fase di riciclo di un oggetto."

msg_style['2016 - Parte 3'] = "Amazon Echo (abbreviato e indicato come Echo) è un marchio di altoparlanti intelligenti sviluppato da" \
                   " Amazon.com. I dispositivi si connettono all'assistente personale intelligente a comando vocale denom" \
                   """inato Amazon Alexa, che risponde all'utente al nome "Alexa". Questa "parola sveglia" può essere modif""" \
                   """icata dall'utente in "Amazon", "Echo" o "Computer"[1]. Il dispositivo è in grado di interagire con la""" \
                   " voce, riprodurre musica, creare elenchi di cose da fare, impostare allarmi, streaming di podcast, ri" \
                   "produrre audiolibri e fornire informazioni meteorologiche, sul traffico e altre informazioni in tempo" \
                   " reale. Può anche controllare diversi smart devices casalinghi agendo da hub di domotica."

msg_style['2017 - Parte 1'] = "Google Home è un marchio di altoparlanti intelligenti sviluppato da Google"

msg_style['2017 - Parte 2'] = "SnatchBot, società israeliana, lancia un sito web per la creazione di chatbot, che ha rivendicato la " \
                   "capacità di costruire bot in grado di compiere analisi sentimentali."
