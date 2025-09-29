transform half_size_lhe:
    zoom 0.5

transform centered_lhe_j:
    ypos 150
    xpos 300

transform centered_lhe_w:
    ypos 150
    xpos 500


label scene_lucia:
    define waltuh = Character("Waltuh")
    define jesse = Character("Jesse")
    define biden = Character("Joseph Robinette Biden Jr., 46th President of the United States of America")
    define Gus = Character("Gus")

    scene new mexico
    show walt at centered_lhe_w
    show jesse at centered_lhe_j
    waltuh "Jesse! Jesse! We need to cook!"
    jesse "Waltuh, 46th Joseph Robinette Biden Jr. seized our van under 21 U.S. Code § 841 - Prohibited acts A"
    waltuh "Damn that meddling Biden!"
    hide walt
    hide jesse
    show bidenlhe at half_size_lhe
    biden "That was some weak-ass meth! Didn't even put me down for my afternoon nap!"
    hide bidenlhe 
    show jesse at centered_lhe_j
    jesse "JOE BIDEN?!?!"
    hide jesse
    show walt at centered_lhe_w
    waltuh "Biden, please help me with my cancer and save me from this life of crime."
    hide walt
    show bidenlhe at half_size_lhe
    biden "Git gud and we'll talk, that was some abysmal methamphetamine." 
    hide bidenlhe
    show jesse at centered_lhe_j
    jesse "That's cuz I smoked all the good shit already. We've been pushing rock candy for the last two weeks."
    hide jesse
    show regular gus 
    Gus "You've been WHAT???"
    Gus "Waltah, I pay you for meth, not rock candy. Now I can't afford the lease on Los Pollos Hermanos, the least profitable food chain in America!"
    Gus "We are family no more." 
    Gus "*cries*"
    hide regular gus
    show walt at centered_lhe_w
    waltuh "I'm so sorry, Mr Fring. I should've listened when you said Jesse was a liability."
    hide walt
    show regular gus
    Gus "This is a betray for the history books. Not just for my buisness..."
    hide regular gus
    show bi gus at centered_lhe_w
    Gus "...but my heart as well."



    return