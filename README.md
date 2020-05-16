# Covid Transmission Pygame Sim

There a lot of families, businesses and individuals suffering from this virus and I hope this project, regardless of its reach and simplicity, does not offend the victims in my attempt to learn something from it during this time of isolation. 

Created a simulation of virus transmission. The inspiration came from a Washington Post article showing how the virus could spread if people didn't heed the mandatory lockdowns and social distancing policies. 

<div style="width:360px;max-width:100%;"><div style="height:0;padding-bottom:80.56%;position:relative;"><iframe width="360" height="290" style="position:absolute;top:0;left:0;width:100%;height:100%;" frameBorder="0" src="https://imgflip.com/embed/41n9x3"></iframe></div><p><a href="https://imgflip.com/gif/41n9x3">via Imgflip</a></p></div>

The Washington Post Article can be found here:
https://www.washingtonpost.com/graphics/2020/world/corona-simulator/

## Few Notes:

* The article's simulation follows different dynamics with the ones shown in the project.
* The nodes representing people in the Washington Post article shows a 'bounce' dynamic, when people collide, they bounce of each other. I didn't think that was accurate in the sense that people don't usually bounce from each other and go to other directions.
* In this project, the boxes representing people pass each other and an infected person (red) infects a non-infected person (white) by collision. I didn't implement any physics when two people collide. They just pass each other. I thought this was more accurate not in the sense that people pass each other like ghosts, but that people that are going one way in the street usually don't stop and go to another direction in response to being in close proximity with someone. 
* Obviously, this is an oversimplified simulation of how the tranmission actually behaves but I just thought it'd be a nice visual to have.

## To-do

1. Do more research regarding transmission rates and the current policies that local administrations want to enact in response to the virus regarding public places like restaurants, public transportations, etc. And maybe transform the project in to a simulation of what would happen if say, a restaurant only allows 10 people given a certain amount of space. 

2. Create a tally of people that are infected and non-infected and display it on the screen.
