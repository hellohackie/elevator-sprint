from model.Elevator import Elevator

class ElevatorController:
  """
  ElevatorSystem - Class that contains array of Elevator objects
    self.number_of_lifts = total number of lifts in the system
    self.floor_max = top floor
    self.floor_min = bottom most floor
    self.request_queue = request queue for each lift
  """

  def __init__(self, numberOfLifts, floorMin, floorMax, requestEach, liftPositions = []) -> None:
    self.numberOfLifts = numberOfLifts
    self.floorMax = floorMax
    self.floorMin = floorMin
    self.elevators = []
    self.requestQueue = requestEach

    # Safegaurd in case no initial positioning of lift is given
    # all start from 0 in that case
    if len(liftPositions) < 0:
      liftPositions = [0] * numberOfLifts

    # create an array of elevator objects
    for each in range(0, numberOfLifts):
      newElevators = Elevator(each, floorMin, floorMax, liftPositions[each])
      self.elevators.append(newElevators)

  
  from util.ElevatorUtil import ElevatorUtil
  processRequest = ElevatorUtil.processRequest