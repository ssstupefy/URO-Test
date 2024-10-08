import random

class Robot:
  def __init__(self, name, health, attackPower):
    self.name = name
    self.health = health
    self.attackPower = attackPower

  def isAlive(self):
    return self.health > 0
  
  def diserang(self, damage):
    self.health -= damage
    if self.health < 0:
      self.health = 0
  def getName(self):
    return self.name
  def menyerang(self, musuh):
    damage = random.randint(1, self.attackPower)
    print(f"{self.name} attacks {musuh.getName()} for {damage} damage!")
    musuh.diserang(damage)

class Battle:
  def __init__(self, robot1, robot2):
    self.robot1 = robot1
    self.robot2 = robot2

  def startFight(self):
    while self.robot1.isAlive() and self.robot2.isAlive():
      # robot1 nyerang robot2
      self.robot1.menyerang(self.robot2)
      if not self.robot2.isAlive():
        print(f"{self.robot2.getName()} is defeated!")
        print(f"{self.robot1.getName()} is wins!")
        break

      self.robot2.menyerang(self.robot1)
      if not self.robot1.isAlive():
        print(f"{self.robot1.getName()} is defeated!")
        print(f"{self.robot2.getName()} is wins!")
        break

class Game:
  def __init__(self):
    self.robots = [] 

  def addRobot(self, robot):
    self.robots.append(robot)

  def displayRobots(self):
    print("Choose robots for the battle:")
    for i in range(len(self.robots)):
      print(f"{i+1}. {self.robots[i].getName()}")
    
  def selectRobot(self):
    self.displayRobots()
    choice = int(input("Select a robot: ")) - 1
    if 0 <= choice < len(self.robots):
      return self.robots[choice]
    else:
      print("Invalid selection! Please try again.")
      return self.selectRobot()
  
  def startGame(self):
    print("Welcome to the Battle of Robots!")
    robot1 = self.selectRobot()
    robot2 = self.selectRobot()
    if robot1 == robot2:
      print("You selected the same robot. Please try again.")
      self.startGame()
    else:
      battle = Battle(robot1, robot2)
      battle.startFight()

if __name__ == "__main__":
  game = Game()

  robo1 = Robot("Bumblebee", 100, 30)
  robo2 = Robot("Megazord", 100, 37)
  robo3 = Robot("MadamEva", 100, 35)

  game.addRobot(robo1)
  game.addRobot(robo2)
  game.addRobot(robo3)

  game.startGame()