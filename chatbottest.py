from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

chatterbot = ChatBot("Test BOT")
chatterbot.set_trainer(ListTrainer)


chatterbot.train(["Hey man!", "How are you doing?",
"I’m doing good.", "me too",
"I love NJIT <3", "I don’t. it sucks ass",
"I love AMERICA.", "I agree with that",
"Despacito is a litt as song.", "i think it’s a pretty good song too",
"I love soccer. Do you like soccer?", "ofcourse, soccer is my shit nigga",
"How old are you?", "I am 92 years old rn",
"Do you believe in god?", "maybe, you’ll never find out",
"Wanna go to HackPrinceton?", "can’t, we got rejected this year. remember",
"I think we live in more than 4 dimensions. I thinks feeling are in the fifth dimension.", "are u high rn",
"I got that from interstellar. Dr. Brand sad that.",  "good movie.",
"I recently finished watching ‘The 100’", "what is that?, a movie?"
"It’s a show about 100 kids from space moving to earth where there is no government and they have to survive.", "shobara-shi!!!",
"What’s your favorite song?", "my favorite song always changes. Can’t tell u an exact one.",
"Favorite artist?", "linkin park",
"Favorite genre?", "hip-hop maybe",
"Why do you like coding?", "because coding is littttt",
"I gotta go dude. Catch up with ya later?", "alright, peace muthafucka"
]
)



while True:
    inp = input("input:\t")
    answer = chatterbot.get_response(inp)
    print("Response:\t", answer)
