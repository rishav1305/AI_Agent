import tempfile
import asyncio
from autogen_core import CancellationToken
from autogen_core.code_executor import with_requirements, CodeBlock
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor
import pandas

@with_requirements(python_packages=["pandas"], global_imports=["pandas"])
def load_data() -> pandas.DataFrame:
    """Load some sample data.

    Returns:
        pandas.DataFrame: A DataFrame with sample data
    """
    data = {
        "name": ["John", "Anna", "Peter", "Linda"],
        "location": ["New York", "Paris", "Berlin", "London"],
        "age": [24, 13, 53, 33],
    }
    return pandas.DataFrame(data)

async def run_example():
    # The decorated function can be used in executed code
    with tempfile.TemporaryDirectory() as temp_dir:
        executor = LocalCommandLineCodeExecutor(work_dir=temp_dir, functions=[load_data])
        code = f"""
from {executor.functions_module} import load_data

# Use the imported function
data = load_data()
print(data['name'][0])
data.to_csv('test.csv')
"""

        result = await executor.execute_code_blocks(
            code_blocks=[CodeBlock(language="python", code=code)],
            cancellation_token=CancellationToken(),
        )
        print(result.output)  # Output: John

# Run the async example
asyncio.run(run_example())