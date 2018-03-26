import firebase

firebaseURL = 'https://hackathon-91c9b.firebaseio.com/'

firebase.push(firebaseURL,'')

print(firebase.get_usernames(firebaseURL))

t = 2

firebaseURL += firebase.get_usernames(firebaseURL)[-t]

firebase.put(firebaseURL,{'userdata':t})