print(
    """
*******************************************************************************
\\;,._                           _,,-
     \\`;, `-._ _..--'''```--.._ __.-',;(
      \\ `;,  `:.  ,   ;.   .   :'  .;` /
       ; `;;,      .:    :.      ,;;` /
        \\ ';/    \\:: :  . ::/    \\;` ;
         ).' __.._`        '_..__ `./
         /<  \\ /I`,      ,'I\\ //   >
         /\\   `;-7/_\\ -- /_\7-;'   /\
         //.    `"':" ;; ":`"'     /\
          |/ .  .:' __..__ `.     \\|
          /\\|: ./. `=_  _=' .\\   |/\
             /:(/::.  \\/  .::\\) /
              ////=-v-'`-v-=\\\\  fL
              ///`Nx_\\;;/_xN'\\\
             / /   `"w==w"'   \\ \
              /                \
*******************************************************************************
""",
)
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

path_direction = input("Which way will you go? LEFT or RIGHT?\n").lower()

if path_direction == "left":
    action_to_take = input(
        "You've approached a big lake. You are not too sure in your swimming skills. You also see some spooky doors nearby. \nDo you SWIM or WAIT?\n",
    ).lower()
    if action_to_take == "wait":
        chosen_door = input(
            "While you wait, you decide it's better and safer for you to go through the door. \nThrough which door will you go? RED, YELLOW or BLUE?\n",
        ).lower()
        if chosen_door == "red":
            print(
                "You open the red door and go through them... \nSuddenly you get surrounded by fire and you die a painfull death. \nGAME OVER",
            )
        elif chosen_door == "blue":
            print(
                "You open a blue door... \nA pack of wild cats rushes towards you, attacks you and rips you apart. \nYou die. \nGAME OVER",
            )
        elif chosen_door == "yellow":
            print(
                "You open a yellow door slowly and go through them. You see endless piles of gold treasure! \nYou've finally found the treasure you were looking for! \nYOU WIN!",
            )
        else:
            print(
                "You've made a forbidden choice! \nA demon manifests in front of you and takes your soul! \nYou are soulless and YOU DIE.",
            )

    else:
        print(
            "You start to swim and an angry trout attacks you. You get killed. \nGAME OVER",
        )

else:
    print(
        "While walking a few steps, you fall into a big hole and you die. \nGAME OVER",
    )
