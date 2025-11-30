import click
from rich.console import Console
from rich.table import Table
from pathlib import Path
import sys

from cm_colors import Color, ColorPair
from .config import load_config, create_default_config, CONFIG_FILE_NAME

console = Console()

@click.group()
def main():
    """A CLI tool to lint color pairs for contrast compliance."""
    pass

@main.command()
def init():
    """Initialize the .color_pairs.yml configuration file."""
    config_path = Path(CONFIG_FILE_NAME)
    if config_path.exists():
        console.print(f"[yellow]Warning:[/yellow] {CONFIG_FILE_NAME} already exists.")
        if not click.confirm("Do you want to overwrite it?"):
            return

    create_default_config(config_path)
    console.print(f"[green]Success:[/green] Created {CONFIG_FILE_NAME} with sample data.")
    console.print("You can now edit this file to add your own color pairs.")

@main.command()
def lint():
    """Lint color pairs defined in .color_pairs.yml."""
    config = load_config()
    if not config:
        console.print(f"[red]Error:[/red] Could not find or parse {CONFIG_FILE_NAME}.")
        console.print(f"Run [bold]cc-lint init[/bold] to create one.")
        sys.exit(1)

    table = Table(title="Color Contrast Lint Results")
    table.add_column("Foreground", style="cyan")
    table.add_column("Background", style="magenta")
    table.add_column("Status", justify="center")

    failed_count = 0
    standard = config.min_contrast.upper()
    console.print(f"Checking against standard: [bold]{standard}[/bold]")

    for pair_config in config.pairs:
        try:
            pair = ColorPair(pair_config.foreground, pair_config.background)
            
            readability = pair.is_readable
            
            passed = False
            if standard == "AAA":
                passed = readability == "Very Readable"
            else: # Default to AA
                passed = readability in ["Readable", "Very Readable"]

            status = "[green]PASS[/green]" if passed else "[red]FAIL[/red]"
            if not passed:
                failed_count += 1

            table.add_row(
                pair_config.foreground,
                pair_config.background,
                status
            )

        except Exception as e:
            console.print(f"[red]Error processing pair {pair_config.foreground} on {pair_config.background}: {e}[/red]")
            failed_count += 1

    console.print(table)

    if failed_count > 0:
        console.print(f"\n[red]Lint failed with {failed_count} errors.[/red]")
        sys.exit(1)
    else:
        console.print("\n[green]All color pairs passed contrast checks![/green]")

if __name__ == "__main__":
    main()
