{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMi8YV3O4691df/4ltc9i5x",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/lf-iacob/MCF/blob/main/E05_provvisorioColab.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "#MCF_E05: Funzioni, Moduli e Classi"
      ],
      "metadata": {
        "id": "Q6mBFwutJQac"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "iyp_dt00JPuL"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Esercizio 0 - Funzioni e Moduli\n",
        "\n",
        "Creare il file python somme.py in cui vanno definite due funzioni:\n",
        "- una funzione che restituisca la somma dei primi n numeri naturali, con n da passare tramite un argomento;\n",
        "- una funzione che restituisca la somma delle radici dei primi n numeri naturali, con n da passare tramite un argomento.\n",
        "\n",
        "Creare uno script python che importi il modulo somme appena creato e ne utilizzi le funzioni\n",
        "\n",
        "Esaminare la cartella di lavoro"
      ],
      "metadata": {
        "id": "Hq4IQsT4Fs16"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#MODULO: somme.py\n",
        "\n",
        "#Funzione 1\n",
        "def somman(x):\n",
        "  sum=0\n",
        "  for i in range (0,x+1):\n",
        "    sum-sum+i\n",
        "  return sum\n",
        "\n",
        "#Funzione 2\n",
        "def sommasqrt(x):\n",
        "  sum=0\n",
        "  for i in range (0, x+1):\n",
        "    sum=sum+np.sqrt(i)\n",
        "  return sum\n",
        "\n",
        "#Funzione 3\n",
        "def sommaprodotto(x):\n",
        "  s=0\n",
        "  p=1\n",
        "  for i in range(1, x+1):\n",
        "    s=s+i\n",
        "    p=p*i\n",
        "  return s, p\n",
        "\n",
        "#Funzione 4\n",
        "def geometrica(x, alpha=1):\n",
        "  sum=0\n",
        "  for i in range (1, x+1):\n",
        "    sum=sum+pow(i, alpha)\n",
        "  return sum"
      ],
      "metadata": {
        "id": "BYbqy_Aq25VW"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#ESERCIZIO 0_uso_somme.py\n",
        "\n",
        "import somme as s\n",
        "\n",
        "print('Somma dei primi n naturali')\n",
        "n=input('-> Inserisca il numero naturale: ')\n",
        "sum=s.somman(int (n))\n",
        "print('Risultato: ', sum)\n",
        "m=input('-> Inserisca il numero naturale: ')\n",
        "rad=s.sommasqrt(int(m))\n",
        "print('Risultato: ',rad)"
      ],
      "metadata": {
        "id": "JaFTGGk3F3h7",
        "collapsed": true
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Esercizio 1 - Moduli e Funzioni con argomenti\n",
        "\n",
        "Modificare il file somme.py aggiungendo:\n",
        "- una funzione che restituisca la somma e il prodotto dei primi n numeri naturali, con n da passare tramite un argomento;\n",
        "- una funzione che restituisca, con n da passare tramite un argomento e  da passare tramite keyword (kwargs), con valore di default pari a 1.\n",
        "\n",
        "Modificare lo script python che importa il modulo somme in modo da utilizzare le funzioni appena create."
      ],
      "metadata": {
        "id": "mvPEAfKAF4Kf"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#ESERCIZIO 1_uso_somme_nuovo.py\n",
        "\n",
        "print('Somma e prodotto dei primi n naturali')\n",
        "n=input('-> Inserisca il numero naturale: ')\n",
        "ss=s.sommaprodotto(int(n))\n",
        "print('Somma: {}, Prodotto: {}'.format(ss[0], ss[1]))\n",
        "\n",
        "print('\\n Serie speciale')\n",
        "m=input('-> Inserisca il numero naturale: ')\n",
        "a=input('-> Inserisca la potenza costante: ')\n",
        "gg=s.geometrica(int(m))\n",
        "gg1=s.geometrica(int(m), int(a))\n",
        "print('Risultato di default (potenza 1): ', gg)\n",
        "print('Risultato: ', gg1)"
      ],
      "metadata": {
        "id": "55J-HYq2F_yY"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "##Esercizio 2 - Classi\n",
        "Esempio di esperimento scientifico con struttura modulare (https://www.km3net.org/). image.png\n",
        "\n",
        "###Accesso ai Dati\n",
        "\n",
        "Per il terzo esercizio utilizzeremo dei dati che possono essere scaricati tramite lo script get_data.py del pacchetto get-mcf-data.\n",
        "\n",
        "###Scaricare i dati\n",
        "\n",
        "Spostarsi nella cartella del pacchetto get-mcf-data e, dopo ave adattato le opzioni necessarie come il percorso, eseguire un comando come di seguito:\n",
        "\n",
        "python3  get_data.py --year 2023 --exn 5 --outdir  percrso/cartella/esercitazione\n",
        "\n",
        "Il file di dati scaricati dovrebbero essere:\n",
        "\n",
        "hit_times_M0.csv\n",
        "hit_times_M1.csv\n",
        "hit_times_M2.csv\n",
        "hit_times_M3.csv\n",
        "\n",
        "###Contenuto File\n",
        "\n",
        "I file rappresentano i dati relativi a un (fittizio) rivelatore con sensori per fotoni organizzato in 4 moduli, ognuno contenenete 5 sensori.\n",
        "\n",
        "- Ogni file corrisponde ai dati di un modulo.\n",
        "- Ogni riga del file contiene l'informazione su un sensore che è stato colpito (Hit).\n",
        "\n",
        "Per ogni Hit viene riportata:\n",
        "identificatore del modulo [0-3];\n",
        "identificatore del sensore [0-4];\n",
        "distanza temporale in ns dall'inizio della presa dati.\n",
        "- Gli Hit sono ordinati temporalmente all'interno di ciascun file.\n",
        "\n",
        "I dati rappresentano un secondo di acquisizione dati.\n",
        "\n",
        "\n",
        "###Geometria Rivelatore\n",
        "\n",
        "Le posizioni esatte di moduli e sensori sono fornite di seguito:\n",
        "\n",
        "Coordinate centro Moduli [m] \\\\\n",
        "xmod = [-5,  5, -5,  5] \\\\\n",
        "ymod = [ 5,  5, -5, -5]\n",
        "        \n",
        "Coordinate dei Sensori rispetto al centro del Modulo [m] \\\\\n",
        "xdet = [-2.5, 2.5, 0, -2.5,  2.5] \\\\\n",
        "ydet = [ 2.5, 2.5, 0, -2.5, -2.5]\n",
        "\n",
        "###Eventi\n",
        "\n",
        "Si può considerare il rivelatore parte di un esperimento che che sfrutta la luce Cerenkov per studuare Eventi relativi ad un fenomeno di interesse.\n",
        "\n",
        "Ad ogni Evento un cono di luce Cerenkov investe i sensori o una parte di essi. I sensori registrano il tempo a cui i fotoni Cerenkov vengono rivelati.\n",
        "\n",
        "Dal punto di vista del nostro rivelatore, un Evento corrisponde ad un insieme di Hit ed alcune informazioni accessorie.\n",
        "\n",
        "Gli Hit apparteneti allo stesso evento saranno presumibilmente raggruppati nel tempo mentre Hit apparteneti ad eventi diversi mostreranno una separazione temporale maggiore."
      ],
      "metadata": {
        "id": "NgiVTTsCGAVf"
      }
    },
    {
      "cell_type": "markdown",
      "source": [
        "###Attività Richieste\n",
        "\n",
        "####Passo 1:\n",
        "\n",
        "Creare uno script python che esegua le seguenti operazioni:\n",
        "- Legga uno o più file di input;\n",
        "- Produca un istogramma dei tempi per uno dei moduli (file);\n",
        "- Produca un istogramma delle differenze di tempi () fra Hit consecutivi per uno dei moduli; \\\\\n",
        "(SUGGERIMENTO: usare il ';')\n",
        "- Interpretare il grafico risultante.\n",
        "\n",
        "####Passo 2:\n",
        "\n",
        "- Creare il file reco.py che definisca la classe Hit.\n",
        "- Un oggetto di tipo Hit deve contenere informazioni su:\n",
        "  Id Modulo; \\\\\n",
        "  Id Sensore; \\\\\n",
        "  Time Stamp rivelazione.\n",
        "- Oggetti di tipo Hit devono essere ordinabili in base al Time Stamp ed eventualmente in base alla Id del Modulo e del Sensore.\n",
        "\n",
        "####Passo 3:\n",
        "\n",
        "- Creare uno script python che svolga le seguenti operazioni:\n",
        "- Importi il modulo reco;\n",
        "- Legga i file di dati e, per ognuno di essi, produca un array di reco.Hit; \\\\\n",
        "(SUGGERIMENTO: creare un funzione da richiamare per ogni file;)\n",
        "- Produca un array che corrisponda alla conbinazione, ordinata temporalmente, di tutti i reco.Hit;\n",
        "- Produca un istogramma dei () fra reco.Hit consecutivi; \\\\\n",
        "(SUGGERIMENTO: valutare l'utilizzo dell' overloading degli operatori + o - (__add__, __sub__))\n",
        "\n",
        "Come stabilire la finestra temporale da applicare ai  che permetta di raggruppare gli Hit dello stesso evento ma separi quelii apparteneti ad eventi differenti? \\\\\n",
        "\n",
        "OPZIONALE: Pensare a come dovrebbe essere strutturata una eventuale classe Event per descrivere l'evento fisico come osservato dal rivelatore (quindi basata suglli Hit)."
      ],
      "metadata": {
        "id": "sUUftkLnHA_N"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "#ESERCIZIO_PASSO1 2_rivelatore_p1.py\n",
        "\n",
        "#Leggo i dati csv\n",
        "tab0=pd.read_csv('hit_times_MO.csv')\n",
        "tab1=pd.read_csv('hit_times_M1.csv')\n",
        "tab2=pd.read_csv('hit_times_M2.csv')\n",
        "tab3=pd.read_csv('hit_times_M3.csv')\n",
        "\n",
        "#Scelgo di istogrammare il modulo 0 (-5, 5: alto, sinistra)\n",
        "t0=tab0['hit_time']\n",
        "n, bis, p = plt.hist(t0, bins=60, color='orchid', edgecolor='darkorchid')\n",
        "plt.title('Istogramma tempi - Modulo 0')\n",
        "plt.xlabel('Valori estratti')\n",
        "plt.show()\n",
        "\n",
        "#Istogramma con differenza dei tempi\n",
        "dt0=np.diff(t0)\n",
        "mask_zeri=dt0>0\n",
        "n, bis, p=plt.hist(np.log10(dt0[mask_zeri]), bins=60, color='teal', edgecolor='black')\n",
        "plt.title('Istogramma delta-tempi - Modulo 0')\n",
        "plt.xlabel('Valori estratti')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "-R7Wf63iHAQ9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#MODULO_PASSO2 reco.py\n",
        "\n",
        "class Hit():\n",
        "  def __init__(self, modulo, sensore, tempo):\n",
        "    self.id_module=modulo\n",
        "    self.id_sensor=sensore\n",
        "    self.time_stamp=tempo\n",
        "  def __repr__(self):\n",
        "    return 'Modulo: {:}, Sensore: {:}, Time Stamp: {:}'.format(self.id_module, self.id_sensor, self.time_stamp)\n",
        "  def __str__(self):\n",
        "    return 'Modulo: {:}, Sensore: {:}, Time Stamp: {:}'.format(self.id_module, self.id_sensor, self.time_stamp)\n",
        "  def __lt__(self, other):\n",
        "    if(self.time_stamp!=other.time_stamp):\n",
        "      return self.time_stamp<other.time_stamp\n",
        "    elif(self.id_module!=other.id_module):\n",
        "      return self.id_module<other.id_module\n",
        "    else:\n",
        "      return self.id_sensor<other.id_sensor\n",
        "  def __sub__(self, other):\n",
        "    return abs(self.time_stamp-other.time_stamp)"
      ],
      "metadata": {
        "id": "T-g1XNqeH5OS"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#ESERCIZIO_PASSO3 2_rivelatore_p3.py\n",
        "import reco as rc\n",
        "\n",
        "#Leggo i dati csv\n",
        "tab0=pd.read_csv('hit_times_MO.csv')\n",
        "tab1=pd.read_csv('hit_times_M1.csv')\n",
        "tab2=pd.read_csv('hit_times_M2.csv')\n",
        "tab3=pd.read_csv('hit_times_M3.csv')\n",
        "\n",
        "#Array di Hit per ogni file\n",
        "def record(tab):\n",
        "  records=np.empty(0)\n",
        "  for i in range (0, len(tab['mod_id']-1)):\n",
        "    add=rc.Hit(tab['mod_id'][i], tab['det_id'][i], tab['hit_time'][i])\n",
        "    records=np.append(records, add)\n",
        "  return records\n",
        "\n",
        "records_0=record(tab0)\n",
        "records_1=record(tab1)\n",
        "records_2=record(tab2)\n",
        "records_3=record(tab3)\n",
        "\n",
        "#Riordino in base al tempo\n",
        "records=np.array([records_0, records_1, records_2, records_3])\n",
        "print(records)\n",
        "records=np.sort(records, kind='mergesort')\n",
        "print(records)\n",
        "\n",
        "#Estraggo delta_t di reco consecutivi: 2 e 3\n",
        "delta_t23=np.empty(0)\n",
        "for i in range(0, len(records_0)-1):\n",
        "  delta_t23=np.append(delta_t23, records_2-records_3)\n",
        "print(delta_t23)\n",
        "\n",
        "#Faccio istogramma con delta_t di reco consecutivi: 2 e 3\n",
        "n, bis, p=plt.hist(delta_t23, bins=60, color='coral', edgecolor='red')\n",
        "plt.title('Istogramma delta-tempi - Moduli 2-3')\n",
        "plt.xlabel('Valori estratti')\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "CJQLLEsXH6XQ"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}