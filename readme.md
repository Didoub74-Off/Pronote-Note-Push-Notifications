
# Pronote Note Mailer

Le premier mailer pronote pour vous avertir de vos notes.


## FAQ

#### Comment se connecter ?

Pour connecter son compte Pronote aux programme, vous devez fork le Repls et ajouter vos variables d'environnements dans les paramètres tel que ceci:

`firstname` -> Votre prénom (n'est pas obligé d'être le vrai)

`jeton` -> Le jeton du QR code à générer depuis Pronote et à décrypter avec https://zxing.org/w/decode.jspx (à changer à chaque reconnexion de plus de 10 minutes après la génération du QR Code)

`login` -> Le login du QR code à générer depuis Pronote et à décrypter avec https://zxing.org/w/decode.jspx (reste toujours le même ; pas besoin de le changer à chaque fois)

`passcode` -> Le code du QR code que vous avez choisis lors de la génération

`url` -> L'url d'accès aux pronote de votre établissement 
```
Exemple: https://your-school.com/pronote/students <-- Mauvaise URL
         https://0000000a.index-education.net/pronote/eleve.html <-- Bonne URL
```

#### Est ce que je stocke les identifiants ?

Bien sûr que non
Vous pouvez vérifier le code source du programme et confirmer que je ne stocke aucun identifiants (de plus les identifiants ne sont valides que 10 minutes après la génération)

#### A tu prévus d'ajouter d'autres fonctionnalitées ?

Oui, j'ai prévu d'ajouter d'autres fonctionnalitées telles que:
- L'avertissement des profs absents par mails
- Envois des messages recu directements par mails
- Envois des devoirs par mails
- Envois des compétences par mails

