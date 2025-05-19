import os
import sys
import importlib.util
import json
import time
from colorama import init, Fore, Style

# Initialize colorama for cross-platform colored terminal output
init(autoreset=True)

# Configuration for test case display
class DisplayConfig:
    # Maximum number of passing tests to show
    MAX_PASS_DISPLAY = 3
    # Maximum number of failing tests to show
    MAX_FAIL_DISPLAY = 3
    # Whether to show detailed inputs/outputs for passing tests
    SHOW_PASS_DETAILS = True
    # Whether to always show the first test case regardless of pass/fail
    ALWAYS_SHOW_FIRST_TEST = True

def clear_screen():
    """Clear the terminal screen in a cross-platform way."""
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Mac and Linux
    else:
        os.system('clear')

def find_file(prefix, folder, suffix=""):
    """Find a file with given prefix and optional suffix in specified folder."""
    for f in os.listdir(folder):
        if f.startswith(f"{prefix}.") and suffix in f:
            return os.path.join(folder, f)
    return None

def format_value(value):
    """Format value for better terminal display."""
    if isinstance(value, list) and len(value) > 10:
        return f"[{', '.join(str(x) for x in value[:5])}..., {', '.join(str(x) for x in value[-5:])}] (length: {len(value)})"
    return str(value)

def run_test(data_file, test_file):
    """Run tests against solution file using test cases."""
    # Clear screen before displaying test results
    clear_screen()
    
    with open(test_file) as f:
        data = json.load(f)

    function_name = data["function"]
    inputs = data["inputs"]
    expected_outputs = data["expected"]

    # Import solution module
    spec = importlib.util.spec_from_file_location("solution_module", data_file)
    solution_module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(solution_module)
    solution = solution_module.Solution()
    func = getattr(solution, function_name)

    # Run tests
    results = []
    pass_count = 0
    fail_count = 0
    passed_indices = []
    failed_indices = []
    start_time = time.time()
    
    for i, inp in enumerate(inputs):
        case_start = time.time()
        if not isinstance(inp, list):
            inp = [inp]
        
        try:
            output = func(*inp)
            correct = output == expected_outputs[i]
            if correct:
                pass_count += 1
                passed_indices.append(i)
            else:
                fail_count += 1
                failed_indices.append(i)
                
            case_time = round((time.time() - case_start) * 1000, 2)
            results.append((correct, output, expected_outputs[i], case_time))
        except Exception as e:
            fail_count += 1
            failed_indices.append(i)
            case_time = round((time.time() - case_start) * 1000, 2)
            results.append((False, str(e), expected_outputs[i], case_time))
            
    end_time = time.time()
    total_time = round((end_time - start_time) * 1000, 2)

    # Display results
    terminal_width = os.get_terminal_size().columns if hasattr(os, 'get_terminal_size') else 80
    
    print(f"{Fore.CYAN}{'='*terminal_width}")
    print(f"{Fore.YELLOW}📋 RUNNING TEST: {Fore.WHITE}{os.path.basename(data_file)}")
    print(f"{Fore.YELLOW}📝 FUNCTION: {Fore.WHITE}{function_name}")
    print(f"{Fore.CYAN}{'='*terminal_width}")
    
    # Determine which test cases to display
    display_indices = set()
    
    # Always show the first test case if configured
    if DisplayConfig.ALWAYS_SHOW_FIRST_TEST and results:
        display_indices.add(0)
    
    # Add passing tests (up to MAX_PASS_DISPLAY)
    for idx in passed_indices[:DisplayConfig.MAX_PASS_DISPLAY]:
        display_indices.add(idx)
    
    # Add failing tests (up to MAX_FAIL_DISPLAY)
    for idx in failed_indices[:DisplayConfig.MAX_FAIL_DISPLAY]:
        display_indices.add(idx)
    
    # Convert to sorted list
    display_indices = sorted(display_indices)
    
    # Display selected test cases
    for i in display_indices:
        correct, out, exp, case_time = results[i]
        status = f"{Fore.GREEN}✅ PASS" if correct else f"{Fore.RED}❌ FAIL"
        print(f"\n{Fore.YELLOW}Test Case #{i+1}:")
        print(f"{Fore.CYAN}  Status: {status}{Style.RESET_ALL}")
        
        # For passing tests, only show details if configured to do so
        if correct and not DisplayConfig.SHOW_PASS_DETAILS:
            print(f"{Fore.CYAN}  Time: {Fore.WHITE}{case_time} ms")
            continue
            
        # Format input for display
        input_val = inputs[i]
        if isinstance(input_val, list) and len(input_val) > 0:
            input_display = format_value(input_val)
        else:
            input_display = format_value(input_val)
            
        print(f"{Fore.CYAN}  Input: {Fore.WHITE}{input_display}")
        
        # Display output with diff formatting if incorrect
        if correct:
            print(f"{Fore.CYAN}  Output: {Fore.GREEN}{format_value(out)}")
        else:
            print(f"{Fore.CYAN}  Output: {Fore.RED}{format_value(out)}")
            print(f"{Fore.CYAN}  Expected: {Fore.GREEN}{format_value(exp)}")
            
        print(f"{Fore.CYAN}  Time: {Fore.WHITE}{case_time} ms")
    
    # If we have more results than displayed, show a summary of what was skipped
    if len(results) > len(display_indices):
        skipped_passes = pass_count - sum(1 for i in display_indices if results[i][0])
        skipped_fails = fail_count - sum(1 for i in display_indices if not results[i][0])
        
        if skipped_passes > 0 or skipped_fails > 0:
            print(f"\n{Fore.YELLOW}📌 SKIPPED TEST CASES:")
            if skipped_passes > 0:
                print(f"{Fore.GREEN}  ✅ {skipped_passes} additional passing tests")
            if skipped_fails > 0:
                print(f"{Fore.RED}  ❌ {skipped_fails} additional failing tests")
                
            # Show indices of skipped failed tests if any
            if skipped_fails > 0:
                hidden_fails = [i+1 for i in failed_indices[DisplayConfig.MAX_FAIL_DISPLAY:]]
                if hidden_fails:
                    print(f"{Fore.RED}  Failed cases not shown: {', '.join(map(str, hidden_fails))}")
    
    # Display summary
    print(f"\n{Fore.CYAN}{'-'*terminal_width}")
    print(f"{Fore.YELLOW}📊 SUMMARY:")
    print(f"{Fore.CYAN}  Total Tests: {Fore.WHITE}{len(results)}")
    print(f"{Fore.CYAN}  Passed: {Fore.GREEN}{pass_count}")
    print(f"{Fore.CYAN}  Failed: {Fore.RED}{fail_count}")
    print(f"{Fore.CYAN}  Success Rate: {Fore.WHITE}{round(pass_count/len(results)*100 if results else 0, 2)}%")
    print(f"{Fore.CYAN}  Total Time: {Fore.WHITE}{total_time} ms")
    print(f"{Fore.CYAN}{'_'*terminal_width}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python test_runner.py <problem_number>")
        sys.exit(1)

    # Clear screen before running tests
    clear_screen()

    prob_num = sys.argv[1]

    data_file = find_file(prob_num, "data")
    test_file = find_file(prob_num, "test cases", "test case")

    if not data_file or not test_file:
        print(f"{Fore.RED}❌ Couldn't find matching files for problem {prob_num}")
        print(f"{Fore.YELLOW}Make sure data and 'test cases' directories exist with proper files.")
        sys.exit(1)

    run_test(data_file, test_file)