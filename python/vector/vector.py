class Vector:

  def __init__(self, list):

      self.list = list #[1,2]
      self.copylist = list

  def __str__(self):
      return ", ".join(map(str, self.list))

  def add(self,Vector):

      try:
          self.list = self.copylist

          #take list from other vector
          other = Vector.list

          #take each value from other Vector and add it to self.list
          for index,item in enumerate(Vector.list,0):
              self.list[index] = item + self.list[index]


      except:
          print("Different size vectors")
      #return the instance of a class
      return self.__class__(self.list)

  def subtract(self,Vector):

      self.list = self.copylist
      other = Vector.list

      print(self.list)
      print(other)

      for index,item in enumerate(Vector.list,0):
          self.list[index] = self.list[index] - item

      return self.__class__(self.list)

  def dot(self,Vector):
      self.list = self.copylist
      other = Vector.list

      #print(self.list)
      #print(other)

      running_sum =0

      for index,item in enumerate(Vector.list,0):
          running_sum = running_sum + item * self.list[index]
          #print(running_sum, " ", self.list[index], " ", item)

      return running_sum

  def norm(self):
      running_sum = 0

      for item in self.list:
          running_sum += item**2

      return running_sum ** 0.5

  def toString(self):
      return str(self.list)

  def equals(self,Vector):
      return self.list == Vector.list
