
class Place(object):
    def __init__(self, items, finished_places):
        self.items = items
        self.finished_places = finished_places
        self.in_thing = []
    def light(self, item):
        print('no fire for ugg')
        return self
    def examine(self, item):
        print (' you look closely at the ' + str(*item) + ' and see nothing useful')
        #TODO -- #implement
        return self
    def get_take(self, item):
        if str(item[0]) == 'all':
            if self.finished_places == 0:
                self.items = ['edelweiss']
                self.items.append('prism')
                self.items.append('pickle')
                self.finished_places += 1
        return self
    def openn( self, thing):
        if thing[0] == 'door':
            if self.finished_places == 1:
                self.finished_places += 1
        return self
    def drop(self, item):
        item = item[0]
        if item not in self.items:
            print( "you don't have a " + str(item) + " to drop")
        self.items.remove(item)
        return self
        #implement
    def put_in(self, items):
        if items[0] not in self.items:
            print( "you don't have a " + str(items[0]))
        if items[1] not in self.items:
            print( "you don't have a " + str(items[1]))
        return self
        #implement
        
    def wait (self, *args):
        print("and why are we stoping here?")
        return self
    def move(self, direction):
        #direction = direction[0]
        print ('moving ' + direction)
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
        return Place(self.items, self.finished_places)
        
        #implement
        # return new instance on class
    def enter(self, thing):
        self.in_thing.append(thing)
        return self
        # if thing == 'cave':
        #     if self.finished_places == 5:
        #         self.finished_places += 1
    def exit(self, thing):
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
    #get meaning of life is only useful thing
    def __init__(self, items, finished_places):
        super(North, self).__init__(items, finished_places)
    #things North has
    def get_take(self, item):
        item = ' '.join(item)
        if self.finished_places == 13:
            if item == 'meaning of life':
                print('you win')
                return False
        return self
        # if item is meaning of life -- win

class Up(Place):
    # ENTER CAVE
# LIGHT FIRE
# WAIT
# PUT EDELWEISS IN FIRE
# PUT HELMET IN STATUE
# PUT PRISM IN PICKLE
# EXIT CAVE
    def __init__(self, items, finished_places):
        print ('makeing up')
        super(Up, self).__init__(items, finished_places)
        self.items.append('helmet')
    def light(self, item):
        print ('ohh fire')
        if self.finished_places == 6:
            if item[0] == 'fire':
                self.items.append('fire')
                self.finished_places += 1
        return self
        #if item is fire do stuff
    def put_in(self, item):
        try:
            place = item[2]
            action = item[1]
            item = item[0]
        except IndexError:
            return self
        if place not in self.items:
            print( "you don't have a " + str(place))
        elif item not in self.items:
            print( "you don't have a " + str(item))
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
        #TODO -- say something
        if self.finished_places == 7:
            self.finished_places += 1
        return self
    def enter(self, thing):
        if thing[0] == 'cave':
            if self.finished_places == 5:
                self.items.append('statue')
                self.finished_places += 1
        return self
    def exit(self, thing):
        if thing[0] == 'cave':
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
    def get_take(self, item):
        if item[0] == 'edelweiss':
            if self.finished_places == 3:
                self.finished_places += 1
        return self
        
    
def main():
    quest = Place(None, 0)
    
    while ( quest ):
        todo = {'light' : quest.light, 'examine' : quest.examine, 'get' : quest.get_take, 
        'take' : quest.get_take, 'drop' : quest.drop, 'put' : quest.put_in, 
        'wait' : quest.wait, 'enter' : quest.enter, 'exit' : quest.exit, 'open' : quest.openn}
        user = input ( "enter something: ")
        user = user.lower()
        user = user.split()
        try:
            quest = todo[user[0]](user[1::])
        except KeyError:
            quest = quest.move(user[0])
        # input()
        # do task
        # if move quest = quest.move()
if __name__ == "__main__":
    main()