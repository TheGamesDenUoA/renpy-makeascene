label pyramid:
    image joe = "idkhow2type/joe.webp"
    image trump = "idkhow2type/trump.webp"
    image pyramids = "idkhow2type/pyramids.jpg"
    image office = "idkhow2type/office.jpeg"
    # scene pyramid at cover_screen
    # "The background is scaled to cover the entire window, with slight cropping if needed."

    define joe = Character("Joe Biden")
    define trump = Character("Donald Trump")
    define obama = Character("Obama")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    scene office
    show joe at left
    show trump at right

    # These display lines of dialogue.

    trump "Hey Joe, sleepy sleepy Joe"
    joe "What?"
    trump "We should go to the pyramids. They're some great pyramids, the greatest pyramids even"
    joe "Sure nerd lesgo"

    scene pyramids at top
    show joe at left
    show trump at right


    obama "Joe! Trump!"
    obama "I turned myself into a pyramid, Joe! Boom! I'm a pyramid. What do you think about that? I turned myself into a pyramid! W-what are you just staring at me for, bro? I turned myself into a pyramid, Joe!"
    trump "And?"
    obama '"And"? What more do you want tacked on to this? I turned myself into a pyramid, and 9/11 was an inside job?'
    trump "Was it?"
    obama "You're the president, don't you know this? The file is right next to Epstein's"
    obama "But who cares, Trump? Global acts of terrorism happen every day. Uh, here's something that's never happened before: I'm a pyramid. I'M OBAMIUUUM!!"


    return
