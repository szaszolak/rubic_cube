from Frontier import Frontier
import unittest
from mock import MagicMock
from mock import Mock


class TestFrontier(unittest.TestCase):

    def setUp(self):
        self.frontier = Frontier()

    def test_append_first_element(self):
    	mocked_path = MagicMock()
    	self.frontier.append(mocked_path)
    	self.assertEqual(mocked_path, self.frontier.paths[0])

    def test_append_second_element(self):
    	mocked_path_1 = MagicMock()
    	mocked_path_1.exploration_cost = MagicMock(return_value=2)
    	mocked_path_2 = MagicMock()
    	mocked_path_2.exploration_cost = MagicMock(return_value=1)

    	self.frontier.append(mocked_path_1)
    	self.frontier.append(mocked_path_2)
    	self.assertEqual(mocked_path_2, self.frontier.paths[0])


    def test_pop(self):
    	mocked_path = Mock()
    	self.frontier.append(mocked_path)
    	self.assertEqual(mocked_path, self.frontier.pop())
    	self.assertEqual([], self.frontier.paths)