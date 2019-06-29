#import unittest # https://www.youtube.com/watch?v=6tNS--WetLI
#import Python

class TestPy(unittest.TestCase):

  def test_next(self):
    Python.check_data('next')
    
  def test_previous(self):
    Python.check_data('previous')
    
  def test_down(self):
    Python.check_data('down')
    
  def test_up(self):
    Python.check_data('up')
    
  def test_change(self):
    Python.check_data('change')
    
if __name__ == '__main__':
  unittest.main()
