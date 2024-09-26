import openai
import runloop

# Lambda functions can take in arbitrary inputs and return arbitrary outputs.
# They will automatically run in a container with all the dependencies needed.
@runloop.function
def test_devbox(name: str, system_coordinator: runloop.SystemCoordinator) -> str:
    # We create a devbox that is tied to the run of this agent. It will be automatically shutdown when the agent is done.
    devbox = system_coordinator.create_devbox()

    # We can use shell tools and file tools to interact with the devbox including running arbitrary commands and writing and reading files.
    exec_result = devbox.shell_tools.exec("echo 'executed hello from devbox'")

    return f"Devbox ID: {devbox.id}\nExec Result: {exec_result}"