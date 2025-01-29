SIMULAZIONE-METODO MONTECARLO: MOTI DI DERIVA
---
La repository in questione contiene il modulo e lo script che permettono la simulazione del moto di una particella carica, in particolare l'elettrone, inserito all'interno di una regione di spazio popolata da campi.

In particolare, nel primo caso ci sono un campo magnetico ed un campo elettrico uniformi, costanti ed ortogonali tra loro: E lungo x e B lungo z. Risolvendo le equazioni differenziali, si osserva come la carica è soggetta ad un moto di deriva EXB lungo la direzione y.

Nel secondo esempio, è presente un solo campo magnetico costante nel tempo in direzione z, ma dotato di un gradiente ortogonale lungo y che lo rende non uniforme. I risultati teorici mostrano che le particelle in media sono sottoposte ad un drift BXgradB su x.

---

Nella simulazione vengono impostate dall'interno le cartteristiche specifiche della particella un studio, le configurazioni di campo, l'intervallo di velocità iniziali generate randomicamente lungo ogni direzione. Nel modulo vengono implementate le funzioni necessarie allo svolgimento del montecarlo, compresa la legge del modo che descrive il fenomeno. Si imposta, inoltre, un valore fisso per il seed delle velocità estratte secondo una distribuzione uniforme, in modo tale da tener meglio traccia dei risultati al variare delle condizioni di svolgimento dell'esperimento e assicurarne la riproducibilità.

L'utente può scegliere quante particelle generare nella simulazione e quanti passi queste hanno compiuto (quindi la durata della simulazione, dove il tempo infinitesimo associato a ciascuno step è fissato dall'interno coerentemente con gli ordini di grandezza delle variabili in gioco).

Si visualizzano di conseguenza per entrambe le tipologie di drift la traiettoria compiuta da una singola carica a mo' di esempio e poi quelle delle varie particelle generate. Per ognuna delle tre configurazioni di campo proposte si mostra la direzione del vettore rappresentante la velocità media di drift nello spazio tridimensionale e la sua proiezione sul piano xy ortogonale. Infine, vengono mostrati gli istogrammi per la proiezione del drift sull'asse x, asse y e piano xy per lo studio statistico della deriva della particella.
