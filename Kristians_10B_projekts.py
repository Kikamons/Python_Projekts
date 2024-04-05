
#Terminālā ieraksti "pip install colorama", lai strādātu krāsas.
from colorama import Fore
#Importē laika moduli, kas nodrošina dažādas ar laiku saistītas funkcijas.
import time
#Importē sys moduli, kas nodrošina piekļuvi dažiem mainīgajiem, ko izmanto vai uztur Python tulks, un funkcijām, kas cieši mijiedarbojas ar tulku.
import sys
#Funkcija teksta drukāšanai ar pauzi. teksts (str): drukājamais teksts. laiks (float): laiks, kas jāpauzē pēc teksta drukāšanas.
def print_pauze(teksts, laiks):
    #Izdrukā norādīto tekstu.
    print(teksts)
    #Aptur izpildi uz norādīto laiku (sekundēs).
    time.sleep(laiks)
print_pauze(Fore.YELLOW+"Ir sācies vasaras brīvlaiks!", 2)
print_pauze("Tu ar saviem diviem draugiem, Tomasu un Elizabeti, esat izdomājuši apmeklēt spocīgu māju.", 3)
#\n funkcija pārvieto nākošo teksta daļu jaunā rindā.
print_pauze("Vai vēlies iet iekšā viens pats, ar draugiem vai iet mājās?\n", 3)
while True:
    sakums = input(Fore.GREEN+"Izvēles opcijas: Viens, Kopā vai Iet mājās.\n> ")
    if sakums.lower().strip() == "viens":
        print_pauze(Fore.YELLOW+"\nTu izdomāji iet iekšā viens.", 1)
        print_pauze("Tu tagad atrodies foajē.", 1)
        print_pauze("Tu redzi durvis uz virtuvi un dzīvojamo istabu.", 2)
        print_pauze("Kur tu vēlies doties?", 2)
        while True:
            viens1 = input(Fore.GREEN+"\nIzvēles opcijas: Virtuve vai Dzīvojamā istaba.\n> ")
            if viens1.lower().strip() == "virtuve":
                print_pauze(Fore.YELLOW+"\nVirtuvē tu redzi Monas Lizas spoku.", 2)
                print_pauze("Tev ir izvēle būt drošam un cīnīties vai būt gļēvulim un skriet prom.", 3)
                print_pauze("Izvēle ir tavās rokās.", 2)
                while True:
                    viens2 = input(Fore.GREEN+"\nIzvēles opcijas: Cīnīties vai Skriet prom.\n> ")
                    if viens2.lower().strip() == "cīnīties":
                        print_pauze(Fore.YELLOW+"Tu mēģināji būt drosmīgs un cīnīties!", 2)
                        print_pauze("Diemžēl tu nebiji pietiekami spējīgs, lai viņu uzveiktu.", 2)
                        print_pauze("Un zaudēji cīņu", 1)
                        print_pauze(Fore.CYAN+"\nSliktās beigas!", 1)
                        #Funkcija, ko nodrošina sys modulis, kas pārtrauc Python tulka darbību.
                        sys.exit()
                    elif viens2.lower().strip() == "skriet prom":
                        print_pauze(Fore.YELLOW+"Tu aizmuki no Monas Lizas izskrienot ārā no mājas!", 2)
                        print_pauze("Tu tiki atpakaļ mājās pie draugiem.", 2)
                        print_pauze("Tu viņiem izstāstīji ko redzēji.", 2)
                        print_pauze(".", 1); print_pauze(".", 1); print_pauze(".", 1)
                        print_pauze("Taču tev ir sajūta, ka kāds jūs novēro...", 2)
                        print_pauze(Fore.CYAN+"\nLabās beigas?", 1)
                        sys.exit()
                    else:
                        print(Fore.RED+"\nLūdzu ievadi derīgu opciju!")
            elif viens1.lower().strip() == "dzīvojamā istaba":
                print_pauze(Fore.YELLOW+"Ieejot dzīvojamajā istabā tu neredzi neko draudīgu.", 3)
                print_pauze("Bet tu redzi ieeju uz istabu un izeju ārā no mājas!", 3)
                print_pauze("Tev ir izvēle iet iekšā istabā vai iet ārā.", 2)
                while True:
                    viens3 = input(Fore.GREEN+"\nIzvēles opcijas: Istaba vai iet ārā.\n> ")
                    if viens3.lower().strip() == "istaba":
                        print_pauze(Fore.YELLOW+"Tu izdomāji iet iekšā istabā.", 2)
                        print_pauze("Bet ieejot istabā tevi noķēra lamatas.", 2)
                        print_pauze("Mona Liza tevi atrada un pagatavoja zupā.", 2)
                        print(Fore.CYAN+"\nZupas beigas.")
                        sys.exit()
                    elif viens3.lower().strip() == "iet ārā":
                        print_pauze(Fore.YELLOW+"Tu izdomāji darīt gudro izvēli un gāji prom.", 3)
                        print_pauze("Tu nu gan nēesi jautrs.", 2)
                        print(Fore.CYAN+"\nGarlaicīgās beigas")
                        sys.exit()
                    else:
                        print(Fore.RED+"Lūdzu ievadi derīgu opciju!")
            else:
                print(Fore.RED+"Lūdzu ievadi derīgu opciju!")
    elif sakums.lower().strip() == "kopā":
        print_pauze(Fore.YELLOW+"\nJūs izdomājāt iet iekšā kopā.", 1)
        print_pauze("Jūs tagad atrodaties foajē.", 1)
        print_pauze("Jūs redzat durvis uz virtuvi un dzīvojamo istabu.", 3)
        while True:
            kopa1 = input(Fore.GREEN+"Izvēles opcijas: Virtuve vai Dzīvojamā istaba.\n> ")
            if kopa1.lower().strip() == "virtuve":
                print_pauze(Fore.YELLOW+"\nVirtuvē jūs redzat Monas Lizas spoku.", 2)
                print_pauze("Jums ir izvēle būt drošiem un cīnīties, bet zaudēt vienu draugu.", 3)
                print_pauze("Vai skriet prom un būt gļēvuļiem.", 3)
                while True:
                    kopa2 = input(Fore.GREEN+"Izvēles opcijas: Cīnīties vai Skriet prom.\n> ")
                    if kopa2.lower().strip() == "cīnīties":
                        print_pauze(Fore.YELLOW+"Kamēr tu ar Elizabeti novērsi Monas Lizas uzmanību.", 2)
                        print_pauze("Tomas ar pannu no muguras iesita viņai!", 2)
                        print_pauze("Taču pirms Mona Liza nokrita, viņa paspēja iegriezt Elizabetei.", 3)
                        print_pauze("Diemžēl Elizabete neizdīvoja...", 2)
                        print_pauze("Taču jūs dabūjāt ļoti vērīgu artifaktu, ko sargāja Mona Liza.", 3)
                        print_pauze("Un pārdevāt to par ļoti lielu summu.", 2)
                        print(Fore.CYAN+"\nBagātības beigas!")
                        sys.exit()
                    elif kopa2.lower().strip() == "skriet prom":
                        print_pauze("Jūs aizbēgāt prom un neko interesantu neizdarījāt.", 2)
                        print(Fore.CYAN+"\nGarlaicīgās beigas.")
                        sys.exit()
                    else:
                        print(Fore.RED+"Lūdzu ievadi derīgu opciju!")
            elif kopa1.lower().strip() == "dzīvojamā istaba":
                print_pauze(Fore.YELLOW+"Jūs iegājāt dzīvojamajā istabā...", 2)
                print_pauze("Taču jūs izsekoja suns.", 1)
                print_pauze("Tomas saka, lai mēs viņu paturam, bet Elizabete saka, ka viņš nav īsts un mums ir jāiet prom.", 5)
                print_pauze("Tev ir izvēle klausīt Tomasu vai Elizabeti", 2)
                while True:
                    kopa3 = input(Fore.GREEN+"Izvēles opcijas: Tomas vai Elizabete.\n> ")
                    if kopa3.lower().strip() == "tomas":
                        print_pauze(Fore.YELLOW+"Tu izvēlējies klausīt Tomasu.", 2)
                        print_pauze("Bet tu drīz sapratu, ka tā bija nepareizā izvēle,\njo suns sāka jūs mēģināt ēst nost un jums nebija spēks suni nosist.", 5)
                        print(Fore.CYAN+"\nSuņa beigas.")
                        sys.exit()
                    elif kopa3.lower().strip() == "elizabete":
                        print_pauze(Fore.YELLOW+"Tu izvēlējies klausīt Elizabeti.", 2)
                        print_pauze("Labi ka tā, jo tas suns bija ļauns un gribēja jūs apēst.", 3)
                        print_pauze("Jūs paspējāt aizmukt no tā trakā suņa un izbaudījāt savu brīvo laiku mājās", 5)
                        print(Fore.CYAN+"\nGandrīz suņa vakariņas beigas.")
                        sys.exit()
                    else:
                        print(Fore.RED+"Lūdzu ievadi derīgu opciju!")
            else:
                print(Fore.RED+"Lūdzu ievadi derīgu opciju!")
    elif sakums.lower().strip() == "iet mājās":
        print_pauze(Fore.YELLOW+"Jūs izdomājāt iet mājās.", 1)
        print_pauze("Un noskatījāties filmu kopā ar popkornu.", 1)
        sys.exit()
    else:
        print(Fore.RED+"Lūdzu ievadi derīgu opciju!")