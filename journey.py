#!/usr/bin/env python3
import sys
import os


class Place(object):
    """
        Fluent Interface for a location in the quest. Provides default behavior.
        
        Args:
            items: a list of items that the player has at their disposal
            finished_places: integer to represent how many steps have been completed in the 
                correct order.
        Returns:
            None
    
    """
    def __init__(self, items, finished_places):
        self.items = items
        self.finished_places = finished_places
        self.in_thing = []
        
        if ( self.finished_places == 0 ):
            os.system('clear')
            print('Here is the part where I tell you a story if i were a better writer'
            ' there would be a better story: You should probably type "GET ALL" followed'
            ' by "OPEN DOOR" and finally "EAST"')

    
    def light(self, item):
        """
            default method -- no real functionality
            Args:
                item: list of items to light
            Returns:
                self
            Throws: 
                IndexError if item is empty
        """
        item = ' '.join(item)
        print('no ' + item + ' for ugg')
        return self
    
    def examine(self, item):
        """
            default method -- no real functionality
            Args:
                item: list of items to examine
            Returns:
                self
            Throws: 
                IndexError if item is empty
        """
        item = ' '.join(item)
        print (' you look closely at the ' + str(item) + ' and see nothing useful')
        #TODO -- #implement
        return self
    
    def get_take(self, item):
        """
            default method adds edelweiss, prism, and pickle to invertory if 'all'
                is the item to get. else adds the item to inventory.
            Args:
                item: list of items to get
            Returns:
                self
            Throws: 
                IndexError if item is empty
        """
        item = ' '.join(item)
        if str(item) == 'all':
            if self.finished_places == 0:
                self.items = ['edelweiss']
                self.items.append('prism')
                self.items.append('pickle')
                self.finished_places += 1
        elif (self.items):
            self.items.append(item)
        else:
            self.items = [item]
        return self
    
    def openn( self, thing):
        """
            default method -- no real functionality
            Args:
                item: list of items to open
            Returns:
                self
            Throws: 
                IndexError if item is empty
        """
        thing = ' '.join(thing)
        if thing == 'door':
            if self.finished_places == 1:
                self.finished_places += 1
        return self
    
    def drop(self, item):
        """
            default method removes item from inventory if it is there -- else prints error
            Args:
                item: list of items to be removed
            Returns:
                self
            Throws:
                IndexError if item is empty
        """
        item = ' '.join(item)
        
        if not (item in self.items):
            print( "you don't have a " + str(item) + " to drop")
        self.items.remove(item)
        return self
        #implement
    
    def put_in(self, items):
        """
            default method no real functionality -- checks to see if both items are in
                inventory
            Args:
                items: list containing items to put in each other
            Returns: 
                self
        """
        try:
            if items[0] not in self.items:
                print( "you don't have a " + str(items[0]))
                return self
            if items[2] not in self.items:
                print( "you don't have a " + str(items[1]))
                return self
        except IndexError:
            print ( 'put ' + str(items[0]) + ' where')
        except TypeError:
            print ('you don\'t have anything')
        return self
        #implement
        
    def wait (self, *args):
        """
            default method -- no real functionality
            Args:
                args: not used at all
            Returns:
                self
        """
        print("and why are we stoping here?")
        return self
    
    def move(self, direction):
        """
            Function to create new instances of the class (or subclasses) 
                with the appropiate functionality.
            Args:
                direction: name of subclass to initialize (north, up, east) 
                    will default to simply creating new Place
            Returns:
                a new instance of Place class or one of its sub-classes
            Throws:
                IndexError if direction is empty
        """
        try:
            
            if self.in_thing:
                print( "You have to get out of the " + str(*self.in_thing[-1]) +" first" )
                return self
            if direction == 'north':
                if self.finished_places == 12:
                    self.finished_places += 1
                return North(self.items, self.finished_places)
            if direction == 'up':
                if self.finished_places == 4:
                    self.finished_places += 1
                return Up(self.items, self.finished_places)
            if direction == 'east':
                if self.finished_places == 2:
                    self.finished_places += 1
                return East(self.items, self.finished_places)
        except AttributeError:
            self.items = []
            return self.move(direction)
        print(' you didn\'t listen to my very subtle hints, i know it was hard'
            ' your lost now. if you remember the commands i told you you can '
            ' go back to where you left off and continue, or just type "QUIT"')
        return Place(self.items, self.finished_places)
        
        #implement
        # return new instance on class
    def enter(self, thing):
        """
            function used to keep track of enter and exit calls -- adds to a stack 
            Args:
                thing: item to 'enter'
            Returns:
                self
            Throws:
                IndexError if thing is empty
        """
        self.in_thing.append(thing)
        return self
        # if thing == 'cave':
        #     if self.finished_places == 5:
        #         self.finished_places += 1
    
    def exit(self, thing):
        """
            function used to keep track of enter and exit calls -- removes from stack 
            Args:
                thing: item to 'exit'
            Returns:
                self
            Throws:
                IndexError if thing is empty
        """
        if ( not len(self.in_thing)):
            print ('you aren\'t in anything')
            return self
        last = self.in_thing.pop()
        if (last != thing):
            print ('you have to get out of the ' + str(*last) + ' first')
            self.in_thing.append(last)
        return self
        # if thing == 'cave':
        #     if self.finished_places == 11:
        #         self.finished_places += 1
        
