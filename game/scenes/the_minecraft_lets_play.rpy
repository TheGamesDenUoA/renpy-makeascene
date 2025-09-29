define joe = Character("Biden-inator9000")
define bar = Character("bama44")
define don = Character("DonnyT1946")

label the_minecraft_lets_play:
    scene meeting room

    show obama portrait
    bar "Hello chat!"
    
    bar "For those of you who are new to the stream, this is our 3rd day of streaming Minecraft until we defeat the Ender Dragon."
    hide obama portrait

    show trump portrait
    don "Yes everyone. And we have been making great, great progress so far!"
    hide trump portrait

    show joe portrait
    menu optional_name:
        "Greet the chat:"
        "Happy":
            joe "Yeah chat I think we got this!"
        "Angry":
            joe "I disagree chat, these two suck and I am carrying them."
    hide joe portrait

    return