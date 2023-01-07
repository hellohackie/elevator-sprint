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
      