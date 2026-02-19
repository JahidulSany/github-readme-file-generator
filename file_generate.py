from rich.progress import Progress
from rich.console import Console    
import time

# Writing on README.md file and Insert content
def generate_file(self, content):
    self.console = Console()
    
    with open("README.md".lower(), "w") as file:
        file.write(content)

    # # Show a progress bar
    with Progress() as progress:
        task = progress.add_task("Processing...", total=100)
        for _ in range(10):
            time.sleep(0.3)
            progress.update(task, advance=10)

    self.console.print("[bold green]README.md created successfully![/bold green] ✅")