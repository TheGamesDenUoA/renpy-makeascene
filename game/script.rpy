
# The entry point for this game.
label start:

    # Calls the beginning scene
    call beginning

    call pyramid
    # Call all the other scenes in between
    call scene001

    # Calls the end scene
    call end

    # This ends the game.
    return
