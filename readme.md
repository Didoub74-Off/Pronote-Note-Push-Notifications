
# Pronote Note Notifications

Le premier robot pronote qui vous envoie des notifications pour vous avertir de vos notes et éviter de regarder votre Pronote toutes les 5 minutes pour vérifier si votre notes que vous attendiez est arrivée.

Le robot vous envoie aussi, si vous le voulez, les modifications de votre emploi du temps.
## FAQ

### Comment se connecter ?

Pour connecter son compte Pronote aux programme, vous devez fork le Repls et ajouter vos variables d'environnements dans les paramètres tel que ceci:

`firstname` -> Votre prénom (n'est pas obligé d'être le vrai)

`username` -> Le nom d'utilisateur de votre compte Pronote. Si votre établissement utilise un ENT, vous pouvez voir votre identifiants envous connectant à Pronote sur un smartphone et en cliquant sur `Gestion de compte`.

`passcode` -> Le mot de passe de votre compte Pronote. Si votre établissement utilise un ENT, il faut réinitialiser votre mot de passe avec le compte parent.

`url` -> L'url d'accès aux pronote de votre établissement.
```
Exemple: https://your-school.com/pronote/students <-- Mauvaise URL
         https://0000000a.index-education.net/pronote/eleve.html <-- Bonne URL
         https://0000000a.index-education.net/pronote/eleve.html?login=true <-- Seulement si vous utilisez un ENT
```
`apikey` -> La clé d'api du site web [pushsafer.com](https://www.pushsafer.com/). (Il faut payer 0.99€ pour 1000 notifications. | Pour tester le programme vous bénificiez de 50 notifications gratuites. Rien ne vous empêche de fermer, de rouvrir un compte à chaque fois.)

`device_id` -> L'ID de votre appareil, disponible dans les réglages de l'applications Push Safer ou alors sur votre Dashboard, dans la catégorie 'Your Devices'

### Stockes tu nos identifiants ?

Bien sûr que non,vous pouvez vérifier le code source du programme et confirmer que je ne stocke aucun identifiants. Les seuls personnes ayant accès à vos variables d'environnements sont vous et Replit (Je ne suis pas sûr que Replit aie quelque chose à faire de vos identifiants Pronote.

### A tu prévus d'ajouter d'autres fonctionnalitées ?

Oui, j'ai prévu d'ajouter d'autres fonctionnalitées telles que:
- Envois des messages recu directements par notifications
- Envois des compétences par notifications

### Bugs connus
- Si vous avez deux fois la même note dans une seule matière le même jours, il ne vous enverra pas la notifications pour la deuxième.
- Pas d'autres bugs connu pour le moment.