# Cram-o-Matic Optimiser
In the _Isle of Armor_ downloadable content for _Pokémon Sword_ and _Pokémon Shield_, there is an interactive object
called the Cram-o-Matic, which allows combination of four items to produce a new item.
In-game, this is functionally a black-box, without any information on what the output will be.
Work from the community has revealed the internal workings of the Cram-o-Matic, as documented on
[Serebii](https://www.serebii.net/swordshield/cram-o-matic.shtml).

This project allows a user to optimise their output from the Cram-o-Matic, by identifying the most efficient 
combinations of items they could enter into the Cram-o-Matic, to receive the highest number of their target item. 

## How the Cram-o-Matic works
The rules of the Cram-o-Matic are as follows:
- Four input items must always be placed into the Cram-o-Matic.
- Each input item will have a designated _type_ and _value_, where the type is one of the common Pokémon types. 
- The type of the _first input item_ will be used in determining the type of the output item
- The value of all four items will be added together to determining the value of the output item
- The output will always be a single class of item, where only Pokéballs may be produced in multiples.

### Example use
To craft a _Metal Coat_, the items in the Cram-o-Matic must reach a value range of _61-70_, and be led by an item with the
_Steel_ type. 

### Special cases
- There are a set of guaranteed Cram-o-Matic combinations, which combine three of a certain item with any other item,
  as shown on [Serebii](https://www.serebii.net/swordshield/cram-o-matic.shtml). This is order-dependent.
- _Apricorn_ items are designed for a specific use with the Cram-o-Matic, combining four apricorns to output Pokéballs,
  and hold 0 value when used outside that scenario.

## Optimising the Cram-o-Matic
### Initial use case
The most simple use of this project is to optimise the number of a desired item that can be created from a user's 
current item supply, by picking the best combination of items that will achieve the desired item's value range and type.

Bag size = 4
Maximum weight W = Minimum Weight = 4

### Deeper use cases 
- Perform multi-level optimisation to choose which lower-value items can be combined into output higher-value items
  suitable for using in crafting the desired item. For example, combining _Nuggets_ into _Big Nuggets_ to use in crafting 
  _Bottle Caps_, where _Nuggets_ would not be directly usable.
- Optimising use of similar value items to create a balanced group of output items. The balance could be directed by 
  the user as a percentage.For example, using _Comet Shards_ to create 75% _Rare Candy_ and 25% _Bottle Cap_ items. 

## Development Backlog
### Key features
- Work out the optimisation algorithm
- Refine data entry for a user
- Host code on GitHub

### Potential features
- Enable do-not-use marking of items in the user's data input
- Separate Apricorn handling from the optimiser
- Present project through a GUI (potentially Streamlit)
- Host service online
- Promote on Reddit for feature requests and bug highlighting
- Dockerise for discrete deployment

### Issues
- _Enigma Berry_ is not valued on Serebii's page, so has been set to value 0
- Ensure that the first item's type will not change output item 
  (like NORMAL type with range 131-140 producing TR42 instead of Rare Candy)
- Dynite Ore, Galarica Wreath and other Crown Tundra items are not in input_items.json 

### Acknowledgements
[Serebii](https://www.serebii.net/swordshield/cram-o-matic.shtml): without their guide to the Cram-o-Matic, _many_
players would have struggled to use this extremely helpful device.

[ThirdSpartan](https://github.com/ThirdSpartan/ThirdSpartan.github.io): found during the development of this project,
their recipe finder proved that users actually welcomed such helpful tools, and they spent the time transcribing items
into JSON format, which was continued for this project.
