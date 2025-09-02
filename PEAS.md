Wolf, Goat and Cabbage Problem


1. Peformance Measure: 
    -Wether or not the farmer is able to get all of the Wolf, Goat, and Cabbage to the other side of the river without one eating the other. 
    -How many times the farmer has to go back and forth before getting all of the items across the river safely
    -If the farmer leaves two items together, where neither one of those items will eat eachother (If the wolf is with the cabbage, or if the goat, wolf, or cabbage are alone on one side)


2. Environment:
    -The boat that the agent (farmer) will be interacting with
    -The Wolf
    -The Goat
    -The Cabbage
    -The River (although, I'm not sure if this counts since the river is technically abstract)
    -Which side the farmer is on

3. Actuators:
    -Choose between the goat, wolf or cabbage
    -Decide if the farmer will go with an item, or go alone

4. Sensors:
    -State of the boat capacity (detects when the boat has the farmer and another item or not)
    -Variable for which side of the river the agent is on
    -Sensor for knowing which items are on which side at a given time
    -Sensor for knowing when there is danger, and when it is safe to move an item accross, or leave an item in tact