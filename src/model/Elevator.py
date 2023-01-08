import numpy as np
import time

class Elevator:
  """
  Elevator class : represents a single elevator
    It can do following:
    1. Move up and down.
    2. Represented by lift_number
    3. Decides which direction to move based on service_list and on_floor
    4. on_floor property denotes currently is on floor.
    5. open and close door.
    6. Start moving and stop moving
  """

  def __init__(self, liftNumber, floorMin, floorMax, onFloor = 0) -> None:
    self.liftNumber = liftNumber
    self.isOperational = True
    self.floorMax = floorMax
    self.floorMin = floorMin
    self.isSelected = False
    self.isRunning = False
    self.onFloor = onFloor
    self.direction = 1
    self.isOverload = False
    self.serviceList = []

  
  from util.ElevatorUtil import ElevatorUtil

  # load required methods from util
  moveOneStep = ElevatorUtil.moveOneStep
  executeRequest = ElevatorUtil.executeRequest

  # prints the current status
  def currentStatus(self):
    time.sleep(0.2)
    print("lift {} is currently at floor {}".format(self.liftNumber+1, self.onFloor))
    time.sleep(0.2)
    print("lift {} running status {}".format(self.liftNumber+1, self.isRunning))
    time.sleep(0.2)
  

  # open door
  def openDoor(self):
    print("lift {} door opening".format(self.liftNumber+1))
    time.sleep(0.5)
    self.doorOpen = True
  

  # close door
  def closeDoor(self):
    print("lift {} door closing".format(self.liftNumber+1))
    time.sleep(0.5)
    self.doorOpen = False
  

  def calculateServiceInDirections(self):
    """
    Creates 2 list from a single service list
        service_in_up_direction - contains all the floor number which are above
        service_in_down_direction - all floor which are below
    """

    self.serviceList = np.sort(self.serviceList)
    serviceInUpDirection = list(self.serviceList[self.serviceList > self.onFloor])
    serviceInDownDirection = list(self.serviceList[self.serviceList < self.onFloor])
    # reaarange order in execution way
    serviceInDownDirection = serviceInDownDirection[::-1]
    return serviceInUpDirection, serviceInDownDirection

  
  def processRequest(self):
    """
    recieves service_list and process them.
        Broabdly 2 tasks:
        TASK 1
        # case when button is pressed from outside
        # go to the requested floor
        TASK 2
        # process request when button from inside are pressed.
    """

    # go to requested floor
    print("Need to process => ", self.serviceList)
    if self.serviceList[0] != self.onFloor:
      self.currentStatus()
      self.executeRequest(self.serviceList[0:1])
    else:
      self.currentStatus()
      self.openDoor()
      self.closeDoor()
    
    # then user presses the buttons
    # lift decides automatically
    self.serviceList = self.serviceList[1:]
    serviceInUpDirection, serviceInDownDirection = self.calculateServiceInDirections()

    # nothing to service in up direction, go down
    if len(serviceInUpDirection) == 0:
      self.direction = -1
    # nothing to service in down direction, go up
    elif len(serviceInDownDirection) == 0:
      self.direction = 1
    # calculate cost & then decide direction
    else:
      # effortUp = distance between first up floor & current floor
      effortUp = abs(serviceInUpDirection[0] - self.onFloor)
      # effortDown = distance between first down floor & current floor
      effortDown = abs(serviceInDownDirection[0] - self.onFloor)

      # choose direction
      if effortUp <= effortDown:
        self.direction = 1
      else:
        self.direction = -1


    # execute once for up
    # once for down
    for turn in range(0, 2):
      if self.direction == -1:
        self.executeRequest(serviceInDownDirection)
      else:
        self.executeRequest(serviceInUpDirection)

      # reverse the direction
      self.direction = - self.direction

    # set params to denote that it is available
    self.resetLiftParams()

  
  def resetLiftParams(self):
    # when request finishes reset the direction
    self.direction = 1
    self.isRunning = False
    self.isSelected = False
    self.serviceList = []

