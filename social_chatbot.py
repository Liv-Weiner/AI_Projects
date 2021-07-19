


!pip install chatterbot
!pip install chatterbot-corpus
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
import chatterbot_corpus



chatbot = ChatBot("Livus")

user_input = input()
response = chatbot.get_response(user_input)
print(response)



def talk_to(chatbot):

  keep_going = "yes"

  while keep_going == "yes":
    
    user_input = input()
    response = chatbot.get_response(user_input)
    print(response)

    if user_input == "quit":
      keep_going = "no"



talk_to(chatbot)



trainer = ListTrainer(chatbot)

conversation = [
    "Tell me a joke!",
    "Why did the duck cross the road?",
    "Because the chicken was on vacation" 
]



trainer.train(conversation)



talk_to(chatbot)




conversation = [
                "Hi",
                "Hello",
                "How are you",
                "I'm doing great",
                "That's good!",
                "It's a beautiful day",
                "Yes, I love the weather"
]
trainer.train(conversation)


talk_to(chatbot)

conversation = [
    
    "Where are you from?",
    "California",
    "What is your favorite food?",
    "Italian food",
    "How about you",
    "I like all sorts of food",
    "What other things do you like?",
    "I like reading and learning",
    "Me too!"
        
]
trainer.train(conversation)

conversation = [
   "Hi", 
   "how are you?", 
   "Im alright thanks", 
   "Where are you from?", 
   "Im from Southern California", 
   "Ah I here southern california is very nice", 
   "yes it is", 
   "What'd you eat this morning for breakfast?", 
   "A bagel with cinnamon sugar and butter",
   "OOOO thats my favorite"
]
trainer.train(conversation)

conversation = [
          "Hey",
          "Hello",
          "How are you?",
          "Good thanks, and you?",
          "Fine.",
          "What are you doing?",
          "Nothing.",
          "How is the weather?",
          "It's pretty sunny here.",
          "That's good.",
]
trainer.train(conversation)

conversation =[
               "Hi",
                "Hello, how are you",
                "I'm doing good, what about you",
                "Great!",
                "How's the weather like",
                "Pretty good, not to bad",
               "What did you eat for breakfast",
               "I ate waffles with fresh syrup!",
               "yum that would taste really good",
               "what do you like to do in your free time",
               "I like playing basketball and coding"
]
trainer.train(conversation)

conversation = [
                "Hi",
                "Hello, what did you eat for breakfast",
                "I had some cerial and A glass of orange juice",
                "yum, I bet that tasted good",
                "how are you",
                "I'm great, what about you",
                "I'm fine thank you",
                "hi",
                "Are you having a good day today",
                "Im having a fun day today"   
]
trainer.train(conversation)

talk_to(chatbot)

