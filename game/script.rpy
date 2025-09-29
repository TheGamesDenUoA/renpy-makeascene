
# The entry point for this game.
label start:

    # Calls the beginning scene
    call beginning

    # Call all the other scenes in between
    call scene001
    call scene_lucia

    call scene_alexk
    call scene_sjkillen

    # Jill vs Trumpter
    call scene_wrennifer

    # Calls the end scene
    call end

    # This ends the game.
    return
