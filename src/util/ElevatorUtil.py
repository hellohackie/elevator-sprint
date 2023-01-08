class ElevatorUtil:
  """
  ElevatorUtil: class that provides functionality to smoothly process task for elevator 
  """

  def executeRequest(self, requests):
    # run untill requests are not finished
    while True:
      # update running status
      self.isRunning = True

      # If currently on floor which is in requests
      if self.onFloor in requests:
        # remove the processed one from the list
        while requests.count(self.onFloor) > 0:
          requests.remove(self.onFloor)
        
        # stop the lift, as it has reached one of its destination
        self.isRunning = False
        self.currentStatus()

        # open door
        self.openDoor()
        # close door
        self.closeDoor()

      # If we have processed all requests - break
      if len(requests) == 0:
        break

      # display current status and move
      self.currentStatus()
      self.moveOneStep()
    
  
  def moveOneStep(self):
    """
    move_one_step : moves lift one step up or down based on direction
    self.on_floor = self.on_floor + self.direction
    direction can have value of 1 or -1
    raises Exception if lift is not operational
    """

    try:
      if self.isOperational:
        self.onFloor = self.onFloor + self.direction
      else:
        raise Exception("Lift is not Operational")
    
    except Exception as e:
      print(e)
      return e


  def processRequest(self, activeFloors):
    """
    processRequest: method to select lift & proces request
    """

    # unique set of active floors
    activeFloors = list(set(activeFloors))
    activeFloors.sort()
    self.activeFloors = activeFloors

    print("Matching Floor Request with Elevator!!")

    # process each floor, select lift which is closest
    print("Active Floors => ", activeFloors)
    for queueCounter, floor in enumerate(activeFloors):
      distance = []
      # find optimal lift for each floor
      for elevator in self.elevators:
        # if it's not already selected
        if not elevator.isSelected:
          distance.append(abs(elevator.onFloor - floor))
        else:
          distance.append(999)
      
      queueCounter = queueCounter % len(self.requestQueue)
      # find the selected lift
      selectedLift = distance.index(min(distance))
      elevatorSelected = self.elevators[selectedLift]

      # assign service queue
      elevatorSelected.serviceList = [floor] + self.requestQueue[queueCounter]

      # set direction
      elevatorSelected.direction = 1 if elevatorSelected.onFloor <= floor else -1

      # mark as selected
      elevatorSelected.isSelected = True

      # print information on screen
      print("##################################################")
      print("Lift number: ", elevatorSelected.liftNumber)
      print("On floor: ", elevatorSelected.onFloor)
      print("Service list: ", elevatorSelected.serviceList)
      print("Direction: ", elevatorSelected.direction)

    # process request for each elevator
    for elevator in self.elevators:
      if elevator.isSelected:
        print("-------------------------------------------------")
        print("\t\t\tLift - {}".format(elevator.liftNumber))
        print("-------------------------------------------------")
        elevator.processRequest()

