import typer

<<<<<<< HEAD
# Master branch comment changed remotely.
=======

# Greeting application for AppSec demo.
>>>>>>> 80f58d5 (style: reformat hello script and improve output handling)
def main(
    name: str,
    lastname: str = typer.Option(
        "",
        help="Фамилия пользователя.",
    ),
    formal: bool = typer.Option(
        False,
        "--formal",
        "-f",
        help="Использовать формальное приветствие.",
    ),
) -> None:
    """
    Говорит "Привет" пользователю, опционально используя фамилию и формальный стиль.
    """
    full_name = " ".join(part for part in [name, lastname] if part).strip()

    if formal:
        typer.echo(f"Добрый день, {full_name}!")
    else:
        typer.echo(f"Привет, {name}!")


if __name__ == "__main__":
    typer.run(main)
