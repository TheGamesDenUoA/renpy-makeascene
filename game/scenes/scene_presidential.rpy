label scene_presidential:
    define georgewashington = Character("George Washington")

    scene white house

    image white house old resized = im.Scale ("images/white house old.jpeg", 1920, 1080) 
    show white house old resized

    show george 1

    georgewashington "hello"

    georgewashington "they call me george"

    show george 2

    georgewashington "don't worry about the background"

    show george 3

    georgewashington "we haven't invented pixels yet"

    show george 5

    georgewashington "anyways"

    show george 6

    georgewashington "i invented merica"

    show george book

    georgewashington "and they made a book about me"

    show george 1

    georgewashington "now listen..."
    georgewashington "you are going to see some meme presidents in the other slides probably"

    show george book 2

    georgewashington "but I am a {i}serious{/i} president"

    show george 1

    georgewashington "let me ask you something"
    georgewashington "theres lots of talk about democracy around these parts"
    georgewashington "but how long should I serve for?"

    label serve:

    show george 1

    menu:
        "4 years":
            jump no
        "8 years":
            jump historical_accuracy
        "200 years":
            jump years_200

    label historical_accuracy:

        show george finger

        georgewashington "so you chose the historically accurate option... this isn't jeopardy"

        jump serve

    label no:

        georgewashington "im not a king but also you need to give me more time than that..."

        jump serve
    
    label years_200:
        show george eighty

        georgewashington "{i}is the 1980s{/i}"
        georgewashington "hm this is pretty nice"
        georgewashington "wait no my head got cut off but i dont have time to fix ok bye"

    return