# ✠ VASCO - VAriable tranSformer CalculatOr
![Badge](https://img.shields.io/badge/license-BeerWare-yellow?style=for-the-badge)

Software que calcula informações de transformadores feita para a matéria de "Conversão Eletromecânica de Energia I" do curso de "Engenharia Elétrica" da Universidade Federal de Santa Maria Campus Cachoeira do Sul (UFSM-CS).

<a href="LISCENSE"><img src="./Images/VASCO.png"></a>

## Autores:
- Arthur Cordeiro Andrade
- João Gabriel Silva de Avellar
## Dependências
- PyGame - https://www.pygame.org
```
pip install pygame
```
# Compilar
## Dependências:
- Pyinstaller - https://www.pyinstaller.org
```
pip install pyinstaller
```
## Comando Compilar
```
pyinstaller --noconfirm --onefile --windowed --icon "Images/Cruz-De-Malta.ico" --add-data "Images;Images/" --add-data "Sounds;Sounds/" "./VASCO.py"
```