class North(Place):
    """
        Implements Place --- overwrites get_take function
    """
    #get meaning of life is only useful thing
    def __init__(self, items, finished_places):
        super(North, self).__init__(items, finished_places)
        os.system('clear')
        print( 'you should probably "GET MEANING OF LIFE"')
    #things North has
    
    def get_take(self, item):
        """
            checks to see if item is 'the meaning of life' and all other steps required
            to win are true. else calls super().get_take
            Args: 
                item: item to get
            Returns:
                false on win condition
                self otherwise
            Throws: 
                IndexError
        """
        item = ' '.join(item)
        if self.finished_places == 13:
            if item == 'meaning of life':
                print('you win')
                return False
        return super(North, self).get_take(item)
        # if item is meaning of life -- win

class Up(Place):
    """
        Implements Place --- overwrites light, wait, put_in, exit functions
    """
    # ENTER CAVE
# LIGHT FIRE
# WAIT
# PUT EDELWEISS IN FIRE
# PUT HELMET IN STATUE
# PUT PRISM IN PICKLE
# EXIT CAVE
    def __init__(self, items, finished_places):
        super(Up, self).__init__(items, finished_places)
        self.items.append('helmet')
        os.system('clear')
        print ( 'I know this is a terrible story, I\'m not a writer'
            'here is where i subtly tell you to "ENTER CAVE", "LIGHT FIRE",'
            ' "WAIT", "PUT EDELWEISS IN FIRE", "PUT HELMET IN STATUE", "PUT PRISM IN'
            ' PICKLE", "EXIT CAVE", "NORTH"')
    
    def light(self, item):
        """
            checks to see if item is fire and all other previous steps have been taken
            if not calls super.light()
            Args:
                item: item to light
            Returns:
                self
            Throws:
                IndexError
        """
        item = ' '.join(item)
        if item == 'fire':
            print ('ohh fire')
            self.items.append('fire')
            if self.finished_places == 6:
                self.finished_places += 1
            return self
        return super(Up, self).light(item)
        #if item is fire do stuff
    
    def put_in(self, item):
        """
            checks for  commands : PUT EDELWEISS IN FIRE # PUT HELMET IN STATUE # PUT PRISM IN PICKLE
            and all other steps to have been completed.
            
            Args:
                item: list of items to put in each other
            Returns:
                self
            Throws:
                IndexError
        """
        try:
            place = item[2]
            action = item[1]
            item = item[0]
        except IndexError:
            print ( 'put ' + str(item[0]) + ' where')
            return self
        except TypeError:
            print ('you don\'t have anything')
        if place not in self.items:
            print( "you don't have a " + str(place))
            return self
        elif item not in self.items:
            print( "you don't have a " + str(item))
            return self
        elif item == 'edelweiss' and place == 'fire':
            if self.finished_places == 8:
                self.finished_places += 1
        elif item == 'helmet' and place == 'statue':
            if self.finished_places == 9:
                self.finished_places += 1
        elif item == 'prism' and place == 'pickle':
            if self.finished_places == 10:
                self.finished_places += 1
        else:
            #TODO
            print ('why whould you do that?')
        return self
        
    
    def wait(self, *args):
        """
            checks to see if all previous steps have been completed in order and
            calls super function. 
            Args:
                *args: not used
            Returns:
                self
        """
        #TODO -- say something
        if self.finished_places == 7:
            self.finished_places += 1
        return super(Up, self).wait(*args)
    
    def enter(self, thing):
        """
            checks to see if you are entering a cave and all other steps have been taken
            
            Args:
                thing: item to 'enter'
            Returns:
                self
            Throws:
                IndexError
        """
        
        super(Up, self).enter(thing)
        thing = ' '.join(thing)
        if thing == 'cave':
            if self.finished_places == 5:
                self.items.append('statue')
                self.finished_places += 1
        return self
    
    def exit(self, thing):
        """
            checks to see if you are exiting a cave and all other steps have been taken
            
            Args:
                thing: item to 'exit'
            Returns:
                self
            Throws:
                IndexError
        """
        super(Up, self).exit(thing)
        thing = ' '.join(thing)
        if thing == 'cave':
            if self.finished_places == 11:
                self.items.remove('statue')
                self.finished_places += 1
        return self
        # implement
        # if command is enter -- add thing to in_thing
        # if out -- check to see if thing is last in list -- remove from list 
    


class East(Place):
    # GET EDELWEISS
    def __init__(self, items, finished_places):
        super(East, self).__init__(items, finished_places)
        os.system('clear')
        print ( ' more story goes here: type "GET EDELWEISS" and "UP"')
    def get_take(self, item):
        """
            checks to see if you are getting edelweiss and all other steps have been taken
            Args:
                item: item to get
            Returns:
                self
            Throws:
                IndexError
        """
        item = ' '.join(item)
        if item == 'edelweiss':
            if self.finished_places == 3:
                self.finished_places += 1
            return self
        return super(East, self).get_take(item)
        
    
def main():
    quest = Place(None, 0)
    
    while ( quest ):
        todo = {'light' : quest.light, 'examine' : quest.examine, 'get' : quest.get_take, 
        'take' : quest.get_take, 'drop' : quest.drop, 'put' : quest.put_in, 
        'wait' : quest.wait, 'enter' : quest.enter, 'exit' : quest.exit, 'open' : quest.openn,
        'quit' : sys.exit}
        user = input ( "enter something: ")
        user = user.lower()
        user = user.split()
        try:
            quest = todo[user[0]](user[1::])
        except KeyError:
            quest = quest.move(user[0])
        except IndexError:
            if( user ):
                print (str(user[0]) + ' what?')
            else:
                print ("Enter a command!")
        except ValueError:
            print ('you don\'t have anything')
            
        # input()
        # do task
        # if task is not in list move 

if __name__ == "__main__":
    main()