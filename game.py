"""
Classes for game
"""


class Room:
    """
    Class for room
    """

    def __init__(self, name):
        self.name = name
        self.description = ""
        self.character = None
        self.item = None
        self.linked_rooms = []

    def set_description(self, description):
        """
        Set description of room
        """
        self.description = description

    def link_room(self, room, direction):
        """
        Makes link between rooms
        """
        self.linked_rooms.append(tuple([room, direction]))

    def set_character(self, character):
        """
        Set character in room
        """
        self.character = character

    def set_item(self, item):
        """
        Set item in room
        """
        self.item = item

    def get_details(self):
        """
        Show information about room
        """
        print(self.description)
        for room in self.linked_rooms:
            print(f"There is {room[0].name} in the {room[1]}")

    def get_character(self):
        """
        Gets character from room
        """
        return self.character

    def get_item(self):
        """
        Gets item from room
        """
        return self.item

    def move(self, direction):
        """
        Move to another room by direction
        """
        for room in self.linked_rooms:
            if room[1] == direction:
                return room[0]
        print(f"There is no room in the {direction}")
        return self


class Character:
    """
    Class for characters
    """

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.conversation = ""

    def set_conversation(self, conversation):
        """
        Set conversation
        """
        self.conversation = conversation

    def describe(self):
        """
        Describe character
        """
        print(f"There is someone in the room!")
        print(f"{self.name}: {self.description}")

    def talk(self):
        """
        Show conversation with character
        """
        print(self.conversation)


class Enemy(Character):
    """
    Class for enemies
    """
    defeated = 0

    def __init__(self, name, description):
        super().__init__(name, description)
        self.weakness = ""

    def set_weakness(self, weakness):
        """
        Set weakness of enemy
        """
        self.weakness = weakness

    def fight(self, item):
        """
        Show if you win in fight with enemy
        """
        return item == self.weakness

    def get_defeated(self):
        """
        Show how many enemies you defeated
        """
        Enemy.defeated += 1
        return self.defeated


class Friend(Character):
    """
    Class for friendly characters
    """

    def __init__(self, name, description):
        super().__init__(name, description)
        self.gift = None

    def set_gift(self, item):
        """
        Set a gift
        """
        self.gift = item

    def get_gift(self):
        """
        Gets gift
        """
        return self.gift


class Item:
    """
    Class for items
    """

    def __init__(self, name):
        self.name = name
        self.description = ""

    def set_description(self, description):
        """
        Set description of item
        """
        self.description = description

    def describe(self):
        """
        Describe item
        """
        print(f"There is something in the room!")
        print(f"{self.name}: {self.description}")

    def get_name(self):
        """
        Get name of item
        """
        return self.name
