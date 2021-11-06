print('''
╦  ╦┌─┐┌─┐┌─┐┬┌┐┌┌─┐  ╦ ╦┬ ┬┌┐┌┬┐┌─┐┬─┐
╚╗╔╝├─┤│  │  ││││├┤   ╠═╣│ │││││ ├┤ ├┬┘
 ╚╝ ┴ ┴└─┘└─┘┴┘└┘└─┘  ╩ ╩└─┘┘└┘┴ └─┘┴└─ ver 0.0.1
''')
print("Welcome to Vaccine Hunter stranger!")
print("What do we need to do, to get our shots?") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

choice1 = input("Should we go to (p)olice or to (v)ax post?\n")
if str(choice1.lower()) == "p":
  print('''Art by Joan G. Stark\n
        _.---._
     .-' ((O)) '-.
      \ _.\_/._ /
       /..___..\ 
       ;-.___.-;
      (| e ) e |)     .;.
       \  /_   /      ||||
       _\__-__/_    (\|'-|
     /` / \V/ \ `\   \ )/
    /   \  Y  /   \  /=/
   /  |  \ | / {}  \/ /
  /  /|   `|'   |\   /
  \  \|    |.   | \_/
   \ /\    |.   |
    \_/\   |.   |
    /)_/   |    |
   // ',__.'.__,'
  //   |   |   |
 //    |   |   |
(/     |   |   |
       |   |   |
       | _ | _ |
       |   |   |
       |   |   |
       |   |   |
 jgs   |___|___|
       /  J L  \ 
      (__/   \__)\n''')
  print("Oh no! We are arrested for peace violation!\n- GAME OVER -\nThank you for playing! - (p)2021. by Sonja Hranjec")
elif str(choice1.lower()) == "v":
    print('''     _____
    ,\_+_/,
   '(("""))'
   '(|o,o|)'
    '; = ;'
     _) (_
   /' \_/ '\ 
  /\(_ : _)/\ 
 /||/)___( \ \ 
 \|_)'    \/ /
   |      (_/
   |       |
   |       |
   |_______|
    \  |  /
Sher^: | :
     ; | ;\n
"Please stay there and wait in lane!"  nurse said\n''')
    
    choice2 = input("Should we (w)ait or (b)ail home, stranger?\n")
    if str(choice2.lower()) == "b":
      print("(▰︶︹︺▰)\nOh no! We missed our chance!\n - GAME OVER - \nThank you for playing! - (p)2021. by Sonja Hranjec\n github.com/njecolina")
    else:
        print('''                          ,;;;;;;;,
                         ;;;;;;;;;;;,
                        ;;;;;'_____;'
                        ;;;(/))))|((\ 
                        _;;((((((|)))) 
                       / |_|||||||||||\ 
                  .--~(  \ ~))))))))))))
                 /     \  `\-((((((((((( 
                 |    | `\   ) |\       /
                  |    |  `. _/  \_____/ | 
                   |    , `\~            / 
                    |    \  \           / 
                   | `.   `\|          / 
                   |   ~-   `\        / 
                    \____~._/~ -_,   (\ 
                     |-----|\   \    ';; 
                    |      | :;;;'     \ 
                   |  /    |            | 
                   |       |            |  - Art by Tua Xiong
                    |      `.           /\n''')
        choice3 = input("Yay! We waited and got our shots! We won!\nThank you for playing!\n(p)2021. by Sonja Hranjec\ngithub.com/njecolina\nHow do you feel?\n")
        print(f"You feel {choice3}.")
