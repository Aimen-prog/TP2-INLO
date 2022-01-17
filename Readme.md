README
======

# TP Programmation Python
Ce TP a été réalisé dans le cadre de l'UE INLO.



**Mode d'emploi**
<br>
Ce programme vérifie si une chaine ADN est valide ou invalide. Sur cette base, ce programme vérifie pour chaque séquence d'un fichier
fasta si la séquence est valide ou pas. Si oui il affiche l'identifiant de la séquence accompagné du  status "valide" et indique 
la longueur de la séquence. Sinon il affiche l'identifiant de la séquence accompagné du  status "invalide", indique sa longueur, reporte
la premiére erreur ( premier faux caractére ) et sa position dans la séquence.     



**Code**
<br>
La librairie *adn.py*

<ol type="I"> 
<li> Une premiére fonction is_valid(adn) prend en entrée une chaîne de caractère (​ adn​ ) et renvoie True​ si elle n’est composée que de ‘​ t ​ ’, ‘​ a ​ ’, ‘​ g ​ ’ ou ‘​ c ​ ’ ; ​ False​ sinon.</li>

<li> Une deuxiéme fonction get_valid_adn() qui demande à l’utilisateur d’entrer une chaîne ADN tant que celle-ci n’est pas valide. </li>

<li> Une fonction purify(adn_str) enlève les mauvais caratéres de la chaine entrée (lettres non nucleotidique incluses). </li>

<li> Fonctions purified_is_valid(adn) et get_valid_purified_adn() qui font la meme chose que les 2 premières fonctions mais avec de l' adn purifié. </li>


<li> Une fonction get_fasta(fasta_file) qui sert à lire un fichier fasta et à le mettre dans un dictionnaire. </li>

<li> Une fonction check_fasta(dico) qui prend un dictionnaire et vérifie pour chaque valeur qu'il y a bien une séquence adn valide. </li>

</ol>

Le programme *select_fasta_parser.py* 
<br>
Ce programme est un parser de fichier.
<br> 
Utilise les fonctions de la librairie adn.py pour vérifier qu'un fichier fasta (-i "fichier.fasta") est bien sous forme de nucléotides










