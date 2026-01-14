from Items import item
class Actions:
    START = "start"
    STOP = "stop"
    PAUSE = "pause"
    RESUME = "resume"
    RESTART = "restart"
    STATUS = "status"
    CONFIGURE = "configure"
    UPDATE = "update"
    DELETE = "delete"
    CREATE = "create"
    def init__(self) -> None:
        pass    

    #def moveUp(self) -> str:
    #    return "move_up"

    def moveDown(self) -> str:
        return "move_down"  

    def moveLeft(self) -> str:
        return "move_left"

    def moveRight(self) -> str:
        return "move_right"
    
    def jump(self) -> str:
        return "jump"
    
    def crouch(self) -> str:
        return "crouch"

    def useItem(self) -> str:
        if (item == None):
            return "punch"
        else:
            return "use_item"
    
        