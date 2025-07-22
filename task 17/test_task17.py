import unittest
import os
from original_script import add_task, view_tasks, delete_task, export_tasks, save_tasks

class TestTodoManager(unittest.TestCase):
    def setUp(self):
        # Setup a clean tasks file for each test
        self.test_tasks = ["Task A", "Task B", "Task C"]
        save_tasks(self.test_tasks)

    def tearDown(self):
        # Remove tasks file after each test
        if os.path.exists("tasks.txt"):
            os.remove("tasks.txt")
        if os.path.exists("exported.txt"):
            os.remove("exported.txt")

    def test_add_task(self):
        self.assertTrue(add_task("Task D"))
        self.assertIn("Task D", view_tasks())

    def test_view_tasks(self):
        tasks = view_tasks()
        self.assertEqual(tasks, self.test_tasks)

    def test_delete_task(self):
        removed = delete_task(2)
        self.assertEqual(removed, "Task B")
        self.assertNotIn("Task B", view_tasks())

    def test_delete_invalid(self):
        removed = delete_task(10)
        self.assertIsNone(removed)

    def test_export_tasks(self):
        self.assertTrue(export_tasks("exported.txt"))
        with open("exported.txt", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f]
        self.assertEqual(lines, self.test_tasks)

if __name__ == "__main__":
    unittest.main()