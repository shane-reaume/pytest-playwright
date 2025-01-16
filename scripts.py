"""Test runner script"""
import sys
import subprocess

def run_unit_1_lessons():
    """Run specific lessons from Unit 1"""
    base_cmd = ["pytest", "-v"]
    lessons = {
        "1": base_cmd + ["tests/test_lessons/test_lesson_1.py"],
        "2": base_cmd + ["tests/test_lessons/test_lesson_2.py"],
        "login_scope": base_cmd + ["tests/test_lessons/test_lesson_login_scope.py"],
    }
    return lessons

def run_with_options(command, headed=False, debug=False):
    """Add optional parameters to any test command"""
    if headed:
        command.append("--headed")
    if debug:
        command.extend(["--slowmo", "1000"])
    subprocess.run(command)

def print_help():
    """Print usage instructions"""
    print("\nAvailable commands:")
    print("  python scripts.py lesson <number>         - Run specific lesson tests")
    print("  python scripts.py unit <number>           - Run specific unit tests")
    print("\nOptions:")
    print("  --headed                                 - Run in headed mode")
    print("  --debug                                  - Run in debug mode (slow)")

if __name__ == "__main__":
    args = sys.argv[1:]
    
    if not args or args[0] == "help":
        print_help()
        sys.exit()

    # Parse options
    headed = "--headed" in args
    debug = "--debug" in args
    # Remove option flags from args
    args = [arg for arg in args if arg not in ["--headed", "--debug"]]

    if args[0] == "lesson" and len(args) > 1:
        lessons = run_unit_1_lessons()
        if args[1] in lessons:
            run_with_options(lessons[args[1]], headed, debug)
        else:
            print(f"Lesson {args[1]} not found. Available lessons: {', '.join(lessons.keys())}")
    
    elif args[0] == "unit" and len(args) > 1:
        units = run_other_units()
        if args[1] in units:
            run_with_options(units[args[1]], headed, debug)
        else:
            print(f"Unit {args[1]} not found. Available units: {', '.join(units.keys())}")
    
    else:
        print("Invalid command.")
        print_help()