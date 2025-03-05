import venv
from pathlib import Path
import asyncio

from autogen_core import CancellationToken
from autogen_core.code_executor import CodeBlock
from autogen_ext.code_executors.local import LocalCommandLineCodeExecutor


async def example():
    work_dir = Path("coding")
    work_dir.mkdir(exist_ok=True)

    venv_dir = work_dir / ".venv"
    venv_builder = venv.EnvBuilder(with_pip=True)
    venv_builder.create(venv_dir)
    venv_context = venv_builder.ensure_directories(venv_dir)

    local_executor = LocalCommandLineCodeExecutor(work_dir=work_dir, virtual_env_context=venv_context)

    code = """
    import pandas as pd
    df = pd.DataFrame([1,2], columns=['a', 'b'])
    df.to_csv()
"""
    await local_executor.execute_code_blocks(
        code_blocks=[
            CodeBlock(language="python", code=code),
        ],
        cancellation_token=CancellationToken(),
    )


asyncio.run(example())