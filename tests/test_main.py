# NO FUNCIONA PK NO EJECUTA EL PROGRAMA, ponlo donde hace el texto este
def atest_output(capsys):
    expected_output = """Ha hecho push 2 veces en el repositorio: Tanixhq23/CLI-program-for-task-manager\n
Ha creado una rama o etiqueta de Git 2 veces en el repositorio: Tanixhq23/CLI-program-for-task-manager\n
Ha creado una rama o etiqueta de Git 2 veces en el repositorio: Tanixhq23/skills-introduction-to-github\n"""
    # Capture the output
    captured_output = capsys.readouterr()
    assert expected_output in captured_output.out
