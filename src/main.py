from controller.ElevatorController import ElevatorController
import time

def setup():
  """
  setup - It make sure about required package to be installed

    if any package is missing it will initiate a pip subprocess
    And it will maintain its dependency in system.
  """
  import sys
  import subprocess
  import pkg_resources

  required  = {'numpy'} 
  installed = {pkg.key for pkg in pkg_resources.working_set}
  missing   = required - installed

  if missing:
      # implement pip as a subprocess:
      print(missing)
      subprocess.check_call([sys.executable, '-m', 'pip', 'install', *missing])


def run():
  """
    Run - It takes a total of 6 input.
    
      active_floors -  floors on which button has been pressed.
      lift_positions - current position of the lift
      no_of_lifts - total number of lifts
      floor_min - the lowest level floor number
      floor_max - the top level floor number
      request_each - request 2d array, represents request for each elevator

      # Assumption
      1. For simplicity i have assumed that there is just a single call button
      2. there is no up and down button on each floor
      3. each floor has a single button to call lift.
      4. each lift individually based on its service queue decides weather to go up or down
    """

    # floors on which the button has been pressed in this sequence
  activeFloors = [5, -2, 7, 9, 10, 12, -1]

  # default posistions of lifts, as of now we have got 5 lifts in place
  liftPositions = [9, 10, 5, 0, 4]

  # noOfLifts, floorMin, floorMax = initializeSystem
  noOfLifts, floorMin, floorMax = 5, -4, 20

  # request for each elevator
  requestEach = [
    [-3, 12, 8, 6, 4, 0, 5],
    [-3, 0, 5],
    [4, 0, 5],
    [8, 6, 4, 0, 5],
    [2, 4, 8, 10, 12]
  ]

  # create the elevator system
  elevatorController = ElevatorController(noOfLifts, floorMin, floorMax, requestEach, liftPositions)

  # process request
  elevatorController.processRequest(activeFloors)

  # printing final message
  time.sleep(1)
  print("~~~~~~~~~~~~~~~~~~~~(;)~~~~~~~~~~~~~~~~~~~~")
  print("System is now idle. Going on maintenance mode!!!")
  print("~~~~~~~~~~~~~~~~~~~~(;)~~~~~~~~~~~~~~~~~~~~")
  time.sleep(1)


if __name__ == '__main__':
  setup()
  run()
