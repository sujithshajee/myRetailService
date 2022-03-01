import unittest as unittest
import coverage

if __name__ == "__main__":
    cov = coverage.Coverage(include="../*.py", omit="../venv/*")
    cov.start()
    all_tests = unittest.TestLoader().discover("test", pattern="*.py")
    unittest.TextTestRunner().run(all_tests)
    cov.stop()
    cov.save()
    cov.html_report()