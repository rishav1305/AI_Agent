import configparser
import colorama
from colorama import Fore, Style
from autogen_ext.models.openai import OpenAIChatCompletionClient


# Initialize colorama for cross-platform color support
colorama.init(autoreset=True)


def get_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    return config


def run_openai_model(model_name, prompt_text):
    
    client = OpenAI(
    api_key=get_config()['OPEN_AI_DETAILS']['API_KEY']
    )

    completion = client.chat.completions.create(
    model=model_name,
    store=True,
    messages=prompt_text
    )
    return completion.choices[0].message


def run_tests(testcases, test_function):
    """
    Run tests with colored logging for pass/fail results.
    
    Args:
        testcases (list): List of test cases, where each test case is [input, expected_output]
        test_function (callable): Function to test
    """
    total_tests = len(testcases)
    passed_tests = 0

    print(f"Running {total_tests} test cases:")

    for i, testcase in enumerate(testcases, 1):
        input_value = testcase[0]
        expected = testcase[1]
        result = test_function(input_value)

        if result == expected:
            print(f"{Fore.GREEN}✓ Test {i}: PASSED{Style.RESET_ALL}")
            print(f"  Input: {input_value}")
            print(f"  Expected: {expected}")
            print(f"  Result: {result}\n")
            passed_tests += 1
        else:
            print(f"{Fore.RED}✗ Test {i}: FAILED{Style.RESET_ALL}")
            print(f"  Input: {input_value}")
            print(f"  Expected: {expected}")
            print(f"  Actual: {result}\n")

    # Summary
    print(f"{Fore.CYAN}Test Summary:{Style.RESET_ALL}")
    print(f"Total Tests: {total_tests}")
    print(f"{Fore.GREEN}Passed: {passed_tests}{Style.RESET_ALL}")
    print(f"{Fore.RED}Failed: {total_tests - passed_tests}{Style.RESET_ALL}")


def get_model_client(model_name):

    if model_name == 'deepseek':
        model_client = OpenAIChatCompletionClient(
            model="deepseek-r1:14b",
            base_url="http://localhost:11434/v1",
            api_key="placeholder",
            model_info={
                "vision": False,
                "function_calling": False,
                "json_output": False,
                "family": "unknown",
            },
        )

    elif model_name =='llama':
        model_client = OpenAIChatCompletionClient(
            model="llama3.2",
            base_url="http://localhost:11434/v1",
            api_key="placeholder",
            model_info={
                "vision": False,
                "function_calling": True,
                "json_output": False,
                "family": "unknown",
            },
        )
    else:
        raise "Unknown model name mentioned."
    
    return model_client
    